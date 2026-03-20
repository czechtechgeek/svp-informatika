---
grade: 7
week: 4
time: 45
area: "Data, informace a modelování / Algoritmizace a programování"
rvp_codes:
  - code: INF-INF-001-ZV9-003
    text: "Modeluje situace různými způsoby, včetně grafů nebo obdobných schémat."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - "Žák zná základní symboly vývojového diagramu (obdélník, kosočtverec, ovál, šipka)"
  - Žák přečte a interpretuje jednoduchý procesní diagram
  - Žák vytvoří vlastní vývojový diagram procesu se alespoň jednou podmínkovou větví
  - Žák vidí souvislost mezi diagramem a podmínkami v programování (příprava na týden 6)
time_budget:
  - type: board
    minutes: 8
  - type: board
    minutes: 10
  - type: pc
    minutes: 20
  - type: discussion
    minutes: 7
friday_tip: "Rychlá aktivita: každý žák nakreslí procesní diagram „jak probíhá můj víkend\" (10 min, papír). Sdílení ve dvojicích. Nenásilně ukazuje rozdíly v životě žáků a propojuje diagramy s reálnou zkušeností."
---

# Modelování III: Procesní diagramy

## 💡 Metodický postup

### 1. Úvod: Symboly vývojového diagramu

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel nakreslí na tabuli legendu základních tvarů:

| Tvar | Název | Použití |
|------|-------|---------|
| Ovál / zaoblený obdélník | Začátek / Konec | Vstupní a výstupní bod |
| Obdélník | Krok / Akce | Co se provede |
| Kosočtverec | Podmínka / Rozhodnutí | Ano/Ne větev |
| Šipka | Tok | Směr postupu |

Učitel projde třídou s kartičkami — žáci hádají, co tvar znamená, než učitel potvrdí.

### 2. Čtení diagramu: Přihlášení do školního systému

<span class="act board">🖊️ Tabule — 10 min</span>

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

### 3. Tvorba: Vlastní procesní diagram

<span class="act pc">💻 PC — 20 min</span>

<div class="zadani-pc" markdown="1">

Otevři [Diagrams.net (draw.io)](https://app.diagrams.net) a vytvoř vlastní vývojový diagram. Nevyžaduje registraci.

**Vyber si jeden proces:**
- **Možnost A:** „Jak se rozhodnu, co si dám k snídani" (podmínky: Je doma mléko? Mám čas vařit?)
- **Možnost B:** „Jak funguje půjčování knihy v knihovně" (registrace, dostupnost, vrácení)
- **Možnost C:** „Algoritmus pro výběr hry na PC/konzoli" (žánr, čas, sám nebo s kamarádem)

**Použij správné tvary:**
- **Ovál** = Začátek / Konec
- **Obdélník** = akce (krok)
- **Kosočtverec** = podmínka (otázka ANO/NE)
- **Šipky** = tok / pořadí kroků

**Tvůj diagram musí obsahovat:**
- Začátek a konec označeny oválem
- Aspoň jednu podmínku (kosočtverec) s větvemi ANO a NE
- Šipky ukazující směr průchodu

**Pro rychlé žáky:** Přidej do diagramu smyčku (zpětnou šipku) — kde by v tvém procesu dávalo smysl „zkus znovu"?

Hotový diagram exportuj jako PNG (Soubor → Exportovat) a odevzdej přes Google Classroom.

</div>

### 4. Propojení s programováním

<span class="act discussion">💬 Diskuse — 7 min</span>

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
