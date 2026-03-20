# 📉 Analýza: Hledání extrémů (MIN/MAX)

> **Stav:** `⬜ Nekontrolováno`

### 📋 Kontext a cíle
> **RVP ZV (Informatika):** Data, informace a modelování
> **Kód:** `INF-INF-001-ZV9-002` – *Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.*

**Po hodině žák:**
* **Použije** funkce MIN, MAX a PRŮMĚR (AVERAGE) pro základní datovou analýzu.
* **Kombinuje** MIN/MAX s funkcí IF k nalezení extrémů v podmíněném výběru.
* **Interpretuje** výsledky analýzy a formuluje závěry slovy.
* **Rozlišuje**, kdy použít MIN/MAX vs. seřazení dat.

---

### 💡 Metodický postup (45 min)

#### 1. Úvod: Proč hledáme extrémy? (8 min)
*Diskuze u tabule.*

Učitel se ptá: „Kdy vás zajímá nejlepší nebo nejhorší výsledek?"
- Nejlevnější produkt v e-shopu
- Nejrychlejší závodník
- Nejvyšší teplota v létě
- Nejhůře placené povolání

Diskuse: Co by nám dala prostá vizuální prohlídka 1000 řádků tabulky? → Nic. Proto potřebujeme funkce.

---

#### 2. Funkce MIN, MAX, AVERAGE — přehled (10 min)
*Tabule — výklad.*

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

#### 3. Praktická analýza (20 min)
*Práce na PC.*

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

#### 4. Interpretace výsledků (7 min)
*Diskuze.*

Žáci verbálně formulují závěry:
- „Nejlepší výsledek měl/a... s průměrem..."
- „Polovina třídy je nad průměrem" (nebo pod — záleží na rozložení)
- „Test č. X byl nejtěžší, protože průměr byl..."

Učitel upozorní: Průměr může být zavádějící — jeden extrém ho silně ovlivní (příklad: průměrný plat vs. medián platu).

---

### 🛠️ Zdroje a nástroje

* **Vzorová data — teploty ČR:** Český hydrometeorologický ústav [chmi.cz](https://www.chmi.cz) — historická data ke stažení
* **Vzorová data — sport:** Výsledky ligových tabulek jsou dostupné na webech sportovních svazů
* **Připravená cvičná tabulka:** Vytvořte nebo sdílejte Google Sheet s 30 fiktivními žáky a 5 testy
* **Video (CZ):** YouTube — „funkce MIN MAX Excel průměr česky"
* **Rozšíření — MINIFS/MAXIFS:** Pro podmíněné extrémy (nejlepší výsledek dívek vs. chlapců)

---

> 💡 **Tip pro učitele:**
> Rozdíl mezi průměrem a mediánem je skvělá příležitost pro mezipředmětové propojení s matematikou. Příklad: průměrná mzda v ČR (ovlivněná vysokými platy managementu) vs. mediánová mzda (polovina lidí vydělává méně). Žáci, kteří mají starší sourozence nebo pracující rodiče, toto snadno pochopí a aktivně přispějí do diskuse.

> 💬 **Tip pro pátek:** Připravte data z reálného světa — třeba teploty v ČR za poslední rok, výsledky sportovního turnaje nebo ceny potravin. Žáci jsou mnohem více motivovaní, pokud data „existují doopravdy".
