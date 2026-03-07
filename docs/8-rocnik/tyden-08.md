# Senzory II: Akcelerometr

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování / Digitální technologie
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje algoritmus v programovacím jazyce</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-3-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-3-01</span><span style="color: #374151;">Žák vysvětlí princip fungování digitálních technologií a sítí</span></div>

## 💬 Tip pro pátek
Ukažte žákům, co dělá akcelerometr v jejich mobilu — otočení obrazovky, detekce pádu, fitness aplikace. Propojení s každodenní zkušeností zvyšuje zájem.

## 🎯 Cíle hodiny

- Žák vysvětlí, co měří akcelerometr a v jakých jednotkách (milli-g)
- Žák využije gesto „zatřesení" a „náklon" jako vstup do programu
- Žák přečte hodnotu osy X, Y nebo Z ze senzoru a zobrazí ji
- Žák navrhne a naprogramuje projekt využívající pohyb jako ovládání

## 💡 Metodický postup

### 1. Co je akcelerometr? (8 min) — tabule

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

### 2. Demo: Odečet hodnot akcelerometru (10 min) — PC + Micro:bit

V MakeCode:
- Kategorie **Vstup** → `zrychlení (mg) [x]`
- Do bloku `opakovat stále` přidejte `zobrazit číslo → zrychlení (mg) x`

Žáci nakláněli Micro:bit vlevo/vpravo a sledují měnící se čísla v simulátoru i na fyzickém zařízení.

Diskuse: Jaká hodnota je při pokojové poloze? (≈ 0 na ose X, ≈ -1000 na ose Z kvůli gravitaci)

### 3. Projekt: Elektronická vodováha (20 min) — Micro:bit

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

### 4. Propojení s praxí (7 min) — diskuse

Aplikace akcelerometru:
- **Mobilní hry:** Ovládání autem náklonem telefonu
- **Krokoměr:** Detekce rytmických pohybů chůze (algoritmus je složitý!)
- **Bezpečnost:** Detektory pádu pro starší lidi
- **Robotika:** Udržování rovnováhy (segway, dron)

Otázka: „Co byste zkonstruovali, kdybyste mohli použít akcelerometr v libovolném projektu?"

## 📂 Podklady

- **MakeCode — Vstup → Gesta:** [makecode.microbit.org](https://makecode.microbit.org) → Vstup → `při gestu`
- **Projektový návod — kostka:** microbit.org/projects → „Dice" (hod kostkou pomocí zatřesení)
- **Vysvětlení akcelerometru (EN):** microbit.org/technology → Accelerometer
- **Video (CZ):** YouTube — „Micro:bit akcelerometr projekt"
- **Rozšíření — kompas:** Micro:bit má také magnetometr (kompas) — čtení směru světa

!!! tip "Tip pro učitele"
    Projekt vodováhy je oblíbený, protože žáci vidí okamžitou fyzickou odezvu — pohybují Micro:bitem a LED matice reaguje. Gesto „zatřesení" je intuitivní a reliabilní. Pokud máte čas, nechte žáky v závěru hodiny navrhnout vlastní projekt s akcelerometrem — třeba alarm pro otevřenou skříňku nebo hra s nakláněním. Nápady si zapíší — vrátíme se k nim při projektových týdnech 12–13.
