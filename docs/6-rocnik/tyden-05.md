# Binární logika: Žárovka svítí/nesvítí

## 🎯 Cíle hodiny

- Žák vysvětlí princip binární soustavy (0/1, vypnuto/zapnuto)
- Žák převede jednociferné číslo do binárního zápisu (a zpět) pomocí mocnin 2
- Žák se aktivně zapojí do „živého binárního kódu" s celou třídou
- Žák uvede příklady, kde v běžném životě funguje logika ano/ne (0/1)

## 💡 Metodický postup

### 1. Úvod: Svět bez čísel 2–9 (5 min) — diskuse

Učitel se zeptá: „Co kdybychom mohli používat jen dvě čísla — 0 a 1?" Žáci hádat, kde to vidí (blikající světlo, vypínač, ano/ne).

Vysvětlení: počítač je elektrický — elektřina buď teče (1) nebo neteče (0). Z milionů takových „žárovek" se skládají všechna čísla, texty a obrázky.

### 2. Aktivita: Živý binární kód (15 min) — unplugged

Učitel rozdá 5 dobrovolníkům kartičky s hodnotami: **16 | 8 | 4 | 2 | 1** (mocniny 2). Stát = 1, Sedět = 0.

Učitel vyvolává čísla (1–31) a dobrovolníci vstávají/sedají tak, aby jejich součet odpovídal číslu.

Příklad pro číslo 13:
```
16=sed  8=stoj  4=stoj  2=sed  1=stoj
  0       1       1      0       1   → 01101 = 13
```

Třída kontroluje výsledek. Po 5–6 kolech se dobrovolníci vystřídají.

### 3. Aktivita: Binární převody na PC (15 min) — PC

Žáci otevřou [CS Unplugged — Binary Numbers](https://csunplugged.org/en/topics/binary-numbers/) nebo kalkulačku v OS (Zobrazit → Programátorský režim → BIN).

Úkoly:
- Zapište čísla 5, 10, 15, 21 v binárním formátu
- Dekódujte binární čísla: `0101`, `1010`, `11111`
- Spočítejte: kolik bitů potřebujete pro číslo 255?

### 4. Shrnutí (5 min)

Učitel ukáže Micro:bit — každý LED pixel je 1 bit (svítí/nesvítí). Třída má před sebou počítač se 64 GB RAM — to je 64 × 8 × 1 000 000 000 jedniček a nul.

**Klíčové pojmy:** bit, binární soustava, mocniny 2, 0/1

## 📂 Podklady

- **Interaktivní lekce:** [CS Unplugged — Binary Numbers](https://csunplugged.org/en/topics/binary-numbers/) — kompletní aktivita s pracovními listy (EN)
- **Online binární kalkulačka:** [rapidtables.com/convert/number/decimal-to-binary](https://www.rapidtables.com/convert/number/decimal-to-binary.html)
- **Windows kalkulačka:** Start → Kalkulačka → Zobrazit → Programátor → přepnout BIN/DEC
- **Micro:bit rozšíření:** Naprogramujte v [MakeCode](https://makecode.microbit.org) zobrazení čísla v binárním formátu na 5 LED diodách
- **Video:** [Binary explained in 01100110 seconds — Computerphile](https://www.youtube.com/watch?v=M41M9ATm49M) (~5 min, EN)
- **Kartičky:** Připravte sadu 5 kartiček s hodnotami 16, 8, 4, 2, 1 pro aktivitu (laminovat pro opakované použití)

!!! tip "Tip pro učitele"
    Živý binární kód funguje nejlépe jako soutěž — dvě skupiny po 5 žácích závodí, kdo správně zobrazí číslo dříve. Přidejte časomíru na tabuli. Pro žáky se slabší matematikou začněte s kartičkami 4, 2, 1 (čísla 0–7) a postupně přidávejte.

