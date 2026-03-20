# Python I: Print, proměnné, input

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Programování / Algoritmické myšlení
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-009" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-009</span><span style="color: #374151;">Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-002-ZV9-006" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-002-ZV9-006</span><span style="color: #374151;">Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.</span></div>

## 💬 Tip pro pátek
První hodina Pythonu je klíčová pro motivaci. Nechejte žáky co nejrychleji zažít úspěch – program, který dělá cokoli viditelného. „Hello, World!" za 5 minut od spuštění editoru je ideální start. Neřešte hned instalaci – použijte online prostředí.

## 🎯 Cíle hodiny

- Žák spustí Python v online prostředí a napíše svůj první program
- Žák používá příkaz `print()` k výpisu textu a čísel
- Žák vytvoří proměnnou a přiřadí jí hodnotu různých typů (int, str)
- Žák napíše interaktivní program, který reaguje na vstup uživatele pomocí `input()`

## 💡 Metodický postup

### 1. Spuštění prostředí a první program (8 min) — PC

Žáci otevřou replit.com nebo trinket.io a vytvoří nový Python projekt.

Učitel diktuje, žáci píší:

```python
print("Ahoj, světe!")
print("Jmenuji se Python.")
print(2025)
print(3 + 5)
```

Spustí program (Run). Diskuse: `print()` je funkce – dává počítači příkaz „vypiš toto".

### 2. Proměnné – krabičky na data (12 min) — tabule + PC

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

### 3. Vstup od uživatele: input() (15 min) — Python

```python
jmeno = input("Jak se jmenuješ? ")
print("Ahoj,", jmeno, "!")

vek = int(input("Kolik ti je let? "))
print("Za 10 let ti bude", vek + 10, "let.")
```

Důležité: `input()` vždy vrací **string**. Pokud chceme počítat, musíme převést na číslo pomocí `int()` nebo `float()`.

Žáci napíší vlastní verzi „představovacího programu" – program se zeptá na jméno, věk a oblíbené číslo a vypíše o uživateli větu.

### 4. Ukázka chyby a reflexe (10 min) — diskuse

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
