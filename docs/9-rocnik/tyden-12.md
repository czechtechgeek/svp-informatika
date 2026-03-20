# Závěrečný kódovací projekt II: Vývoj

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování / Debugging
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-009" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-009</span><span style="color: #374151;">Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-010" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-010</span><span style="color: #374151;">Pro řešení problému vytvoří tabulku evidence dat a stanoví pravidla pro práci se záznamy.</span></div>

## 💬 Tip pro pátek
Dejte žákům od začátku jasný časový plán: „Za 30 minut musí program fungovat alespoň v základu." Krátké check-iny každých 10 minut (zvedněte ruku, kdo má spuštěný alespoň první část) udržují tempo celé třídy.

## 🎯 Cíle hodiny

- Žák implementuje pseudokód z minulé hodiny do funkčního Python programu
- Žák identifikuje a opraví alespoň jednu chybu pomocí debuggingu
- Žák provede peer-review — otestuje kód spolužáka a poskytne konstruktivní zpětnou vazbu
- Žák program dokončí do prezentovatelné podoby s komentáři v kódu

## 💡 Metodický postup

### 1. Rychlý check-in a připomenutí (5 min) — tabule

Učitel krátce shrne: „Dnes kódujete, já chodím a pomáhám. Cíl: funkční program."

Připomenout nejčastější chyby v Pythonu:

| Chyba | Příklad | Oprava |
|-------|---------|--------|
| `IndentationError` | Chybná odsazenost | Zkontroluj mezery/tabu |
| `NameError` | Proměnná neexistuje | Zkontroluj překlep v názvu |
| `ValueError` | `int("ahoj")` | Ošetři vstup přes `try/except` |
| `ZeroDivisionError` | `10 / 0` | Přidej podmínku `if b != 0` |
| Nekonečná smyčka | `while True` bez `break` | Přidej podmínku ukončení |

### 2. Samostatná práce na projektu (25 min) — Python

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

### 3. Peer-review (10 min) — diskuse / Python

Žáci si vymění počítače (nebo sedí vedle sebe) a testují projekt spolužáka.

**Kontrolní seznam pro testování:**
- Program se spustí bez chyby? ✓/✗
- Co se stane, když zadám neplatný vstup (písmeno místo čísla)? ✓/✗
- Jsou výpisy čitelné a srozumitelné? ✓/✗
- Funguje ukončení programu správně? ✓/✗
- Chápu, co program dělá, i bez vysvětlení autora? ✓/✗

Každý tester napíše spolužákovi 1 věc, která funguje dobře, a 1 věc k vylepšení.

### 4. Finalizace a komentáře (5 min) — Python

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
