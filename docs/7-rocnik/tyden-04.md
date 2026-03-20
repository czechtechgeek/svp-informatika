# Modelování III: Procesní diagramy

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Data, informace a modelování / Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-001-ZV9-003" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-001-ZV9-003</span><span style="color: #374151;">Modeluje situace různými způsoby, včetně grafů nebo obdobných schémat.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-002-ZV9-006" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-002-ZV9-006</span><span style="color: #374151;">Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.</span></div>

## 💬 Tip pro pátek
Rychlá aktivita: každý žák nakreslí procesní diagram „jak probíhá můj víkend" (10 min, papír). Sdílení ve dvojicích. Nenásilně ukazuje rozdíly v životě žáků a propojuje diagramy s reálnou zkušeností.

## 🎯 Cíle hodiny

- Žák zná základní symboly vývojového diagramu (obdélník, kosočtverec, ovál, šipka)
- Žák přečte a interpretuje jednoduchý procesní diagram
- Žák vytvoří vlastní vývojový diagram procesu se alespoň jednou podmínkovou větví
- Žák vidí souvislost mezi diagramem a podmínkami v programování (příprava na týden 6)

## 💡 Metodický postup

### 1. Úvod: Symboly vývojového diagramu (8 min) — tabule

Učitel nakreslí na tabuli legendu základních tvarů:

| Tvar | Název | Použití |
|------|-------|---------|
| Ovál / zaoblený obdélník | Začátek / Konec | Vstupní a výstupní bod |
| Obdélník | Krok / Akce | Co se provede |
| Kosočtverec | Podmínka / Rozhodnutí | Ano/Ne větev |
| Šipka | Tok | Směr postupu |

Učitel projde třídou s kartičkami — žáci hádají, co tvar znamená, než učitel potvrdí.

### 2. Čtení diagramu: Přihlášení do školního systému (10 min) — tabule

Učitel promítne nebo nakreslí kompletní diagram:

```
(START)
  ↓
[Zadej jméno a heslo]
  ↓
◇ Heslo správné?
  → NE → [Zobraz chybu] → [Zadej znovu] → zpět na ◇
  → ANO
  ↓
[Zobraz hlavní stránku]
  ↓
(KONEC)
```

Žáci „čtou" diagram nahlas — učitel ukazuje šipkou, žáci říkají, co se děje. Diskuse: Co by se stalo bez podmínky? Co kdybychom neměli smyčku „zadej znovu"?

### 3. Tvorba: Vlastní procesní diagram (20 min) — PC nebo papír

**Zadání — vyberte jeden proces:**
- Možnost A: „Jak se rozhodnu, co si dám k snídani" (obsahuje podmínky: Je doma mléko? Mám čas vařit?)
- Možnost B: „Jak funguje půjčování knihy v knihovně" (registrace, dostupnost, vrácení)
- Možnost C: „Algoritmus pro výběr hry na PC/konzoli" (žánr, čas, sám nebo s kamarádem)

**Nástroje:**
- Online: [Diagrams.net (draw.io)](https://app.diagrams.net) — zdarma, bez registrace, shapes panel obsahuje flowchart
- Alternativa: Google Slides nebo PowerPoint (tvary + šipky)
- Offline: Papír A4, tužka, pravítko

Požadavky:
- Začátek a konec označeny oválem
- Alespoň jedna podmínka (kosočtverec) s větvemi ANO/NE
- Šipky ukazují směr

### 4. Propojení s programováním (7 min) — diskuse

Učitel ukáže hotový žákovský diagram a vedle něj otevře Scratch. Ukáže, že:
- Obdélník = jeden blok příkazu
- Kosočtverec = blok `když... pak...`
- Smyčka = blok `opakuj dokola`

Závěr: Diagram je jen jiný způsob zápisu algoritmu — přátelský pro lidi, Scratch je přátelský pro počítač. V 7. ročníku budeme přecházet od diagramu k programu.

## 📂 Podklady

- **Nástroj — draw.io / diagrams.net:** [app.diagrams.net](https://app.diagrams.net) — nejlepší volba, zdarma, výborné šablony pro flowchart
- **Nástroj — Lucidchart (EN):** [lucidchart.com](https://www.lucidchart.com) — alternativa, zdarma pro studenty, propojení s Google Workspace
- **Cvičení na čtení diagramů (CZ):** [imysleni.cz](https://imysleni.cz) — hledejte sekci „Algoritmy a diagramy"
- **Šablona vývojového diagramu:** Připravte prázdnou šablonu (START → akce → podmínka → END) na papíře pro rychlé skupiny nebo žáky s problémy s orientací v nástroji

!!! tip "Tip pro učitele"
    Procesní diagramy jsou most mezi myšlenkovými mapami a programováním. Zdůrazněte žákům, že IT firmy (Google, Alza, ČSOB) kreslí takové diagramy před každým větším projektem — není to „jenom škola". Pokud máte ve třídě žáky s rodiči v IT, zeptejte se jich předem, zda mohou přinést reálný pracovní diagram (anonymizovaný).
