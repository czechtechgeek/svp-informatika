# Scratch II: Události - Po kliknutí na vlajku

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-03" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-03</span><span style="color: #374151;">Žák zapíše algoritmus v programovacím jazyce</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-01</span><span style="color: #374151;">Žák rozloží problém na podproblémy</span></div>

## 💬 Tip pro pátek
Pátky v 6. třídě jsou ideální pro **"Chaos Challenge"**. Dejte žákům 3 minuty na to, aby do jednoho projektu přidali co nejvíce postav, a každé z nich dali událost `Po stisknutí libovolné klávesy` s jiným zvukem nebo pohybem. Po spuštění a náhodném mačkání klávesnice vznikne "digitální orchestr/chaos", který skvěle demonstruje paralelní běh skriptů a okamžitou reakci na událost.

## 🎯 Cíle hodiny

- Žák vysvětlí, co je událost v programování (event-driven programming)
- Žák použije blok „Po kliknutí na zelenou vlajku" jako spouštěč programu
- Žák naprogramuje postavu, která reaguje na klik myší a stisk klávesy
- Žák vytvoří animaci s více sprity reagujícími na různé události

## 💡 Metodický postup

### 1. Úvod: Co je událost? (5 min)

Učitel se zeptá: „Co se stane, když zmáčknete vypínač světla? Co se stane, když zazvoní telefon?" Žáci odpovídají.

Klíčová myšlenka: **Událost = něco, co se stane → spustí reakci**. V počítači je to stejné — klik myší, stisk klávesy, spuštění programu jsou události.

### 2. Ukázka: Reagující duch (10 min) — tabule + PC

Učitel na tabuli (sdílená obrazovka) postaví jednoduché schéma:

```
UDÁLOST: "Po kliknutí na zelenou vlajku"
  ↓
AKCE: "řekni Ahoj! po dobu 2 sekund"
  ↓
AKCE: "pohni se o 50 kroků"
```

Žáci sledují, jak se bloky skládají a spouštějí.

### 3. Aktivita: Reagující duch (25 min) — PC

Žáci vytvoří projekt „Reagující duch":

#### Krok 1 — Základní reakce
1. Smaž kocoura → přidej sprite „Ghost" (nebo jiný)
2. Z palety **Události** vezmi blok `Po kliknutí na zelenou vlajku`
3. Přidej: `řekni [Buuu!] po dobu [2] sekund`
4. Přidej: `přejdi na pozici náhodnou`

#### Krok 2 — Reakce na klik myší
5. Přidej nový skript — z palety **Události**: `Po kliknutí na tento sprite`
6. Přidej: `změň kostým na [další kostým]`
7. Přidej: `přehraj zvuk [meow]`

#### Krok 3 — Reakce na klávesu
8. Přidej skript: `Po stisknutí klávesy [mezerník]`
9. Přidej: `pohni se o [100] kroků`

Výsledek: Duch se teleportuje při startu, změní kostým při kliknutí, skočí při mezerníku.

### 4. Shrnutí (5 min)

Žáci sdílí projekty. Učitel shrne: „V jakých situacích v reálném životě funguje logika ‚když nastane X, udělej Y'?"

**Klíčové pojmy:** událost (event), spouštěč (trigger), handler, kostým

## 📂 Podklady

- **Scratch projekt k inspiraci:** [scratch.mit.edu/projects/explore](https://scratch.mit.edu/explore/projects/all?q=ghost+react) — hledejte „ghost interactive"
- **Scratch wiki (CZ):** [cs.scratch-wiki.info](https://cs.scratch-wiki.info) — česká dokumentace Scratch bloků; hledejte „Bloky Události"
- **Scratch karty — Activity Cards:** [scratch.mit.edu/ideas](https://scratch.mit.edu/ideas) → Activity Cards — sada 10 vytisknutelných karet s projekty (dostupné v češtině)
- **Video tutorial (CZ):** Na YouTube vyhledejte „Scratch události tutoriál" nebo „Scratch programování pro děti česky"
- **Rozšíření:** Přidejte více postav, každá reaguje na jinou klávesu — základ budoucí hry

!!! tip "Tip pro učitele"
    Kostýmy (Costumes) jsou silný nástroj — ukažte žákům záložku Kostýmy a možnost nakreslení vlastního kostýmu v editoru. Kreativita s kostýmy udrží žáky motivované po celou sérii Scratch hodin.

