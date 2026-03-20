---
grade: 7
week: 7
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - "Žák rozlišuje bloky `pokud... pak` a `pokud... pak... jinak`"
  - Žák vysvětlí logické operátory AND (a) a OR (nebo) a uvede příklady
  - Žák sestaví program se složenou podmínkou kombinující více stavů
  - "Žák použije podmínky pro vytvoření jednoduché herní logiky (kolize, reakce na hráče)"
time_budget:
  - type: board
    minutes: 8
  - type: board
    minutes: 10
  - type: pc
    minutes: 22
friday_tip: "Logická hra „AND nebo OR\": učitel říká věty a žáci zvedají ruku pro AND nebo OR — „Otevřu deštník, pokud prší A fouká / nebo prší NEBO fouká.\" Odhalí intuitivní rozdíl v logice ještě před zapnutím počítačů."
---

# Podmínky II: Složené podmínky

## 💡 Metodický postup

### 1. Opakování a rozšíření: POKUD–JINAK

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel zapíše na tabuli:

```
POKUD [podmínka] PAK [akce A] JINAK [akce B]
```

Příklady:
- „POKUD je venku > 20 °C, PAK si vezmi triko, JINAK si vezmi svetr"
- „POKUD je skóre > 0, PAK zobraz skóre, JINAK zobraz ‚Game Over'"

Klíčová otázka: „Co se stane, když podmínka není splněna — chceme nic, nebo jinou akci?"

### 2. Logické operátory: AND a OR

<span class="act board">🖊️ Tabule — 10 min</span>

Učitel kreslí pravdivostní tabulky (jednoduché):

**AND (a zároveň)** — obě podmínky musí být pravda:
| Podmínka 1 | Podmínka 2 | Výsledek |
|-----------|-----------|---------|
| Pravda | Pravda | ✅ Pravda |
| Pravda | Nepravda | ❌ Nepravda |
| Nepravda | Pravda | ❌ Nepravda |

**OR (nebo)** — stačí jedna podmínka:
| Podmínka 1 | Podmínka 2 | Výsledek |
|-----------|-----------|---------|
| Pravda | Pravda | ✅ Pravda |
| Pravda | Nepravda | ✅ Pravda |
| Nepravda | Nepravda | ❌ Nepravda |

Příklad ve Scratch: `pokud [dotýkám se červeného spritu] A [skóre > 5] pak [konec hry]`

### 3. Kodování: Semafor nebo hlídač hranic

<span class="act pc">💻 PC — 22 min</span>

#### Projekt A — Semafor

- Tři barevné sprity (červená, oranžová, zelená)
- Stisknutím kláves 1/2/3 se zobrazuje jiná kombinace
- Podmínky JINAK: vždy jeden svítí, ostatní jsou skryté

#### Projekt B — Hlídač nebezpečné zóny

- Hráčem ovládaný sprite se pohybuje po obrazovce
- Červená zóna vlevo: pokud vstoupí → zobraz varování
- Zelená zóna vpravo: pokud vstoupí + skóre > 3 → zobraz gratulaci
- Splňuje podmínku AND (poloha + skóre)

#### Projekt C — Noční/denní režim

- Spritová postava reaguje na stav prostředí
- Pokud je pozadí tmavé NEBO je čas > 20 (proměnná) → postava spí
- Jinak → postava jde

Žáci si vyberou projekt, pracují individuálně, učitel chodí po třídě.

### 4. Debriefing (5 min)

Učitel vybere 2 žáky, kteří ukáží projekt. Třída odhadne, kde v kódu je AND, kde OR a kde POKUD–JINAK.

## 📂 Podklady

- **Scratch — bloky logiky:** Kategorie **Operátory** (zelená) obsahuje bloky `a`, `nebo`, `není` — lze je vkládat do podmínek
- **Scratch — POKUD–JINAK:** Kategorie **Řízení** (oranžová) — blok s dvěma „kapsami"
- **Interaktivní cvičení (CZ):** [umimeinformatiku.cz](https://www.umimeinformatiku.cz) — hledejte „podmínky" nebo „logické výrazy"
- **Rozšíření — NOT (není):** Pro rychlé žáky ukažte blok `není` — negace podmínky; příklad: `pokud NENÍ dotýkám se okraje pak pohni se`

!!! tip "Tip pro učitele"
    AND vs. OR je klasická záměna — žáci si je pletou i v češtině. Pomáhá příklad ze života: „Dostanu zmrzlinu, pokud mám peníze A jsem dobře" (AND, přísné). „Koupu se, pokud je teplo NEBO jedeme k moři" (OR, benevolentní). Nechejte žáky vymyslet vlastní příklady z každodenního života ještě před prací na PC.
