---
grade: 9
week: 6
time: 45
area: Programování / Algoritmické myšlení
rvp_codes:
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - Žák používá aritmetické operátory Pythonu včetně celočíselného dělení a zbytku
  - "Žák převádí datové typy pomocí `int()`, `float()` a `str()`"
  - "Žák napíše program s podmínkou `if/elif/else`"
  - Žák vytvoří funkční kalkulačku nebo konvertor jednotek
time_budget:
  - type: board
    minutes: 8
  - type: pc
    minutes: 7
  - type: board
    minutes: 20
  - type: discussion
    minutes: 10
friday_tip: "Nechejte žáky si vybrat, co jejich kalkulačka bude počítat – BMI, cenu nákupu, převod měn. Vlastní volba zvyšuje zapojení. Pokud třída zvládá rychle, přidejte podmínku: „Pokud BMI > 25, vypiš upozornění.\""
---

# Python II: Jednoduché výpočty

## 💡 Metodický postup

### 1. Aritmetické operátory

<span class="act board">🖊️ Tabule — 8 min</span>

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

### 2. Konverze typů

<span class="act pc">💻 PC — 7 min</span>

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

### 3. Kalkulačka s podmínkou

<span class="act board">🖊️ Tabule — 20 min</span>

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

### 4. Sdílení a reflexe

<span class="act discussion">💬 Diskuse — 10 min</span>

2–3 žáci ukáží svůj program. Třída zkusí zadat krajní hodnoty (0, záporná čísla). Diskuse: Co program dělá v neočekávaných situacích?

## 📂 Podklady

- **Online interpret:** replit.com nebo python.org/shell (online REPL)
- **Výzvy pro rychlé žáky:** Konvertor měn (pevný kurz), BMI kalkulačka, výpočet slevy
- **Video (CZ):** YouTube „Python podmínky if else česky"
- **Cheat sheet:** Připravte přehled operátorů a funkcí na A5

!!! tip "Tip pro učitele"
    Ošetření dělení nulou je skvělý příklad, proč programátoři musí myslet na krajní případy. Zeptejte se: „Co by se stalo v reálné aplikaci, kdyby uživatel zadal nulu?" Propojení s bezpečností a robustností softwaru – relevantní pro starší žáky.
