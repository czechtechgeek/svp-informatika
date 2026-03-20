---
grade: 8
week: 8
time: 45
area: Algoritmizace a programování / Digitální technologie
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - "**Vysvětlí**, co měří akcelerometr a v jakých jednotkách (milli-g)."
  - "**Využije** gesto „zatřesení\" a „náklon\" jako vstup do programu."
  - "**Přečte** hodnotu osy X, Y nebo Z ze senzoru a zobrazí ji."
  - "**Navrhne** a naprogramuje projekt využívající pohyb jako ovládání."
time_budget:
  - type: board
    minutes: 8
  - type: pc
    minutes: 10
  - type: board
    minutes: 20
  - type: discussion
    minutes: 7
friday_tip: "Ukažte žákům, co dělá akcelerometr v jejich mobilu — otočení obrazovky, detekce pádu, fitness aplikace. Propojení s každodenní zkušeností zvyšuje zájem."
---

# Senzory II: Akcelerometr

## 💡 Metodický postup

### 1. Co je akcelerometr?

<span class="act board">🖊️ Tabule — 8 min</span>

Akcelerometr měří zrychlení — změnu rychlosti nebo směru pohybu. V klidu měří gravitaci (1 g ≈ 1000 milli-g). Osy:

```
Z ↑
  |
  +──→ X
 /
Y
```

- **Osa X:** náklon doleva/doprava
- **Osa Y:** náklon dopředu/dozadu
- **Osa Z:** pohyb nahoru/dolů, včetně gravitace

Reálné použití: mobilní telefon — rotace displeje; airbag — detekce nárazu; fitness náramek — počítání kroků.

---

### 2. Demo: Odečet hodnot akcelerometru

<span class="act pc">💻 PC — 10 min</span>

V MakeCode:
- Kategorie **Vstup** → `zrychlení (mg) [x]`
- Do bloku `opakovat stále` přidejte `zobrazit číslo → zrychlení (mg) x`

Žáci nakláněli Micro:bit vlevo/vpravo a sledují měnící se čísla v simulátoru i na fyzickém zařízení.

Diskuse: Jaká hodnota je při pokojové poloze? (≈ 0 na ose X, ≈ -1000 na ose Z kvůli gravitaci)

---

### 3. Projekt: Elektronická vodováha

<span class="act board">🖊️ Tabule — 20 min</span>

<div class="zadani-pc" markdown="1">

Naprogramujte jednoduchý indikátor náklonu:

```
opakovat stále:
  pokud zrychlení(x) > 200:
    zobrazit ikonu (šipka vpravo)
  jinak pokud zrychlení(x) < -200:
    zobrazit ikonu (šipka vlevo)
  jinak:
    zobrazit ikonu (čtverec / bod uprostřed) ← rovnováha
```

**Rozšíření *(pro rychlé)*:**
- Přidejte osu Y pro detekci náklonu vpřed/vzad
- Přidejte gesto „zatřesení": kategorie Vstup → `při gestu [zatřesení]` → zobrazit náhodné číslo (hod kostkou)

</div>

---

### 4. Propojení s praxí

<span class="act discussion">💬 Diskuse — 7 min</span>

Aplikace akcelerometru:
- **Mobilní hry:** Ovládání autem náklonem telefonu
- **Krokoměr:** Detekce rytmických pohybů chůze (algoritmus je složitý!)
- **Bezpečnost:** Detektory pádu pro starší lidi
- **Robotika:** Udržování rovnováhy (segway, dron)

Otázka: „Co byste zkonstruovali, kdybyste mohli použít akcelerometr v libovolném projektu?"

---

## 📂 Zdroje a podklady

* **MakeCode — Vstup → Gesta:** [makecode.microbit.org](https://makecode.microbit.org) → Vstup → `při gestu`
* **Projektový návod — kostka:** microbit.org/projects → „Dice" (hod kostkou pomocí zatřesení)
* **Vysvětlení akcelerometru (EN):** microbit.org/technology → Accelerometer
* **Video (CZ):** YouTube — „Micro:bit akcelerometr projekt"
* **Rozšíření — kompas:** Micro:bit má také magnetometr (kompas) — čtení směru světa

---

!!! tip "Tip pro učitele"
    Projekt vodováhy je oblíbený, protože žáci vidí okamžitou fyzickou odezvu — pohybují Micro:bitem a LED matice reaguje. Gesto „zatřesení" je intuitivní a reliabilní. Pokud máte čas, nechte žáky v závěru hodiny navrhnout vlastní projekt s akcelerometrem — třeba alarm pro otevřenou skříňku nebo hra s nakláněním. Nápady si zapíší — vrátíme se k nim při projektových týdnech 12–13.
