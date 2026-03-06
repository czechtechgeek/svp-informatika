# Tabulky III: Součet a AutoSum

## 🎯 Cíle hodiny

- Žák zapíše jednoduchý vzorec začínající znakem `=` (např. `=A1+B1`)
- Žák použije funkci `SUMA` nebo tlačítko AutoSum pro součet rozsahu buněk
- Žák pochopí, že vzorec se automaticky přepočítá při změně vstupních dat
- Žák rozliší vzorec (výpočet) od hodnoty (číslo zadané ručně)

## 🎯 Vazba na RVP ZV (Informatika)
- **Oblast:** Data, informace a modelování
- **Výstup:** <div class="curriculumTag" data-code="I-9-1-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-1-01</span><span style="color: #374151;">Žák modeluje a simuluje procesy a systémy</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-1-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-1-02</span><span style="color: #374151;">Žák interpretuje data a vyvozuje z nich závěry</span></div>

## 💡 Metodický tip pro pátky
V pátek si zahrajte **„Magický součet"** — učitel změní jedno číslo v tabulce a třída sleduje, jak se výsledek vzorce okamžitě změní. Žáci hádají, jaké číslo učitel zadal. Demystifikuje to „kouzlo" vzorců — žáci vidí, že tabulkový procesor opravdu počítá v reálném čase.

## 💡 Metodický postup

### 1. Úvod: Vzorec vs. číslo (7 min) — tabule

Učitel ukáže na tabuli:

```
Buňka C1 obsahuje číslo:    45
Buňka C1 obsahuje vzorec:   =A1+B1
```

Otázka: „Jaký je rozdíl?" → Číslo se nemění. Vzorec se přepočítá vždy, když se změní A1 nebo B1.

Zlaté pravidlo: **vzorce vždy začínají znakem `=`**

Základní operátory: `+` `-` `*` `/` (násobení, dělení)

### 2. Výukový průchod: Moje první vzorce (15 min) — PC, učitel na tabuli

Žáci vytvoří nový list a zadají:

```
   A          B          C
1  10         20         =A1+B1     → výsledek: 30
2  100        =A2*2      (bonus)    → výsledek: 200
3  =A1+A2     (zkuste!)
```

Pak naformátují jako tabulku výdajů třídy:

| Den | Svačina (Kč) | Oběd (Kč) | Celkem |
|-----|-------------|-----------|--------|
| Po  | 25          | 60        | =B2+C2 |
| Út  | 30          | 55        | =B3+C3 |
| ...  | ...         | ...       | ...    |
| **Součet** | **=SUMA(B2:B6)** | **=SUMA(C2:C6)** | **=SUMA(D2:D6)** |

### 3. Aktivita: AutoSum (13 min) — PC

Žáci se naučí rychlý způsob:
1. Klikněte na buňku pod sloupcem čísel
2. Stiskněte tlačítko **AutoSum** (Σ) nebo zkratku `Alt+Shift+0`
3. Excel/Sheets sám navrhne rozsah — stiskněte Enter

Úkol: vytvořte tabulku „Měsíční výdaje" s 5 kategoriemi (jídlo, doprava, sport, kultura, ostatní) a doplňte součty pomocí SUMA.

### 4. Shrnutí (5 min)

Žáci změní jedno číslo v tabulce a sledují, jak se přepočítají všechny součty. „To je síla tabulkového procesoru — nemusíte přepočítávat ručně."

## 📂 Podklady

- **Funkce SUMA — nápověda (CZ):** Podpora Microsoft Office — hledejte „SUMA funkce Excel"
- **Google Sheets funkce:** [support.google.com/docs](https://support.google.com/docs) — kompletní referenční příručka v češtině
- **Procvičování vzorců:** [exceljet.net](https://exceljet.net) — stovky vzorových příkladů (EN)
- **Video (CZ):** YouTube „Excel vzorce pro začátečníky" nebo „SUMA funkce Google Sheets"
- **Šablona „Měsíční výdaje":** Připravte předvyplněný soubor — žáci pouze doplňují čísla a píší vzorce do označených buněk

!!! tip "Tip pro učitele"
    Nejčastější chyba žáků: zapomenou napsat `=` na začátku vzorce — tabulka zobrazí text `A1+B1` místo výsledku. Udělejte z toho lekci: „Všimli jste si rozdílu? Co musím udělat jinak?" Chyba je nejlepší učitel. Další problém: česká verze Excelu používá středník místo čárky v argumentech funkcí (`=SUMA(A1:A5)` funguje, `=SUM(A1,A5)` může selhat).
