---
grade: 9
week: 8
time: 45
area: Programování / Testování a ladění
rvp_codes:
  - code: INF-INF-003-ZV9-010
    text: Pro řešení problému vytvoří tabulku evidence dat a stanoví pravidla pro práci se záznamy.
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - "Žák rozliší tři typy chyb: syntax error, runtime error a logic error"
  - Žák přečte a interpretuje chybovou hlášku Pythonu
  - Žák systematicky lokalizuje a opraví chyby v připraveném kódu
  - "Žák použije `print()` jako nástroj debuggingu (print debugging)"
time_budget:
  - type: board
    minutes: 10
  - type: pc
    minutes: 10
  - type: board
    minutes: 18
  - type: discussion
    minutes: 7
friday_tip: "Debugging je skill, který programátoři používají každý den – a většina žáků si myslí, že chyby v kódu jsou selhání. Změňte perspektivu: „Každý profesionální programátor tráví 50 % času debuggingem. Je to normální část práce, ne ostuda.\""
---

# Debugging: Proč program nefunguje?

## 💡 Metodický postup

### 1. Tři typy chyb

<span class="act board">🖊️ Tabule — 10 min</span>

**Syntax Error** – gramatická chyba, Python kód vůbec nespustí:
```python
print("Ahoj"   # chybí závorka
if x = 5:      # = místo ==
```

**Runtime Error** – kód se spustí, ale za běhu havaruje:
```python
x = int("abc")   # ValueError: nelze převést text na číslo
y = 10 / 0       # ZeroDivisionError
```

**Logic Error** – kód běží, ale dělá špatnou věc (nehlásí chybu!):
```python
# Průměr dvou čísel – chyba v logice:
a = 10
b = 20
prumer = a + b / 2   # Správně: (a + b) / 2
print(prumer)        # Vypíše 20, ne 15
```

Logic error je nejnebezpečnější – program nehlásí chybu, ale výsledek je špatný.

### 2. Čtení chybových hlášek

<span class="act pc">💻 PC — 10 min</span>

<div class="zadani-pc" markdown="1">

Otevři [replit.com](https://replit.com) a záměrně napiš chybný kód — přečti a porozuměj chybové hlášce:

```python
print(jmeno)   # proměnná jmeno neexistuje
```

Výstup bude:
```
NameError: name 'jmeno' is not defined
```

Anatomie chybové hlášky:
- **File / line** — kde se chyba stala
- **Typ chyby** — `NameError`, `TypeError`, `ValueError`…
- **Popis** — co přesně se stalo

Nyní spusť tyto kódy jeden po druhém, přečti chybovou hlášku a napiš: Co znamená? Jak ji opravíš?

```python
# Chyba 1
cislo = "5"
print(cislo + 1)

# Chyba 2
print(10 / 0)

# Chyba 3
jmena = ["Anna", "Petr"]
print(jmena[5])
```

</div>

Žáci identifikují typ a příčinu každé chyby.

### 3. Debugging challenge

<span class="act board">🖊️ Tabule — 18 min</span>

<div class="zadani-pc" markdown="1">

Otevři [replit.com](https://replit.com) a zkopíruj do editoru tento program s 5 chybami — najdi je všechny a oprav je:

```python
# Program má 5 chyb – najdi je všechny!
def vypocet_bmi(vaha, vyska)
    bmi = vaha / vyska * vyska
    return bmi

vaha = float(input("Váha v kg: ")
vyska = float(input("Výška v m: "))

bmi = vypocet_bmi(vaha vyska)
print("Vaše BMI je:", bmi)

if bmi < 18.5:
    print("Podváha")
elif bmi < 25.0:
    print("Normální váha")
elif bmi < 30.0
    print("Nadváha")
```

Pro každou nalezenou chybu zapiš do sešitu:
- Na jakém řádku je chyba?
- Jaký typ chyby to je? (syntax / runtime / logic)
- Jak jsi ji opravil/a?

Spusť opravený program a ověř, že funguje správně pro různé hodnoty.

**Pro rychlé žáky:** Přidej do programu větev pro `bmi >= 30` s výpisem „Obezita". Pak použij techniku **print debugging** — přidej `print()` výpisy na klíčová místa a sleduj, jaké hodnoty má program v průběhu výpočtu.

</div>

### 4. Print debugging

<span class="act discussion">💬 Diskuse — 7 min</span>

Technika: Když nevíme, kde je chyba, vložíme `print()` na různá místa:

```python
def vypocet(a, b):
    print("DEBUG: a =", a, "b =", b)   # sledujeme hodnoty
    vysledek = a * b
    print("DEBUG: vysledek =", vysledek)
    return vysledek
```

Profíci používají debugger (nástroj v IDE), ale `print()` je rychlé a vždy funkční.

## 📂 Podklady

- **Online Python:** replit.com – zvýrazňuje syntax chyby v reálném čase
- **Python Tutor:** pythontutor.com – vizualizuje běh kódu krok po kroku (skvělé pro pochopení logic error)
- **Buggy code cvičení:** Připravte 3–5 programů s různými chybami pro individuální práci
- **Video:** YouTube „Python debugging tips" nebo „jak číst chybové hlášky Python"

!!! tip "Tip pro učitele"
    Nejcennější část hodiny je moment, kdy žák sám najde chybu. Nepomáhejte příliš rychle – nechte je 2–3 minuty hledat sami. Frustrace je součástí procesu učení. Oceňte postup, ne jen výsledek: „Skvěle jsi identifikoval, kde problém není – to je polovina debuggingu."
