# Seznamy: Práce s více daty najednou

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Programování / Data a informace
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-009" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-009</span><span style="color: #374151;">Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-001-ZV9-001" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-001-ZV9-001</span><span style="color: #374151;">Získá z dat informace, interpretuje data získaná pro řešení konkrétního problému.</span></div>

## 💬 Tip pro pátek
Použijte reálná data třídy – oblíbené filmy, hry nebo jídla. „Napište mi každý jeden oblíbený film" – sbírejte odpovědi a vytvořte z nich seznam živě před třídou. Osobní data okamžitě zvyšují zájem.

## 🎯 Cíle hodiny

- Žák vytvoří seznam (`list`) v Pythonu a přistupuje k jeho prvkům pomocí indexu
- Žák přidává a odebírá prvky ze seznamu (`append`, `remove`, `pop`)
- Žák prochází seznam pomocí `for` cyklu
- Žák používá funkce `len()`, `sorted()`, `min()`, `max()` na seznamech

## 💡 Metodický postup

### 1. Proč potřebujeme seznamy? (8 min) — diskuse

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

### 2. Operace se seznamy (12 min) — PC

```python
znamy = ["Honza", "Petra", "Martin"]

# Přidání na konec
znamy.append("Lucie")
print(znamy)  # ["Honza", "Petra", "Martin", "Lucie"]

# Odebrání
znamy.remove("Martin")
print(znamy)  # ["Honza", "Petra", "Lucie"]

# Seřazení
znamy.sort()
print(znamy)  # abecedně

# Procházení
for jmeno in znamy:
    print("Ahoj,", jmeno)
```

Žáci si vytvoří vlastní seznam (oblíbené hry, filmy, jídla) a vyzkouší operace.

### 3. Práce s číselnými seznamy (15 min) — Python

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

### 4. Reflexe: Kdy použít seznam? (10 min) — diskuse

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
