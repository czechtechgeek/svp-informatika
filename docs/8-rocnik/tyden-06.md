# Úvod do Micro:bitu: První program

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování / Digitální technologie
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-01</span><span style="color: #374151;">Žák rozloží problém na podproblémy a navrhne algoritmus</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-3-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-3-01</span><span style="color: #374151;">Žák vysvětlí princip fungování digitálních technologií a sítí</span></div>

## 💬 Tip pro pátek
Nechejte žáky Micro:bit prohlédnout dříve, než začnete programovat. Kolik pinů vidí? Co je ta LED matice? Fyzický průzkum zařízení zvyšuje zájem a snižuje ostych.

## 🎯 Cíle hodiny

- Žák popíše fyzické součásti BBC Micro:bitu (LED matice, tlačítka, piny, konektor USB)
- Žák napíše a nahraje svůj první program v MakeCode (zobrazení textu nebo obrázku)
- Žák propojí znalosti z blokového programování (Scratch) s prostředím MakeCode
- Žák pochopí cyklus vývoje: napsat kód → přeložit → nahrát → otestovat

## 💡 Metodický postup

### 1. Fyzická prohlídka Micro:bitu (8 min) — bez počítače

Učitel rozdá Micro:bity (nebo projde s jedním) a žáci identifikují:
- **LED matice 5×5** — 25 individuálně řiditelných LED
- **Tlačítko A a B** — fyzické vstupy
- **USB konektor** — nahrávání programů z PC
- **Zlaté piny** — připojení externích senzorů a zařízení
- **Mikrofon, reproduktor** (verze 2) nebo bzučák (verze 1)
- **Akcelerometr, kompas, teploměr** — vestavěné senzory

Otázka: „Jak se Micro:bit liší od Scratche?" → Micro:bit je fyzické zařízení — program řídí reálný hardware.

### 2. Prostředí MakeCode — orientace (8 min) — PC

Žáci otevřou [makecode.microbit.org](https://makecode.microbit.org) a prozkoumají prostředí:
- Levý panel: kategorie bloků (Základní, Vstup, Logika, Smyčky, Proměnné...)
- Střed: pracovní plocha s bloky `při spuštění` a `opakovat stále`
- Vpravo: simulátor — vidíme výsledek BEZ fyzického zařízení
- Klíčový rozdíl od Scratche: bloky `při spuštění` = setup, `opakovat stále` = loop

### 3. První program: Animovaný pozdrav (18 min) — Micro:bit

Žáci krok za krokem sestaví program:

**Krok 1:** Do bloku `při spuštění` přidejte `zobrazit text "Ahoj!"` (kategorie Základní)

**Krok 2:** Do bloku `opakovat stále` přidejte `zobrazit ikonu` (srdce) s pauzou 500 ms, pak `vymazat obrazovku` s pauzou 500 ms

**Krok 3:** Otestujte v simulátoru — funguje animace?

**Krok 4:** Nahrajte na fyzický Micro:bit (připojit USB, kliknout „Stáhnout", přetáhnout soubor na zařízení)

**Krok 5 (pro rychlé):** Změňte text nebo ikonu. Přidejte druhý obrázek do animace.

### 4. Diskuse: Kde se Micro:bit používá? (6 min) — diskuse

Reálné aplikace:
- Školní projekty: meteorologické stanice, alarmy, krokometry
- Průmysl: prototypy IoT zařízení, vzdělávací roboti
- Umění: interaktivní instalace ovládané pohybem

Závěr: Micro:bit je zjednodušený model toho, jak funguje každý chytrý přístroj — telefon, chytré hodinky, termostat.

## 📂 Podklady

- **MakeCode editor:** [makecode.microbit.org](https://makecode.microbit.org) — funguje bez instalace, má simulátor
- **Oficiální průvodce (CZ):** [microbit.org/cs](https://microbit.org/cs) — lekce a projekty v češtině
- **Videonávody (CZ):** YouTube — „Micro:bit MakeCode česky" — komunitní videa od českých učitelů
- **Kniha aktivit:** microbit.org/projects — desítky volných projektů seřazených podle obtížnosti
- **Náhradní řešení — simulátor:** Pokud nemáte fyzické Micro:bity, celá hodina funguje pouze v simulátoru

!!! tip "Tip pro učitele"
    Nahrávání programu na Micro:bit je pro žáky magický okamžik — poprvé vidí, že jejich kód ovládá fyzický svět. Ujistěte se, že máte funkční USB kabely (ne jen nabíjecí!). Pokud máte Micro:bit v2, využijte vestavěný reproduktor pro zvukové efekty. Nechejte žáky experimentovat — „co se stane, když..." je nejlepší způsob učení.
