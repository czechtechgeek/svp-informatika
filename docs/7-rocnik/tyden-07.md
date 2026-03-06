# Podmínky II: Složené podmínky

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje algoritmus v programovacím jazyce</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-01</span><span style="color: #374151;">Žák rozloží problém na podproblémy a navrhne algoritmus</span></div>

## 💬 Tip pro pátek
Logická hra „AND nebo OR": učitel říká věty a žáci zvedají ruku pro AND nebo OR — „Otevřu deštník, pokud prší A fouká / nebo prší NEBO fouká." Odhalí intuitivní rozdíl v logice ještě před zapnutím počítačů.

## 🎯 Cíle hodiny

- Žák rozlišuje bloky `pokud... pak` a `pokud... pak... jinak`
- Žák vysvětlí logické operátory AND (a) a OR (nebo) a uvede příklady
- Žák sestaví program se složenou podmínkou kombinující více stavů
- Žák použije podmínky pro vytvoření jednoduché herní logiky (kolize, reakce na hráče)

## 💡 Metodický postup

### 1. Opakování a rozšíření: POKUD–JINAK (8 min) — tabule

Učitel zapíše na tabuli:

```
POKUD [podmínka] PAK [akce A] JINAK [akce B]
```

Příklady:
- „POKUD je venku > 20 °C, PAK si vezmi triko, JINAK si vezmi svetr"
- „POKUD je skóre > 0, PAK zobraz skóre, JINAK zobraz ‚Game Over'"

Klíčová otázka: „Co se stane, když podmínka není splněna — chceme nic, nebo jinou akci?"

### 2. Logické operátory: AND a OR (10 min) — tabule

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

### 3. Kodování: Semafor nebo hlídač hranic (22 min) — PC

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
