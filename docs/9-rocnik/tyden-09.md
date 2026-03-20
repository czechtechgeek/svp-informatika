---
grade: 9
week: 9
time: 45
area: Programování / Data a informace
rvp_codes:
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
  - code: INF-INF-001-ZV9-001
    text: "Získá z dat informace, interpretuje data získaná pro řešení konkrétního problému."
goals:
  - "Žák vytvoří seznam (`list`) v Pythonu a přistupuje k jeho prvkům pomocí indexu"
  - "Žák přidává a odebírá prvky ze seznamu (`append`, `remove`, `pop`)"
  - "Žák prochází seznam pomocí `for` cyklu"
  - "Žák používá funkce `len()`, `sorted()`, `min()`, `max()` na seznamech"
time_budget:
  - type: discussion
    minutes: 8
  - type: pc
    minutes: 12
  - type: board
    minutes: 15
  - type: discussion
    minutes: 10
friday_tip: "Použijte reálná data třídy – oblíbené filmy, hry nebo jídla. „Napište mi každý jeden oblíbený film\" – sbírejte odpovědi a vytvořte z nich seznam živě před třídou. Osobní data okamžitě zvyšují zájem."
---

# Seznamy: Práce s více daty najednou

## 💡 Metodický postup

### 1. Proč potřebujeme seznamy?

<span class="act discussion">💬 Diskuse — 8 min</span>

Problém bez seznamu: Chceme uložit 5 oblíbených filmů:
```python
film1 = "Avengers"
film2 = "Matrix"
film3 = "Interstellar"
# ... a co 100 filmů?
```

Řešení – seznam:
```python
filmy = ["Avengers", "Matrix", "Interstellar", "Titanic", "Joker"]
print(filmy[0])   # "Avengers" – indexy začínají od 0!
print(filmy[-1])  # "Joker" – záporný index = od konce
print(len(filmy)) # 5 – délka seznamu
```

### 2. Operace se seznamy

<span class="act pc">💻 PC — 12 min</span>

<div class="zadani-pc">

Otevři [replit.com](https://replit.com) a zkopíruj/napiš tento kód. Pak ho spusť a experimentuj:

```python
znamy = ["Honza", "Petra", "Martin"]

# Přidání na konec
znamy.append("Lucie")
print(znamy)

# Odebrání
znamy.remove("Martin")
print(znamy)

# Seřazení
znamy.sort()
print(znamy)  # abecedně

# Procházení
for jmeno in znamy:
    print("Ahoj,", jmeno)
```

Teď vytvoř **vlastní seznam** — oblíbené hry, filmy, jídla nebo cokoliv jiného:
1. Vytvoř seznam s alespoň 5 položkami
2. Přidej 2 nové pomocí `append()`
3. Odeber 1 pomocí `remove()`
4. Seřaď seznam a vypiš každou položku pomocí cyklu `for`

</div>

Žáci si vytvoří vlastní seznam a vyzkouší operace.

### 3. Práce s číselnými seznamy

<span class="act board">🖊️ Tabule — 15 min</span>

```python
teploty = [18, 22, 25, 19, 23, 21, 17]   # teploty za týden

print("Maximální teplota:", max(teploty))
print("Minimální teplota:", min(teploty))
print("Průměr:", sum(teploty) / len(teploty))
print("Seřazené:", sorted(teploty))

# Procházení s indexem
for i, t in enumerate(teploty):
    print(f"Den {i+1}: {t}°C")
```

**Výzva:** Žáci napíší program, který:
1. Nechá uživatele zadat 5 čísel (pomocí cyklu a `append`)
2. Vypíše největší, nejmenší a průměr

### 4. Reflexe: Kdy použít seznam?

<span class="act discussion">💬 Diskuse — 10 min</span>

| Situace | Řešení |
|---------|--------|
| Uložit jednu hodnotu | proměnná |
| Uložit N hodnot stejného typu | seznam |
| Uložit pár klíč–hodnota | slovník (příště) |

## 📂 Podklady

- **Online Python:** replit.com – vyzkoušejte seznam žáků třídy jako příklad
- **Cvičení:** Připravte 3 úlohy: filtrování seznamu, hledání duplicit, spojení dvou seznamů
- **Video (CZ):** YouTube „Python list česky" nebo „Python seznamy"
- **Rozšíření:** List comprehension – elegantní zkratka pro práci se seznamy (pro rychlé žáky)

!!! tip "Tip pro učitele"
    Index od nuly je pro žáky zpočátku matoucí. Použijte analogii: „Výtah v Americe – přízemí je 0, první patro je 1." Nebo: „Stojíš na startovní čáře, první krok je krok č. 0." Záporné indexy (`-1` = poslední prvek) ocení žáci jako „cool trik". Nechte je hádat, co vypíše `filmy[-2]`.
