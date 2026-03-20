# 📐 Senzory II: Akcelerometr

> **Stav:** `⬜ Nekontrolováno`

### 📋 Kontext a cíle
> **RVP ZV (Informatika):** Algoritmizace a programování / Digitální technologie
> **Kód:** `INF-INF-002-ZV9-007` – *V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné.*
> **Kód:** `INF-INF-003-ZV9-009` – *Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.*

**Po hodině žák:**
* **Vysvětlí**, co měří akcelerometr a v jakých jednotkách (milli-g).
* **Využije** gesto „zatřesení" a „náklon" jako vstup do programu.
* **Přečte** hodnotu osy X, Y nebo Z ze senzoru a zobrazí ji.
* **Navrhne** a naprogramuje projekt využívající pohyb jako ovládání.

---

### 💡 Metodický postup (45 min)

#### 1. Co je akcelerometr? (8 min)
*Tabule — výklad.*

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

#### 2. Demo: Odečet hodnot akcelerometru (10 min)
*PC + Micro:bit — demonstrace.*

V MakeCode:
- Kategorie **Vstup** → `zrychlení (mg) [x]`
- Do bloku `opakovat stále` přidejte `zobrazit číslo → zrychlení (mg) x`

Žáci nakláněli Micro:bit vlevo/vpravo a sledují měnící se čísla v simulátoru i na fyzickém zařízení.

Diskuse: Jaká hodnota je při pokojové poloze? (≈ 0 na ose X, ≈ -1000 na ose Z kvůli gravitaci)

---

#### 3. Projekt: Elektronická vodováha (20 min)
*Práce s Micro:bitem.*

Žáci naprogramují jednoduchý indikátor náklonu:

```
opakovat stále:
  pokud zrychlení(x) > 200:
    zobrazit ikonu (šipka vpravo)
  jinak pokud zrychlení(x) < -200:
    zobrazit ikonu (šipka vlevo)
  jinak:
    zobrazit ikonu (čtverec / bod uprostřed) ← rovnováha
```

**Rozšíření:**
- Přidejte osu Y pro detekci náklonu vpřed/vzad
- Přidejte gesto „zatřesení": kategorie Vstup → `při gestu [zatřesení]` → zobrazit náhodné číslo (hod kostkou)

---

#### 4. Propojení s praxí (7 min)
*Diskuze.*

Aplikace akcelerometru:
- **Mobilní hry:** Ovládání autem náklonem telefonu
- **Krokoměr:** Detekce rytmických pohybů chůze (algoritmus je složitý!)
- **Bezpečnost:** Detektory pádu pro starší lidi
- **Robotika:** Udržování rovnováhy (segway, dron)

Otázka: „Co byste zkonstruovali, kdybyste mohli použít akcelerometr v libovolném projektu?"

---

### 🛠️ Zdroje a nástroje

* **MakeCode — Vstup → Gesta:** [makecode.microbit.org](https://makecode.microbit.org) → Vstup → `při gestu`
* **Projektový návod — kostka:** microbit.org/projects → „Dice" (hod kostkou pomocí zatřesení)
* **Vysvětlení akcelerometru (EN):** microbit.org/technology → Accelerometer
* **Video (CZ):** YouTube — „Micro:bit akcelerometr projekt"
* **Rozšíření — kompas:** Micro:bit má také magnetometr (kompas) — čtení směru světa

---

> 💡 **Tip pro učitele:**
> Projekt vodováhy je oblíbený, protože žáci vidí okamžitou fyzickou odezvu — pohybují Micro:bitem a LED matice reaguje. Gesto „zatřesení" je intuitivní a reliabilní. Pokud máte čas, nechte žáky v závěru hodiny navrhnout vlastní projekt s akcelerometrem — třeba alarm pro otevřenou skříňku nebo hra s nakláněním. Nápady si zapíší — vrátíme se k nim při projektových týdnech 12–13.

> 💬 **Tip pro pátek:** Ukažte žákům, co dělá akcelerometr v jejich mobilu — otočení obrazovky, detekce pádu, fitness aplikace. Propojení s každodenní zkušeností zvyšuje zájem.
