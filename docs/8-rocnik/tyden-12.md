---
grade: 8
week: 12
time: 45
area: "Algoritmizace a programování / Data, informace a modelování"
rvp_codes:
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
  - code: INF-INF-001-ZV9-003
    text: "Modeluje situace různými způsoby, včetně grafů nebo obdobných schémat."
goals:
  - "**Navrhne** vlastní projekt s Micro:bitem (definuje problém, vstupy, výstupy a algoritmus)."
  - "**Vytvoří** vývojový diagram nebo pseudokód pro svůj projekt."
  - "**Zdůvodní**, proč zvolil konkrétní senzory a akce."
  - "**Připraví** realizovatelný plán pro implementaci v dalším týdnu."
time_budget:
  - type: unplugged
    minutes: 10
  - type: unplugged
    minutes: 15
  - type: pc
    minutes: 13
  - type: unplugged
    minutes: 7
friday_tip: "Inspirativní přehled: ukažte žákům příklady žákovských projektů z minulých let nebo z microbit.org/showcase. Reálné výsledky vrstevníků motivují víc než jakýkoli učitelův výklad."
---

# Projekt Robot I: Návrh zařízení

## 💡 Metodický postup

### 1. Brainstorming témat

<span class="act unplugged">✋ Bez počítače — 10 min</span>

Učitel rozdá každé skupině (2–3 žáci) sadu karet s tématy pro inspiraci:

**Kategorie:** Bezpečnost a alarmy
- Alarm pro otevřenou skříňku (akcelerometr)
- Systém volání o pomoc (tlačítko + rádio)

**Kategorie:** Sport a zdraví
- Krokoměr s cílovou vzdáleností (akcelerometr + proměnné)
- Signalizace správné polohy při sezení (akcelerometr)

**Kategorie:** Příroda a prostředí
- Meteorologická stanice (teploměr + světlo)
- Indikátor teploty pro akvárko (teploměr + alarm)

**Kategorie:** Hry a zábava
- Rychlostní kvíz na tlačítkách (rádio + proměnné)
- Simulátor hodu kostkou (akcelerometr + náhoda)

Skupiny si vyberou nebo navrhnou vlastní téma.

---

### 2. Specifikace projektu

<span class="act unplugged">✋ Bez počítače — 15 min</span>

Každá skupina vyplní projektový list:

```
Název projektu: ________________________________
Popis (1–2 věty): _______________________________
Problém, který řeší: ____________________________

VSTUPY (co program přijímá):
□ Tlačítko A/B/A+B    □ Akcelerometr
□ Teploměr            □ Světelný senzor
□ Rádio               □ Jiné: _____________

VÝSTUPY (co program dělá):
□ LED matice          □ Zvuk
□ Rádio zpráva        □ Jiné: _____________

Algoritmus (pseudokód nebo diagram):
```

---

### 3. Skica algoritmu a kontrola proveditelnosti

<span class="act pc">💻 PC — 13 min</span>

<div class="zadani-pc" markdown="1">

Nakresli algoritmus svého projektu (flowchart nebo pseudokód) na papír nebo v [app.diagrams.net](https://app.diagrams.net) a zkontroluj:
- Mám správné senzory pro to, co chci měřit?
- Je rozsah projektu zvládnutelný za jednu hodinu programování?
- Co je minimální funkční verze (MVP)?

</div>

Učitel obchází a pomáhá zpřesnit zadání — příliš ambiciózní projekty se zužují na jádro funkčnosti.

---

### 4. Sdílení plánů

<span class="act unplugged">✋ Bez počítače — 7 min</span>

Každá skupina za 1 minutu představí svůj projekt třídě. Ostatní mohou klást otázky nebo navrhovat vylepšení.

---

## 📂 Zdroje a podklady

* **Projekty pro inspiraci:** [microbit.org/projects](https://microbit.org/projects) — filtrujte podle obtížnosti
* **Showcase žákovských projektů:** [microbit.org/do-your-bit](https://microbit.org/do-your-bit) — soutěžní projekty z celého světa
* **Projektový list:** Připravte tisknutelný formulář specifikace projektu (viz šablona výše)
* **Vývojové diagramy:** [app.diagrams.net](https://app.diagrams.net) pro digitální skicu algoritmu
* **Kritéria hodnocení:** Připravte a sdílejte hodnotící kritéria před začátkem — transparentnost motivuje

---

!!! tip "Tip pro učitele"
    Fáze návrhu je stejně důležitá jako programování — v praxi se odhaduje, že příprava zabírá 30–50 % celkového času projektu. Nedovolte žákům přeskočit specifikaci a rovnou „klikat v MakeCode". Skupiny se 2–3 žáky fungují lépe než jednotlivci nebo větší skupiny. Zužte ambiciózní projekty — lepší malý funkční produkt než velký nefunkční.
