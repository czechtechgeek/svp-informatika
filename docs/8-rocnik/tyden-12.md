# Projekt Robot I: Návrh zařízení

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování / Data, informace a modelování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-01</span><span style="color: #374151;">Žák rozloží problém na podproblémy a navrhne algoritmus</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-1-03" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-1-03</span><span style="color: #374151;">Žák vytvoří model pro řešení problému nebo organizaci informací</span></div>

## 💬 Tip pro pátek
Inspirativní přehled: ukažte žákům příklady žákovských projektů z minulých let nebo z microbit.org/showcase. Reálné výsledky vrstevníků motivují víc než jakýkoli učitelův výklad.

## 🎯 Cíle hodiny

- Žák navrhne vlastní projekt s Micro:bitem (definuje problém, vstupy, výstupy a algoritmus)
- Žák vytvoří vývojový diagram nebo pseudokód pro svůj projekt
- Žák zdůvodní, proč zvolil konkrétní senzory a akce
- Žák připraví realizovatelný plán pro implementaci v dalším týdnu

## 💡 Metodický postup

### 1. Brainstorming témat (10 min) — bez počítače

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

### 2. Specifikace projektu (15 min) — bez počítače

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

### 3. Skica algoritmu a kontrola proveditelnosti (13 min) — PC nebo papír

Skupiny skicují algoritmus (flowchart nebo pseudokód) a diskutují s učitelem:
- „Mají na to správné senzory?"
- „Je rozsah projektu zvládnutelný za jednu hodinu programování?"
- „Co je minimální funkční verze (MVP)?"

Učitel obchází a pomáhá zpřesnit zadání — příliš ambiciózní projekty se zužují na jádro funkčnosti.

### 4. Sdílení plánů (7 min) — bez počítače

Každá skupina za 1 minutu představí svůj projekt třídě. Ostatní mohou klást otázky nebo navrhovat vylepšení.

## 📂 Podklady

- **Projekty pro inspiraci:** [microbit.org/projects](https://microbit.org/projects) — filtrujte podle obtížnosti
- **Showcase žákovských projektů:** [microbit.org/do-your-bit](https://microbit.org/do-your-bit) — soutěžní projekty z celého světa
- **Projektový list:** Připravte tisknutelný formulář specifikace projektu (viz šablona výše)
- **Vývojové diagramy:** [app.diagrams.net](https://app.diagrams.net) pro digitální skicu algoritmu
- **Kritéria hodnocení:** Připravte a sdílejte hodnotící kritéria před začátkem — transparentnost motivuje

!!! tip "Tip pro učitele"
    Fáze návrhu je stejně důležitá jako programování — v praxi se odhaduje, že příprava zabírá 30–50 % celkového času projektu. Nedovolte žákům přeskočit specifikaci a rovnou „klikat v MakeCode". Skupiny se 2–3 žáky fungují lépe než jednotlivci nebo větší skupiny. Zužte ambiciózní projekty — lepší malý funkční produkt než velký nefunkční.
