# Kódování obrazu: Čtverečkovaný papír jako rastr

## 📋 Vazba na RVP ZV (Informatika)
- Oblast: Data, informace a modelování
- **Výstup:** <div class="curriculumTag" data-code="I-9-1-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-1-02</span><span style="color: #374151;">Žák modeluje a simuluje procesy a systémy</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-1-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-1-02</span><span style="color: #374151;">Žák interpretuje data a vyvozuje z nich závěry</span></div>

## 💬 Tip pro pátek
Pokud máte ve třídě Micro:bity, nechte žáky v závěru hodiny "rozsvítit" jejich pixel-art na displeji Micro:bitu. Je to pro ně silný moment, kdy vidí, že kód (čísla v programu) se okamžitě mění ve fyzické světlo (pixely).

## 🎯 Cíle hodiny

- Žák vysvětlí, co je rastrový obrázek a jak se skládá z pixelů
- Žák zakóduje jednoduchý obrázek jako souřadnice nebo čísla barev na čtverečkovaném papíře
- Žák pochopí, že počítač ukládá obrázek jako čísla, ne jako „kresbu"
- Žák vytvoří vlastní pixel-art v online editoru a exportuje výsledek

## 💡 Metodický postup

### 1. Úvod: Co je pixel? (5 min) — interaktivní tabule

Učitel přiblíží na interaktivní tabuli fotografii nebo obrázek z internetu tak, aby byly vidět jednotlivé čtverce (pixely). Vhodné je použít extrémní zoom v prohlížeči (Ctrl + kolečko myši).

**Otázka:** Co vidíte, když přiblížíte obrázek hodně blízko?

Učitel vysvětlí: počítač obrázek nevidí jako „kresbu" — vidí mřížku čísel. Každé číslo = jedna barva jednoho pixelu.

### 2. Aktivita: Pixel-art na papíře (20 min) — bez počítače

Každý žák dostane čtverečkovaný papír (minimálně 10×10 čtverečků). Úkol:

1. **Nakreslete** jednoduchý obrázek (srdce, hvězda, domeček, písmeno) — max. 10×10 pixelů, 2 barvy: bílá a černá
2. **Zakódujte** obrázek: procházejte řádky zleva doprava, zapisujte kolik černých a kolik bílých čtverečků jde za sebou

Příklad kódu pro jeden řádek:
```
3B, 4Č, 3B  → 3 bílé, 4 černé, 3 bílé
```

3. Vyměňte kód se sousedem — spolužák zkusí z kódu obrázek **rekonstruovat** na svém papíře

### 3. Aktivita: Pixel-art na PC (15 min) — PC

Žáci otevřou [Piskel.com](https://www.piskelapp.com) — bezplatný online pixel-art editor.

Úkol:
- Vytvořte stejný obrázek jako na papíře, ale v Piskel editoru
- Zkuste přidat druhou barvu
- Exportujte jako PNG (File → Export → PNG)

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

