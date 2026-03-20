---
grade: 6
week: 5
time: 45
area: "Data, informace a modelování"
rvp_codes:
  - code: INF-INF-001-ZV9-002
    text: Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - "Žák vysvětlí princip binární soustavy (0/1, vypnuto/zapnuto)"
  - Žák převede jednociferné číslo do binárního zápisu (a zpět) pomocí mocnin 2
  - "Žák se aktivně zapojí do „živého binárního kódu\" s celou třídou"
  - "Žák uvede příklady, kde v běžném životě funguje logika ano/ne (0/1)"
time_budget:
  - type: discussion
    minutes: 5
  - type: unplugged
    minutes: 15
  - type: pc
    minutes: 15
friday_tip: "Pro odlehčení na konci hodiny ukažte žákům **\"Binární hodiny\"** (stačí vyhledat online \"Binary clock\"). Nechte je společně dekódovat, kolik je právě hodin. Je to skvělý trénink rychlého převodu z hlavy a žáci vidí praktické (i když netradiční) využití binárního zápisu v reálném čase."
---

# 

## 💡 Metodický postup

### 1. Úvod: Svět bez čísel 2–9

<span class="act discussion">💬 Diskuse — 5 min</span>

Učitel se zeptá: „Co kdybychom mohli používat jen dvě čísla — 0 a 1?" Žáci hádat, kde to vidí (blikající světlo, vypínač, ano/ne).

Vysvětlení: počítač je elektrický — elektřina buď teče (1) nebo neteče (0). Z milionů takových „žárovek" se skládají všechna čísla, texty a obrázky.

### 2. Aktivita: Živý binární kód

<span class="act unplugged">✋ Bez počítače — 15 min</span>

Učitel rozdá 5 dobrovolníkům kartičky s hodnotami: **16 | 8 | 4 | 2 | 1** (mocniny 2). Stát = 1, Sedět = 0.

Učitel vyvolává čísla (1–31) a dobrovolníci vstávají/sedají tak, aby jejich součet odpovídal číslu.

Příklad pro číslo 13:
```
16=sed  8=stoj  4=stoj  2=sed  1=stoj
  0       1       1      0       1   → 01101 = 13
```

Třída kontroluje výsledek. Po 5–6 kolech se dobrovolníci vystřídají.

### 3. Aktivita: Binární převody na PC

<span class="act pc">💻 PC — 15 min</span>

<div class="zadani-pc">

Otevři [umimeinformatiku.cz](https://www.umimeinformatiku.cz) (sekce „Binární čísla") nebo kalkulačku v OS (Zobrazit → Programátorský režim → BIN) a splň tyto úkoly:

- Zapište čísla 5, 10, 15, 21 v binárním formátu
- Dekódujte binární čísla: `0101`, `1010`, `11111`
- Spočítejte: kolik bitů potřebujete pro číslo 255?

</div>

### 4. Shrnutí (5 min)

Učitel ukáže Micro:bit — každý LED pixel je 1 bit (svítí/nesvítí). Třída má před sebou počítač se 64 GB RAM — to je 64 × 8 × 1 000 000 000 jedniček a nul.

**Klíčové pojmy:** bit, binární soustava, mocniny 2, 0/1

## 📂 Podklady

- **Cvičení na binární čísla (CZ):** [umimeinformatiku.cz](https://www.umimeinformatiku.cz) — interaktivní cvičení na binární číselnou soustavu v češtině
- **Windows kalkulačka:** Start → Kalkulačka → Zobrazit → Programátor → přepnout BIN/DEC (zabudovaná v každém Windows)
- **Micro:bit rozšíření:** Naprogramujte v [MakeCode](https://makecode.microbit.org) zobrazení čísla v binárním formátu na 5 LED diodách — MakeCode má české UI
- **Video (CZ):** [ČT edu — Jak funguje počítač](https://edu.ceskatelevize.cz/predmet/informatika) — hledejte „binární čísla" nebo „jak počítač počítá"
- **Kartičky:** Připravte sadu 5 kartiček s hodnotami 16, 8, 4, 2, 1 pro aktivitu (laminovat pro opakované použití)

!!! tip "Tip pro učitele"
    Živý binární kód funguje nejlépe jako soutěž — dvě skupiny po 5 žácích závodí, kdo správně zobrazí číslo dříve. Přidejte časomíru na tabuli. Pro žáky se slabší matematikou začněte s kartičkami 4, 2, 1 (čísla 0–7) a postupně přidávejte.
