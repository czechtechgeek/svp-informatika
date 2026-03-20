---
grade: 6
week: 3
time: 45
rvp_codes:
  - code: INF-INF-001-ZV9-001
    text: "Získá z dat informace, interpretuje data získaná pro řešení konkrétního problému."
  - code: INF-INF-001-ZV9-002
    text: Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.
goals:
  - "Žák vysvětlí, co je rastrový obrázek a jak se skládá z pixelů"
  - Žák zakóduje jednoduchý obrázek jako souřadnice nebo čísla barev na čtverečkovaném papíře
  - "Žák pochopí, že počítač ukládá obrázek jako čísla, ne jako „kresbu\""
  - Žák vytvoří vlastní pixel-art v online editoru a exportuje výsledek
time_budget:
  - type: board
    minutes: 5
  - type: unplugged
    minutes: 20
  - type: pc
    minutes: 15
friday_tip: "Pokud máte ve třídě Micro:bity, nechte žáky v závěru hodiny \"rozsvítit\" jejich pixel-art na displeji Micro:bitu. Je to pro ně silný moment, kdy vidí, že kód (čísla v programu) se okamžitě mění ve fyzické světlo (pixely)."
---

# 

## 💡 Metodický postup

### 1. Úvod: Co je pixel?

<span class="act board">🖊️ Tabule — 5 min</span>

Učitel přiblíží na interaktivní tabuli fotografii nebo obrázek z internetu tak, aby byly vidět jednotlivé čtverce (pixely). Vhodné je použít extrémní zoom v prohlížeči (Ctrl + kolečko myši).

**Otázka:** Co vidíte, když přiblížíte obrázek hodně blízko?

Učitel vysvětlí: počítač obrázek nevidí jako „kresbu" — vidí mřížku čísel. Každé číslo = jedna barva jednoho pixelu.

### 2. Aktivita: Pixel-art na papíře

<span class="act unplugged">✋ Bez počítače — 20 min</span>

Každý žák dostane čtverečkovaný papír (minimálně 10×10 čtverečků). Úkol:

1. **Nakreslete** jednoduchý obrázek (srdce, hvězda, domeček, písmeno) — max. 10×10 pixelů, 2 barvy: bílá a černá
2. **Zakódujte** obrázek: procházejte řádky zleva doprava, zapisujte kolik černých a kolik bílých čtverečků jde za sebou

Příklad kódu pro jeden řádek:
```
3B, 4Č, 3B  → 3 bílé, 4 černé, 3 bílé
```

3. Vyměňte kód se sousedem — spolužák zkusí z kódu obrázek **rekonstruovat** na svém papíře

### 3. Aktivita: Pixel-art na PC

<span class="act pc">💻 PC — 15 min</span>

<div class="zadani-pc">

Otevři [Piskel.com](https://www.piskelapp.com) — bezplatný online pixel-art editor (bez registrace).

**Úloha 1:** Vytvoř v editoru stejný obrázek, který jsi nakreslil/a na papíře (srdce, hvězda, domeček nebo písmeno, max. 10×10 pixelů).

**Úloha 2:** Přidej k obrázku druhou barvu — přebarvi aspoň část obrázku.

**Úloha 3:** Exportuj výsledek jako PNG: v menu vyber **File → Export → PNG** a ulož soubor.

**Pro rychlé žáky:** Vytvoř úplně nový obrázek — tentokrát animaci (Piskel umí animovat — přidej druhý snímek tlačítkem + vpravo dole).

Hotový soubor PNG ulož do složky Informatika na svém školním disku nebo odevzdej přes Google Classroom.

</div>

### 4. Shrnutí (5 min)

Učitel ukáže na tabuli příklad: černobílý obrázek 4×4 pixely → zapíše jako matici čísel (0 = bílá, 1 = černá).

**Závěrečná otázka:** Proč fotografie ve vysokém rozlišení zabírá víc místa na disku než malý obrázek?

## 📂 Podklady

- **Pixel-art editor:** [Piskel.com](https://www.piskelapp.com) — online, zdarma, bez registrace
- **Alternativa:** [Make8BitArt.com](https://make8bitart.com) — jednodušší rozhraní pro začátečníky
- **Kódování obrazu (CZ):** [imysleni.cz](https://imysleni.cz) — sekce „Reprezentace dat", aktivity o kódování obrazu pro ZŠ v češtině
- **Čtverečkovaný papír:** Vytvořte v MS Word (Vložit → Tabulka → 10 sloupců × 10 řádků, zmenšit buňky na čtverce) nebo stáhněte PDF s vyhledávačem „čtverečkovaný papír A4 PDF"
- **Rozšíření — Micro:bit:** Žáci naprogramují vlastní ikonu na 5×5 LED matici v [MakeCode](https://makecode.microbit.org) — propojení pixel-artu s fyzickým světem

!!! tip "Tip pro učitele"
    Aktivita výměny kódů mezi spolužáky je klíčová — žáci zažijí na vlastní kůži, jak počítač „čte" obrázek ze souboru. Pokud má třída čas navíc, vyzkoušejte kódování s více barvami (0=bílá, 1=šedá, 2=černá) a diskutujte, jak to zvyšuje velikost souboru.
