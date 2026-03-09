# 🤖 Úvod do Micro:bitu: První program

> **Stav:** `⬜ Nekontrolováno`

### 📋 Kontext a cíle
> **RVP ZV (Informatika):** Algoritmizace a programování / Digitální technologie
> **Kód:** `I-9-2-01` – *Žák rozloží problém na podproblémy a navrhne algoritmus.*
> **Kód:** `I-9-3-01` – *Žák vysvětlí princip fungování digitálních technologií a sítí.*

**Po hodině žák:**
* **Popíše** fyzické součásti BBC Micro:bitu (LED matice, tlačítka, piny, konektor USB).
* **Napíše** a nahraje svůj první program v MakeCode (zobrazení textu nebo obrázku).
* **Propojí** znalosti z blokového programování (Scratch) s prostředím MakeCode.
* **Pochopí** cyklus vývoje: napsat kód → přeložit → nahrát → otestovat.

---

### 💡 Metodický postup (45 min)

#### 1. Fyzická prohlídka Micro:bitu (8 min)
*Aktivita bez počítače.*

Učitel rozdá Micro:bity (nebo projde s jedním) a žáci identifikují:
- **LED matice 5×5** — 25 individuálně řiditelných LED
- **Tlačítko A a B** — fyzické vstupy
- **USB konektor** — nahrávání programů z PC
- **Zlaté piny** — připojení externích senzorů a zařízení
- **Mikrofon, reproduktor** (verze 2) nebo bzučák (verze 1)
- **Akcelerometr, kompas, teploměr** — vestavěné senzory

Otázka: „Jak se Micro:bit liší od Scratche?" → Micro:bit je fyzické zařízení — program řídí reálný hardware.

---

#### 2. Prostředí MakeCode — orientace (8 min)
*Práce na PC.*

Žáci otevřou [makecode.microbit.org](https://makecode.microbit.org) a prozkoumají prostředí:
- Levý panel: kategorie bloků (Základní, Vstup, Logika, Smyčky, Proměnné...)
- Střed: pracovní plocha s bloky `při spuštění` a `opakovat stále`
- Vpravo: simulátor — vidíme výsledek BEZ fyzického zařízení
- Klíčový rozdíl od Scratche: bloky `při spuštění` = setup, `opakovat stále` = loop

---

#### 3. První program: Animovaný pozdrav (18 min)
*Práce s Micro:bitem.*

Žáci krok za krokem sestaví program:

**Krok 1:** Do bloku `při spuštění` přidejte `zobrazit text "Ahoj!"` (kategorie Základní)

**Krok 2:** Do bloku `opakovat stále` přidejte `zobrazit ikonu` (srdce) s pauzou 500 ms, pak `vymazat obrazovku` s pauzou 500 ms

**Krok 3:** Otestujte v simulátoru — funguje animace?

**Krok 4:** Nahrajte na fyzický Micro:bit (připojit USB, kliknout „Stáhnout", přetáhnout soubor na zařízení)

**Krok 5 (pro rychlé):** Změňte text nebo ikonu. Přidejte druhý obrázek do animace.

---

#### 4. Diskuse: Kde se Micro:bit používá? (6 min)
*Diskuze.*

Reálné aplikace:
- Školní projekty: meteorologické stanice, alarmy, krokometry
- Průmysl: prototypy IoT zařízení, vzdělávací roboti
- Umění: interaktivní instalace ovládané pohybem

Závěr: Micro:bit je zjednodušený model toho, jak funguje každý chytrý přístroj — telefon, chytré hodinky, termostat.

---

### 🛠️ Zdroje a nástroje

* **MakeCode editor:** [makecode.microbit.org](https://makecode.microbit.org) — funguje bez instalace, má simulátor
* **Oficiální průvodce (CZ):** [microbit.org/cs](https://microbit.org/cs) — lekce a projekty v češtině
* **Videonávody (CZ):** YouTube — „Micro:bit MakeCode česky" — komunitní videa od českých učitelů
* **Kniha aktivit:** microbit.org/projects — desítky volných projektů seřazených podle obtížnosti
* **Náhradní řešení — simulátor:** Pokud nemáte fyzické Micro:bity, celá hodina funguje pouze v simulátoru

---

> 💡 **Tip pro učitele:**
> Nahrávání programu na Micro:bit je pro žáky magický okamžik — poprvé vidí, že jejich kód ovládá fyzický svět. Ujistěte se, že máte funkční USB kabely (ne jen nabíjecí!). Pokud máte Micro:bit v2, využijte vestavěný reproduktor pro zvukové efekty. Nechejte žáky experimentovat — „co se stane, když..." je nejlepší způsob učení.

> 💬 **Tip pro pátek:** Nechejte žáky Micro:bit prohlédnout dříve, než začnete programovat. Kolik pinů vidí? Co je ta LED matice? Fyzický průzkum zařízení zvyšuje zájem a snižuje ostych.
