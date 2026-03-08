# Funkce: Vlastní bloky kódu

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Programování / Algoritmické myšlení
- **Výstup:** <div class="curriculumTag" data-code="I-9-3-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-3-01</span><span style="color: #374151;">Žák vytvoří jednoduchý program v textovém prostředí</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-01</span><span style="color: #374151;">Žák navrhne a zapíše algoritmus řešení problému</span></div>

## 💬 Tip pro pátek
Funkce jsou jako recepty v kuchařce – jednou je napíšeš, pak je opakuješ bez přepisování. Přirovnání ze života žáků: playlist v Spotify je funkce – jednou ho sestavíš, pak ho spouštíš jedno tlačítko.

## 🎯 Cíle hodiny

- Žák definuje vlastní funkci pomocí `def` a zavolá ji
- Žák rozlišuje funkce bez parametrů, s parametry a s návratovou hodnotou (`return`)
- Žák aplikuje princip DRY (Don't Repeat Yourself) – vyčlení opakující se kód do funkce
- Žák napíše program složený z více funkcí

## 💡 Metodický postup

### 1. Proč funkce? (8 min) — tabule

Problém bez funkce – opakující se kód:
```python
print("=" * 20)
print("Ahoj!")
print("=" * 20)

print("=" * 20)
print("Nashledanou!")
print("=" * 20)
```

Řešení s funkcí:
```python
def ramecek(text):
    print("=" * 20)
    print(text)
    print("=" * 20)

ramecek("Ahoj!")
ramecek("Nashledanou!")
ramecek("Jak se máš?")
```

Princip **DRY**: Don't Repeat Yourself. Změna rámu stačí na jednom místě.

### 2. Anatomie funkce (12 min) — tabule + PC

```python
def pozdrav(jmeno, hodina):      # def + název + parametry
    if hodina < 12:
        return f"Dobré ráno, {jmeno}!"
    elif hodina < 18:
        return f"Dobré odpoledne, {jmeno}!"
    else:
        return f"Dobrý večer, {jmeno}!"

zprava = pozdrav("Honza", 10)    # volání funkce
print(zprava)                    # "Dobré ráno, Honza!"
```

Klíčové pojmy:
- `def` – klíčové slovo pro definici funkce
- **parametry** – vstupy funkce (v závorce)
- `return` – výstup funkce (vrácená hodnota)
- **volání** – spuštění funkce s konkrétními argumenty

### 3. Vlastní funkce (18 min) — Python

Žáci napíší program s alespoň 3 vlastními funkcemi:

**Ukázkový projekt – jednoduchý kvíz:**
```python
def otazka(text, spravna):
    odpoved = input(text)
    if odpoved.lower() == spravna.lower():
        print("Správně!")
        return 1
    else:
        print(f"Špatně. Správná odpověď: {spravna}")
        return 0

def vysledek(body, celkem):
    print(f"\nSkóre: {body}/{celkem}")
    if body == celkem:
        print("Perfektní výsledek!")
    elif body >= celkem / 2:
        print("Dobrá práce!")
    else:
        print("Příště lépe!")

# Hlavní program
body = 0
body += otazka("Hlavní město ČR? ", "Praha")
body += otazka("Kolik je 7 * 8? ", "56")
body += otazka("Zkratka CPU? ", "Central Processing Unit")
vysledek(body, 3)
```

Žáci napíší vlastní verzi kvízu nebo jiný projekt s funkcemi.

### 4. Reflexe a přehled (7 min) — diskuse

Shrnutí: Co funkce umí?
- Rozdělit velký problém na menší části
- Kód znovu použít bez kopírování
- Kód lépe číst a testovat

Náhled na příště: Funkce jsou základ projektu – každý projekt bude složen z funkcí.

## 📂 Podklady

- **Online Python:** replit.com – sdílejte kvíz šablonu jako startovní kód
- **Cvičení:** Přepsat kód „spaghetti" do funkcí – klasická refaktorovací úloha
- **Video (CZ):** YouTube „Python funkce def česky"
- **Rozšíření pro rychlé žáky:** Rekurze – funkce, která volá samu sebe (faktoriál)

!!! tip "Tip pro učitele"
    Častá chyba: žáci napíší funkci, ale zapomenou ji zavolat, nebo zavolají před definicí. Ukažte obojí jako příklady chyb. Také upozorněte na rozsah proměnných (scope) – proměnná uvnitř funkce „neexistuje" vně. Jednoduchá demonstrace: `def test(): x = 5` a pak `print(x)` vyvolá NameError.
