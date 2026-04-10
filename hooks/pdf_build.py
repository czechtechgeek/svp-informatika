"""
MkDocs hook: Generování per-ročníkových PDF knih pomocí WeasyPrint.

Spouští se automaticky po dokončení `mkdocs build` (on_post_build).

Pro každý ročník (6–9) sestaví kompletní PDF obsahující:
  1. Titulní stranu (název školy, ročník, podtitul, autor, rok)
  2. Stránku s RVP ZV metadaty a klíčovými kompetencemi
  3. Všechny hodiny ročníku — každá na samostatné stránce

INTEGRITA HODINY:
  Každá hodina je obalena do <div class="lesson-unit">.
  CSS pravidlo break-before: page zaručí, že hodina vždy začne
  na nové stránce. Zadání na PC (.zadani-pc) + jejich nadpis (h3)
  jsou svázány pravidly break-after/before: avoid — nikdy nevznikne
  prázdná stránka před zadáním.

ZÁVISLOSTI:
  pip install weasyprint
  # Systémové knihovny (Debian/Ubuntu):
  # sudo apt-get install libpango-1.0-0 libcairo2 libgdk-pixbuf2.0-0

VÝSTUPNÍ SOUBORY:
  site/pdf/6-rocnik.pdf
  site/pdf/7-rocnik.pdf
  site/pdf/8-rocnik.pdf
  site/pdf/9-rocnik.pdf

KONFIGURACE:
  Upravte konstanty GRADES, SKOLA_NAZEV, AUTOR na začátku souboru.
"""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path


# ─────────────────────────────────────────────────────────────────────────────
# Konfigurace — upravujte zde
# ─────────────────────────────────────────────────────────────────────────────

#: Název školy pro titulní stranu (např. "ZŠ Masarykova, Praha 6")
SKOLA_NAZEV: str = "Základní škola"

#: Jméno autora / garanty ŠVP
AUTOR: str = "Mgr. Jan Novák"

#: Rok vydání — None = automaticky z aktuálního data
ROK: str | None = None

#: Definice ročníků: barva titulní strany, podtitul, počet týdnů
GRADES: dict[int, dict] = {
    6: {
        "nazev": "6. ročník – Objevitel",
        "podtitul": "Data a základy logiky · Technologie a tabulky",
        "pocet_tydnu": 32,
        "barva": "#004d40",          # tmavozelená
    },
    7: {
        "nazev": "7. ročník – Tvůrce",
        "podtitul": "Modelování a podmínky · Sítě a spolupráce",
        "pocet_tydnu": 31,
        "barva": "#1a237e",          # tmavomodrá
    },
    8: {
        "nazev": "8. ročník – Analytik",
        "podtitul": "Data a robotika · Internet a bezpečnost",
        "pocet_tydnu": 31,
        "barva": "#880e4f",          # tmavočervená
    },
    9: {
        "nazev": "9. ročník – Expert",
        "podtitul": "Simulace a kód · AI a společnost",
        "pocet_tydnu": 31,
        "barva": "#4a148c",          # tmavofialová
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# MkDocs hook: on_post_build
# ─────────────────────────────────────────────────────────────────────────────

def on_post_build(config: dict, **kwargs) -> None:
    """
    Volán MkDocs po dokončení sestavení webu.
    Generuje per-ročníkové PDF soubory do site/pdf/.
    """
    try:
        from weasyprint import HTML as WeasyHTML, CSS as WeasyCSS  # noqa: PLC0415
    except ImportError:
        _warn(
            "WeasyPrint není nainstalován — přeskočení per-ročníkového PDF exportu.\n"
            "        Instalace: pip install weasyprint\n"
            "        Systémové závislosti: sudo apt-get install "
            "libpango-1.0-0 libcairo2 libgdk-pixbuf2.0-0"
        )
        return

    site_dir = Path(config["site_dir"])
    docs_dir = Path(config["docs_dir"])
    pdf_dir = site_dir / "pdf"
    pdf_dir.mkdir(exist_ok=True)

    # Sestavení CSS (extra.css + print.css) pro WeasyPrint
    css_string = _compose_pdf_css(site_dir)

    rok = ROK or str(date.today().year)

    for grade, info in GRADES.items():
        output_path = pdf_dir / f"{grade}-rocnik.pdf"
        _info(f"Generuji {output_path.name} ({info['nazev']}) …")
        try:
            html = _assemble_grade_html(site_dir, docs_dir, grade, info, rok)
            WeasyHTML(
                string=html,
                base_url=site_dir.as_uri() + "/",
            ).write_pdf(
                str(output_path),
                stylesheets=[WeasyCSS(string=css_string)],
            )
            _info(f"✅  {output_path.name}")
        except Exception as exc:  # noqa: BLE001
            _warn(f"Chyba při generování {output_path.name}: {exc}")


# ─────────────────────────────────────────────────────────────────────────────
# Sestavení HTML dokumentu
# ─────────────────────────────────────────────────────────────────────────────

def _assemble_grade_html(
    site_dir: Path,
    docs_dir: Path,
    grade: int,
    info: dict,
    rok: str,
) -> str:
    """Sestaví kompletní HTML dokument pro jeden ročník."""
    parts: list[str] = []

    # 1. Titulní strana
    parts.append(_render_cover(grade, info, rok))

    # 2. Stránka s RVP metadaty a klíčovými kompetencemi
    # pdf-src/ je v exclude_docs → soubory nejsou v site/.
    # Čteme je přímo ze zdrojového Markdown (docs_dir) přes Python-Markdown.
    rvp_html = _docs_md_to_html(docs_dir, "pdf-src/rvp-metadata.md")
    kompetence_html = _docs_md_to_html(docs_dir, "pdf-src/klic-kompetence.md")

    if rvp_html or kompetence_html:
        meta_content = (rvp_html or "") + "\n" + (kompetence_html or "")
    else:
        meta_content = _render_metadata_fallback(grade, info)

    parts.append(
        f'<div class="pdf-metadata">\n'
        f'<h1 class="pdf-metadata__title">'
        f'Školní vzdělávací program – {info["nazev"]}'
        f'</h1>\n'
        f'{meta_content}\n'
        f'</div>'
    )

    # 3. Hodiny — každá obalená do .lesson-unit
    missing = 0
    for week in range(1, info["pocet_tydnu"] + 1):
        content = _extract_lesson_content(site_dir, grade, week)
        if content:
            parts.append(
                f'<div class="lesson-unit" id="tyden-{week:02d}">\n'
                f'{content}\n'
                f'</div>'
            )
        else:
            missing += 1

    if missing:
        _warn(
            f"  {info['nazev']}: {missing} hodin nebylo nalezeno v "
            f"site/{grade}-rocnik/tyden-*/index.html"
        )

    return _wrap_html_document(info["nazev"], "\n\n".join(parts))


def _docs_md_to_html(docs_dir: Path, rel_path: str) -> str:
    """
    Přečte Markdown soubor ze zdrojového adresáře docs/ a převede na HTML.

    Používá Python-Markdown (součást MkDocs závislostí — vždy dostupné).
    Automaticky odstraní YAML front matter, pokud je přítomen.

    Tento přístup nevyžaduje, aby soubor byl sestaven do site/ — funguje
    i pro soubory v exclude_docs (čteme ze zdrojového Markdown, ne z HTML).

    Podporované rozšíření: tables, attr_list, fenced_code.
    """
    import markdown as _md  # noqa: PLC0415 — MkDocs zaručuje přítomnost

    md_path = docs_dir / rel_path
    if not md_path.exists():
        _warn(f"Markdown soubor nenalezen: {md_path}")
        return ""

    text = md_path.read_text(encoding="utf-8")

    # Odstraň YAML front matter (---…--- na začátku souboru), pokud existuje
    text = re.sub(r"\A---[\s\S]*?---\s*\n", "", text, count=1).strip()

    return _md.markdown(
        text,
        extensions=["tables", "attr_list", "fenced_code"],
    )


def _extract_lesson_content(site_dir: Path, grade: int, week: int) -> str:
    """
    Extrahuje HTML obsah hodiny z vybudovaného souboru v site/.

    MkDocs Material umísťuje obsah stránky do:
      <article class="md-content__inner md-typeset">…</article>

    Odstraní tlačítka a zápatí specifická pro webové zobrazení.
    """
    html_path = site_dir / f"{grade}-rocnik" / f"tyden-{week:02d}" / "index.html"
    return _extract_article(html_path)


def _extract_article(html_path: Path) -> str:
    """
    Extrahuje a vyčistí obsah <article> z MkDocs Material HTML.

    Odstraní:
    - Tlačítka „Upravit stránku" / „Zobrazit zdroj" (.md-content__button)
    - Zápatí se zdrojovými metadaty (.md-source-file)
    - Prázdné řádky na začátku/konci
    """
    if not html_path.exists():
        return ""

    raw = html_path.read_text(encoding="utf-8")

    # Extrakce obsahu <article class="…md-typeset…">
    m = re.search(
        r'<article\b[^>]*class="[^"]*\bmd-typeset\b[^"]*"[^>]*>([\s\S]*?)</article>',
        raw,
    )
    if not m:
        return ""

    content = m.group(1)

    # Odstraň tlačítka (Upravit / Zobrazit zdroj)
    content = re.sub(
        r'<a\b[^>]*class="[^"]*\bmd-content__button\b[^"]*"[^>]*>[\s\S]*?</a>',
        "",
        content,
    )

    # Odstraň zápatí se zdrojovými metadaty
    content = re.sub(
        r'<div\b[^>]*class="[^"]*\bmd-source-file\b[^"]*"[^>]*>[\s\S]*?</div>',
        "",
        content,
    )

    # Odstraň prázdné script/noscript bloky (MkDocs Material výjimečně vkládá)
    content = re.sub(r'<script\b[^>]*>[\s\S]*?</script>', "", content)
    content = re.sub(r'<noscript\b[^>]*>[\s\S]*?</noscript>', "", content)

    return content.strip()


# ─────────────────────────────────────────────────────────────────────────────
# HTML šablony pro titulní stranu a metadata
# ─────────────────────────────────────────────────────────────────────────────

def _render_cover(grade: int, info: dict, rok: str) -> str:
    """
    Generuje HTML titulní strany ročníku.

    CSS třída .pdf-cover spolu s @page cover zajistí,
    že tato stránka:
    - nemá záhlaví ani zápatí
    - nemá standardní okraje (margin: 0)
    - zabírá celou stránku A4

    Inline style přepíše výchozí barvu z print.css.
    """
    barva = info["barva"]
    # Tmavší varianta pro gradient (80% neprůhlednosti)
    barva_light = barva + "bb"

    return (
        f'<div class="pdf-cover" '
        f'style="background: linear-gradient(160deg, {barva} 0%, {barva_light} 100%);">\n'
        f'  <div class="pdf-cover__logo">\n'
        f'    {_logo_svg()}\n'
        f'  </div>\n'
        f'  <div class="pdf-cover__skola">{SKOLA_NAZEV}</div>\n'
        f'  <div class="pdf-cover__nazev">{info["nazev"]}</div>\n'
        f'  <div class="pdf-cover__podtitul">{info["podtitul"]}</div>\n'
        f'  <div class="pdf-cover__meta">\n'
        f'    Školní vzdělávací program\n'
        f'    <span class="pdf-cover__sep">|</span>\n'
        f'    Informatika &ndash; 2.&nbsp;stupeň ZŠ\n'
        f'    <span class="pdf-cover__sep">|</span>\n'
        f'    {rok}\n'
        f'  </div>\n'
        f'  <div class="pdf-cover__autor">Autor: {AUTOR}</div>\n'
        f'  <div class="pdf-cover__rvp">'
        f'V souladu s RVP ZV (platnost od 1.&nbsp;9.&nbsp;2021)'
        f'</div>\n'
        f'</div>'
    )


def _logo_svg() -> str:
    """
    Výchozí SVG logo — stylizovaná žárovka v kruhu.

    Nahraďte skutečným logem školy:
      logo_path = Path(config["docs_dir"]) / "assets" / "images" / "logo-skola.svg"
      return logo_path.read_text(encoding="utf-8")
    """
    return (
        '<svg width="90" height="90" viewBox="0 0 90 90" fill="none" '
        'xmlns="http://www.w3.org/2000/svg">'
        '<circle cx="45" cy="45" r="42" '
        'stroke="rgba(255,255,255,0.35)" stroke-width="2" '
        'fill="rgba(255,255,255,0.12)"/>'
        # Žárovka
        '<circle cx="45" cy="38" r="14" fill="rgba(255,255,255,0.85)"/>'
        '<rect x="40" y="52" width="10" height="6" rx="1" '
        'fill="rgba(255,255,255,0.85)"/>'
        '<rect x="41" y="58" width="8" height="2" rx="1" '
        'fill="rgba(255,255,255,0.6)"/>'
        '<rect x="42" y="60" width="6" height="2" rx="1" '
        'fill="rgba(255,255,255,0.4)"/>'
        # Záře
        '<line x1="45" y1="18" x2="45" y2="13" '
        'stroke="rgba(255,255,255,0.5)" stroke-width="2" stroke-linecap="round"/>'
        '<line x1="62" y1="21" x2="65" y2="17" '
        'stroke="rgba(255,255,255,0.5)" stroke-width="2" stroke-linecap="round"/>'
        '<line x1="28" y1="21" x2="25" y2="17" '
        'stroke="rgba(255,255,255,0.5)" stroke-width="2" stroke-linecap="round"/>'
        '<line x1="70" y1="38" x2="75" y2="38" '
        'stroke="rgba(255,255,255,0.5)" stroke-width="2" stroke-linecap="round"/>'
        '<line x1="20" y1="38" x2="15" y2="38" '
        'stroke="rgba(255,255,255,0.5)" stroke-width="2" stroke-linecap="round"/>'
        '</svg>'
    )


def _render_metadata_fallback(grade: int, info: dict) -> str:
    """
    Záložní HTML pro metadata stránku — použije se, pokud
    soubory pdf-src/rvp-metadata.md a pdf-src/klic-kompetence.md
    nebyly vybudovány (chybí v not_in_nav nebo mkdocs.yml).
    """
    return (
        f"<h2>Informace o výuce — {info['nazev']}</h2>\n"
        f"<table class='pdf-table'>"
        f"<tbody>"
        f"<tr><td><strong>Oblast RVP ZV</strong></td>"
        f"<td>Informační a komunikační technologie – Informatika (INF)</td></tr>"
        f"<tr><td><strong>Platnost RVP ZV</strong></td>"
        f"<td>od 1. 9. 2021</td></tr>"
        f"<tr><td><strong>Počet hodin</strong></td>"
        f"<td>{info['pocet_tydnu']} hodin (1 hod. týdně)</td></tr>"
        f"</tbody></table>\n"
        f"<p><em>Pro úplné RVP ZV metadata a klíčové kompetence vytvořte soubory "
        f"docs/pdf-src/rvp-metadata.md a docs/pdf-src/klic-kompetence.md "
        f"a přidejte je do not_in_nav v mkdocs.yml.</em></p>"
    )


def _wrap_html_document(title: str, body: str) -> str:
    """Obalí obsah do kompletního HTML dokumentu pro WeasyPrint."""
    return (
        "<!DOCTYPE html>\n"
        '<html lang="cs">\n'
        "<head>\n"
        '  <meta charset="UTF-8">\n'
        f"  <title>Digitální kniha Informatiky – {title}</title>\n"
        "</head>\n"
        "<body>\n"
        f"{body}\n"
        "</body>\n"
        "</html>"
    )


# ─────────────────────────────────────────────────────────────────────────────
# CSS sestavení pro WeasyPrint
# ─────────────────────────────────────────────────────────────────────────────

def _compose_pdf_css(site_dir: Path) -> str:
    """
    Sestaví CSS řetězec pro WeasyPrint kombinací:
    1. extra.css — styly komponent (lesson-meta, goals, zadani-pc, …)
    2. print.css — pravidla stránkování, titulní strana, @page

    WeasyPrint renderuje vždy v tiskovém médiu, takže @media print {}
    bloky v print.css se plně uplatní.
    """
    parts: list[str] = []

    for filename in ("stylesheets/extra.css", "stylesheets/print.css"):
        css_path = site_dir / filename
        if css_path.exists():
            parts.append(css_path.read_text(encoding="utf-8"))
        else:
            _warn(f"CSS soubor nebyl nalezen: {css_path}")

    return "\n\n/* ── next file ── */\n\n".join(parts)


# ─────────────────────────────────────────────────────────────────────────────
# Pomocné funkce
# ─────────────────────────────────────────────────────────────────────────────

def _info(msg: str) -> None:
    print(f"  [pdf_build] {msg}")


def _warn(msg: str) -> None:
    print(f"  ⚠️  [pdf_build] {msg}")
