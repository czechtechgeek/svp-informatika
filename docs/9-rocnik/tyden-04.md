# Algoritmy III: Cykly a podmínky v kódu

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmické myšlení a programování
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-002-ZV9-006" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-002-ZV9-006</span><span style="color: #374151;">Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-009" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-009</span><span style="color: #374151;">Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.</span></div>

## 💬 Tip pro pátek
Propojte Scratch ze 6. třídy s Pythonem – ukažte vedle sebe blokový kód a jeho textový ekvivalent. Žáci, kteří Scratch ovládali, okamžitě vidí analogii a překoná se psychologická bariéra „textový kód je těžký".

## 🎯 Cíle hodiny

- Žák zapíše podmínku a cyklus nejprve v pseudokódu, pak v syntaxi Pythonu
- Žák přeloží blokový kód ze Scratche do textového kódu
- Žák rozlišuje `for` cyklus (opakování pevněkrát) a `while` cyklus (opakování dokud platí podmínka)
- Žák odladí drobnou chybu v připraveném kódu

## 💡 Metodický postup

### 1. Ze Scratche do Pythonu (10 min) — tabule

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

### 2. Pseudokód → Python (15 min) — PC nebo papír

Žáci dostají 3 pseudokódy a přepíší je do Pythonu:

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

### 3. Debugging: Najdi chybu (12 min) — PC

Žáci dostanou kód s úmyslnými chybami a opraví je:

```python
# Tento kód má 3 chyby – najdi je!
vek = input("Zadej věk: ")
if vek >= 18
    print("Dospělý")
else:
    print("Nezletilý)
```

Chyby: 1) `input()` vrací string – chybí `int()`, 2) chybí `:` za `if`, 3) chybí uzavírací `"` v posledním print.

### 4. Reflexe: Jaký cyklus kdy? (8 min) — diskuse

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
