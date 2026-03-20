---
grade: 8
week: 7
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
goals:
  - "**Naprogramuje** reakci Micro:bitu na stisk tlačítka A, tlačítka B a kombinaci A+B."
  - "**Propojí** koncept podmínek (Scratch) s událostmi hardware (tlačítko stisknuto)."
  - "**Navrhne** jednoduchý program ovládaný tlačítky s vlastní logikou."
  - "**Odladí** chyby v programu metodou systematického testování."
time_budget:
  - type: board
    minutes: 7
  - type: pc
    minutes: 10
  - type: board
    minutes: 20
  - type: discussion
    minutes: 8
friday_tip: "Soutěž: kdo naprogramuje nejrychlejší „bzučák\" — program, který přehraje tón při stisku A a jiný tón při stisku B? Soutěžní prvek silně motivuje."
---

# Senzory I: Tlačítka jako vstupy

## 💡 Metodický postup

### 1. Vstup vs. výstup na Micro:bitu

<span class="act board">🖊️ Tabule — 7 min</span>

Učitel nakreslí schéma:

```
VSTUP                   ZPRACOVÁNÍ              VÝSTUP
─────────────────────   ──────────────────────  ──────────────────
Tlačítko A / B          Váš program             LED matice
Akcelerometr            (podmínky a akce)       Zvuk (bzučák)
Teploměr                                        Radiový signál
```

Propojení: Tlačítka jsou ekvivalent klávesnice — žák dává pokyn, zařízení reaguje.

---

### 2. Blok „při stisknutí tlačítka" — demo

<span class="act pc">💻 PC — 10 min</span>

<div class="zadani-pc" markdown="1">

Učitel ukáže v MakeCode:
- Kategorie **Vstup** → blok `při stisknutí tlačítka [A]`
- Uvnitř bloku libovolná akce (zobrazit číslo, text, ikonu)

Live demo — 3 bloky:
```
při stisknutí tlačítka A → zobrazit ikonu (šipka nahoru)
při stisknutí tlačítka B → zobrazit ikonu (šipka dolů)
při stisknutí A+B        → zobrazit text "OK"
```

Žáci sledují simulátor a diskutují: „Co je to událost?" (Reakce na akci uživatele — stejně jako `po kliknutí` v Scratchi.)

</div>

---

### 3. Vlastní projekt: Binární volba

<span class="act board">🖊️ Tabule — 20 min</span>

Žáci programují vlastní „rozhodovač":

<div class="zadani-pc" markdown="1">

**Zadání:** Naprogramujte Micro:bit, který funguje jako pomocník při rozhodování:
- Stisk **A** = zobrazit „ANO" + ikona fajfky
- Stisk **B** = zobrazit „NE" + ikona křížku
- Stisk **A+B** = zobrazit „MOŽNÁ" + otazník

**Rozšíření *(pro rychlé)*:**
- Přidejte náhodu: při stisku A+B vygenerujte náhodné číslo 0 nebo 1 a zobrazte ANO nebo NE
- Blok: Matematika → `vybrat náhodně 0 až 1`

</div>

Žáci testují na fyzickém zařízení a sdílejí s vedlejším sousedem.

---

### 4. Reflexe: Vstupy v reálných zařízeních

<span class="act discussion">💬 Diskuse — 8 min</span>

Otázka: „Jaké vstupy má váš mobilní telefon?" (Dotyková obrazovka, akcelerometr, mikrofon, GPS, kamera, tlačítka hlasitosti)

Každý vstup = senzor, který přijímá data z okolí. Program reaguje na tyto vstupy podmínkami — stejně jako my dnes s tlačítky.

---

## 📂 Zdroje a podklady

* **MakeCode — Vstup:** [makecode.microbit.org](https://makecode.microbit.org) → kategorie Vstup → `při stisknutí tlačítka`
* **Projektový návod (CZ/EN):** microbit.org/projects — „Magic 8 Ball" projekt využívá tlačítka + akcelerometr
* **Rozšíření — kapacitní piny:** Piny na Micro:bitu mohou fungovat jako tlačítka při dotyku (pin 0, 1, 2 + GND)
* **Video (CZ):** YouTube — „Micro:bit tlačítka MakeCode česky"
* **Pro pokročilé — JavaScript:** MakeCode umožňuje přepnout z bloků do JavaScriptu — ukázka pro zájemce

---

!!! tip "Tip pro učitele"
    Projekt „Binární volba" (ANO/NE rozhodovač) je záměrně jednoduchý, aby se žáci soustředili na logiku a ne na syntaxi. Varianta s náhodou výrazně zvyšuje motivaci — žáci přirozeně zkouší kombinace a testují. Pokud zbývá čas, nechejte žáky vymyslet vlastní „hru" s tlačítky — papírový návrh → implementace. Skupinová práce ve dvojicích funguje dobře.
