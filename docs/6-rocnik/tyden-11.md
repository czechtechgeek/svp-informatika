---
grade: 6
week: 11
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-005
    text: "Po přečtení jednotlivých kroků algoritmu vysvětlí celý postup a určí problém, který je daným algoritmem řešen."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - "Žák vysvětlí, proč se v programování používají cykly (opakování)"
  - "Žák použije blok `opakuj dokola` (forever) pro vytvoření nepřetržité animace"
  - "Žák použije blok `opakuj X-krát` pro ohraničené opakování"
  - Žák porovná kód bez cyklu vs. s cyklem a vysvětlí výhodu cyklu
time_budget:
  - type: unplugged
    minutes: 5
  - type: board
    minutes: 10
  - type: pc
    minutes: 20
friday_tip: "Pátky v 6. třídě jsou ideální pro **\"Nekonečnou diskotéku\"**. Nechte žáky do cyklu `opakuj dokola` přidat blok `změň efekt [barva] o [25]`. Celá třída pak má na monitorech barevně blikající sprity. Je to vizuálně atraktivní důkaz toho, že cyklus běží neustále a mění vlastnosti objektu v reálném čase."
---

# 

## 💡 Metodický postup

### 1. Úvod: Opakování bez konce

<span class="act unplugged">✋ Bez počítače — 5 min</span>

Učitel požádá jednoho žáka, aby vstal a sednul si, vstal a sednul — 10×. Pak se zeptá: „Kdybychom to chtěli zapsat jako program, jak by to vypadalo?"

**Bez cyklu:** 20 bloků (vstát, sednout, vstát, sednout...)
**S cyklem:** `opakuj 10-krát: [vstát, sednout]` → 3 bloky

Klíčová otázka: „Co kdybychom chtěli 1000× opakovat?"

### 2. Ukázka: Tančící kočka

<span class="act board">🖊️ Tabule — 10 min</span>

Učitel ukáže na tabuli postup vytvoření tančící animace:

```
Po kliknutí na zelenou vlajku
  opakuj dokola:
    změň kostým na [další]
    čekej [0.2] sekund
```

Vysvětlí: `opakuj dokola` = nekonečný cyklus, program běží dokud nezmáčkneme STOP.

### 3. Aktivita: Věčný tanec

<span class="act pc">💻 PC — 20 min</span>

<div class="zadani-pc">

Vytvoř animaci „Věčný tanec":

#### Základní verze

1. Vyberte sprite s více kostýmy (např. Ballerina, Dinosaur, Crab)
2. Z palety **Ovládání** přidejte blok `opakuj dokola`
3. Dovnitř: `změň kostým na [další kostým]` + `čekej [0.2] sekund`
4. Spusťte — sprite tančí!

#### Rozšíření

5. Přidejte druhý sprite na druhé straně jeviště tančící jinak
6. Nechte oba sprity pohybovat se vlevo-vpravo pomocí cyklu:
   ```
   opakuj dokola:
     pohni se o 5 kroků
     pokud na kraji, odraz se
   ```

#### Ohraničený cyklus (bonus)

7. Ukažte rozdíl: `opakuj [10]-krát: pohni se o [20] kroků` → sprite se zastaví po 10 krocích

</div>

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
