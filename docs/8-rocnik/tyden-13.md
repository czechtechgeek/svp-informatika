# Projekt Robot II: Programování a ladění

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje algoritmus v programovacím jazyce</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-01</span><span style="color: #374151;">Žák rozloží problém na podproblémy a navrhne algoritmus</span></div>

## 💬 Tip pro pátek
Nechejte skupiny otestovat projekt kamarádem, ne autorem — „uživatel" najde jiné chyby než tvůrce. Peer testing je technika z profesionálního vývoje softwaru.

## 🎯 Cíle hodiny

- Žák implementuje svůj projekt z týdne 12 v MakeCode
- Žák systematicky ladí program — identifikuje a opravuje chyby metodou testování
- Žák upraví projekt na základě zpětné vazby od spolužáků (peer testing)
- Žák dokáže verbálně popsat, co jeho program dělá a proč

## 💡 Metodický postup

### 1. Krátká rekapitulace a start práce (5 min) — PC

Skupiny otevřou MakeCode a začínají podle návrhu z minulého týdne. Učitel připomene:
- Začněte s **minimální funkční verzí** (MVP) — základní funkce fungují
- Teprve pak přidávejte rozšíření
- Každou změnu otestujte v simulátoru PŘED nahráním na fyzické zařízení

### 2. Implementace projektu (25 min) — Micro:bit

Žáci pracují ve skupinách na implementaci. Učitel aktivně obchází a pomáhá:

**Časté problémy a řešení:**
- Program nereaguje na tlačítko → zkontrolujte, zda je blok mimo `opakovat stále`
- Animace je příliš rychlá → přidejte pauzu 200–500 ms
- Rádio nefunguje → zkontrolujte stejné číslo skupiny na obou zařízeních
- Program se chová nepředvídatelně → zkuste `przy spuštění` resetovat všechny proměnné

**Debugovací strategie:**
1. Izolujte problém — zakomentujte části kódu
2. Přidejte `zobrazit číslo` pro sledování hodnot proměnných
3. Testujte jeden vstup po druhém

### 3. Peer testing (10 min) — Micro:bit

Skupiny si navzájem vymění Micro:bity (nebo demonstrují na místě):
- „Tester" zkouší projekt bez instrukcí — co funguje, co ne?
- Autor sleduje a zapisuje si zpětnou vazbu
- 3 minuty testování, 2 minuty feedback

Formulář zpětné vazby:
- Co fungovalo dobře?
- Co fungovalo špatně nebo neočekávaně?
- Co byste přidali?

### 4. Závěrečná úprava a uložení (5 min) — PC

Skupiny zapracují nejdůležitější feedback a uloží finální verzi:
- Screenshot kódu do Google Drive / USB
- Příprava na případnou prezentaci po Vánocích (tyden-15)

## 📂 Podklady

- **MakeCode — debugování:** simulátor umožňuje krokování programu bloky
- **Peer testing formulář:** Připravte tisknutelný lístek (3 otázky výše)
- **GitHub — ukládání projektů:** MakeCode umožňuje propojení s GitHub pro verzování kódu (pro pokročilé)
- **Video — debugging tipy (EN):** microbit.org/teach → teaching resources
- **Záloha projektů:** Připomeňte žákům uložit projekt — MakeCode ukládá lokálně v prohlížeči, při vyčištění cache se ztratí

!!! tip "Tip pro učitele"
    Tato hodina je o procesu, ne o produktu. Každá skupina bude jinde — některé mají hotovo a ladí, jiné teprve začínají implementaci. To je v pořádku. Nejdůležitější je, aby žáci zažili cyklus: návrh → kód → test → oprava → znovu. Hodnocení zohledněte podle procesu a prezentace záměru, ne jen podle výsledného produktu.
