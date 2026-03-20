---
grade: 9
week: 5
time: 45
area: Programování / Algoritmické myšlení
rvp_codes:
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - Žák spustí Python v online prostředí a napíše svůj první program
  - "Žák používá příkaz `print()` k výpisu textu a čísel"
  - "Žák vytvoří proměnnou a přiřadí jí hodnotu různých typů (int, str)"
  - "Žák napíše interaktivní program, který reaguje na vstup uživatele pomocí `input()`"
time_budget:
  - type: pc
    minutes: 8
  - type: pc
    minutes: 12
  - type: board
    minutes: 15
  - type: discussion
    minutes: 10
friday_tip: "První hodina Pythonu je klíčová pro motivaci. Nechejte žáky co nejrychleji zažít úspěch – program, který dělá cokoli viditelného. „Hello, World!\" za 5 minut od spuštění editoru je ideální start. Neřešte hned instalaci – použijte online prostředí."
---

# Python I: Print, proměnné, input

## 💡 Metodický postup

### 1. Spuštění prostředí a první program

<span class="act pc">💻 PC — 8 min</span>

Žáci otevřou replit.com nebo trinket.io a vytvoří nový Python projekt.

Učitel diktuje, žáci píší:

```python
print("Ahoj, světe!")
print("Jmenuji se Python.")
print(2025)
print(3 + 5)
```

Spustí program (Run). Diskuse: `print()` je funkce – dává počítači příkaz „vypiš toto".

### 2. Proměnné – krabičky na data

<span class="act pc">💻 PC — 12 min</span>

Učitel na tabuli: Proměnná je pojmenovaná „krabička" v paměti počítače.

```python
jmeno = "Honza"
vek = 15
oblibena_cisla = 7

print("Jmenuji se", jmeno)
print("Je mi", vek, "let")
print("Moje číslo je", oblibena_cisla)
```

Klíčové pojmy:
- **str** (string) – text v uvozovkách: `"Ahoj"`
- **int** (integer) – celé číslo: `42`
- **float** – desetinné číslo: `3.14`

Žáci změní hodnoty proměnných a spustí znovu.

### 3. Vstup od uživatele: input()

<span class="act board">🖊️ Tabule — 15 min</span>

```python
jmeno = input("Jak se jmenuješ? ")
print("Ahoj,", jmeno, "!")

vek = int(input("Kolik ti je let? "))
print("Za 10 let ti bude", vek + 10, "let.")
```

Důležité: `input()` vždy vrací **string**. Pokud chceme počítat, musíme převést na číslo pomocí `int()` nebo `float()`.

Žáci napíší vlastní verzi „představovacího programu" – program se zeptá na jméno, věk a oblíbené číslo a vypíše o uživateli větu.

### 4. Ukázka chyby a reflexe

<span class="act discussion">💬 Diskuse — 10 min</span>

Učitel záměrně napíše chybný kód:

```python
vek = input("Věk: ")
print(vek + 1)  # Chyba! Nelze sčítat string a číslo
```

Žáci čtou chybovou hlášku: `TypeError: can only concatenate str (not "int") to str`

Oprava: `vek = int(input("Věk: "))`

Reflexe: Python je přesný – musíme mu říct, jaký typ dat zpracovává.

## 📂 Podklady

- **Online prostředí:** replit.com (doporučeno, bez instalace), trinket.io (alternativa)
- **Thonny IDE:** thonny.org – pro instalaci na školní počítače, ideální pro začátečníky
- **Kurz (CZ):** naucsepython.cz – český úvod do Pythonu pro začátečníky
- **Referenční karta:** Připravte A5 přehled základních příkazů: print, input, int, str, float

!!! tip "Tip pro učitele"
    Nenechte žáky ztrácet čas instalací. Online prostředí (Replit) funguje okamžitě a není třeba nic nastavovat. Klíčový moment je, když žák poprvé spustí vlastní program a „funguje to" – chraňte tento okamžik. Žáci, kteří zažijí brzký úspěch, jsou motivovanější pro celý zbytek kurzu.
