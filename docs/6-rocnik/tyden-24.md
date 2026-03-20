---
grade: 6
week: 24
time: 45
area: "Data, informace a modelování"
rvp_codes:
  - code: INF-INF-001-ZV9-001
    text: "Získá z dat informace, interpretuje data získaná pro řešení konkrétního problému."
  - code: INF-INF-001-ZV9-002
    text: Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.
goals:
  - "Žák zapíše jednoduchý vzorec začínající znakem `=` (např. `=A1+B1`)"
  - "Žák použije funkci `SUMA` nebo tlačítko AutoSum pro součet rozsahu buněk"
  - "Žák pochopí, že vzorec se automaticky přepočítá při změně vstupních dat"
  - Žák rozliší vzorec (výpočet) od hodnoty (číslo zadané ručně)
time_budget:
  - type: board
    minutes: 7
  - type: pc
    minutes: 15
  - type: pc
    minutes: 13
friday_tip: "V pátek si zahrajte **„Magický součet\"** — učitel změní jedno číslo v tabulce a třída sleduje, jak se výsledek vzorce okamžitě změní. Žáci hádají, jaké číslo učitel zadal. Demystifikuje to „kouzlo\" vzorců — žáci vidí, že tabulkový procesor opravdu počítá v reálném čase."
---

# Tabulky III: Součet a AutoSum

## 💡 Metodický postup

### 1. Úvod: Vzorec vs. číslo

<span class="act board">🖊️ Tabule — 7 min</span>

Učitel ukáže na tabuli:

```
Buňka C1 obsahuje číslo:    45
Buňka C1 obsahuje vzorec:   =A1+B1
```

Otázka: „Jaký je rozdíl?" → Číslo se nemění. Vzorec se přepočítá vždy, když se změní A1 nebo B1.

Zlaté pravidlo: **vzorce vždy začínají znakem `=`**

Základní operátory: `+` `-` `*` `/` (násobení, dělení)

### 2. Výukový průchod: Moje první vzorce

<span class="act pc">💻 PC — 15 min</span>

<div class="zadani-pc" markdown="1">

Otevři novou tabulku v Excelu nebo Google Sheets a do buněk zadej tato čísla a vzorce — sleduj, co se stane:

```
   A          B          C
1  10         20         =A1+B1     → výsledek: 30
2  100        =A2*2                 → výsledek: 200
3  =A1+A2
```

Pamatuj: **vzorec vždy začíná znakem `=`**. Pokud napíšeš `A1+B1` bez rovnítka, tabulka to zobrazí jako text, ne jako výsledek výpočtu.

Pak vytvoř tabulku výdajů pro jeden školní týden:

| Den | Svačina (Kč) | Oběd (Kč) | Celkem |
|-----|-------------|-----------|--------|
| Po  | 25          | 60        | =B2+C2 |
| Út  | 30          | 55        | =B3+C3 |
| St  | 20          | 65        | =B4+C4 |
| Čt  | 35          | 60        | =B5+C5 |
| Pá  | 15          | 55        | =B6+C6 |
| **Součet** | **=SUMA(B2:B6)** | **=SUMA(C2:C6)** | **=SUMA(D2:D6)** |

Změň jedno číslo ve sloupci „Svačina" — co se stane se součty?

</div>

### 3. Aktivita: AutoSum

<span class="act pc">💻 PC — 13 min</span>

<div class="zadani-pc" markdown="1">

Nauč se používat funkci **AutoSum** pro rychlý součet sloupce:

1. Klikni na prázdnou buňku **pod** sloupcem čísel
2. Stiskni tlačítko **AutoSum** (Σ) na panelu nástrojů — nebo zkratku `Alt+Shift+0`
3. Excel nebo Sheets sám navrhne rozsah buněk — zkontroluj ho a stiskni **Enter**

**Úkol:** Vytvoř tabulku „Měsíční výdaje" s 5 kategoriemi (Jídlo, Doprava, Sport, Kultura, Ostatní) a vymyšlenými čísly. Všechny součty doplň pomocí funkce SUMA nebo AutoSum.

**Pro rychlé žáky:** Přidej do tabulky sloupec „Průměr" a vypočítej průměrné výdaje na kategorii pomocí funkce `=PRŮMĚR(...)` (v Excelu) nebo `=AVERAGE(...)` (v Google Sheets).

Hotovou tabulku ulož a odevzdej přes Google Classroom.

</div>

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
