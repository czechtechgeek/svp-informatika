# Proměnné v robotice: Počítadlo kroků

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-01</span><span style="color: #374151;">Žák rozloží problém na podproblémy a navrhne algoritmus</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje algoritmus v programovacím jazyce</span></div>

## 💬 Tip pro pátek
Reálná výzva: kolik kroků uděláte od lavice ke dveřím? Nejprve odhadněte, pak změřte Micro:bitem — diskuse o přesnosti a algoritmech krokoměru je přirozená.

## 🎯 Cíle hodiny

- Žák vytvoří proměnnou v MakeCode a manipuluje s její hodnotou (zvýšení, resetování)
- Žák implementuje počítadlo kroků pomocí akcelerometru a proměnné
- Žák propojí znalosti o proměnných ze Scratche (7. ročník) s fyzickým programováním
- Žák navrhne algoritmus pro rozlišení „kroku" od náhodného pohybu

## 💡 Metodický postup

### 1. Co je proměnná v hardwarovém programování? (8 min) — tabule

Propojení se Scratchem:
- Ve Scratchi: `nastav skóre na 0`, `změň skóre o 1`
- V MakeCode: stejná logika, jiné bloky

Proměnná = pojmenované „šuplíčko" v paměti zařízení. Micro:bit má omezenou RAM (16 KB v1, 128 KB v2) — proměnné zabírají místo.

Typy proměnných v MakeCode:
- **Číslo** (number): celá čísla, desetinná čísla
- **Text** (string): řetězec znaků
- **Boolean**: pravda / nepravda

### 2. Tvorba proměnné a počítadlo (10 min) — PC

Učitel ukáže krok za krokem:

1. Kategorie **Proměnné** → `Vytvoř proměnnou...` → název `kroky`
2. Do bloku `při spuštění`: `nastav kroky na 0`
3. Do bloku `při gestu [zatřesení]`: `změň kroky o 1`
4. Do bloku `opakovat stále`: `zobrazit číslo kroky`

Žáci implementují a testují — kolik kroků detekuje za 10 sekund chůze?

### 3. Projekt: Krokoměr s resetem (20 min) — Micro:bit

Žáci rozšíří základní počítadlo:

```
při spuštění:
  nastav kroky na 0

při gestu zatřesení:
  změň kroky o 1

při stisknutí A:
  zobrazit číslo kroky

při stisknutí B:
  nastav kroky na 0
  zobrazit text "RESET"

při stisknutí A+B:
  zobrazit text → "KROKY:"
  zobrazit číslo kroky
```

**Diskuse:** Proč krokoměr není přesný? (Zachytí každé zatřesení, nejen kroky. Profesionální algoritmus filtruje frekvenci a intenzitu pohybu.)

**Rozšíření:** Přidejte proměnnou `vzdalenost` — každý krok = 0,7 m, zobrazit vzdálenost.

### 4. Propojení: Proměnné ve fyzickém světě (7 min) — diskuse

Proměnné v IoT zařízeních:
- Termostat: proměnná `požadovaná_teplota`, `aktuální_teplota`
- Fitbit: proměnné `kroky`, `tepová_frekvence`, `kalorie`
- Auto: `rychlost`, `vzdálenost`, `palivo`

Závěr: Každé chytré zařízení je v podstatě sbírka senzorů a proměnných, které jsou zpracovávány algoritmem.

## 📂 Podklady

- **MakeCode — Proměnné:** [makecode.microbit.org](https://makecode.microbit.org) → Proměnné
- **Projekt — krokoměr (EN):** microbit.org/projects → „Stopwatch" nebo „Pedometer"
- **Propojení s matematikou:** Přepočet kroků na vzdálenost — délka kroku se liší dle výšky člověka
- **Video (CZ):** YouTube — „Micro:bit proměnné počítadlo"
- **Rozšíření — datalogging:** Micro:bit v2 umí zaznamenávat data na integrovanou paměť — lze stáhnout jako CSV

!!! tip "Tip pro učitele"
    Propojení proměnných ze Scratche s MakeCode je klíčové — žáci se učí, že proměnná je univerzální programátorský koncept, ne záležitost konkrétního nástroje. Krokoměr je záměrně nepřesný — to je pedagogicky cenné. Diskuse o tom, jak vylepšit algoritmus (filtrování signálu, práh citlivosti), připravuje půdu pro projektové týdny 12–13.
