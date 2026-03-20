---
grade: 9
week: 16
time: 45
area: Umělá inteligence / Data a informace
rvp_codes:
  - code: INF-INF-001-ZV9-001
    text: "Získá z dat informace, interpretuje data získaná pro řešení konkrétního problému."
  - code: INF-INF-004-ZV9-014
    text: Diskutuje o fungování digitálních technologií určujících trendy ve světě.
goals:
  - "Žák vysvětlí, co je strojové učení a jak se liší od tradičního programování"
  - "Žák popíše princip supervised learningu na konkrétním příkladu (spam filtr, doporučovací systém)"
  - Žák vlastníma rukama natrénuje jednoduchý model v Teachable Machine
  - "Žák pojmenuje alespoň dvě omezení strojového učení (bias, potřeba dat, chybovost)"
time_budget:
  - type: board
    minutes: 10
  - type: discussion
    minutes: 8
  - type: pc
    minutes: 20
  - type: discussion
    minutes: 7
friday_tip: "Začněte hodinu otázkou „Jak se počítač naučil rozpoznat kočku?\" — nechte žáky hádat 2 minuty. Jejich odpovědi odhalí, jaké předpoklady mají, a poslouží jako výborný odrazový můstek."
---

# 

## 💡 Metodický postup

### 1. Tradiční programování vs. strojové učení

<span class="act board">🖊️ Tabule — 10 min</span>

Učitel nakreslí na tabuli srovnání:

**Tradiční programování:**
```
Programátor → Pravidla → Počítač → Výsledek
Vstup: email
Pravidlo: if "výhra" in email: označit jako spam
```
Problém: Spameři se přizpůsobí, pravidel je tisíce.

**Strojové učení:**
```
Data + Správné odpovědi → Algoritmus → Model → Výsledky na nových datech
Vstup: 10 000 emailů (označených spam/nespam)
Model: naučí se sám, co spam vypadá jako
```

Klíčový princip: Počítač se učí z příkladů, ne z pravidel.

**Typy strojového učení (zjednodušeně):**
| Typ | Princip | Příklad |
|-----|---------|---------|
| **Supervised learning** | Učení s označenými daty | spam filtr, rozpoznání obrázků |
| **Unsupervised learning** | Hledání vzorů bez označení | segmentace zákazníků |
| **Reinforcement learning** | Odměna za správnou akci | hraní her (AlphaGo) |

### 2. Příklady z reálného světa

<span class="act discussion">💬 Diskuse — 8 min</span>

Učitel prochází příklady, žáci hádají, jaká data model potřeboval:

- **Netflix doporučení:** Model dostal data o tom, co diváci sledovali a hodnotili. Naučil se, že „kdo sledoval Breaking Bad, rád i Narcos".
- **Gmail spam filtr:** Miliony emailů označených spam/nespam. Naučil se vzory (cizí odesílatel, podezřelé slovo, podivné přílohy).
- **Face ID na iPhonu:** Tisíce fotografií tváří z různých úhlů a světel. Model naučil rozlišovat obličeje.
- **Google Translate:** Miliardy přeložených vět. Model naučil překlad bez toho, aby znal gramatická pravidla.

Otázka pro diskusi: „Jaká data musel Google použít, aby Translate fungoval v češtině?"

### 3. Praktická ukázka: Teachable Machine

<span class="act pc">💻 PC — 20 min</span>

<div class="zadani-pc" markdown="1">

Otevři [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com) → **Image Project** a natrénuj vlastní model:

**Krok 1 — Vytvoř trénovací data:**
- Třída A (název: „Palec nahoru") → nafoť nebo nahrej 30+ obrázků palce nahoru z různých úhlů
- Třída B (název: „Dlaň otevřená") → nafoť nebo nahrej 30+ obrázků otevřené dlaně

**Krok 2 — Trénuj:**
- Klikni „Trénovat model" a počkej

**Krok 3 — Testuj a experimentuj:**
- Ukaž kameře různé polohy ruky — funguje to?
- Co se stane, když data jsou jen z jednoho úhlu?
- Co se stane při špatném osvětlení?

📝 Zapiš svá pozorování: „Model fungoval správně při ___, ale selhal při ___."

</div>

Žáci zapisují pozorování.

### 4. Reflexe: Omezení strojového učení

<span class="act discussion">💬 Diskuse — 7 min</span>

Učitel vede diskusi nad otázkami:
- „Co se stane, když trénovací data jsou neúplná nebo zaujaté?" → Bias (model diskriminuje)
- „Může model vždy říct, proč se tak rozhodl?" → Ne — model je „černá skříňka"
- „Co potřebuje ML model, co tradiční program nepotřebuje?" → Velké množství dat

Reálný příklad biasu: Amazon v roce 2018 musel zastavit AI náborový systém — model se naučil upřednostňovat muže, protože historická data obsahovala více mužů na technických pozicích.

## 📂 Podklady

- **Teachable Machine:** [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com) — funguje v prohlížeči, nepotřebuje instalaci
- **Video (EN, titulky CZ):** YouTube — „How machines learn" — CGP Grey (7 min, výborné vizualizace)
- **Článek (CZ):** Lupa.cz nebo VTM — základy strojového učení pro začátečníky
- **Rozšíření — ml5.js:** [ml5js.org](https://ml5js.org) — strojové učení v JavaScriptu pro pokročilé žáky
- **Bias v AI:** Hledejte „Amazon AI hiring bias" pro reálný příklad diskuse

!!! tip "Tip pro učitele"
    Teachable Machine potřebuje funkční webkameru. Otestujte ji před hodinou! Pokud kamery nefungují, připravte zálohu — trénování modelu na textu (klasifikace recenzí). Žáci jsou nadšeni, když model v reálném čase reaguje na jejich gesta — nechte jim čas na experimentování, i když to „není v plánu".
