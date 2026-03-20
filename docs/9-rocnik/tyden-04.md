---
grade: 9
week: 4
time: 45
area: Algoritmické myšlení a programování
rvp_codes:
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - "Žák zapíše podmínku a cyklus nejprve v pseudokódu, pak v syntaxi Pythonu"
  - Žák přeloží blokový kód ze Scratche do textového kódu
  - "Žák rozlišuje `for` cyklus (opakování pevněkrát) a `while` cyklus (opakování dokud platí podmínka)"
  - Žák odladí drobnou chybu v připraveném kódu
time_budget:
  - type: board
    minutes: 10
  - type: pc
    minutes: 15
  - type: pc
    minutes: 12
  - type: discussion
    minutes: 8
friday_tip: "Propojte Scratch ze 6. třídy s Pythonem – ukažte vedle sebe blokový kód a jeho textový ekvivalent. Žáci, kteří Scratch ovládali, okamžitě vidí analogii a překoná se psychologická bariéra „textový kód je těžký\"."
---

# Algoritmy III: Cykly a podmínky v kódu

## 💡 Metodický postup

### 1. Ze Scratche do Pythonu

<span class="act board">🖊️ Tabule — 10 min</span>

Učitel promítne vedle sebe dvě verze toho samého algoritmu:

**Scratch (bloky):** blok „opakuj 5×" s blokem „řekni Ahoj"

**Python (text):**
```python
for i in range(5):
    print("Ahoj!")
```

Společně projdou analogie:
- Blok „opakuj N×" → `for i in range(N):`
- Blok „pokud … jinak" → `if … else:`
- Blok „proměnná" → `x = hodnota`

Důraz na **odsazení** – Python nevyužívá závorky, ale mezery (4 mezery nebo Tab).

### 2. Pseudokód → Python

<span class="act pc">💻 PC — 15 min</span>

<div class="zadani-pc" markdown="1">

**Úloha — Pseudokód → Python** (15 min)

Otevři [replit.com](https://replit.com) a přepiš tyto pseudokódy do funkčního Pythonu:

**Úloha 1 – podmínka:**
```
Vstup: věk
Pokud věk >= 18:
    Vypiš "Smíš volit"
Jinak:
    Vypiš "Ještě ne"
```

**Úloha 2 – for cyklus:**
```
Pro i od 1 do 10:
    Vypiš i * i
```

**Úloha 3 – while cyklus:**
```
číslo = 1
Dokud číslo <= 100:
    Vypiš číslo
    číslo = číslo * 2
```

💡 Nezapomeň: Python vyžaduje **odsazení** (4 mezery nebo Tab) místo závorek!

</div>

### 3. Debugging: Najdi chybu

<span class="act pc">💻 PC — 12 min</span>

<div class="zadani-pc" markdown="1">

**Debugging — Najdi 3 chyby!** (12 min)

Tento kód nefunguje správně. Zkopíruj ho do editoru, spusť ho a oprav **3 chyby**:

```python
# Tento kód má 3 chyby – najdi je!
vek = input("Zadej věk: ")
if vek >= 18
    print("Dospělý")
else:
    print("Nezletilý)
```

Nápověda: Přečti si chybovou hlášku pozorně — Python ti řekne, na kterém řádku je problém.

</div>

Chyby: 1) `input()` vrací string – chybí `int()`, 2) chybí `:` za `if`, 3) chybí uzavírací `"` v posledním print.

### 4. Reflexe: Jaký cyklus kdy?

<span class="act discussion">💬 Diskuse — 8 min</span>

| Situace | Cyklus |
|---------|--------|
| Projdi seznam 10 položek | `for` |
| Opakuj, dokud uživatel nezadá správné heslo | `while` |
| Vykresli 100 hvězdiček | `for` |
| Čekej, dokud není soubor připraven | `while` |

## 📂 Podklady

- **Online Python interpret:** replit.com nebo pythonanywhere.com – žáci nepotřebují instalaci
- **Scratch → Python překlad:** Připravte PDF s tabulkou ekvivalentů bloků a Python příkazů
- **Cvičení:** code.org – Python kurz, nebo Codecademy „Learn Python"
- **Reference:** docs.python.org – dokumentace Pythonu

!!! tip "Tip pro učitele"
    Nejčastější chyba začátečníků je odsazení (indentation). Python je na odsazení závislý – místo závorek. Věnujte tomu explicitní pozornost: ukažte, co se stane, když odsazení chybí. Žáci si to zapamatují lépe, když sami uvidí chybovou hlášku `IndentationError`.
