# Simulace I: Co se stane, když...?

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Modelování a simulace / Algoritmické myšlení
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-01</span><span style="color: #374151;">Žák navrhne a zapíše algoritmus řešení problému</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák simuluje průběh algoritmu na datech</span></div>

## 💬 Tip pro pátek
Simulace šíření nákazy je téma, které žáci zažili na vlastní kůži (COVID-19). Začněte přímým odkazem: „Pamatujete si, jak se mluvilo o R čísle a exponenciálním růstu?" Reálná zkušenost okamžitě zapojí pozornost.

## 🎯 Cíle hodiny

- Žák vysvětlí, co je simulace a k čemu se používá v praxi
- Žák popíše, jak počítačový model zjednodušuje realitu a proč
- Žák pracuje s interaktivní simulací a mění vstupní parametry
- Žák interpretuje výstup simulace a vyvodí závěry

## 💡 Metodický postup

### 1. Co je simulace? (8 min) — diskuse

Učitel se ptá: „Kdy jste naposledy viděli simulaci?" Žáci navrhují: počasí, letecký trenažér, videohry, předpověď pandemie, havárie aut.

Definice: **Simulace je napodobení chování reálného systému pomocí modelu.** Model je zjednodušení – zachycuje klíčové vlastnosti, ale vynechává nepodstatné detaily.

Proč simulovat?
- Je to **bezpečnější** než realita (havárie letadla v simulátoru)
- Je to **levnější** (nestavíme skutečný most, abychom zjistili, jestli drží)
- Je to **rychlejší** (simulujeme 100 let klimatu za hodinu)
- Umožňuje to **„co kdyby" otázky** bez rizika

### 2. Demonstrace: Šíření nákazy (12 min) — tabule

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

### 3. Samostatná práce se simulátorem (18 min) — PC

Žáci si vyberou jednu ze dvou simulací a experimentují:

**Možnost A – Šíření nákazy:** ncase.me/pandemic (EN, vizuálně skvělé)

**Možnost B – Predátor a kořist:** Simulátor vlků a losů (viz podklady)

Každý žák zapíše do sešitu nebo sdíleného dokumentu:
1. Výchozí parametry a výsledek
2. Co se stane, když změním parametr X?
3. Jedno překvapení, které mě zaujalo

### 4. Sdílení a reflexe (7 min) — diskuse

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
