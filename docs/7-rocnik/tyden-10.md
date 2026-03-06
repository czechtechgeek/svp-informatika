# Proměnné II: Časomíra

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje algoritmus v programovacím jazyce</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-03" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-03</span><span style="color: #374151;">Žák pracuje s proměnnými a datovými typy</span></div>

## 💬 Tip pro pátek
Odlehčení na konci hodiny: „Stopky challenge" — kdo zastaví stopky na přesně 10 sekund bez dívání? Žáci soutěží. Pak diskuse: jak počítač ví, kdy uplynula sekunda? (přerušení, oscilátor, čítač)

## 🎯 Cíle hodiny

- Žák vytvoří odpočítávač (countdown timer) pomocí proměnné a cyklu s čekáním
- Žák použije blok `čekej 1 sekund` k simulaci reálného času
- Žák kombinuje časomíru s podmínkami — čas = 0 → konec hry
- Žák pochopí, že „čas" v programu je jen proměnná, ne skutečný čas

## 💡 Metodický postup

### 1. Čas jako proměnná (7 min) — tabule

Diskuse: „Jak poznáte, kolik zbývá času ve hře?" → odpovědi: číslo na obrazovce, ubývající pruh, tikání.

Klíčový poznatek: Všechny typy časomíry jsou implementovány pomocí **čítače** (proměnné, která se pravidelně mění).

Dva typy:
- **Odpočet (countdown):** `čas = 30`, každou sekundu `čas = čas - 1`
- **Stopky (countup):** `čas = 0`, každou sekundu `čas = čas + 1`

### 2. Demo: Odpočítávač krok za krokem (13 min) — tabule

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

### 3. Kodování: Hra s časovým limitem (20 min) — PC

Žáci přidají časomíru do svého herního projektu nebo vytvoří nový:

**Minimální požadavky:**
- Proměnná `čas` odpočítává od 30 do 0
- Po uplynutí času se hra zastaví s hláškou

**Rozšíření:**
- **A:** Vizuální upozornění — pokud `čas < 10`, změnit barvu spritu nebo pozadí na červenou
- **B:** Bonusový čas — sebrání speciálního předmětu přidá 5 sekund
- **C:** Kombinace skóre + čas — výsledná obrazovka zobrazí dosažené skóre i čas
- **D:** Nejvyšší skóre v limitu — po skončení hry porovnej skóre s rekordem

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
