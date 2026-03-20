---
grade: 9
week: 3
time: 45
area: Modelování a simulace / Data a informace
rvp_codes:
  - code: INF-INF-001-ZV9-002
    text: Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
goals:
  - Žák vytvoří tabulkovou simulaci spoření s úrokem
  - Žák pochopí princip složeného úroku a jeho vliv v čase
  - Žák porovná různé finanční scénáře pomocí grafu
  - Žák propojí matematiku a informatiku při modelování reálných situací
time_budget:
  - type: board
    minutes: 8
  - type: pc
    minutes: 20
  - type: pc
    minutes: 12
  - type: discussion
    minutes: 5
friday_tip: "Finanční gramotnost je téma, které žáci v 9. třídě potřebují – brzy budou mít první výplatu nebo půjčku. Začněte provokativní otázkou: „Kdybyste dostali 10 000 Kč, co byste s nimi udělali?\" Různé odpovědi přirozeně otevřou téma spoření a investic."
---

# Simulace II: Finanční gramotnost

## 💡 Metodický postup

### 1. Úvod: Proč je čas důležitý v penězích

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel napíše na tabuli dvě jména:

- **Anička** začne spořit 500 Kč měsíčně ve věku 20 let
- **Honzík** začne spořit 500 Kč měsíčně ve věku 30 let

Otázka: „Kdo bude mít v 60 letech více? O kolik?" (intuitivní odhad žáků)

Pak ukáže výpočet: Anička má díky složenému úroku (5 % p.a.) zhruba **2× více** než Honzík – i když vložila celkem podobnou sumu.

Klíčový pojem: **Složený úrok** = úrok se připočítává k jistině a v dalším roce nese sám další úrok.

### 2. Tvorba simulace v tabulce

<span class="act pc">💻 PC — 20 min</span>

Žáci vytvoří tabulku v Google Sheets nebo LibreOffice Calc:

**Struktura simulace spoření:**

| Rok | Počáteční stav | Roční vklad | Úrok (5 %) | Konečný stav |
|-----|---------------|-------------|------------|-------------|
| 1   | 0             | 6 000       | 300        | 6 300       |
| 2   | 6 300         | 6 000       | 615        | 12 915      |
| ... | ...           | ...         | ...        | ...         |

Vzorce:
- Úrok: `=B2*0,05`
- Konečný stav: `=B2+C2+D2`
- Příští rok začátek: `=E2`

Po 10 řádcích (10 let) žáci přidají **graf** – spojnicový, osa X = rok, osa Y = úspory.

### 3. Experimenty: Co se změní?

<span class="act pc">💻 PC — 12 min</span>

Žáci zkusí tři scénáře a porovnají grafy:

1. **Základní:** 500 Kč/měsíc, 5 % úrok, 20 let
2. **Více vkladů:** 1 000 Kč/měsíc, 5 % úrok, 20 let
3. **Vyšší úrok:** 500 Kč/měsíc, 8 % úrok, 20 let

Závěr: Která proměnná má největší vliv? (Zpravidla čas > výše vkladu > úrok)

### 4. Diskuse: Inflace a reálná hodnota

<span class="act discussion">💬 Diskuse — 5 min</span>

Učitel doplní: „Ale co inflace?" – pokud inflace 3 %, ale úrok 5 %, reálný výnos je jen 2 %.

Propojení s aktuálním světem: Proč jsou spořicí účty s 2 % úrokem při 6 % inflaci nevýhodné?

## 📂 Podklady

- **Google Sheets šablona:** Připravte sdílenou šablonu s prázdnými buňkami – žáci doplní vzorce sami
- **Kalkulačka složeného úroku:** penize.cz – sekce kalkulačky
- **Video (CZ):** YouTube „složený úrok česky" nebo „jak funguje spoření"
- **Propojení s matematikou:** Vzorec složeného úroku: `K = P × (1 + r)^t`

!!! tip "Tip pro učitele"
    Žáci 9. třídy jsou překvapeni, jak velký rozdíl dělá čas. Ukažte jim výsledek za 40 let – čísla jsou ohromující a motivující zároveň. Pokud máte čas, přidejte scénář „půjčka" – stejný mechanismus funguje opačně (dluh roste). Propojte se třídním učitelem, pokud škola má projekt finanční gramotnosti.
