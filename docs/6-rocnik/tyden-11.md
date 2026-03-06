# Scratch III: Jednoduché cykly

## 🎯 Cíle hodiny

- Žák vysvětlí, proč se v programování používají cykly (opakování)
- Žák použije blok `opakuj dokola` (forever) pro vytvoření nepřetržité animace
- Žák použije blok `opakuj X-krát` pro ohraničené opakování
- Žák porovná kód bez cyklu vs. s cyklem a vysvětlí výhodu cyklu

## 🎯 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-03" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-03</span><span style="color: #374151;">Žák používá proměnné, větvení a cykly</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-01</span><span style="color: #374151;">Žák rozloží problém na podproblémy</span></div>

## 💡 Metodický tip pro pátky
Pátky v 6. třídě jsou ideální pro **"Nekonečnou diskotéku"**. Nechte žáky do cyklu `opakuj dokola` přidat blok `změň efekt [barva] o [25]`. Celá třída pak má na monitorech barevně blikající sprity. Je to vizuálně atraktivní důkaz toho, že cyklus běží neustále a mění vlastnosti objektu v reálném čase.

## 💡 Metodický postup

### 1. Úvod: Opakování bez konce (5 min) — bez počítače

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
- **Scratch wiki (CZ):** [cs.scratch-wiki.info](https://cs.scratch-wiki.info) — česká dokumentace; hledejte „Bloky Ovládání" pro dokumentaci cyklů
- **Scratch Activity Card:** [scratch.mit.edu/ideas](https://scratch.mit.edu/ideas) → Activity Cards — karta „Make it Fly" (tisknutelná, dostupná v češtině)
- **Video tutorial (CZ):** Na YouTube vyhledejte „Scratch cykly tutoriál česky" nebo „Scratch opakuj dokola"
- **Rozšíření — Micro:bit:** Ukažte žákům, jak `opakuj dokola` funguje v MakeCode — blikající LED je totéž co tančící sprite

!!! tip "Tip pro učitele"
    Žáci mají tendenci zapomenout na `čekej` uvnitř cyklu — bez něj animace běží tak rychle, že není vidět. Nechejte je to zažít a pak přijít na řešení sami — „Co přidáme, aby se animace zpomalila?" Tento debugging moment je velmi cenný.

