# Scratch III: Jednoduché cykly

## 🎯 Cíle hodiny

- Žák vysvětlí, proč se v programování používají cykly (opakování)
- Žák použije blok `opakuj dokola` (forever) pro vytvoření nepřetržité animace
- Žák použije blok `opakuj X-krát` pro ohraničené opakování
- Žák porovná kód bez cyklu vs. s cyklem a vysvětlí výhodu cyklu

## 💡 Metodický postup

### 1. Úvod: Opakování bez konce (5 min) — unplugged

Učitel požádá jednoho žáka, aby vstal a sednul si, vstal a sednul — 10×. Pak se zeptá: „Kdybychom to chtěli zapsat jako program, jak by to vypadalo?"

**Bez cyklu:** 20 bloků (vstát, sednout, vstát, sednout...)
**S cyklem:** `opakuj 10-krát: [vstát, sednout]` → 3 bloky

Klíčová otázka: „Co kdybychom chtěli 1000× opakovat?"

### 2. Ukázka: Tančící kočka (10 min) — tabule

Učitel ukáže na tabuli postup vytvoření tančící animace:

```
Po kliknutí na zelenou vlajku
  opakuj dokola:
    změň kostým na [další]
    čekej [0.2] sekund
```

Vysvětlí: `opakuj dokola` = nekonečný cyklus, program běží dokud nezmáčkneme STOP.

### 3. Aktivita: Věčný tanec (20 min) — PC

Žáci vytvoří animaci „Věčný tanec":

**Základní verze:**
1. Vyberte sprite s více kostýmy (např. Ballerina, Dinosaur, Crab)
2. Z palety **Ovládání** přidejte blok `opakuj dokola`
3. Dovnitř: `změň kostým na [další kostým]` + `čekej [0.2] sekund`
4. Spusťte — sprite tančí!

**Rozšíření:**
5. Přidejte druhý sprite na druhé straně jeviště tančící jinak
6. Nechte oba sprity pohybovat se vlevo-vpravo pomocí cyklu:
   ```
   opakuj dokola:
     pohni se o 5 kroků
     pokud na kraji, odraz se
   ```

**Ohraničený cyklus (bonus):**
7. Ukažte rozdíl: `opakuj [10]-krát: pohni se o [20] kroků` → sprite se zastaví po 10 krocích

### 4. Shrnutí (5 min)

Žáci sdílí projekty. Diskuse: „Kde v reálném životě vidíte nekonečný cyklus?" (srdeční tep, střídání ročních období, animace načítání).

**Klíčové pojmy:** cyklus (loop), `opakuj dokola`, `opakuj X-krát`, kostým, animace

## 📂 Podklady

- **Scratch projekt — vzor:** Vytvořte vzorový projekt „Dancing Cat" a sdílejte odkaz přes Google Classroom
- **Scratch wiki — Loops:** [en.scratch-wiki.info/wiki/Control_Blocks](https://en.scratch-wiki.info/wiki/Control_Blocks)
- **Scratch Activity Card — „Make it Fly":** [scratch.mit.edu/ideas](https://scratch.mit.edu/ideas) → karta č. 3
- **Video tutorial:** „Scratch Loops Tutorial for Beginners" na YouTube
- **Rozšíření — Micro:bit:** Ukažte žákům, jak `opakuj dokola` funguje v MakeCode — blikající LED je totéž co tančící sprite

!!! tip "Tip pro učitele"
    Žáci mají tendenci zapomenout na `čekej` uvnitř cyklu — bez něj animace běží tak rychle, že není vidět. Nechejte je to zažít a pak přijít na řešení sami — „Co přidáme, aby se animace zpomalila?" Tento debugging moment je velmi cenný.

