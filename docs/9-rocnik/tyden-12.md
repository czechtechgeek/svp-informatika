---
grade: 9
week: 12
time: 45
area: Algoritmizace a programování / Debugging
rvp_codes:
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
  - code: INF-INF-003-ZV9-010
    text: Pro řešení problému vytvoří tabulku evidence dat a stanoví pravidla pro práci se záznamy.
goals:
  - Žák implementuje pseudokód z minulé hodiny do funkčního Python programu
  - Žák identifikuje a opraví alespoň jednu chybu pomocí debuggingu
  - Žák provede peer-review — otestuje kód spolužáka a poskytne konstruktivní zpětnou vazbu
  - Žák program dokončí do prezentovatelné podoby s komentáři v kódu
time_budget:
  - type: board
    minutes: 5
  - type: board
    minutes: 25
  - type: discussion
    minutes: 10
  - type: board
    minutes: 5
friday_tip: "Dejte žákům od začátku jasný časový plán: „Za 30 minut musí program fungovat alespoň v základu.\" Krátké check-iny každých 10 minut (zvedněte ruku, kdo má spuštěný alespoň první část) udržují tempo celé třídy."
---

# Strategie 1: Vypisování mezivýsledků

## 💡 Metodický postup

### 1. Rychlý check-in a připomenutí

<span class="act board">🖊️ Tabule — 5 min</span>

Učitel krátce shrne: „Dnes kódujete, já chodím a pomáhám. Cíl: funkční program."

Připomenout nejčastější chyby v Pythonu:

| Chyba | Příklad | Oprava |
|-------|---------|--------|
| `IndentationError` | Chybná odsazenost | Zkontroluj mezery/tabu |
| `NameError` | Proměnná neexistuje | Zkontroluj překlep v názvu |
| `ValueError` | `int("ahoj")` | Ošetři vstup přes `try/except` |
| `ZeroDivisionError` | `10 / 0` | Přidej podmínku `if b != 0` |
| Nekonečná smyčka | `while True` bez `break` | Přidej podmínku ukončení |

### 2. Samostatná práce na projektu

<span class="act board">🖊️ Tabule — 25 min</span>

Žáci pracují samostatně na svém projektu. Učitel obchází třídu a pomáhá.

**Doporučené kroky při kódování:**
1. Nejprve zprovoznit základní kostru (vstup → výstup)
2. Přidat podmínky a cykly
3. Otestovat s různými vstupy
4. Přidat komentáře

**Debugovací strategie — ukažte na tabuli:**
```python
# Strategie 1: Vypisování mezivýsledků
skore = 0
for i, q in enumerate(otazky):
    print(f"--- Otázka {i+1} ---")   # DEBUG výpis
    odpoved = input(q["otazka"] + " ")
    print(f"Odpověď: {odpoved}, Správná: {q['spravna']}")  # DEBUG
    if odpoved == q["spravna"]:
        skore += 1
print(f"Finální skóre: {skore}")
# Po opravení chyby DEBUG výpisy smaž nebo zakomentuj
```

```python
# Strategie 2: Ošetření chybného vstupu
while True:
    try:
        cislo = float(input("Zadej číslo: "))
        break  # vstup byl platný, vyjde ze smyčky
    except ValueError:
        print("To není číslo! Zkus znovu.")
```

```python
# Typická chyba v konvertoru — špatné pořadí operací:
# ŠPATNĚ:
fahrenheit = stupen_c + 32 * 9 / 5   # matematická priorita!
# SPRÁVNĚ:
fahrenheit = (stupen_c * 9 / 5) + 32
```

Učitel věnuje 2–3 minuty každému žákovi nebo skupince. Priorita pomoci: ti, kteří mají prázdnou obrazovku nebo chybovou hlášku, které nechápou.

### 3. Peer-review

<span class="act discussion">💬 Diskuse — 10 min</span>

Žáci si vymění počítače (nebo sedí vedle sebe) a testují projekt spolužáka.

**Kontrolní seznam pro testování:**
- Program se spustí bez chyby? ✓/✗
- Co se stane, když zadám neplatný vstup (písmeno místo čísla)? ✓/✗
- Jsou výpisy čitelné a srozumitelné? ✓/✗
- Funguje ukončení programu správně? ✓/✗
- Chápu, co program dělá, i bez vysvětlení autora? ✓/✗

Každý tester napíše spolužákovi 1 věc, která funguje dobře, a 1 věc k vylepšení.

### 4. Finalizace a komentáře

<span class="act board">🖊️ Tabule — 5 min</span>

Žáci zapracují zpětnou vazbu a přidají komentáře do kódu:

```python
# Příklad dobře komentovaného kódu:
def vypocti_skore(spravnych, celkem):
    """Vrátí procentuální skóre jako celé číslo."""
    if celkem == 0:
        return 0
    return int((spravnych / celkem) * 100)

# Hlavní smyčka programu
for otazka in seznam_otazek:
    zobraz_otazku(otazka)      # zobrazí otázku s možnostmi
    odpoved = nacti_odpoved()  # načte a validuje vstup
    zkontroluj_odpoved(odpoved, otazka["spravna"])  # aktualizuje skóre
```

## 📂 Podklady

- **Python IDE:** Doporučit Thonny (pro začátečníky) nebo VS Code; alternativa online: replit.com nebo python.org/shell
- **Dokumentace Python (CZ):** docs.python.org/cs — základní datové typy a funkce
- **Cheatsheet Python (tisk):** Připravte jednostránkový přehled: podmínky, cykly, funkce, seznam, slovník
- **Hodnotící arch peer-review:** Vytiskněte nebo sdílejte digitálně pro strukturovanou zpětnou vazbu
- **Vzorová řešení:** Mějte připravená plně funkční vzorová řešení pro případ, že žák úplně ztroskotá

```python
# Vzorové řešení: Textová hra (ukázka větvení)
def zacatek():
    print("=== Záhada v lese ===")
    print("Jdeš lesem a narazíš na rozcestí.")
    print("a) Jdeš vlevo k jezeru")
    print("b) Jdeš vpravo k jeskyni")
    volba = input("Tvá volba (a/b): ").lower()
    if volba == "a":
        jezero()
    elif volba == "b":
        jeskyne()
    else:
        print("Neplatná volba, zkus znovu.")
        zacatek()

def jezero():
    print("\nU jezera najdeš starou loďku.")
    print("a) Vypluj na loďce")
    print("b) Vrať se zpět")
    volba = input("Tvá volba (a/b): ").lower()
    if volba == "a":
        print("\nNa ostrůvku najdeš poklad! Vyhrál/a jsi!")
    else:
        zacatek()

def jeskyne():
    print("\nV jeskyni je tma. Slyšíš podivný zvuk.")
    print("Utíkáš ven. Konec hry.")

zacatek()
```

!!! tip "Tip pro učitele"
    Nejúčinnější pomoc při debuggingu je nekódovat za žáka — místo toho pokládejte otázky: „Co si myslíš, že tento řádek dělá?" nebo „Kde přesně program přestane fungovat?". Pokud žák neví vůbec jak pokračovat, ukažte analogický příklad v jiném kontextu — mozek si pak sám přenese princip.
