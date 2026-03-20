# Python II: Jednoduché výpočty

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Programování / Algoritmické myšlení
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-009" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-009</span><span style="color: #374151;">Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-002-ZV9-006" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-002-ZV9-006</span><span style="color: #374151;">Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.</span></div>

## 💬 Tip pro pátek
Nechejte žáky si vybrat, co jejich kalkulačka bude počítat – BMI, cenu nákupu, převod měn. Vlastní volba zvyšuje zapojení. Pokud třída zvládá rychle, přidejte podmínku: „Pokud BMI > 25, vypiš upozornění."

## 🎯 Cíle hodiny

- Žák používá aritmetické operátory Pythonu včetně celočíselného dělení a zbytku
- Žák převádí datové typy pomocí `int()`, `float()` a `str()`
- Žák napíše program s podmínkou `if/elif/else`
- Žák vytvoří funkční kalkulačku nebo konvertor jednotek

## 💡 Metodický postup

### 1. Aritmetické operátory (8 min) — tabule

Přehled operátorů v Pythonu:

| Operátor | Popis | Příklad | Výsledek |
|----------|-------|---------|---------|
| `+` | sčítání | `3 + 5` | `8` |
| `-` | odčítání | `10 - 4` | `6` |
| `*` | násobení | `6 * 7` | `42` |
| `/` | dělení | `10 / 3` | `3.333...` |
| `//` | celočíselné dělení | `10 // 3` | `3` |
| `%` | zbytek po dělení | `10 % 3` | `1` |
| `**` | umocňování | `2 ** 8` | `256` |

Žáci zkusí v Pythonu: Co je `17 % 5`? Co je `2 ** 10`?

### 2. Konverze typů (7 min) — PC

```python
# Problém:
x = "5"
y = "3"
print(x + y)   # Výsledek: "53" (spojení stringů!)

# Řešení:
x = int("5")
y = int("3")
print(x + y)   # Výsledek: 8

# Jiné konverze:
pi = float("3.14")
text = str(42)
```

Žáci vyzkoušejí a zapíší, co každá funkce dělá.

### 3. Kalkulačka s podmínkou (20 min) — Python

Žáci napíší kalkulačku, která:
1. Načte dvě čísla
2. Zeptá se na operaci (+, -, *, /)
3. Provede výpočet
4. Vypíše výsledek

```python
a = float(input("První číslo: "))
b = float(input("Druhé číslo: "))
op = input("Operace (+, -, *, /): ")

if op == "+":
    print("Výsledek:", a + b)
elif op == "-":
    print("Výsledek:", a - b)
elif op == "*":
    print("Výsledek:", a * b)
elif op == "/":
    if b == 0:
        print("Nelze dělit nulou!")
    else:
        print("Výsledek:", a / b)
else:
    print("Neznámá operace")
```

Rychlí žáci přidají konvertor (km na míle, °C na °F, Kč na EUR).

### 4. Sdílení a reflexe (10 min) — diskuse

2–3 žáci ukáží svůj program. Třída zkusí zadat krajní hodnoty (0, záporná čísla). Diskuse: Co program dělá v neočekávaných situacích?

## 📂 Podklady

- **Online interpret:** replit.com nebo python.org/shell (online REPL)
- **Výzvy pro rychlé žáky:** Konvertor měn (pevný kurz), BMI kalkulačka, výpočet slevy
- **Video (CZ):** YouTube „Python podmínky if else česky"
- **Cheat sheet:** Připravte přehled operátorů a funkcí na A5

!!! tip "Tip pro učitele"
    Ošetření dělení nulou je skvělý příklad, proč programátoři musí myslet na krajní případy. Zeptejte se: „Co by se stalo v reálné aplikaci, kdyby uživatel zadal nulu?" Propojení s bezpečností a robustností softwaru – relevantní pro starší žáky.
