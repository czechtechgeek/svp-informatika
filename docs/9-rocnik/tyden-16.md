# Umělá inteligence I: Strojové učení

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Umělá inteligence / Data a informace
- **Výstup:** <div class="curriculumTag" data-code="I-9-1-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-1-01</span><span style="color: #374151;">Žák popíše, jak jsou data reprezentována a zpracována v digitálních systémech</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-4-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-4-01</span><span style="color: #374151;">Žák kriticky hodnotí možnosti a omezení umělé inteligence</span></div>

## 💬 Tip pro pátek
Začněte hodinu otázkou „Jak se počítač naučil rozpoznat kočku?" — nechte žáky hádat 2 minuty. Jejich odpovědi odhalí, jaké předpoklady mají, a poslouží jako výborný odrazový můstek.

## 🎯 Cíle hodiny

- Žák vysvětlí, co je strojové učení a jak se liší od tradičního programování
- Žák popíše princip supervised learningu na konkrétním příkladu (spam filtr, doporučovací systém)
- Žák vlastníma rukama natrénuje jednoduchý model v Teachable Machine
- Žák pojmenuje alespoň dvě omezení strojového učení (bias, potřeba dat, chybovost)

## 💡 Metodický postup

### 1. Tradiční programování vs. strojové učení (10 min) — tabule

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

### 2. Příklady z reálného světa (8 min) — diskuse

Učitel prochází příklady, žáci hádají, jaká data model potřeboval:

- **Netflix doporučení:** Model dostal data o tom, co diváci sledovali a hodnotili. Naučil se, že „kdo sledoval Breaking Bad, rád i Narcos".
- **Gmail spam filtr:** Miliony emailů označených spam/nespam. Naučil se vzory (cizí odesílatel, podezřelé slovo, podivné přílohy).
- **Face ID na iPhonu:** Tisíce fotografií tváří z různých úhlů a světel. Model naučil rozlišovat obličeje.
- **Google Translate:** Miliardy přeložených vět. Model naučil překlad bez toho, aby znal gramatická pravidla.

Otázka pro diskusi: „Jaká data musel Google použít, aby Translate fungoval v češtině?"

### 3. Praktická ukázka: Teachable Machine (20 min) — PC

Žáci otevřou [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com) → Image Project.

**Zadání: Natrénujte model na rozpoznání dvou tříd:**

Třída A: „Palec nahoru"
Třída B: „Dlaň otevřená"

Postup:
1. Vytvořit třídu A — nahrát 30+ obrázků palce nahoru (z různých úhlů)
2. Vytvořit třídu B — nahrát 30+ obrázků otevřené dlaně
3. Kliknout „Trénovat model"
4. Otestovat — ukázat kameru různé polohy ruky

**Experimenty:**
- Co se stane, když trénovací data jsou jen z jednoho úhlu?
- Co se stane, když přidáme špatně označený obrázek?
- Jak přesný je model při špatném osvětlení?

Žáci zapisují pozorování: „Model fungoval správně při ___, ale selhal při ___."

### 4. Reflexe: Omezení strojového učení (7 min) — diskuse

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
