---
grade: 9
week: 19
time: 45
area: AI etika / Digitální společnost
rvp_codes:
  - code: INF-INF-004-ZV9-014
    text: Diskutuje o fungování digitálních technologií určujících trendy ve světě.
  - code: INF-INF-004-ZV9-013
    text: "Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje, na základě posouzení rizik ztráty, poškození či zneužití dat."
goals:
  - "Žák vysvětlí, co je deepfake a pomocí jaké technologie vzniká"
  - "Žák identifikuje vizuální a kontextové znaky, které mohou odhalit deepfake"
  - Žák diskutuje o etických otázkách autorských práv na AI-generovaný obsah
  - Žák zaujme vlastní informované stanovisko k regulaci deepfakes
time_budget:
  - type: review
    minutes: 10
  - type: board
    minutes: 10
  - type: discussion
    minutes: 12
  - type: pc
    minutes: 13
friday_tip: "Toto téma bývá emocionálně silné — žáci mohou mít osobní zkušenosti s manipulovaným obsahem nebo kyberšikanou. Nastavte bezpečnou atmosféru a zdůrazněte, že jde o kritické myšlení, ne o strach z technologie."
---

# 

## 💡 Metodický postup

### 1. Úvod: Skutečné nebo deepfake?

<span class="act review">🔍 Reflexe — 10 min</span>

Učitel promítne sérii 6–8 obrázků/videoukázek — žáci hlasují: „Skutečné / Deepfake?"

**Doporučené ukázky (veřejně dostupné):**
- Obrázky generované DALL-E nebo Midjourney (lidé, kteří neexistují — thispersondoesnotexist.com)
- Ukázky deepfake videa (veřejně dostupné vzdělávací materiály, např. z MIT Media Lab)
- Skutečné fotografie, které vypadají „nereálně"

Po každém obrázku: žáci zvedají ruku, pak učitel odhalí správnou odpověď.

Závěr aktivity: „Jak jste se rozhodovali? Podle čeho?"

**Znaky deepfake (zápiš na tabuli):**
- Rozmazané okraje vlasů nebo uší
- Chybné zuby nebo oči (nepřirozený lesk)
- Chyby v pozadí nebo stínech
- Přechody mezi záběry (video) — blikání, artefakty
- Kontext nedává smysl — proč by tato osoba říkala toto?

### 2. Jak deepfaky vznikají — princip

<span class="act board">🖊️ Tabule — 10 min</span>

Generative Adversarial Networks (GAN) — zjednodušené vysvětlení:

```
GENERÁTOR → vytváří falešné obrázky
     ↓
DISKRIMINÁTOR → rozlišuje skutečné od falešných
     ↑
Smyčka zpětné vazby — oba se zlepšují
```

Analogie: Padělatel bankovek vs. detektiv. Generátor = padělatel, diskriminátor = detektiv. Po tisících kol jsou padělky tak dobré, že jsou k nerozeznání.

**Reálné zneužití deepfakes:**
- Politická manipulace (falešné projevy politiků)
- Podvody (hlas šéfa firmy → zaměstnanci převedou peníze)
- Kyberšikana (falešné intimní fotografie)
- Dezinformace (falešné zpravodajské záběry)

### 3. Autorská práva a AI-generovaný obsah

<span class="act discussion">💬 Diskuse — 12 min</span>

Učitel předloží 3 scénáře, žáci diskutují ve skupinách (3 min na skupinu):

**Scénář 1:** Umělec Tomáš trénuje AI model na 10 000 obrazech jiných malířů bez jejich souhlasu. AI pak tvoří „v jejich stylu". Kdo vlastní výsledný obraz? Je to krádež?

**Scénář 2:** Novela napsaná AI, vydaná pod jménem autorky Marie. Marie zadala 20 promptů a upravila výstup. Je Marie autorka? Může knihu chránit autorské právo?

**Scénář 3:** Firma použije deepfake hlas (bez souhlasu) herečky Evy pro reklamu. Eva zemřela před 2 lety. Je to eticky přijatelné? A legálně?

Po diskusi: každá skupina sdílí svůj závěr — učitel shrnuje různá stanoviska.

**Aktuální právní situace (2024–2025):**
- EU: AI Act — první komplexní regulace AI v Evropě
- Deepfakes musí být označeny (ve většině zemí)
- Autorská práva na AI výstupy jsou stále nevyjasněna v mnoha jurisdikcích

### 4. Jak se chránit a jak ověřovat

<span class="act pc">💻 PC — 13 min</span>

<div class="zadani-pc">

Otestuj nástroje pro detekci AI obsahu a ověřování obrázků:

**Cvičení 1 — Zpětné vyhledávání obrázku** 🔍
1. Najdi jakýkoli obrázek tváře na webu (nebo vygeneruj na [thispersondoesnotexist.com](https://thispersondoesnotexist.com))
2. Jdi na [Google Images](https://images.google.com), klikni na ikonu fotoaparátu
3. Nahraj nebo vlož URL obrázku → Co Google najde?

**Cvičení 2 — AI detektor** 🤖
1. Otevři [hivemoderation.com](https://hivemoderation.com) nebo [illuminarty.ai](https://illuminarty.ai)
2. Zkopíruj libovolný text (z novin, z webu, z AI chatbotu)
3. Vloží do detektoru → Jak jistý je, že text napsal člověk nebo AI?

**Cvičení 3 — Kontext obrázku** 🧐
Najdi podezřelý obrázek a zjisti: Kdo ho zveřejnil? Kdy? Na jakém webu?

Zapiš výsledky — co tě překvapilo?

</div>

**Pravidlo SIFT:** Stop → Investigate the source → Find better coverage → Trace claims.

## 📂 Podklady

- **This Person Does Not Exist:** [thispersondoesnotexist.com](https://thispersondoesnotexist.com) — generátor neexistujících tváří, výborný pro intro
- **Deepfake detekce:** [hivemoderation.com/ai-generated-content-detection](https://hivemoderation.com) — online detektor
- **EU AI Act (CZ):** Shrnutí na Euractiv.cz nebo ec.europa.eu/cs
- **Video (EN, titulky):** YouTube — „The danger of AI is weirder than you think" — Janelle Shane (TED Talk)
- **SIFT metoda:** Materiály z MediaWise nebo CheckMedia.cz

!!! tip "Tip pro učitele"
    Scénáře k diskusi pracují nejlépe ve skupinách 3–4 žáků — jednotlivci bývají opatrnější vyjádřit se. Uveďte, že neexistuje „správná odpověď" — jde o etický diskurz, kde různá stanoviska jsou legitimní. Zároveň upozorněte na právní realitu: sdílení deepfake obsahu bez souhlasu osoby může být trestné. Tato hodina je přímou přípravou na kariérní téma v týdnu 20.
