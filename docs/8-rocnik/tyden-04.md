# Vizualizace: Který graf pro jaká data

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Data, informace a modelování
- **Výstup:** <div class="curriculumTag" data-code="I-9-1-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-1-02</span><span style="color: #374151;">Žák zpracuje a interpretuje data pomocí vhodných nástrojů</span></div>

## 💬 Tip pro pátek
Ukažte žákům infografiku z novin nebo webu (viz Datawrapper nebo Flourish) a nechte je hádat: „Jaký typ grafu byl použit a proč?" Vizuální diskuse funguje lépe než přednáška.

## 🎯 Cíle hodiny

- Žák rozlišuje základní typy grafů a ví, pro jaká data je každý vhodný
- Žák vybere správný typ grafu pro zadaná data a zdůvodní volbu
- Žák vytvoří alespoň dva různé typy grafů v tabulkovém procesoru
- Žák posoudí, zda zvolený typ grafu správně komunikuje informaci

## 💡 Metodický postup

### 1. Přehled typů grafů (10 min) — tabule

Učitel projde se třídou přehled:

| Typ grafu | Kdy použít | Příklad |
|-----------|-----------|---------|
| Sloupcový / pruhový | Porovnání kategorií | Prodeje podle měsíce |
| Spojnicový | Vývoj v čase | Teploty v průběhu roku |
| Výsečový (koláčový) | Podíly celku (max. 5–6 dílů) | Rozdělení rozpočtu |
| Bodový (scatter) | Vztah dvou proměnných | Výška vs. váha |
| Teplotní mapa | Intenzita v mřížce | Aktivita uživatelů po hodinách |

Klíčová pravidla:
- Koláčový graf NIKDY pro vývoj v čase
- Sloupcový NIKDY pro procentuální podíly nad 6 kategorií (lépe vodorovný pruh)
- Spojnicový POUZE pokud osa X je čas nebo pořadí

### 2. Aktivita: Přiřaď graf k datům (10 min) — bez počítače

Učitel rozdá kartičky (nebo promítne) — žáci ve dvojicích přiřadí:

- Podíl žáků, kteří jezdí do školy autobusem / autem / pěšky → koláčový
- Vývoj průměrné teploty každý měsíc → spojnicový
- Počet knih přečtených žáky za rok — porovnání tříd → sloupcový
- Vztah mezi dobou spánku a výsledky testů → bodový
- Denní návštěvnost školního webu po hodinách → teplotní mapa nebo sloupcový

### 3. Tvorba grafů (18 min) — PC

Žáci vytvoří dva grafy ze dvou různých datových sad:

**Dataset A — návštěvnost školní jídelny:**
| Den | Pondělí | Úterý | Středa | Čtvrtek | Pátek |
|-----|---------|-------|--------|---------|-------|
| Počet obědů | 312 | 298 | 321 | 305 | 267 |
→ Vhodný typ: sloupcový

**Dataset B — oblíbené předměty třídy (anketní výsledky):**
| Předmět | % žáků |
|---------|--------|
| Informatika | 38 % |
| Tělocvik | 27 % |
| Výtvarná | 18 % |
| Matematika | 17 % |
→ Vhodný typ: koláčový nebo vodorovný pruh

Podmínka: Graf musí mít název, popsané osy a legendu.

### 4. Vzájemné hodnocení (7 min) — diskuse

Žáci si navzájem ukáží grafy a odpovídají na otázky:
- „Jaký typ grafu zvolil/a? Proč?"
- „Je volba správná? Co by ses změnil/a?"

## 📂 Podklady

- **Nástroj — Datawrapper (EN/CZ):** [datawrapper.de](https://www.datawrapper.de) — profesionální vizualizace online, zdarma, velmi snadné ovládání
- **Nástroj — Flourish (EN):** [flourish.studio](https://flourish.studio) — interaktivní grafy a infografiky
- **Reference — chart chooser:** Hledejte „chart chooser" nebo „which chart to use" — přehledné plakáty pro výběr grafu
- **Video (CZ):** YouTube — „jak vytvořit graf Excel" nebo „typy grafů kdy použít"
- **Rozšíření:** Google Data Studio / Looker Studio — profesionální dashboardy zdarma

!!! tip "Tip pro učitele"
    Koláčové grafy jsou u žáků oblíbené, ale datový svět je odmítá — příliš těžko se porovnávají výseče. Pokud žáci chtějí koláčový, povolte to, ale pak ukažte stejná data ve vodorovném pruhovém grafu — žáci sami uvidí, který je čitelnější. Tato hodina je přímou přípravou na hodinu 5 o klamavých grafech.
