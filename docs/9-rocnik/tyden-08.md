# Debugging: Proč program nefunguje?

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Programování / Testování a ladění
- **Výstup:** <div class="curriculumTag" data-code="I-9-3-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-3-02</span><span style="color: #374151;">Žák testuje a ladí program, opravuje chyby</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-3-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-3-01</span><span style="color: #374151;">Žák vytvoří jednoduchý program v textovém prostředí</span></div>

## 💬 Tip pro pátek
Debugging je skill, který programátoři používají každý den – a většina žáků si myslí, že chyby v kódu jsou selhání. Změňte perspektivu: „Každý profesionální programátor tráví 50 % času debuggingem. Je to normální část práce, ne ostuda."

## 🎯 Cíle hodiny

- Žák rozliší tři typy chyb: syntax error, runtime error a logic error
- Žák přečte a interpretuje chybovou hlášku Pythonu
- Žák systematicky lokalizuje a opraví chyby v připraveném kódu
- Žák použije `print()` jako nástroj debuggingu (print debugging)

## 💡 Metodický postup

### 1. Tři typy chyb (10 min) — tabule

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

### 2. Čtení chybových hlášek (10 min) — PC

Žáci záměrně napíší chybný kód a čtou výstup:

```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print(jmeno)
NameError: name 'jmeno' is not defined
```

Anatomie chybové hlášky:
- **File / line** – kde se chyba vyskytla
- **Typ chyby** – `NameError`, `TypeError`, `ValueError`…
- **Popis** – co přesně se stalo

Žáci dostanu 5 různých chybových hlášek a identifikují typ a příčinu.

### 3. Debugging challenge (18 min) — Python

Žáci dostanou program s 5 chybami (mix syntax, runtime, logic) a opraví je:

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

Správné chyby: 1) chybí `:` za `def`, 2) vzorec BMI špatně `(vaha / vyska**2)`, 3) chybí `)` v `input`, 4) chybí `,` mezi parametry, 5) chybí `:` za `elif`.

### 4. Print debugging (7 min) — diskuse

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
