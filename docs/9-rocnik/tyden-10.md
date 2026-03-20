---
grade: 9
week: 10
time: 45
area: Programování / Algoritmické myšlení
rvp_codes:
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - "Žák definuje vlastní funkci pomocí `def` a zavolá ji"
  - "Žák rozlišuje funkce bez parametrů, s parametry a s návratovou hodnotou (`return`)"
  - "Žák aplikuje princip DRY (Don't Repeat Yourself) – vyčlení opakující se kód do funkce"
  - Žák napíše program složený z více funkcí
time_budget:
  - type: board
    minutes: 8
  - type: pc
    minutes: 12
  - type: board
    minutes: 18
  - type: discussion
    minutes: 7
friday_tip: "Funkce jsou jako recepty v kuchařce – jednou je napíšeš, pak je opakuješ bez přepisování. Přirovnání ze života žáků: playlist v Spotify je funkce – jednou ho sestavíš, pak ho spouštíš jedno tlačítko."
---

# Funkce: Vlastní bloky kódu

## 💡 Metodický postup

### 1. Proč funkce?

<span class="act board">🖊️ Tabule — 8 min</span>

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

### 2. Anatomie funkce

<span class="act pc">💻 PC — 12 min</span>

<div class="zadani-pc" markdown="1">

**Úloha — Anatomie funkce** (12 min)

Napiš do [replit.com](https://replit.com) tento kód a spusť ho:

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

Zkus zavolat funkci s různými hodnotami hodiny (10, 15, 22) a svým vlastním jménem. Co se změnilo?

</div>

Klíčové pojmy:
- `def` – klíčové slovo pro definici funkce
- **parametry** – vstupy funkce (v závorce)
- `return` – výstup funkce (vrácená hodnota)
- **volání** – spuštění funkce s konkrétními argumenty

### 3. Vlastní funkce

<span class="act board">🖊️ Tabule — 18 min</span>

<div class="zadani-pc" markdown="1">

**Projekt — Vlastní kvíz s funkcemi** (18 min)

Napiš program, který obsahuje **alespoň 3 vlastní funkce**. Jako základ použij tento kvíz a uprav ho na vlastní otázky:

```python
def otazka(text, spravna):
    odpoved = input(text)
    if odpoved.lower() == spravna.lower():
        print("Správně! ✅")
        return 1
    else:
        print(f"Špatně. Správná odpověď: {spravna}")
        return 0

def vysledek(body, celkem):
    print(f"\nSkóre: {body}/{celkem}")
    if body == celkem:
        print("Perfektní výsledek! 🏆")
    elif body >= celkem / 2:
        print("Dobrá práce! 👍")
    else:
        print("Příště lépe! 💪")

# Hlavní program
body = 0
body += otazka("Hlavní město ČR? ", "Praha")
body += otazka("Kolik je 7 * 8? ", "56")
body += otazka("Zkratka CPU? ", "Central Processing Unit")
vysledek(body, 3)
```

Uprav aspoň 3 otázky na vlastní téma (sport, zeměpis, filmy...). Kdo chce, může přidat 4. funkci — třeba `uvod()`, která přivítá hráče.

</div>

Žáci napíší vlastní verzi kvízu nebo jiný projekt s funkcemi.

### 4. Reflexe a přehled

<span class="act discussion">💬 Diskuse — 7 min</span>

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
