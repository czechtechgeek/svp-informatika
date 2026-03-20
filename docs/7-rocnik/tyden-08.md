---
grade: 7
week: 8
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
  - code: INF-INF-002-ZV9-008
    text: "Průběžně ověřuje správnost vytvářeného postupu, zkouší program, opravuje chyby, posoudí efektivitu postupu, programu."
goals:
  - "Žák použije bloky událostí `když stisknuta klávesa` pro ovládání spritu"
  - Žák implementuje pohyb do čtyř směrů pomocí šipkových kláves
  - Žák přidá animaci kostýmu reagující na směr pohybu
  - Žák rozlišuje dva přístupy k ovládání (polling v cyklu vs. event-driven)
time_budget:
  - type: board
    minutes: 8
  - type: board
    minutes: 12
  - type: pc
    minutes: 20
friday_tip: "Dejte žákům k dispozici gamepad nebo klávesnici a nechejte je „naučit\" virtuálního žáka pohyb — kdo zvládne ovládat postavu čtyřmi šipkami bez kouknutí do kódu, má solidní intuici pro vstupní události."
---

# Interakce: Ovládání postavy šipkami

## 💡 Metodický postup

### 1. Analýza: Jak funguje ovládání ve hře?

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel se zeptá: „Jak počítač ví, že stiskujete klávesu?" Žáci hádají.

Vysvětlení dvou přístupů:

#### Přístup 1 — Pollování (testování v cyklu)
```
opakuj dokola:
  pokud klávesa ↑ stisknuta? pak: pohni se nahoru
  pokud klávesa ↓ stisknuta? pak: pohni se dolů
```

#### Přístup 2 — Událost (event-driven)
```
když stisknuta klávesa [↑]:
  pohni se nahoru
```

Diskuse: Který je přehlednější? Který lépe reaguje na rychlé stisky? (Pollování reaguje hladčeji, events jsou přehlednější.)

### 2. Demo: Postava ovládaná šipkami

<span class="act board">🖊️ Tabule — 12 min</span>

Učitel postupně staví hráčský sprite na projektoru:

#### Krok 1 — Základní pohyb
```
když stisknuta klávesa [šipka vpravo]: změň x o 10
když stisknuta klávesa [šipka vlevo]:  změň x o -10
když stisknuta klávesa [šipka nahoru]: změň y o 10
když stisknuta klávesa [šipka dolů]:   změň y o -10
```

#### Krok 2 — Omezení obrazovkou
```
pokud x > 230 pak: nastav x na 230
pokud x < -230 pak: nastav x na -230
```

#### Krok 3 — Animace směru
```
když stisknuta klávesa [šipka vpravo]: nastav směr na 90; změn kostým na "chůze-vpravo"
```

### 3. Kodování: Hráčův sprite + prostředí

<span class="act pc">💻 PC — 20 min</span>

Žáci vytvoří hráčský sprite a alespoň jedno z prostředí:

**Základ (povinný):**
- Sprite ovladatelný čtyřmi šipkami
- Nesmí přejít přes okraj obrazovky

**Prostředí — vyberte jedno:**
- **A:** Sběratelská hra — náhodně se objevují hvězdy, hráč je sbírá dotykem (zmizí)
- **B:** Labyrint — pozadí je labyrint (nakreslený v editoru), hráč nesmí přejít přes stěny (detekce barvy)
- **C:** Dva hráči — druhý sprite ovládá hráč 2 klávesami WASD

### 4. Showcase (5 min)

Dva žáci ukáží svůj projekt. Třída hodnotí:
- Reaguje sprite plynule?
- Kde by přidal/a nepřítele nebo překážku?

Učitel naznačí: „Příští týden přidáme **skóre** — proměnná, která počítá, co hráč sesbíral."

## 📂 Podklady

- **Scratch — snímání klávesy:** Blok `klávesa [_] stisknuta?` je v kategorii **Snímání** (světle modrá)
- **Scratch — změna x/y:** Kategorie **Pohyb** (modrá) — `změň x o`, `změň y o`, `nastav x na`, `nastav y na`
- **Detekce barvy:** Kategorie **Snímání** — `dotýkám se barvy [_]?` — pro labyrint nastavit barvu stěny
- **Tutoriál (EN):** Hledejte „Scratch arrow key movement tutorial" — Griffpatch nebo ScratchJr YouTube kanál
- **Inspirace — hra:** Pac-Man je čistě arrow-key hra — ukažte žákům jako motivaci, co se dá postavit

!!! tip "Tip pro učitele"
    Nejčastější chyba: sprite „skáče" přes okraj nebo „propíchne" zeď labyrintu. Ukažte žákům, že `změň x o 10` = teleportace o 10 pixelů, ne plynulý pohyb. Pro hladší pohyb použijte polling v cyklu s hodnotou 3–5 kroků. Detekce barvy pro labyrint (varianta B) je obtížnější — doporučte ji pouze rychlejším žákům.
