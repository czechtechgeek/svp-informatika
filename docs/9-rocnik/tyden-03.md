# Simulace II: Finanční gramotnost

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Modelování a simulace / Data a informace
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-001-ZV9-002" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-001-ZV9-002</span><span style="color: #374151;">Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-002-ZV9-007" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-002-ZV9-007</span><span style="color: #374151;">V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné.</span></div>

## 💬 Tip pro pátek
Finanční gramotnost je téma, které žáci v 9. třídě potřebují – brzy budou mít první výplatu nebo půjčku. Začněte provokativní otázkou: „Kdybyste dostali 10 000 Kč, co byste s nimi udělali?" Různé odpovědi přirozeně otevřou téma spoření a investic.

## 🎯 Cíle hodiny

- Žák vytvoří tabulkovou simulaci spoření s úrokem
- Žák pochopí princip složeného úroku a jeho vliv v čase
- Žák porovná různé finanční scénáře pomocí grafu
- Žák propojí matematiku a informatiku při modelování reálných situací

## 💡 Metodický postup

### 1. Úvod: Proč je čas důležitý v penězích (8 min) — tabule

Učitel napíše na tabuli dvě jména:

- **Anička** začne spořit 500 Kč měsíčně ve věku 20 let
- **Honzík** začne spořit 500 Kč měsíčně ve věku 30 let

Otázka: „Kdo bude mít v 60 letech více? O kolik?" (intuitivní odhad žáků)

Pak ukáže výpočet: Anička má díky složenému úroku (5 % p.a.) zhruba **2× více** než Honzík – i když vložila celkem podobnou sumu.

Klíčový pojem: **Složený úrok** = úrok se připočítává k jistině a v dalším roce nese sám další úrok.

### 2. Tvorba simulace v tabulce (20 min) — PC

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

### 3. Experimenty: Co se změní? (12 min) — PC

Žáci zkusí tři scénáře a porovnají grafy:

1. **Základní:** 500 Kč/měsíc, 5 % úrok, 20 let
2. **Více vkladů:** 1 000 Kč/měsíc, 5 % úrok, 20 let
3. **Vyšší úrok:** 500 Kč/měsíc, 8 % úrok, 20 let

Závěr: Která proměnná má největší vliv? (Zpravidla čas > výše vkladu > úrok)

### 4. Diskuse: Inflace a reálná hodnota (5 min) — diskuse

Učitel doplní: „Ale co inflace?" – pokud inflace 3 %, ale úrok 5 %, reálný výnos je jen 2 %.

Propojení s aktuálním světem: Proč jsou spořicí účty s 2 % úrokem při 6 % inflaci nevýhodné?

## 📂 Podklady

- **Google Sheets šablona:** Připravte sdílenou šablonu s prázdnými buňkami – žáci doplní vzorce sami
- **Kalkulačka složeného úroku:** penize.cz – sekce kalkulačky
- **Video (CZ):** YouTube „složený úrok česky" nebo „jak funguje spoření"
- **Propojení s matematikou:** Vzorec složeného úroku: `K = P × (1 + r)^t`

!!! tip "Tip pro učitele"
    Žáci 9. třídy jsou překvapeni, jak velký rozdíl dělá čas. Ukažte jim výsledek za 40 let – čísla jsou ohromující a motivující zároveň. Pokud máte čas, přidejte scénář „půjčka" – stejný mechanismus funguje opačně (dluh roste). Propojte se třídním učitelem, pokud škola má projekt finanční gramotnosti.
