---
grade: 8
week: 3
time: 45
area: "Data, informace a modelování"
rvp_codes:
  - code: INF-INF-001-ZV9-002
    text: Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.
goals:
  - "**Použije** funkce MIN, MAX a PRŮMĚR (AVERAGE) pro základní datovou analýzu."
  - "**Kombinuje** MIN/MAX s funkcí IF k nalezení extrémů v podmíněném výběru."
  - "**Interpretuje** výsledky analýzy a formuluje závěry slovy."
  - "**Rozlišuje**, kdy použít MIN/MAX vs. seřazení dat."
time_budget:
  - type: discussion
    minutes: 8
  - type: board
    minutes: 10
  - type: pc
    minutes: 20
  - type: discussion
    minutes: 7
friday_tip: "Připravte data z reálného světa — třeba teploty v ČR za poslední rok, výsledky sportovního turnaje nebo ceny potravin. Žáci jsou mnohem více motivovaní, pokud data „existují doopravdy\"."
---

# Analýza: Hledání extrémů (MIN/MAX)

## 💡 Metodický postup

### 1. Úvod: Proč hledáme extrémy?

<span class="act discussion">💬 Diskuse — 8 min</span>

Učitel se ptá: „Kdy vás zajímá nejlepší nebo nejhorší výsledek?"
- Nejlevnější produkt v e-shopu
- Nejrychlejší závodník
- Nejvyšší teplota v létě
- Nejhůře placené povolání

Diskuse: Co by nám dala prostá vizuální prohlídka 1000 řádků tabulky? → Nic. Proto potřebujeme funkce.

---

### 2. Funkce MIN, MAX, AVERAGE — přehled

<span class="act board">🖊️ Tabule — 10 min</span>

Učitel ukáže na příkladu tabulky výsledků třídy:

```
=MIN(B2:B30)     → nejnižší hodnota v rozsahu
=MAX(B2:B30)     → nejvyšší hodnota v rozsahu
=AVERAGE(B2:B30) → průměrná hodnota
=COUNT(B2:B30)   → počet číselných hodnot
=COUNTA(B2:B30)  → počet neprázdných buněk
```

**Klíčový rozdíl:** MIN/MAX vrátí hodnotu, ne řádek. Jak zjistit, KDO má nejlepší výsledek? → Funkce MATCH nebo ruční hledání (pro pokročilé).

---

### 3. Praktická analýza

<span class="act pc">💻 PC — 20 min</span>

Žáci pracují s připravenou tabulkou — výsledky 30 žáků v pěti testech:

| Jméno | Test 1 | Test 2 | Test 3 | Test 4 | Test 5 | Průměr |
|-------|--------|--------|--------|--------|--------|--------|
| ... | ... | ... | ... | ... | ... | =AVERAGE(...) |

<div class="zadani-pc">

**Úkoly:**
1. Doplňte sloupec Průměr pro každého žáka
2. Pod tabulkou vypočítejte: MIN průměrů, MAX průměrů, průměr třídy
3. Přidejte sloupec „Nad průměrem?" — IF(průměr žáka > průměr třídy; "Ano"; "Ne")
4. *(Pro rychlé)* Podmíněné formátování — obarvěte buňky pod průměrem červeně

</div>

---

### 4. Interpretace výsledků

<span class="act discussion">💬 Diskuse — 7 min</span>

Žáci verbálně formulují závěry:
- „Nejlepší výsledek měl/a... s průměrem..."
- „Polovina třídy je nad průměrem" (nebo pod — záleží na rozložení)
- „Test č. X byl nejtěžší, protože průměr byl..."

Učitel upozorní: Průměr může být zavádějící — jeden extrém ho silně ovlivní (příklad: průměrný plat vs. medián platu).

---

## 📂 Zdroje a podklady

* **Vzorová data — teploty ČR:** Český hydrometeorologický ústav [chmi.cz](https://www.chmi.cz) — historická data ke stažení
* **Vzorová data — sport:** Výsledky ligových tabulek jsou dostupné na webech sportovních svazů
* **Připravená cvičná tabulka:** Vytvořte nebo sdílejte Google Sheet s 30 fiktivními žáky a 5 testy
* **Video (CZ):** YouTube — „funkce MIN MAX Excel průměr česky"
* **Rozšíření — MINIFS/MAXIFS:** Pro podmíněné extrémy (nejlepší výsledek dívek vs. chlapců)

---

!!! tip "Tip pro učitele"
    Rozdíl mezi průměrem a mediánem je skvělá příležitost pro mezipředmětové propojení s matematikou. Příklad: průměrná mzda v ČR (ovlivněná vysokými platy managementu) vs. mediánová mzda (polovina lidí vydělává méně). Žáci, kteří mají starší sourozence nebo pracující rodiče, toto snadno pochopí a aktivně přispějí do diskuse.
