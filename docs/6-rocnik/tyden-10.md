---
grade: 6
week: 10
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-005
    text: "Po přečtení jednotlivých kroků algoritmu vysvětlí celý postup a určí problém, který je daným algoritmem řešen."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - "Žák vysvětlí, co je událost v programování (event-driven programming)"
  - "Žák použije blok „Po kliknutí na zelenou vlajku\" jako spouštěč programu"
  - "Žák naprogramuje postavu, která reaguje na klik myší a stisk klávesy"
  - Žák vytvoří animaci s více sprity reagujícími na různé události
time_budget:
  - type: pc
    minutes: 10
  - type: pc
    minutes: 25
friday_tip: "Pátky v 6. třídě jsou ideální pro **\"Chaos Challenge\"**. Dejte žákům 3 minuty na to, aby do jednoho projektu přidali co nejvíce postav, a každé z nich dali událost `Po stisknutí libovolné klávesy` s jiným zvukem nebo pohybem. Po spuštění a náhodném mačkání klávesnice vznikne \"digitální orchestr/chaos\", který skvěle demonstruje paralelní běh skriptů a okamžitou reakci na událost."
---

# 

## 💡 Metodický postup

### 1. Úvod: Co je událost? (5 min)

Učitel se zeptá: „Co se stane, když zmáčknete vypínač světla? Co se stane, když zazvoní telefon?" Žáci odpovídají.

Klíčová myšlenka: **Událost = něco, co se stane → spustí reakci**. V počítači je to stejné — klik myší, stisk klávesy, spuštění programu jsou události.

### 2. Ukázka: Reagující duch

<span class="act pc">💻 PC — 10 min</span>

Učitel na tabuli (sdílená obrazovka) postaví jednoduché schéma:

```
UDÁLOST: "Po kliknutí na zelenou vlajku"
  ↓
AKCE: "řekni Ahoj! po dobu 2 sekund"
  ↓
AKCE: "pohni se o 50 kroků"
```

Žáci sledují, jak se bloky skládají a spouštějí.

### 3. Aktivita: Reagující duch

<span class="act pc">💻 PC — 25 min</span>

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
