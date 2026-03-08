# AI a etika: Deepfakes, autorská práva

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** AI etika / Digitální společnost
- **Výstup:** <div class="curriculumTag" data-code="I-9-4-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-4-01</span><span style="color: #374151;">Žák kriticky hodnotí digitální obsah a rozpozná manipulaci</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-4-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-4-02</span><span style="color: #374151;">Žák bezpečně a odpovědně se chová v digitálním prostředí</span></div>

## 💬 Tip pro pátek
Toto téma bývá emocionálně silné — žáci mohou mít osobní zkušenosti s manipulovaným obsahem nebo kyberšikanou. Nastavte bezpečnou atmosféru a zdůrazněte, že jde o kritické myšlení, ne o strach z technologie.

## 🎯 Cíle hodiny

- Žák vysvětlí, co je deepfake a pomocí jaké technologie vzniká
- Žák identifikuje vizuální a kontextové znaky, které mohou odhalit deepfake
- Žák diskutuje o etických otázkách autorských práv na AI-generovaný obsah
- Žák zaujme vlastní informované stanovisko k regulaci deepfakes

## 💡 Metodický postup

### 1. Úvod: Skutečné nebo deepfake? (10 min) — kvíz / tabule

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

### 2. Jak deepfaky vznikají — princip (10 min) — tabule

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

### 3. Autorská práva a AI-generovaný obsah (12 min) — diskuse

Učitel předloží 3 scénáře, žáci diskutují ve skupinách (3 min na skupinu):

**Scénář 1:** Umělec Tomáš trénuje AI model na 10 000 obrazech jiných malířů bez jejich souhlasu. AI pak tvoří „v jejich stylu". Kdo vlastní výsledný obraz? Je to krádež?

**Scénář 2:** Novela napsaná AI, vydaná pod jménem autorky Marie. Marie zadala 20 promptů a upravila výstup. Je Marie autorka? Může knihu chránit autorské právo?

**Scénář 3:** Firma použije deepfake hlas (bez souhlasu) herečky Evy pro reklamu. Eva zemřela před 2 lety. Je to eticky přijatelné? A legálně?

Po diskusi: každá skupina sdílí svůj závěr — učitel shrnuje různá stanoviska.

**Aktuální právní situace (2024–2025):**
- EU: AI Act — první komplexní regulace AI v Evropě
- Deepfakes musí být označeny (ve většině zemí)
- Autorská práva na AI výstupy jsou stále nevyjasněna v mnoha jurisdikcích

### 4. Jak se chránit a jak ověřovat (13 min) — PC / diskuse

Žáci otestují nástroje pro detekci AI obsahu:

**Praktická cvičení:**
1. Vyhledejte obraz na Google Images → klikněte na ikonu fotoaparátu → zpětné vyhledávání obrázku
2. Zkuste AI detector: [hivemoderation.com](https://hivemoderation.com) nebo [illuminarty.ai](https://illuminarty.ai)
3. Zkuste vyhledat kontext: Kdo zveřejnil? Kdy? Na jakém webu?

**Pravidlo SIFT pro ověřování digitálního obsahu:**
- **S**top — nepřeposílej hned, zamysli se
- **I**nvestigate the source — kdo to zveřejnil?
- **F**ind better coverage — jsou jiné zdroje, které to potvrzují?
- **T**race claims — sleduj, odkud informace pochází původně

## 📂 Podklady

- **This Person Does Not Exist:** [thispersondoesnotexist.com](https://thispersondoesnotexist.com) — generátor neexistujících tváří, výborný pro intro
- **Deepfake detekce:** [hivemoderation.com/ai-generated-content-detection](https://hivemoderation.com) — online detektor
- **EU AI Act (CZ):** Shrnutí na Euractiv.cz nebo ec.europa.eu/cs
- **Video (EN, titulky):** YouTube — „The danger of AI is weirder than you think" — Janelle Shane (TED Talk)
- **SIFT metoda:** Materiály z MediaWise nebo CheckMedia.cz

!!! tip "Tip pro učitele"
    Scénáře k diskusi pracují nejlépe ve skupinách 3–4 žáků — jednotlivci bývají opatrnější vyjádřit se. Uveďte, že neexistuje „správná odpověď" — jde o etický diskurz, kde různá stanoviska jsou legitimní. Zároveň upozorněte na právní realitu: sdílení deepfake obsahu bez souhlasu osoby může být trestné. Tato hodina je přímou přípravou na kariérní téma v týdnu 20.
