---
grade: 6
week: 25
time: 45
area: "Data, informace a modelování"
rvp_codes:
  - code: INF-INF-001-ZV9-002
    text: Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.
  - code: INF-INF-001-ZV9-003
    text: "Modeluje situace různými způsoby, včetně grafů nebo obdobných schémat."
goals:
  - Žák vybere vhodná data pro vizualizaci a označí je v tabulce
  - "Žák vloží sloupcový graf a pochopí, co osy X a Y zobrazují"
  - Žák přidá název grafu a popisky os
  - "Žák vysvětlí, proč je graf lepší než samotná čísla pro komunikaci dat"
time_budget:
  - type: board
    minutes: 7
  - type: unplugged
    minutes: 8
  - type: pc
    minutes: 20
friday_tip: "Pátky jsou výborné pro **„Hlasování živě\"** — učitel klade otázky a žáci hlasují zvednutím ruky, učitel zapisuje na tabuli. Data pak v reálu zadají do tabulky a vytvoří graf. Vidět svůj hlas v grafu je silný zážitek — „to jsou opravdu naše data!\""
---

# Grafy I: Sloupcový graf z dat třídy

## 💡 Metodický postup

### 1. Úvod: Graf místo čísel

<span class="act board">🖊️ Tabule — 7 min</span>

Učitel promítne tabulku s čísly a vedle ní hotový sloupcový graf ze stejných dat.

Otázka: „Z čeho rychleji pochopíte, co je nejoblíbenější jídlo?" → Graf vyhraje vždy.

Typy grafů a kdy je použít:
- **Sloupcový / pruhový** — porovnání kategorií (oblíbené sporty, počty hlasů)
- **Koláčový** — podíl celku (% zastoupení)
- **Spojnicový** — vývoj v čase (teplota v průběhu dne)

### 2. Aktivita: Sběr dat ze třídy

<span class="act unplugged">✋ Bez počítače — 8 min</span>

Žáci hlasují o oblíbené barvě (nebo jiné jednoduché kategorii dle učitele). Učitel zapíše výsledky na tabuli:

| Barva | Počet hlasů |
|-------|-------------|
| Modrá | 8 |
| Červená | 5 |
| Zelená | 7 |
| Žlutá | 3 |
| Jiná | 4 |

### 3. Aktivita: Vytvoření grafu

<span class="act pc">💻 PC — 20 min</span>

Žáci zadají data ze sběru do tabulky a vytvoří graf:

**Excel:**
1. Označte data (A1:B6 včetně záhlaví)
2. Záložka Vložení → Graf → Sloupcový → 2D sloupcový
3. Klikněte na „Název grafu" a napište vlastní název
4. Klikněte na osu X → přidat popis „Barva"
5. Klikněte na osu Y → přidat popis „Počet žáků"

**Google Sheets:**
1. Označte data → Vložení → Graf
2. Sheets automaticky navrhne typ — zkontrolujte, zda je „Sloupcový"
3. V pravém panelu upravte název a popisky os

### 4. Shrnutí (5 min)

Žáci ukáží graf třídě. Diskuse: „Co nám graf říká? Co bychom se dozvěděli, kdybychom měli data z celé školy?"

**Klíčové pojmy:** osa X, osa Y, datová řada, sloupcový graf, vizualizace dat

## 📂 Podklady

- **Google Sheets — vkládání grafů:** [support.google.com/docs](https://support.google.com/docs) — hledejte „vložit graf"
- **Excel grafy (CZ):** Podpora Microsoft Office — „vytvořit graf Excel"
- **Inspirace vizualizacemi:** [informationisbeautiful.net](https://informationisbeautiful.net) — příklady krásných datových vizualizací (EN)
- **Video (CZ):** YouTube „Excel jak udělat graf" nebo „Google Sheets graf sloupcový"
- **Sběr dat online:** Google Formuláře → odpovědi automaticky do tabulky → okamžitý graf — pro pokročilé třídy

!!! tip "Tip pro učitele"
    Pro sběr dat využijte Google Formulář — učitel ho připraví předem, žáci vyplní na telefonu nebo PC, výsledky se okamžitě zobrazí v tabulce. Žáci pak pracují s reálnými daty ze své třídy, ne s vymyšlenými čísly. To dramaticky zvyšuje zájem o téma. Formulář s výsledky si nechte pro projekt v týdnu 28–29.
