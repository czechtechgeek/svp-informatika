---
# Tato stránka je záměrně mimo navigaci (viz not_in_nav v mkdocs.yml).
# Slouží jako živá ukázka struktury titulní strany PDF.
# Skutečná titulní strana se generuje inline v hooks/pdf_build.py.
---

# Vzor titulní strany PDF

Titulní strana každého per-ročníkového PDF se generuje automaticky
hookem `hooks/pdf_build.py` při spuštění `mkdocs build`.

Níže je **živá ukázka** HTML struktury titulní strany. V PDF se zobrazí
jako plná barevná stránka A4 bez záhlaví a zápatí (CSS `@page cover`).

---

## HTML šablona titulní strany

Každý ročník má vlastní barvu pozadí (konfigurováno v `GRADES` slovníku
v `hooks/pdf_build.py`):

| Ročník | Barva | Podtitul |
|--------|-------|----------|
| 6. ročník – Objevitel | `#004d40` (tmavozelená) | Data a základy logiky · Technologie a tabulky |
| 7. ročník – Tvůrce | `#1a237e` (tmavomodrá) | Modelování a podmínky · Sítě a spolupráce |
| 8. ročník – Analytik | `#880e4f` (tmavočervená) | Data a robotika · Internet a bezpečnost |
| 9. ročník – Expert | `#4a148c` (tmavofialová) | Simulace a kód · AI a společnost |

---

## Živá ukázka struktury

<div class="pdf-cover" style="background: linear-gradient(160deg, #004d40 0%, #00695ccc 100%); min-height: 420px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 40px; border-radius: 8px; color: white; margin: 2rem 0;">
  <div style="font-size: 2rem; margin-bottom: 1rem; opacity: 0.9;">💡</div>
  <div class="pdf-cover__skola" style="font-size: 0.9rem; letter-spacing: 0.15em; text-transform: uppercase; opacity: 0.8; margin-bottom: 1.5rem;">Základní škola</div>
  <div class="pdf-cover__nazev" style="font-size: 2rem; font-weight: 700; line-height: 1.2; margin-bottom: 0.5rem;">6. ročník – Objevitel</div>
  <div class="pdf-cover__podtitul" style="font-size: 1rem; font-weight: 300; opacity: 0.75; margin-bottom: 2rem;">Data a základy logiky · Technologie a tabulky</div>
  <div class="pdf-cover__meta" style="font-size: 0.8rem; opacity: 0.65; margin-bottom: 0.3rem;">Školní vzdělávací program · Informatika · 2. stupeň ZŠ <span style="margin: 0 6px; opacity: 0.5;">|</span> 2025</div>
  <div class="pdf-cover__autor" style="font-size: 0.85rem; opacity: 0.8; margin-bottom: 0.2rem;">Autor: Mgr. Jan Novák</div>
  <div class="pdf-cover__rvp" style="font-size: 0.75rem; opacity: 0.6; font-style: italic;">V souladu s RVP ZV (platnost od 1. 9. 2021)</div>
</div>

---

## Jak přizpůsobit titulní stranu

Titulní stranu upravujete v souboru `hooks/pdf_build.py`, ve funkci `_cover_html()`.

Pro použití skutečného loga školy (soubor SVG nebo PNG):

```python
# V hooks/pdf_build.py — funkce _cover_html()

# Místo inline SVG vložte:
logo_path = Path(config["docs_dir"]) / "assets" / "images" / "logo-skola.svg"
with open(logo_path) as f:
    logo_svg = f.read()

# Pak použijte logo_svg v HTML šabloně místo emoji SVG
```

### Kde měnit texty

| Co chcete změnit | Kde v `pdf_build.py` |
|------------------|----------------------|
| Název školy | Konstanta `SKOLA_NAZEV` |
| Jméno autora | Konstanta `AUTOR` |
| Rok vydání | Konstanta `ROK` (výchozí = aktuální rok) |
| Barvu ročníku | Klíč `"barva"` ve slovníku `GRADES[grade]` |
| Podtitul ročníku | Klíč `"podtitul"` ve slovníku `GRADES[grade]` |

!!! tip "Tip pro správce"
    Pro každý školní rok stačí aktualizovat konstantu `ROK` nebo ji nechat
    automaticky nastavit z `date.today().year` (výchozí chování).
