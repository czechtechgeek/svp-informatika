---
# Tento soubor je záměrně mimo navigaci (not_in_nav v mkdocs.yml).
# Slouží jako virtuální PDF zdroj 6. ročníku.
# Samotné PDF generuje hooks/pdf_build.py při mkdocs build.
# Výstup: site/pdf/6-rocnik.pdf
---

# Virtuální zdroj PDF — 6. ročník: Objevitel

!!! info "Automatické generování"
    PDF pro 6. ročník se **generuje automaticky** hookem `hooks/pdf_build.py`
    při každém spuštění `mkdocs build`. Výstupní soubor:
    `site/pdf/6-rocnik.pdf`

    Tento soubor slouží jako dokumentace struktury PDF a
    umožňuje vkládání sdílených sekcí přes `pymdownx.snippets`.

---

## Obsah PDF – 6. ročník: Objevitel

Vygenerované PDF má tuto strukturu:

1. **Titulní strana** — logo školy, název, ročník, autor, rok
2. **RVP ZV metadata** — vazba na vzdělávací obor, tabulka kódů
3. **Klíčové kompetence** — přehled rozvíjených kompetencí
4. **32 kompletních hodin** — každá hodina na nové stránce

---

## Sdílené sekce (vkládané přes snippets)

Níže jsou vloženy sdílené sekce, které se opakují ve všech ročníkových PDF.
Editujete je na **jednom místě** (`docs/pdf-src/rvp-metadata.md`
a `docs/pdf-src/klic-kompetence.md`) — změna se projeví ve všech PDF.

--8<-- "pdf-src/rvp-metadata.md"

---

--8<-- "pdf-src/klic-kompetence.md"

---

## Seznam hodin 6. ročníku

*Hodiny jsou do PDF přidány automaticky hookem — zde jsou uvedeny pro přehled.*

### 1. pololetí: Data a základy logiky

| Týden | Téma | Hlavní oblast RVP |
|-------|------|-------------------|
| 1 | Úvod: Pravidla učebny, digitální identita | INF-DTS |
| 2 | Informace vs. Data | INF-DIM |
| 3 | Kódování obrazu: rastrová grafika | INF-DIM |
| 4 | Kódování textu: ASCII, Unicode | INF-DIM |
| 5 | Binární logika: 0 a 1 | INF-IM |
| 6 | Souborový systém: složky, přípony | INF-DTS |
| 7 | Algoritmus v kuchyni: recept jako postup | INF-AP |
| 8 | Příkazy pro robota: přesnost instrukcí | INF-AP |
| 9 | Scratch I: prostředí, scéna, sprite | INF-AP |
| 10 | Scratch II: události, bloky | INF-AP |
| 11 | Scratch III: cykly | INF-AP |
| 12 | Scratch IV: zvuky, bubliny | INF-AP |
| 13 | Vánoční kódování: digitální přání | INF-AP |
| 14 | Opakování: projekt „Můj první program" | INF-AP |
| 15 | Pololetní reflexe: co vím o datech? | INF-DIM |

### 2. pololetí: Technologie a tabulky

| Týden | Téma | Hlavní oblast RVP |
|-------|------|-------------------|
| 16 | Hardware: monitor, myš, procesor | INF-DTS |
| 17 | Vstupy a výstupy: fotka do PC, papír z tiskárny | INF-DTS |
| 18 | Software: operační systém vs. aplikace | INF-DTS |
| 19 | Internet: prohlížeč a vyhledávač | INF-DTS |
| 20 | Bezpečné heslo: trezor v hlavě | INF-DTS |
| 21 | Netiketa: psaní e-mailů a zpráv | INF-TDO |
| 22 | Tabulky I: první buňky v Excelu/Sheets | INF-DIM |
| 23 | Tabulky II: formátování | INF-DIM |
| 24 | Tabulky III: součet a AutoSum | INF-DIM |
| 25 | Grafy I: sloupcový graf z dat třídy | INF-DIM |
| 26 | Velikonoce (rezerva) | — |
| 27 | Vyhledávání: ověřování pravdy na internetu | INF-DTS |
| 28 | Autorská práva: obrázky z Googlu | INF-TDO |
| 29 | Projekt: sběr dat (oblíbené zvíře) | INF-DIM |
| 30 | Projekt: dokončení a sdílení | INF-DIM |
| 31 | Rezerva: opakování hrou | — |
| 32 | Závěr: úklid digitálního portfolia | INF-DTS |
