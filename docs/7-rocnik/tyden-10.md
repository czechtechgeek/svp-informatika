---
grade: 7
week: 10
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
  - code: INF-INF-002-ZV9-005
    text: "Po přečtení jednotlivých kroků algoritmu vysvětlí celý postup a určí problém, který je daným algoritmem řešen."
goals:
  - Žák vytvoří odpočítávač (countdown timer) pomocí proměnné a cyklu s čekáním
  - "Žák použije blok `čekej 1 sekund` k simulaci reálného času"
  - Žák kombinuje časomíru s podmínkami — čas = 0 → konec hry
  - "Žák pochopí, že „čas\" v programu je jen proměnná, ne skutečný čas"
time_budget:
  - type: board
    minutes: 7
  - type: board
    minutes: 13
  - type: pc
    minutes: 20
friday_tip: "Odlehčení na konci hodiny: „Stopky challenge\" — kdo zastaví stopky na přesně 10 sekund bez dívání? Žáci soutěží. Pak diskuse: jak počítač ví, kdy uplynula sekunda? (přerušení, oscilátor, čítač)"
---

# Proměnné II: Časomíra

## 💡 Metodický postup

### 1. Čas jako proměnná

<span class="act board">🖊️ Tabule — 7 min</span>

Diskuse: „Jak poznáte, kolik zbývá času ve hře?" → odpovědi: číslo na obrazovce, ubývající pruh, tikání.

Klíčový poznatek: Všechny typy časomíry jsou implementovány pomocí **čítače** (proměnné, která se pravidelně mění).

Dva typy:
- **Odpočet (countdown):** `čas = 30`, každou sekundu `čas = čas - 1`
- **Stopky (countup):** `čas = 0`, každou sekundu `čas = čas + 1`

### 2. Demo: Odpočítávač krok za krokem

<span class="act board">🖊️ Tabule — 13 min</span>

Učitel postaví odpočítávač na projektoru:

```
po kliknutí na vlajku:
  nastav [čas] na 30
  opakuj dokola:
    čekej 1 sekund
    změň [čas] o -1
    pokud [čas] = 0 pak:
      řekni "Čas vypršel!" po dobu 2 sekund
      zastav vše
```

Žáci sledují proměnnou `čas` jak se mění. Otázky:
- „Co se stane, pokud čekej změníme na 0,5 sekund?" (odpočítává 2× rychleji)
- „Jak bychom přidali bonusový čas za sebrání hvězdy?"

Demo rozšíření: `změň [čas] o 5` při kolizi s bonusem.

### 3. Kodování: Hra s časovým limitem

<span class="act pc">💻 PC — 20 min</span>

<div class="zadani-pc">

Otevři svůj herní projekt ve [scratch.mit.edu](https://scratch.mit.edu) a přidej odpočítávač (časomíru).

**Postup:**
1. Vytvoř proměnnou `čas`
2. Na začátku hry nastav `čas` na 30
3. Přidej cyklus: `čekej 1 sekund` → `změň [čas] o -1`
4. Přidej podmínku: pokud `čas = 0`, řekni „Čas vypršel!" a zastav vše

**Minimální požadavky:**
- Proměnná `čas` odpočítává od 30 do 0
- Po uplynutí času se hra zastaví se zprávou pro hráče

**Rozšíření (vyber si aspoň jedno):**
- **A:** Vizuální upozornění — pokud `čas < 10`, změň barvu spritu nebo pozadí na červenou
- **B:** Bonusový čas — sebrání speciálního předmětu přidá 5 sekund (`změň [čas] o 5`)
- **C:** Výsledná obrazovka — zobraz dosažené skóre i zbývající čas po skončení
- **D:** Rekord — porovnej skóre s nejvyšším dosaženým skóre

Na konci hodiny napiš na kartičku: „V mé hře bude...", „Chci použít...", „Obávám se...". Kartičku odevzdej učiteli.

</div>

### 4. Reflexe a příprava na projekt (5 min)

Učitel oznámí: „Příští tři týdny budete navrhovat a programovat vlastní hru — použijete vše, co jste se naučili: podmínky, ovládání šipkami, skóre, čas."

Žáci napíší na kartičku:
- „V mé hře bude..."
- „Chci použít..."
- „Obávám se..."

Kartičky učitel vybere jako podklad pro plánování projektů.

## 📂 Podklady

- **Scratch — časový blok:** Kategorie **Řízení** — blok `čekej [1] sekund`; pro přesnější měření viz blok `časovač` v kategorii Snímání
- **Scratch — zábudovaný časovač:** Blok `resetovat časovač` a `časovač` (hodnota v sekundách od startu) — alternativa k vlastní proměnné
- **Inspirace — herní žánry s časem:** Trivia hry, jumping puzzles, escape rooms — všechny spoléhají na countdown
- **Rozšíření — animovaný pruh:** Namísto číselného displeje lze zobrazit pruh (sprite měnící velikost dle hodnoty proměnné)

!!! tip "Tip pro učitele"
    Blok `čekej 1 sekund` není přesný — ve Scratch záleží na výkonu prohlížeče. Pro školní účely to nevadí. Pokud se někdo zeptá na přesnější měření, ukažte zabudovaný `časovač` (stopky od startu programu) — je přesnější, ale hůře se s ním tvoří odpočet. Hodina přirozeně vede k projektu — nechejte žáky začít přemýšlet o námětu vlastní hry.
