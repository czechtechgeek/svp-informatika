---
grade: 9
week: 2
time: 45
area: Modelování a simulace / Algoritmické myšlení
rvp_codes:
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
goals:
  - "Žák vysvětlí, co je simulace a k čemu se používá v praxi"
  - "Žák popíše, jak počítačový model zjednodušuje realitu a proč"
  - Žák pracuje s interaktivní simulací a mění vstupní parametry
  - Žák interpretuje výstup simulace a vyvodí závěry
time_budget:
  - type: discussion
    minutes: 8
  - type: board
    minutes: 12
  - type: pc
    minutes: 18
  - type: discussion
    minutes: 7
friday_tip: "Simulace šíření nákazy je téma, které žáci zažili na vlastní kůži (COVID-19). Začněte přímým odkazem: „Pamatujete si, jak se mluvilo o R čísle a exponenciálním růstu?\" Reálná zkušenost okamžitě zapojí pozornost."
---

# Simulace I: Co se stane, když...?

## 💡 Metodický postup

### 1. Co je simulace?

<span class="act discussion">💬 Diskuse — 8 min</span>

Učitel se ptá: „Kdy jste naposledy viděli simulaci?" Žáci navrhují: počasí, letecký trenažér, videohry, předpověď pandemie, havárie aut.

Definice: **Simulace je napodobení chování reálného systému pomocí modelu.** Model je zjednodušení – zachycuje klíčové vlastnosti, ale vynechává nepodstatné detaily.

Proč simulovat?
- Je to **bezpečnější** než realita (havárie letadla v simulátoru)
- Je to **levnější** (nestavíme skutečný most, abychom zjistili, jestli drží)
- Je to **rychlejší** (simulujeme 100 let klimatu za hodinu)
- Umožňuje to **„co kdyby" otázky** bez rizika

### 2. Demonstrace: Šíření nákazy

<span class="act board">🖊️ Tabule — 12 min</span>

Učitel otevře simulátor šíření nákazy (viz podklady) a ukáže ho celé třídě.

Parametry, které žáci navrhují měnit:
- **R₀** (kolik lidí jeden nemocný průměrně nakazí)
- **Doba nakažlivosti**
- **Procento očkovaných**

Společně sledují grafy – SIR model (Susceptible, Infected, Recovered).

Klíčová pozorování:
- Při R₀ < 1 se nákaza sama uhasí
- Při R₀ > 1 roste exponenciálně
- Očkování chrání i neočkované (kolektivní imunita)

### 3. Samostatná práce se simulátorem

<span class="act pc">💻 PC — 18 min</span>

<div class="zadani-pc" markdown="1">

Vyber si jednu ze dvou simulací a experimentuj s parametry:

**Možnost A — Šíření nákazy** 🦠
Otevři [ncase.me/pandemic](https://ncase.me/pandemic) (anglicky, vše jasné z obrázků)

**Možnost B — Predátor a kořist** 🐺
Vyhledej online „Lotka-Volterra simulation" nebo „wolves and moose simulation"

Do sešitu nebo sdíleného dokumentu zapiš:
1. Výchozí parametry, které jsi nastavil/a, a výsledek simulace
2. Co se stalo, když jsi změnil/a jeden parametr? (napiš konkrétně co a jak)
3. Jedno překvapení nebo zajímavé zjištění

</div>

Každý žák zapisuje, učitel obchází.

### 4. Sdílení a reflexe

<span class="act discussion">💬 Diskuse — 7 min</span>

3–4 žáci sdílí svůj „objev" z experimentování. Učitel sumarizuje:

- Simulace jsou nástroj – záleží na kvalitě modelu
- „Garbage in, garbage out" – špatné vstupní předpoklady dají špatné výsledky
- Proto vědci a vývojáři neustále validují modely oproti realitě

## 📂 Podklady

- **Simulátor pandemie (EN):** ncase.me/pandemic – vizuálně skvělý, interaktivní, s vysvětlením
- **PhET Simulations (CZ/EN):** phet.colorado.edu – simulace z fyziky, chemie i matematiky
- **Predátor-kořist:** hledejte „Lotka-Volterra simulation online"
- **Video:** YouTube „exponenciální růst vysvětlení" – 3Blue1Brown nebo ČT edu

!!! tip "Tip pro učitele"
    Nechte žáky experimentovat volně – záměrné „rozbíjení" simulace (nastavení extrémních hodnot) je skvělý způsob, jak pochopit model. Otázka „Co musíte změnit, aby se nákaza nikdy nerozšířila?" vede k přirozenému objevení pojmu prahová hodnota (herd immunity threshold).
