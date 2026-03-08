# Prompt Engineering: Jak se ptát AI

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Umělá inteligence / Digitální gramotnost
- **Výstup:** <div class="curriculumTag" data-code="I-9-4-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-4-01</span><span style="color: #374151;">Žák kriticky a efektivně využívá nástroje umělé inteligence</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-4-03" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-4-03</span><span style="color: #374151;">Žák efektivně komunikuje a formuluje požadavky v digitálním prostředí</span></div>

## 💬 Tip pro pátek
Dejte žákům soutěžní rámec — kdo ze třídy dostane nejlepší AI odpověď na stejnou otázku pomocí různých promptů? Soutěž o „nejlepší prompt" silně motivuje a přirozeně vede k diskusi o tom, proč jeden prompt funguje lépe než druhý.

## 🎯 Cíle hodiny

- Žák vysvětlí, co je prompt a proč záleží na jeho formulaci
- Žák aplikuje techniky prompt engineeringu: kontext, role, formát, few-shot příklady
- Žák porovná výsledky špatně a dobře formulovaného promptu na konkrétním příkladu
- Žák vytvoří vlastní systémový prompt pro specifický účel

## 💡 Metodický postup

### 1. Proč záleží na tom, jak se ptám? (8 min) — tabule / diskuse

Učitel ukáže srovnání stejné otázky formulované různě:

**Špatný prompt:**
```
Napiš mi něco o klimatu.
```
→ AI vyprodukuje obecný, nezaměřený text o 500 slovech, který k ničemu není.

**Dobrý prompt:**
```
Napiš stručné vysvětlení (150 slov) změny klimatu pro žáka 9. třídy.
Použij konkrétní příklady z Česka. Vyhni se odborným termínům.
```
→ AI vyprodukuje přesně to, co potřebujeme.

Analogie: Příkaz AI je jako pracovní zadání zaměstnanci. Čím přesnější zadání, tím lepší výsledek.

### 2. Techniky prompt engineeringu (12 min) — tabule

Učitel projde 5 klíčových technik s příklady:

**1. Kontext — říct, k čemu výstup slouží:**
```
Jsem žák 9. třídy a píšu referát o vesmíru. Vysvětli mi...
```

**2. Role — přidělit AI roli:**
```
Jsi zkušený programátor v Pythonu. Zkontroluj tento kód a najdi chyby:
[kód]
```

**3. Formát výstupu — specifikovat strukturu:**
```
Odpověz ve formátu tabulky se sloupci: Výhoda | Nevýhoda | Příklad
```

**4. Few-shot — ukázat příklady požadovaného výstupu:**
```
Přepiš věty do formálního stylu:
Vstup: "Ahoj, potřebuju vědět kdy je schůzka"
Výstup: "Dobrý den, rád bych se dotázal na termín schůzky."
Vstup: "Hele, ta zpráva byla divná"
Výstup: [?]
```

**5. Omezení — říct, co AI nemá dělat:**
```
Vysvětli princip černých děr. Nepoužívej matematické vzorce.
Délka: maximálně 3 věty.
```

### 3. Soutěž: Nejlepší prompt (18 min) — PC / kvíz

Žáci pracují ve dvojicích. Každá dvojice dostane stejný úkol a má 10 minut vytvořit co nejlepší prompt.

**Zadání 1 — Pomoc s učením:**
Cíl: Nechat AI vytvořit 5 testových otázek z dějepisu o 2. světové válce, vhodných pro žáka 9. třídy, ve formátu kvízu s výběrem ze 3 možností.

**Zadání 2 — Ladění kódu:**
Cíl: Nechat AI najít a vysvětlit chybu v tomto Python kódu:
```python
def secti_seznam(seznam):
    soucet = 0
    for i in seznam
        soucet += i
    return soucet
```

**Zadání 3 — Kreativní psaní:**
Cíl: Nechat AI napsat vtipný příběh (5 vět) o robotovi, který se poprvé ocitne v české škole, psaný pro teenagery.

Po 10 minutách: každá dvojice sdílí svůj prompt a výsledek. Třída hlasuje, který výsledek je nejlepší.

**Diskuse:** Jaké prvky nejúspěšnějšího promptu ho odlišovaly?

### 4. Systémový prompt a limity AI (7 min) — diskuse

Učitel vysvětlí koncept systémového promptu (instrukce, která nastaví chování AI před konverzací):

```
Systémový prompt:
"Jsi asistent pro výuku matematiky na ZŠ. Vždy odpovídej v češtině.
Vysvětluj krok po kroku. Neposkytuj přímo výsledek — veď žáka otázkami."
```

Diskuse: Proč AI odmítá některé požadavky?
- Safety guidelines — ochrana před zneužitím
- „Jailbreak" pokusy — proč to funguje někdy a jindy ne
- Etická odpovědnost uživatele vs. odpovědnost firmy

## 📂 Podklady

- **ChatGPT:** [chat.openai.com](https://chat.openai.com) — nutné přihlášení (Google účet)
- **Claude:** [claude.ai](https://claude.ai) — alternativa, dobrý pro delší texty
- **Gemini:** [gemini.google.com](https://gemini.google.com) — od Google, přímá integrace s Google Workspace
- **Prompt Engineering Guide (EN):** [promptingguide.ai](https://www.promptingguide.ai) — obsáhlý průvodce technikami
- **Soutěžní zadání (tisk):** Připravte kartičky s zadáními pro soutěž v každé dvojici

!!! tip "Tip pro učitele"
    Soutěžní formát v aktivitě 3 funguje výborně — žáci jsou přirozeně motivováni napsat lepší prompt než spolužáci. Upozorněte žáky, že prompt engineering je reálná pracovní dovednost — v roce 2024 existují pracovní pozice „Prompt Engineer" s platem nad průměrem. Hodina přirozeně navazuje na diskusi o AI a etice v týdnu 19.
