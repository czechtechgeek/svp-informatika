---
grade: 7
week: 30
time: 45
area: Algoritmizace a programování / Digitální technologie
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - "Žák naprogramuje robota (Ozobot, micro:bit nebo online simulátor) pro splnění jednoduchého úkolu"
  - "Žák aplikuje znalosti z algoritmizace (podmínky, cykly) v fyzickém nebo simulovaném prostředí"
  - Žák spolupracuje ve skupině na řešení problému s jasným cílem a omezeními
  - Žák porovná programování robota s programováním ve Scratch a identifikuje podobnosti
time_budget:
  - type: discussion
    minutes: 7
  - type: board
    minutes: 5
  - type: pc
    minutes: 28
friday_tip: Robotika na konci roku je přirozená motivace — žáci jsou uvolněnější a kreativnější. Nechejte skupiny soutěžit v jednoduchém závodu nebo splnění úkolu. Rivalita (zdravá) zvyšuje angažovanost.
---

# Rezerva: Robotika

## 💡 Metodický postup

### 1. Roboti kolem nás

<span class="act discussion">💬 Diskuse — 7 min</span>

Učitel se ptá: „Kde jste viděli roboty v reálném světě?" Žáci odpovídají.

Příklady: průmyslové rameno (auto-výroba), robotické vysavače (Roomba), drony, Mars Rover, chirurgický robot, pokladní robot.

Klíčový rozdíl: **Autonomní** robot (rozhoduje sám) vs. **řízený** robot (člověk dálkově ovládá). Dnes budeme programovat autonomní chovánít (robot splní úkol sám).

### 2. Výběr platformy a zadání

<span class="act board">🖊️ Tabule — 5 min</span>

**Dle dostupnosti vyberte jednu z variant:**

#### Varianta A — Ozobot (pokud škola vlastní)

- Ozobot sleduje čáry, reaguje na barevné kódy
- Žáci kreslí trasu + kódy na papír nebo programují v OzoBlockly

#### Varianta B — micro:bit (pokud škola vlastní)

- Žáci naprogramují micro:bit v MakeCode ([makecode.microbit.org](https://makecode.microbit.org))
- Blokové programování podobné Scratch
- Úkoly: zobrazení vzorce, reakce na tlačítko, compass

#### Varianta C — Online simulátor (bez fyzického robota)
- [code.org/learn](https://code.org/learn) — kurzy s robotickými postavami (online, CZ lokalizace)
- [csedweek.org](https://csedweek.org) — Hour of Code aktivity
- Scratch simulace robota v bludišti (vlastní projekt)

### 3. Skupinová robotická výzva

<span class="act pc">💻 PC — 28 min</span>

Žáci pracují ve skupinách 3–4 a řeší přidělený úkol:

#### Úkol A — Ozobot
- Nakreslite trasu z bodu A do bodu B s alespoň 3 zatáčkami
- Přidejte kód „zrychlení" a „zatočení na místě"
- Ozobot musí dokončit trasu bez vyjetí z čáry

#### Úkol B — micro:bit
- Program zobrazí šipku ve směru pohybu (akcelerometr)
- Při zatřesení zobrazí náhodné číslo
- Při stisku tlačítka A přehraje melodii

#### Úkol C — online simulátor
- Dokončete 5 levelů zvolené online aktivity (Code.org nebo Scratch bludiště)
- Zapište: Kolik bloků jste použili? Kde jste se zasekli?

### 4. Prezentace řešení (5 min)

Každá skupina ukáže výsledek. Třída komentuje: Co bylo složité? Kde robot selhal a proč?

## 📂 Podklady

- **Ozobot — OzoBlockly:** [games.ozobot.com](https://games.ozobot.com) — blokové programování online, výsledek stáhnout do Ozobota
- **micro:bit — MakeCode:** [makecode.microbit.org](https://makecode.microbit.org) — zdarma, blokové i textové programování, simulátor v prohlížeči
- **Code.org:** [code.org/learn](https://code.org/learn) — CZ lokalizace, vhodné pro všechny věkové skupiny, bez registrace
- **Scratch bludiště:** Připravte předem projekt Scratch s labyrintem — žáci programují pohyb bez dotýkání stěn

!!! tip "Tip pro učitele"
    Pokud škola nemá fyzické roboty, Code.org je výborná alternativa — kurzy jsou kvalitní a žáci je berou vážně. Robotická hodina na konci roku slouží jako motivační uzavření: „Podívejte se, kde jste byli v září a kde jste teď." Pokud máte Ozobot nebo micro:bit, přineste je i bez přípravy — improvizovaná skupina 5 žáků s fyzickým robotem je lepší než 30 žáků u obrazovky.
