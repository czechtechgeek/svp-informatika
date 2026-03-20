---
grade: 8
week: 10
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
goals:
  - "**Vytvoří** proměnnou v MakeCode a manipuluje s její hodnotou (zvýšení, resetování)."
  - "**Implementuje** počítadlo kroků pomocí akcelerometru a proměnné."
  - "**Propojí** znalosti o proměnných ze Scratche (7. ročník) s fyzickým programováním."
  - "**Navrhne** algoritmus pro rozlišení „kroku\" od náhodného pohybu."
time_budget:
  - type: board
    minutes: 8
  - type: pc
    minutes: 10
  - type: board
    minutes: 20
  - type: discussion
    minutes: 7
friday_tip: "Reálná výzva: kolik kroků uděláte od lavice ke dveřím? Nejprve odhadněte, pak změřte Micro:bitem — diskuse o přesnosti a algoritmech krokoměru je přirozená."
---

# Proměnné v robotice: Počítadlo kroků

## 💡 Metodický postup

### 1. Co je proměnná v hardwarovém programování?

<span class="act board">🖊️ Tabule — 8 min</span>

Propojení se Scratchem:
- Ve Scratchi: `nastav skóre na 0`, `změň skóre o 1`
- V MakeCode: stejná logika, jiné bloky

Proměnná = pojmenované „šuplíčko" v paměti zařízení. Micro:bit má omezenou RAM (16 KB v1, 128 KB v2) — proměnné zabírají místo.

Typy proměnných v MakeCode:
- **Číslo** (number): celá čísla, desetinná čísla
- **Text** (string): řetězec znaků
- **Boolean**: pravda / nepravda

---

### 2. Tvorba proměnné a počítadlo

<span class="act pc">💻 PC — 10 min</span>

Učitel ukáže krok za krokem:

1. Kategorie **Proměnné** → `Vytvoř proměnnou...` → název `kroky`
2. Do bloku `při spuštění`: `nastav kroky na 0`
3. Do bloku `při gestu [zatřesení]`: `změň kroky o 1`
4. Do bloku `opakovat stále`: `zobrazit číslo kroky`

Žáci implementují a testují — kolik kroků detekuje za 10 sekund chůze?

---

### 3. Projekt: Krokoměr s resetem

<span class="act board">🖊️ Tabule — 20 min</span>

<div class="zadani-pc">

Rozšiřte základní počítadlo kroků o zobrazení a reset:

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

**Rozšíření *(pro rychlé)*:** Přidejte proměnnou `vzdalenost` — každý krok = 0,7 m, zobrazte vzdálenost v metrech.

</div>

**Diskuse:** Proč krokoměr není přesný? (Zachytí každé zatřesení, nejen kroky. Profesionální algoritmus filtruje frekvenci a intenzitu pohybu.)

---

### 4. Propojení: Proměnné ve fyzickém světě

<span class="act discussion">💬 Diskuse — 7 min</span>

Proměnné v IoT zařízeních:
- Termostat: proměnná `požadovaná_teplota`, `aktuální_teplota`
- Fitbit: proměnné `kroky`, `tepová_frekvence`, `kalorie`
- Auto: `rychlost`, `vzdálenost`, `palivo`

Závěr: Každé chytré zařízení je v podstatě sbírka senzorů a proměnných, které jsou zpracovávány algoritmem.

---

## 📂 Zdroje a podklady

* **MakeCode — Proměnné:** [makecode.microbit.org](https://makecode.microbit.org) → Proměnné
* **Projekt — krokoměr (EN):** microbit.org/projects → „Stopwatch" nebo „Pedometer"
* **Propojení s matematikou:** Přepočet kroků na vzdálenost — délka kroku se liší dle výšky člověka
* **Video (CZ):** YouTube — „Micro:bit proměnné počítadlo"
* **Rozšíření — datalogging:** Micro:bit v2 umí zaznamenávat data na integrovanou paměť — lze stáhnout jako CSV

---

!!! tip "Tip pro učitele"
    Propojení proměnných ze Scratche s MakeCode je klíčové — žáci se učí, že proměnná je univerzální programátorský koncept, ne záležitost konkrétního nástroje. Krokoměr je záměrně nepřesný — to je pedagogicky cenné. Diskuse o tom, jak vylepšit algoritmus (filtrování signálu, práh citlivosti), připravuje půdu pro projektové týdny 12–13.
