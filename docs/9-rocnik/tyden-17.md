# Umělá inteligence II: Jak fungují LLM

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Umělá inteligence / Data a informace
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-001-ZV9-001" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-001-ZV9-001</span><span style="color: #374151;">Získá z dat informace, interpretuje data získaná pro řešení konkrétního problému.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-004-ZV9-014" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-004-ZV9-014</span><span style="color: #374151;">Diskutuje o fungování digitálních technologií určujících trendy ve světě.</span></div>

## 💬 Tip pro pátek
Začněte s otázkou: „Myslíte si, že ChatGPT skutečně rozumí tomu, co píše?" Nechte žáky říct ano/ne a proč — pak v průběhu hodiny zjistí odpověď, což je mnohem silnější než přednáška.

## 🎯 Cíle hodiny

- Žák vysvětlí princip tokenizace — jak LLM „vidí" text
- Žák popíše, jak LLM předpovídá další slovo na základě pravděpodobnosti
- Žák demystifikuje AI: pochopí, že LLM „nerozumí", ale predikuje statistické vzory
- Žák identifikuje typické selhání LLM (halucinace, neaktuálnost dat, chybná logika)

## 💡 Metodický postup

### 1. Co je token? Hra s tokenizací (10 min) — tabule / kvíz

Učitel vysvětlí: LLM nepracuje s písmeny ani slovy, ale s tokeny — kousky textu.

**Ukázka tokenizace (napište na tabuli):**
```
Věta: "ChatGPT je skvělý pomocník"
Tokeny: ["Chat", "G", "PT", " je", " skvělý", " pomocník"]

Věta: "Informatika je zábava"
Tokeny: ["Inform", "atika", " je", " z", "ábava"]
```

Klíčový fakt: GPT-4 má slovník ~100 000 tokenů. Běžné anglické slovo = 1 token, složité nebo cizí slovo = více tokenů.

Hra pro třídu: Učitel napíše větu — žáci hádají, kolik tokenů bude mít (výsledek ukáže na platform.openai.com/tokenizer).

Proč to záleží: Počet tokenů určuje „paměť" modelu (kontextové okno) a cenu API volání.

### 2. Jak LLM predikuje další slovo (12 min) — diskuse / tabule

Klíčový princip: LLM je v jádru „velmi pokročilý doplňovač textu". Trénink na miliardách textů mu dal schopnost odhadnout, jaké slovo nejpravděpodobněji následuje.

**Třídní aktivita — „Lidský LLM":**
Učitel napíše začátek věty a ptá se žáků, co následuje:

```
"Kapitál Francie je ___"         → Paříž (téměř jistě)
"Oblíbená barva žáků 9. třídy je ___"  → modrá / zelená / ... (nejistota)
"Recept na špagety: uvař vodu, přidej ___"  → sůl / těstoviny / ...
```

Pointa: Čím více kontextu, tím jistější predikce. LLM dělá přesně to — ale s miliony parametrů a celým internetem jako tréninkovými daty.

**Zjednodušená architektura (nákres na tabuli):**
```
Vstup (tokeny) → Transformer → Pravděpodobnosti slov → Výběr dalšího tokenu
"Slunce svítí ___"  →  ["jasně" 45%, "silně" 20%, "příliš" 15%, ...]
```

### 3. Halucinace a omezení LLM (13 min) — PC / diskuse

Žáci otevřou ChatGPT nebo Gemini a testují selhání:

**Experiment 1 — Halucinace (vymyšlené fakty):**
Prompt: „Napiš mi životopis českého fyzika Jana Nováka, který v roce 1998 získal Nobelovu cenu."
→ Model pravděpodobně vymyslí přesvědčivě znějící, ale zcela fiktivní životopis.

**Experiment 2 — Špatná aritmetika:**
Prompt: „Kolik je 17 × 83?"
→ LLM dělá chyby v aritmetice, protože počítá statisticky, ne numericky.
Správný výsledek: 1 411

**Experiment 3 — Neaktuálnost:**
Prompt: „Kdo je aktuální premiér Česka?" nebo „Jaký byl výsledek voleb v roce 2025?"
→ Model má cut-off datum tréninku a neví o novějších událostech.

Žáci zaznamenají výsledky experimentů do tabulky:
| Experiment | Co model odpověděl | Správná odpověď | Typ selhání |
|-----------|-------------------|-----------------|-------------|
| Halucinace | ... | neexistující osoba | vymyšlený fakt |
| Aritmetika | ... | 1 411 | numerická chyba |
| Aktuálnost | ... | aktuální info | zastaralé data |

### 4. Závěr: LLM rozumí, nebo ne? (10 min) — diskuse

Návrat k úvodní otázce: „ChatGPT skutečně rozumí tomu, co píše?"

Odpověď: Závisí na definici „rozumění". LLM:
- NENÍ: vědomý, nemá záměry, neví co říká
- JE: extrémně výkonný statistický predikátor, trénovaný na lidském jazyce
- Výsledek: Chová se tak, jako by rozuměl — ale mechanismus je zcela jiný než lidské myšlení

Filozofická otázka pro diskusi: „Kdy se statistická predikce stane porozuměním?"

## 📂 Podklady

- **Tokenizer (EN):** [platform.openai.com/tokenizer](https://platform.openai.com/tokenizer) — interaktivní ukázka tokenizace
- **Video (EN, titulky):** YouTube — „But what is a GPT?" — 3Blue1Brown (vizuální vysvětlení, ~27 min, lze zkrátit na 10 min)
- **Halucinace — příklady:** Hledejte „ChatGPT hallucination examples" pro dokumentované případy
- **Článek (CZ):** Root.cz nebo Lupa.cz — „Jak funguje ChatGPT"
- **Rozšíření:** Andrej Karpathy — „Intro to Large Language Models" (YouTube, EN) pro nadšené žáky

!!! tip "Tip pro učitele"
    Experiment s halucinacemi funguje nejlépe, když žáci sami vidí, jak přesvědčivě model lže. Klíčový výstup hodiny není technické pochopení architektury, ale kritický postoj: „Výstup AI je třeba ověřovat." Tato hodina výborně navazuje na téma deepfakes a dezinformací v týdnu 19.
