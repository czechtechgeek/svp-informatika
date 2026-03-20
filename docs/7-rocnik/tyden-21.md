---
grade: 7
week: 21
time: 45
area: Algoritmizace a programování / Digitální technologie
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - "Žák vysvětlí, co je HTML a jaký je jeho vztah k webové stránce (struktura obsahu)"
  - "Žák použije základní HTML tagy: `<h1>`, `<p>`, `<a>`, `<img>`, `<ul>`, `<li>`"
  - "Žák vytvoří jednoduchou HTML stránku s nadpisem, textem a odkazem"
  - "Žák rozlišuje HTML (struktura), CSS (vzhled) a JavaScript (chování) — základní přehled"
time_budget:
  - type: board
    minutes: 8
  - type: board
    minutes: 10
  - type: pc
    minutes: 22
friday_tip: "\"Zobrazit zdrojový kód\" je magický moment: klikněte pravým tlačítkem na jakoukoli webovou stránku a vyberte \"Zobrazit zdrojový kód\". Žáci vidí HTML každé stránky. Nechejte je hádat, co jednotlivé tagy dělají — intuice je překvapivě dobrá."
---

# Webová stránka: Základy HTML

## 💡 Metodický postup

### 1. Úvod: Jak funguje webová stránka?

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel nakreslí schéma:

```
Prohlížeč ← HTTP ← Server
    ↓ stáhne HTML soubor
    ↓ přečte tagy
    → zobrazí stránku
```

Analogie: HTML je jako kostra domu — říká, co je kde, ale neurčuje barvu stěn (to dělá CSS).

**Tři vrstvy webu:**
| Vrstva | Jazyk | Co dělá |
|--------|-------|---------|
| Struktura | HTML | Co je na stránce (text, obrázky) |
| Vzhled | CSS | Jak to vypadá (barvy, písmo) |
| Chování | JavaScript | Co se stane po kliknutí |

Dnes: jen HTML. CSS a JS jsou témata pro 8.–9. ročník.

### 2. Demo: Základní tagy

<span class="act board">🖊️ Tabule — 10 min</span>

Učitel píše kód živě na projektoru (Poznámkový blok nebo online editor):

```html
<!DOCTYPE html>
<html>
<head>
  <title>Moje první stránka</title>
</head>
<body>
  <h1>Vítejte na mé stránce!</h1>
  <p>Jmenuji se Jan a učím se HTML.</p>
  <h2>Mé oblíbené věci</h2>
  <ul>
    <li>Programování</li>
    <li>Hry</li>
    <li>Sport</li>
  </ul>
  <p>Navštivte <a href="https://scratch.mit.edu">Scratch</a>.</p>
</body>
</html>
```

Žáci říkají, co každý tag dělá. Učitel uloží jako `index.html` a otevře v prohlížeči — stránka se zobrazí!

### 3. Tvorba: Osobní webová stránka

<span class="act pc">💻 PC — 22 min</span>

<div class="zadani-pc">

Vytvoř vlastní HTML stránku „O mně". Použij Poznámkový blok (ulož jako `omne.html` a otevři v prohlížeči) nebo online editor [codepen.io](https://codepen.io).

**Povinné prvky:**
- Nadpis `<h1>` s tvým jménem nebo přezdívkou
- Aspoň **2 odstavce** `<p>` s textem o sobě (koníčky, oblíbená věc...)
- **Seznam** `<ul>` s oblíbenými věcmi (min. 3 položky pomocí `<li>`)
- Jeden **odkaz** `<a href="...">` na libovolný web (např. Scratch, YouTube...)

**Volitelné rozšíření:**
- Obrázek: `<img src="URL_obrázku" alt="popis">`
- Druhý nadpis `<h2>` jako název sekce
- Tučné písmo `<strong>` nebo kurzíva `<em>` pro zdůraznění

Zkontroluj: každý otevírací tag (`<p>`) musí mít odpovídající zavírací tag (`</p>`).

**Pro rychlé žáky:** Přidej na stránku jednoduchý CSS styl — do sekce `<head>` vlož:
```html
<style>
  body { background-color: lightblue; font-family: Arial; }
</style>
```

Hotový soubor ulož nebo sdílej odkaz přes Google Classroom.

</div>

### 4. Sdílení a reflexe (5 min)

Dva dobrovolníci ukáží svou stránku na projektoru. Třída poznává tagy v kódu.

Závěr: „Každá webová stránka, kterou jste kdy viděli, je napsána tímto způsobem — jen je složitější."

## 📂 Podklady

- **Online editor — CodePen:** [codepen.io](https://codepen.io) — HTML, CSS, JS s živým náhledem, bez registrace
- **Tutoriál (CZ):** [jakpsatweb.cz](https://jakpsatweb.cz) — klasický český tutoriál HTML pro začátečníky
- **Interaktivní kurz (CZ/EN):** [w3schools.com](https://www.w3schools.com/html/) — cvičení s okamžitou zpětnou vazbou
- **Tagy k procvičení:** h1–h6, p, a, img, ul/ol, li, strong, em, br, hr
- **Rozšíření — CSS intro:** Pro rychlé žáky ukažte jednoduché CSS: `<style> body { background-color: lightblue; } </style>`

!!! tip "Tip pro učitele"
    HTML je výborný přechod od blokového programování (Scratch) k textovému kódu. Žáci vidí okamžitý výsledek svého kódu v prohlížeči — silná motivace. Nejčastější chyba: nezavřený tag (chybí `</p>` nebo `</li>`). Naučte žáky pravidlo: každý otevírací tag má zavírací. CodePen nebo Replit jsou ideální, protože zobrazují výsledek okamžitě bez ukládání souborů.
