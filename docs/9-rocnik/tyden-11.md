---
grade: 9
week: 11
time: 45
area: Algoritmizace a programování / Projektová výuka
rvp_codes:
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - Žák vybere téma závěrečného projektu z nabídky a zdůvodní svůj výběr
  - "Žák sepíše specifikaci projektu: co program bude dělat, co bude vstup a výstup"
  - Žák vytvoří pseudokód nebo vývojový diagram hlavní logiky programu
  - Žák odhadne složitost projektu a rozplánuje práci na příští hodinu
time_budget:
  - type: board
    minutes: 10
  - type: unplugged
    minutes: 10
  - type: unplugged
    minutes: 18
  - type: discussion
    minutes: 7
friday_tip: "Nechte žáky vybrat si téma projektu sami — vlastní volba výrazně zvyšuje motivaci. Pokud někdo neví, dejte mu 5 minut na rozmyšlení a pak mu pomozte výběrem — nepřikazujte. Kdo má jasno od začátku, může rovnou začít s pseudokódem."
---

# Kostra: Kvíz

## 💡 Metodický postup

### 1. Představení projektu a zadání

<span class="act board">🖊️ Tabule — 10 min</span>

Učitel vysvětlí smysl závěrečného projektu: nejde o dokonalý program, ale o vlastní kompletní dílo, které žák umí vysvětlit.

**Čtyři připravená zadání (žák si vybere jedno):**

| Projekt | Co dělá | Klíčové koncepty |
|---------|---------|-----------------|
| **Kalkulačka** | Počítá příklady zadané uživatelem (+, −, ×, ÷) | funkce, podmínky, cyklus, vstup/výstup |
| **Kvíz** | Ptá se na otázky, počítá skóre, zobrazí výsledek | seznam, cyklus, podmínky, formátování |
| **Textová hra** | Příběh s větvením — hráč volí možnosti A/B/C | podmínky, funkce, proměnné |
| **Konvertor** | Převádí jednotky (km↔míle, °C↔°F, kg↔libry) | funkce, slovník, vstup/výstup |

Pravidla projektu:
- Program musí fungovat (spustit se bez chyby)
- Musí mít alespoň 30 řádků kódu
- Žák ho musí umět vysvětlit spolužákovi

### 2. Výběr tématu a specifikace

<span class="act unplugged">✋ Bez počítače — 10 min</span>

Každý žák dostane kartičku / list papíru a vyplní specifikaci:

```
Název projektu: ___________________________
Co program dělá (1–2 věty): ________________
Vstup (co zadá uživatel): __________________
Výstup (co program zobrazí): _______________
Nejsložitější část, kterou musím vyřešit: ____
```

Příklad vyplnění pro kvíz:
```
Název: Kvíz o fotbale
Co dělá: Program pokládá 10 otázek o fotbale, po každé odpovědi řekne
         správně/špatně a na konci zobrazí skóre
Vstup: Uživatel píše a, b nebo c
Výstup: Správně/Špatně + finální skóre X/10
Nejsložitější: Uložit všechny otázky a odpovědi přehledně
```

### 3. Pseudokód — naplánování logiky

<span class="act unplugged">✋ Bez počítače — 18 min</span>

Žáci napíší pseudokód svého projektu. Učitel ukáže příklad na tabuli:

**Příklad pseudokódu pro kvíz:**
```
PROGRAM: Kvíz o fotbale

nastav skóre = 0
nastav seznam otázek a správných odpovědí

PRO každou otázku v seznamu:
    zobraz otázku
    zobraz možnosti a, b, c
    načti odpověď od uživatele
    POKUD odpověď = správná odpověď:
        vypiš "Správně!"
        přidej 1 ke skóre
    JINAK:
        vypiš "Špatně, správná odpověď byla X"

zobraz "Tvé skóre: [skóre] z 10"
POKUD skóre >= 8:
    vypiš "Výborně!"
JINAK POKUD skóre >= 5:
    vypiš "Dobrý výkon!"
JINAK:
    vypiš "Příště to zvládneš lépe!"
```

Učitel obchází třídu a kontroluje pseudokódy — 5 minut individuální konzultace.

### 4. Sdílení plánu a zpětná vazba

<span class="act discussion">💬 Diskuse — 7 min</span>

Dobrovolníci (2–3 žáci) krátce představí svůj plán: „Dělám ___, program bude umět ___." Třída může pokládat otázky. Učitel upozorní na typická úskalí (dělení nulou v kalkulačce, nevalidní vstup, nekonečná smyčka).

## 📂 Podklady

- **Šablona specifikace:** Připravte papírový formulář nebo sdílený Google Docs pro vyplnění specifikace projektu
- **Kostra kódu — kvíz:** Viz ukázka níže jako výchozí bod pro žáky
- **Kostra kódu — kalkulačka:** Viz ukázka níže
- **Referenční karta Python:** Připomeňte žákům přehled příkazů z předchozích hodin
- **Hodnotící kritéria projektu:** Sdělte předem — funkčnost (50 %), čitelnost kódu (25 %), prezentace (25 %)

```python
# Kostra: Kvíz
otazky = [
    {
        "otazka": "Kdo vyhrál MS ve fotbale 2022?",
        "moznosti": ["a) Brazílie", "b) Argentina", "c) Francie"],
        "spravna": "b"
    },
    # přidej další otázky...
]

skore = 0

for q in otazky:
    print("\n" + q["otazka"])
    for m in q["moznosti"]:
        print(m)
    odpoved = input("Tvá odpověď (a/b/c): ").lower().strip()
    if odpoved == q["spravna"]:
        print("Správně!")
        skore += 1
    else:
        print(f"Špatně. Správná odpověď: {q['spravna']}")

print(f"\nTvé skóre: {skore}/{len(otazky)}")
```

```python
# Kostra: Kalkulačka
def scitani(a, b):
    return a + b

def odcitani(a, b):
    return a - b

def nasobeni(a, b):
    return a * b

def deleni(a, b):
    if b == 0:
        return "Chyba: dělení nulou!"
    return a / b

print("=== Kalkulačka ===")
a = float(input("První číslo: "))
operace = input("Operace (+, -, *, /): ")
b = float(input("Druhé číslo: "))

# Doplň podmínky pro výběr operace...
if operace == "+":
    print(f"Výsledek: {scitani(a, b)}")
# ...
```

!!! tip "Tip pro učitele"
    Největší chyba žáků je, že chtějí naprogramovat příliš složitý projekt. Pokud vidíte, že plán je nerealistický (např. RPG hra s grafickým rozhraním), jemně ho omezte — „super nápad, ale pro tyto dvě hodiny zkus zaměřit na jádro". Kvalitní pseudokód v této hodině je klíč — žáci, kteří ho přeskočí, se příští hodinu ztratí v kódu bez jasného cíle.
