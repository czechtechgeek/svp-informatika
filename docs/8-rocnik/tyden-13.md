---
grade: 8
week: 13
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - "**Implementuje** svůj projekt z týdne 12 v MakeCode."
  - "**Systematicky ladí** program — identifikuje a opravuje chyby metodou testování."
  - "**Upraví** projekt na základě zpětné vazby od spolužáků (peer testing)."
  - "**Dokáže** verbálně popsat, co jeho program dělá a proč."
time_budget:
  - type: pc
    minutes: 5
  - type: board
    minutes: 25
  - type: review
    minutes: 10
  - type: pc
    minutes: 5
friday_tip: "Nechejte skupiny otestovat projekt kamarádem, ne autorem — „uživatel\" najde jiné chyby než tvůrce. Peer testing je technika z profesionálního vývoje softwaru."
---

# ️ Projekt Robot II: Programování a ladění

## 💡 Metodický postup

### 1. Krátká rekapitulace a start práce

<span class="act pc">💻 PC — 5 min</span>

<div class="zadani-pc" markdown="1">

Otevřete MakeCode a začněte programovat podle návrhu z minulého týdne. Pamatujte:
- Začněte s **minimální funkční verzí** (MVP) — základní funkce fungují
- Teprve pak přidávejte rozšíření
- Každou změnu otestujte v simulátoru PŘED nahráním na fyzické zařízení

</div>

---

### 2. Implementace projektu

<span class="act board">🖊️ Tabule — 25 min</span>

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

---

### 3. Peer testing

<span class="act review">🔍 Reflexe — 10 min</span>

Skupiny si navzájem vymění Micro:bity (nebo demonstrují na místě):
- „Tester" zkouší projekt bez instrukcí — co funguje, co ne?
- Autor sleduje a zapisuje si zpětnou vazbu
- 3 minuty testování, 2 minuty feedback

Formulář zpětné vazby:
- Co fungovalo dobře?
- Co fungovalo špatně nebo neočekávaně?
- Co byste přidali?

---

### 4. Závěrečná úprava a uložení

<span class="act pc">💻 PC — 5 min</span>

<div class="zadani-pc" markdown="1">

Zapracujte nejdůležitější feedback a uložte finální verzi projektu:
- Screenshot kódu do Google Drive / USB
- Připravte se na případnou prezentaci po Vánocích (tyden-15)

</div>

---

## 📂 Zdroje a podklady

* **MakeCode — debugování:** simulátor umožňuje krokování programu bloky
* **Peer testing formulář:** Připravte tisknutelný lístek (3 otázky výše)
* **GitHub — ukládání projektů:** MakeCode umožňuje propojení s GitHub pro verzování kódu (pro pokročilé)
* **Video — debugging tipy (EN):** microbit.org/teach → teaching resources
* **Záloha projektů:** Připomeňte žákům uložit projekt — MakeCode ukládá lokálně v prohlížeči, při vyčištění cache se ztratí

---

!!! tip "Tip pro učitele"
    Tato hodina je o procesu, ne o produktu. Každá skupina bude jinde — některé mají hotovo a ladí, jiné teprve začínají implementaci. To je v pořádku. Nejdůležitější je, aby žáci zažili cyklus: návrh → kód → test → oprava → znovu. Hodnocení zohledněte podle procesu a prezentace záměru, ne jen podle výsledného produktu.
