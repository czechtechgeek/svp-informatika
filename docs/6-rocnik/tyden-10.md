# Scratch II: Události - Po kliknutí na vlajku

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

**Krok 1 — Základní reakce:**
1. Smaž kocoura → přidej sprite „Ghost" (nebo jiný)
2. Z palety **Události** vezmi blok `Po kliknutí na zelenou vlajku`
3. Přidej: `řekni [Buuu!] po dobu [2] sekund`
4. Přidej: `přejdi na pozici náhodnou`

**Krok 2 — Reakce na klik myší:**
5. Přidej nový skript — z palety **Události**: `Po kliknutí na tento sprite`
6. Přidej: `změň kostým na [další kostým]`
7. Přidej: `přehraj zvuk [meow]`

**Krok 3 — Reakce na klávesu:**
8. Přidej skript: `Po stisknutí klávesy [mezerník]`
9. Přidej: `pohni se o [100] kroků`

Výsledek: Duch se teleportuje při startu, změní kostým při kliknutí, skočí při mezerníku.

### 4. Shrnutí (5 min)

Žáci sdílí projekty. Učitel shrne: „V jakých situacích v reálném životě funguje logika ‚když nastane X, udělej Y'?"

**Klíčové pojmy:** událost (event), spouštěč (trigger), handler, kostým

## 📂 Podklady

- **Scratch projekt k inspiraci:** [scratch.mit.edu/projects/explore](https://scratch.mit.edu/explore/projects/all?q=ghost+react) — hledejte „ghost interactive"
- **Scratch wiki — Events:** [en.scratch-wiki.info/wiki/Events_Blocks](https://en.scratch-wiki.info/wiki/Events_Blocks) — dokumentace bloků Události
- **Scratch karty — Activity Cards:** [scratch.mit.edu/ideas](https://scratch.mit.edu/ideas) → Activity Cards — sada 10 vytisknutelných karet s projekty
- **Video tutorial:** „Scratch Events Tutorial" na YouTube — hledejte podle názvu
- **Rozšíření:** Přidejte více postav, každá reaguje na jinou klávesu — základ budoucí hry

!!! tip "Tip pro učitele"
    Kostýmy (Costumes) jsou silný nástroj — ukažte žákům záložku Kostýmy a možnost nakreslení vlastního kostýmu v editoru. Kreativita s kostýmy udrží žáky motivované po celou sérii Scratch hodin.

