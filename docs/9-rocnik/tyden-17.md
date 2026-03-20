---
grade: 9
week: 17
time: 45
area: Umělá inteligence / Data a informace
rvp_codes:
  - code: INF-INF-001-ZV9-001
    text: "Získá z dat informace, interpretuje data získaná pro řešení konkrétního problému."
  - code: INF-INF-004-ZV9-014
    text: Diskutuje o fungování digitálních technologií určujících trendy ve světě.
goals:
  - "Žák vysvětlí princip tokenizace — jak LLM „vidí\" text"
  - "Žák popíše, jak LLM předpovídá další slovo na základě pravděpodobnosti"
  - "Žák demystifikuje AI: pochopí, že LLM „nerozumí\", ale predikuje statistické vzory"
  - "Žák identifikuje typické selhání LLM (halucinace, neaktuálnost dat, chybná logika)"
time_budget:
  - type: review
    minutes: 10
  - type: discussion
    minutes: 12
  - type: pc
    minutes: 13
  - type: discussion
    minutes: 10
friday_tip: "Začněte s otázkou: „Myslíte si, že ChatGPT skutečně rozumí tomu, co píše?\" Nechte žáky říct ano/ne a proč — pak v průběhu hodiny zjistí odpověď, což je mnohem silnější než přednáška."
---

# 

## 💡 Metodický postup

### 1. Co je token? Hra s tokenizací

<span class="act review">🔍 Reflexe — 10 min</span>

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

### 2. Jak LLM predikuje další slovo

<span class="act discussion">💬 Diskuse — 12 min</span>

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

### 3. Halucinace a omezení LLM

<span class="act pc">💻 PC — 13 min</span>

<div class="zadani-pc" markdown="1">

Otevři **ChatGPT** nebo **Gemini** a testuj, kdy AI selže. Proveď tyto 3 experimenty a zaznamenej výsledky:

**Experiment 1 — Halucinace (vymyšlené fakty)**
Zadej: *„Napiš mi životopis českého fyzika Jana Nováka, který v roce 1998 získal Nobelovu cenu."*
→ Co model vymyslel? Ověř, zda tato osoba skutečně existuje.

**Experiment 2 — Špatná aritmetika**
Zadej: *„Kolik je 17 × 83?"*
→ Správný výsledek je **1 411**. Splnil to model správně?

**Experiment 3 — Neaktuálnost**
Zadej: *„Kdo je aktuální premiér České republiky?"*
→ Porovnej odpověď s realitou. Je model aktuální?

Zapiš výsledky do tabulky:

| Experiment | Co model odpověděl | Správná odpověď | Typ selhání |
|-----------|-------------------|-----------------|-------------|
| Halucinace | … | neexistující osoba | vymyšlený fakt |
| Aritmetika | … | 1 411 | numerická chyba |
| Aktuálnost | … | aktuální info | zastaralé data |

</div>

Žáci sdílejí výsledky — co je nejvíce překvapilo?

### 4. Závěr: LLM rozumí, nebo ne?

<span class="act discussion">💬 Diskuse — 10 min</span>

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
