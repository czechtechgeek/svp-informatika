# Senzory I: Tlačítka jako vstupy

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-01</span><span style="color: #374151;">Žák rozloží problém na podproblémy a navrhne algoritmus</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje algoritmus v programovacím jazyce</span></div>

## 💬 Tip pro pátek
Soutěž: kdo naprogramuje nejrychlejší „bzučák" — program, který přehraje tón při stisku A a jiný tón při stisku B? Soutěžní prvek silně motivuje.

## 🎯 Cíle hodiny

- Žák naprogramuje reakci Micro:bitu na stisk tlačítka A, tlačítka B a kombinaci A+B
- Žák propojí koncept podmínek (Scratch) s událostmi hardware (tlačítko stisknuto)
- Žák navrhne jednoduchý program ovládaný tlačítky s vlastní logikou
- Žák odladí chyby v programu metodou systematického testování

## 💡 Metodický postup

### 1. Vstup vs. výstup na Micro:bitu (7 min) — tabule

Učitel nakreslí schéma:

```
VSTUP                   ZPRACOVÁNÍ              VÝSTUP
─────────────────────   ──────────────────────  ──────────────────
Tlačítko A / B          Váš program             LED matice
Akcelerometr            (podmínky a akce)       Zvuk (bzučák)
Teploměr                                        Radiový signál
```

Propojení: Tlačítka jsou ekvivalent klávesnice — žák dává pokyn, zařízení reaguje.

### 2. Blok „při stisknutí tlačítka" — demo (10 min) — PC + Micro:bit

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

### 3. Vlastní projekt: Binární volba (20 min) — Micro:bit

Žáci programují vlastní „rozhodovač":

**Zadání:** Naprogramujte Micro:bit, který funguje jako pomocník při rozhodování:
- Stisk A = zobrazit „ANO" + ikona fajfky
- Stisk B = zobrazit „NE" + ikona křížku
- Stisk A+B = zobrazit „MOŽNÁ" + otazník

**Rozšíření (pro rychlé):**
- Přidejte náhodu: při stisku A+B vygenerujte náhodné číslo 0 nebo 1 a podle toho zobrazit ANO nebo NE
- Blok: Matematika → `vybrat náhodně 0 až 1`

Žáci testují na fyzickém zařízení a sdílejí s vedlejším sousedem.

### 4. Reflexe: Vstupy v reálných zařízeních (8 min) — diskuse

Otázka: „Jaké vstupy má váš mobilní telefon?" (Dotyková obrazovka, akcelerometr, mikrofon, GPS, kamera, tlačítka hlasitosti)

Každý vstup = senzor, který přijímá data z okolí. Program reaguje na tyto vstupy podmínkami — stejně jako my dnes s tlačítky.

## 📂 Podklady

- **MakeCode — Vstup:** [makecode.microbit.org](https://makecode.microbit.org) → kategorie Vstup → `při stisknutí tlačítka`
- **Projektový návod (CZ/EN):** microbit.org/projects — „Magic 8 Ball" projekt využívá tlačítka + akcelerometr
- **Rozšíření — kapacitní piny:** Piny na Micro:bitu mohou fungovat jako tlačítka při dotyku (pin 0, 1, 2 + GND)
- **Video (CZ):** YouTube — „Micro:bit tlačítka MakeCode česky"
- **Pro pokročilé — JavaScript:** MakeCode umožňuje přepnout z bloků do JavaScriptu — ukázka pro zájemce

!!! tip "Tip pro učitele"
    Projekt „Binární volba" (ANO/NE rozhodovač) je záměrně jednoduchý, aby se žáci soustředili na logiku a ne na syntaxi. Varianta s náhodou výrazně zvyšuje motivaci — žáci přirozeně zkouší kombinace a testují. Pokud zbývá čas, nechejte žáky vymyslet vlastní „hru" s tlačítky — papírový návrh → implementace. Skupinová práce ve dvojicích funguje dobře.
