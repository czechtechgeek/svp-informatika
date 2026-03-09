# ⚙️ Projekt Robot II: Programování a ladění

> **Stav:** `⬜ Nekontrolováno`

### 📋 Kontext a cíle
> **RVP ZV (Informatika):** Algoritmizace a programování
> **Kód:** `I-9-2-02` – *Žák implementuje algoritmus v programovacím jazyce.*
> **Kód:** `I-9-2-01` – *Žák rozloží problém na podproblémy a navrhne algoritmus.*

**Po hodině žák:**
* **Implementuje** svůj projekt z týdne 12 v MakeCode.
* **Systematicky ladí** program — identifikuje a opravuje chyby metodou testování.
* **Upraví** projekt na základě zpětné vazby od spolužáků (peer testing).
* **Dokáže** verbálně popsat, co jeho program dělá a proč.

---

### 💡 Metodický postup (45 min)

#### 1. Krátká rekapitulace a start práce (5 min)
*Práce na PC — úvod.*

Skupiny otevřou MakeCode a začínají podle návrhu z minulého týdne. Učitel připomene:
- Začněte s **minimální funkční verzí** (MVP) — základní funkce fungují
- Teprve pak přidávejte rozšíření
- Každou změnu otestujte v simulátoru PŘED nahráním na fyzické zařízení

---

#### 2. Implementace projektu (25 min)
*Práce s Micro:bitem.*

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

#### 3. Peer testing (10 min)
*Práce s Micro:bitem — vzájemné testování.*

Skupiny si navzájem vymění Micro:bity (nebo demonstrují na místě):
- „Tester" zkouší projekt bez instrukcí — co funguje, co ne?
- Autor sleduje a zapisuje si zpětnou vazbu
- 3 minuty testování, 2 minuty feedback

Formulář zpětné vazby:
- Co fungovalo dobře?
- Co fungovalo špatně nebo neočekávaně?
- Co byste přidali?

---

#### 4. Závěrečná úprava a uložení (5 min)
*Práce na PC.*

Skupiny zapracují nejdůležitější feedback a uloží finální verzi:
- Screenshot kódu do Google Drive / USB
- Příprava na případnou prezentaci po Vánocích (tyden-15)

---

### 🛠️ Zdroje a nástroje

* **MakeCode — debugování:** simulátor umožňuje krokování programu bloky
* **Peer testing formulář:** Připravte tisknutelný lístek (3 otázky výše)
* **GitHub — ukládání projektů:** MakeCode umožňuje propojení s GitHub pro verzování kódu (pro pokročilé)
* **Video — debugging tipy (EN):** microbit.org/teach → teaching resources
* **Záloha projektů:** Připomeňte žákům uložit projekt — MakeCode ukládá lokálně v prohlížeči, při vyčištění cache se ztratí

---

> 💡 **Tip pro učitele:**
> Tato hodina je o procesu, ne o produktu. Každá skupina bude jinde — některé mají hotovo a ladí, jiné teprve začínají implementaci. To je v pořádku. Nejdůležitější je, aby žáci zažili cyklus: návrh → kód → test → oprava → znovu. Hodnocení zohledněte podle procesu a prezentace záměru, ne jen podle výsledného produktu.

> 💬 **Tip pro pátek:** Nechejte skupiny otestovat projekt kamarádem, ne autorem — „uživatel" najde jiné chyby než tvůrce. Peer testing je technika z profesionálního vývoje softwaru.
