# Binární logika: Žárovka svítí/nesvítí

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Data, informace a modelování
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-001-ZV9-002" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-001-ZV9-002</span><span style="color: #374151;">Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-009" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-009</span><span style="color: #374151;">Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.</span></div>

## 💬 Tip pro pátek
Pro odlehčení na konci hodiny ukažte žákům **"Binární hodiny"** (stačí vyhledat online "Binary clock"). Nechte je společně dekódovat, kolik je právě hodin. Je to skvělý trénink rychlého převodu z hlavy a žáci vidí praktické (i když netradiční) využití binárního zápisu v reálném čase.

## 🎯 Cíle hodiny

- Žák vysvětlí princip binární soustavy (0/1, vypnuto/zapnuto)
- Žák převede jednociferné číslo do binárního zápisu (a zpět) pomocí mocnin 2
- Žák se aktivně zapojí do „živého binárního kódu" s celou třídou
- Žák uvede příklady, kde v běžném životě funguje logika ano/ne (0/1)

## 💡 Metodický postup

### 1. Úvod: Svět bez čísel 2–9 (5 min) — diskuse

Učitel se zeptá: „Co kdybychom mohli používat jen dvě čísla — 0 a 1?" Žáci hádat, kde to vidí (blikající světlo, vypínač, ano/ne).

Vysvětlení: počítač je elektrický — elektřina buď teče (1) nebo neteče (0). Z milionů takových „žárovek" se skládají všechna čísla, texty a obrázky.

### 2. Aktivita: Živý binární kód (15 min) — bez počítače

Učitel rozdá 5 dobrovolníkům kartičky s hodnotami: **16 | 8 | 4 | 2 | 1** (mocniny 2). Stát = 1, Sedět = 0.

Učitel vyvolává čísla (1–31) a dobrovolníci vstávají/sedají tak, aby jejich součet odpovídal číslu.

Příklad pro číslo 13:
```
16=sed  8=stoj  4=stoj  2=sed  1=stoj
  0       1       1      0       1   → 01101 = 13
```

Třída kontroluje výsledek. Po 5–6 kolech se dobrovolníci vystřídají.

### 3. Aktivita: Binární převody na PC (15 min) — PC

Žáci otevřou [umimeinformatiku.cz](https://www.umimeinformatiku.cz) (sekce „Binární čísla") nebo kalkulačku v OS (Zobrazit → Programátorský režim → BIN).

Úkoly:
- Zapište čísla 5, 10, 15, 21 v binárním formátu
- Dekódujte binární čísla: `0101`, `1010`, `11111`
- Spočítejte: kolik bitů potřebujete pro číslo 255?

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

