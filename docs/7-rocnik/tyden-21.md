# Webová stránka: Základy HTML

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování / Digitální technologie
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje jednoduchý program / stránku</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-3-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-3-01</span><span style="color: #374151;">Žák vysvětlí princip fungování digitálních technologií</span></div>

## 💬 Tip pro pátek
"Zobrazit zdrojový kód" je magický moment: klikněte pravým tlačítkem na jakoukoli webovou stránku a vyberte "Zobrazit zdrojový kód". Žáci vidí HTML každé stránky. Nechejte je hádat, co jednotlivé tagy dělají — intuice je překvapivě dobrá.

## 🎯 Cíle hodiny

- Žák vysvětlí, co je HTML a jaký je jeho vztah k webové stránce (struktura obsahu)
- Žák použije základní HTML tagy: `<h1>`, `<p>`, `<a>`, `<img>`, `<ul>`, `<li>`
- Žák vytvoří jednoduchou HTML stránku s nadpisem, textem a odkazem
- Žák rozlišuje HTML (struktura), CSS (vzhled) a JavaScript (chování) — základní přehled

## 💡 Metodický postup

### 1. Úvod: Jak funguje webová stránka? (8 min) — tabule

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

### 2. Demo: Základní tagy (10 min) — tabule

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

### 3. Tvorba: Osobní webová stránka (22 min) — PC

Žáci vytvoří vlastní HTML stránku „O mně" s těmito prvky:

**Povinné:**
- Nadpis `<h1>` s jejich jménem (nebo přezdívkou)
- Alespoň 2 odstavce `<p>` s textem o sobě
- Seznam `<ul>` s oblíbenými věcmi (min. 3 položky)
- Jeden odkaz `<a href="...">` na libovolný web

**Volitelné rozšíření:**
- Obrázek `<img src="..." alt="...">` (lokální soubor nebo URL)
- Druhý nadpis `<h2>` jako sekce
- Tučný text `<strong>` nebo kurzíva `<em>`

**Nástroje:**
- Poznámkový blok Windows + prohlížeč (uložit jako .html)
- Online: [codepen.io](https://codepen.io) nebo [replit.com](https://replit.com) — okamžitý náhled

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
