---
grade: 7
week: 9
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
  - code: INF-INF-002-ZV9-005
    text: "Po přečtení jednotlivých kroků algoritmu vysvětlí celý postup a určí problém, který je daným algoritmem řešen."
goals:
  - "Žák vysvětlí, co je proměnná, a odliší ji od konstanty"
  - Žák vytvoří proměnnou ve Scratch a nastaví její počáteční hodnotu
  - "Žák používá bloky `nastav [skóre] na 0`, `změň [skóre] o 1` a zobrazí hodnotu na scéně"
  - "Žák propojí proměnnou s podmínkou — skóre > 10 → konec hry"
time_budget:
  - type: board
    minutes: 8
  - type: board
    minutes: 12
  - type: pc
    minutes: 20
friday_tip: "Živý model proměnné: vezmte krabičku a kartičku s názvem „skóre\". Do krabičky vložte lístek s číslem 0. Při každém „bodu\" vyměňte lístek za vyšší číslo. Žáci vidí proměnnou fyzicky — má jméno, má hodnotu, hodnota se mění."
---

# Proměnné I: Skóre ve hře

## 💡 Metodický postup

### 1. Co je proměnná?

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel napíše:

```
skóre = 0
skóre = skóre + 1
skóre = skóre + 1
skóre = ?   →  skóre = 2
```

Analogie: Proměnná je jako **jmenovka na šuplíku**. Jmenovka se nemění (název), ale obsah šuplíku ano (hodnota).

Typy proměnných (základní přehled):
- **Číslo:** skóre, čas, životy, věk
- **Text:** jméno hráče, zpráva
- **Pravda/Nepravda:** hraje? splněno?

Ve Scratch: všechny proměnné jsou viditelné na scéně jako displej — to je výhoda pro výuku.

### 2. Demo: Přidání skóre do hry

<span class="act board">🖊️ Tabule — 12 min</span>

Učitel vezme projekt z minulé hodiny (hráč sbírá hvězdy) a přidá skóre:

#### Krok 1 — Vytvoření proměnné

- Kategorie **Proměnné** → „Vytvořit proměnnou" → název: `skóre`
- Automaticky se přidají bloky: `nastav [skóre] na 0`, `změň [skóre] o 1`

#### Krok 2 — Inicializace na startu
```
po kliknutí na vlajku:
  nastav [skóre] na 0
```

#### Krok 3 — Přidání bodu při kolizi
```
opakuj dokola:
  pokud dotýkám se [hvězda]? pak:
    změň [skóre] o 1
    skryj hvězdu (nebo přesuň na nové místo)
```

#### Krok 4 — Podmínka pro výhru
```
pokud [skóre] = 10 pak:
  řekni "Výhra!" po dobu 2 sekund
  zastav vše
```

### 3. Kodování: Hra se skóre

<span class="act pc">💻 PC — 20 min</span>

<div class="zadani-pc" markdown="1">

Otevři svůj projekt z minulé hodiny (hráč sbírá hvězdy) nebo začni nový. Přidej proměnnou `skóre`.

**Postup:**
1. V kategorii **Proměnné** klikni na „Vytvořit proměnnou" → název: `skóre`
2. Na začátku programu (po kliknutí na vlajku) nastav `skóre` na 0
3. Při každé kolizi se sbíraným předmětem zvyš skóre o 1 (`změň [skóre] o 1`)
4. Přidej podmínku: pokud `skóre = 10`, řekni „Výhra!" a zastav vše

**Minimální požadavky:**
- Proměnná `skóre` se inicializuje na 0 při startu hry
- Skóre se zvyšuje při určité události (kolize, kliknutí, stisk klávesy)
- Skóre je viditelné na scéně

**Rozšíření (vyber si):**
- **Životy:** přidej druhou proměnnou `životy` (začíná na 3, snižuje se při chybě)
- **Rekord:** proměnná `rekord` — aktualizuje se, pokud `skóre > rekord`
- **Hladiny:** po dosažení 10 bodů se zvýší obtížnost (rychlejší pohyb nepřátel nebo více předmětů)

Projekt ulož a sdílej odkaz přes Google Classroom.

</div>

### 4. Shrnutí (5 min)

Žáci odpoví ústně:
- „Proměnná je..."
- „Rozdíl mezi `nastav` a `změň` je..."
- „Kdybych přidal/a životy, co bych použil/a?"

## 📂 Podklady

- **Scratch — proměnné:** Kategorie **Proměnné** (oranžová, tmavší) — `nastav [_] na`, `změň [_] o`, `zobraz proměnnou`
- **Scratch tutoriál — proměnné:** [scratch.mit.edu/ideas](https://scratch.mit.edu/ideas) — hledejte „variables" nebo „score"
- **Analogie pro žáky:** Proměnná = schránka s názvem (krabičky, šuplíky, kontejnery)
- **Rozšíření — seznam (list):** Pro pokročilé žáky ukažte, že Scratch má i **Listy** (seznamy) — pro uložení více hodnot najednou (highscore tabulka)

!!! tip "Tip pro učitele"
    Nejčastější chyba: žáci zapomenou inicializovat proměnnou na 0 při startu — skóre pak pokračuje od minulého spuštění. Zdůrazněte, že blok `nastav [skóre] na 0` patří vždy k události `po kliknutí na vlajku`. Druhá častá chyba: záměna `nastav` (přepíše hodnotu) a `změň o` (přidá k hodnotě). Nechejte žáky si oba bloky vyzkoušet a pozorovat rozdíl.
