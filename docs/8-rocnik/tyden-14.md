# Vánoce: Světelná show

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje algoritmus v programovacím jazyce</span></div>

## 💬 Tip pro pátek
Skvělá hodina pro sdílení s rodiči nebo jinou třídou — pozvěte publikum a nechejte žáky předvést světelné show. Motivace exploduje.

## 🎯 Cíle hodiny

- Žák naprogramuje animovanou světelnou sekvenci na LED matici Micro:bitu
- Žák využije cykly a pauzy pro kontrolu rytmu animace
- Žák volitelně synchronizuje více Micro:bitů přes rádio
- Žák tvůrčím způsobem aplikuje znalosti z 1. pololetí

## 💡 Metodický postup

### 1. Inspirace: Co je světelná show? (5 min) — tabule

Učitel ukáže příklady:
- Světelné rampouchy na domech (animace LED)
- Vánoční strom s programovatelnými světly (RGB LED pásky)
- Velké billboard displeje (matice LED panelů — jako váš Micro:bit, jen větší)

Propojení: Všechny tyto efekty jsou programy — posloupnosti příkazů se správným časováním.

### 2. Základní techniky světelné show (10 min) — PC

Učitel ukáže 3 základní techniky v MakeCode:

**Technika 1 — Blikání:**
```
opakovat stále:
  zobrazit ikonu (srdce)
  pauza 300 ms
  vymazat obrazovku
  pauza 300 ms
```

**Technika 2 — Plynulá animace (více snímků):**
Přidejte více ikon za sebou s různými pauzami.

**Technika 3 — Jas individuálních pixelů:**
Kategorie LED → `vykreslit x [0] y [0] jas [9]` (hodnota 0–9)

### 3. Vlastní světelná show (25 min) — Micro:bit

Žáci vytvoří vlastní vánoční animaci. Doporučené motivy:
- Sněhová vločka (symetrie pomocí pixelů)
- Padající sníh (animace pohyblivého bodu shora dolů)
- Blikající hvězdička (střídání vzorů)
- Vánoční strom (vykreslení tvar + blikání)
- Scroll textu „Veselé vánoce" (kategorie Základní → `zobrazit text`)

**Bonus — synchronizace přes rádio:**
Skupiny nastaví stejný kanál a synchronizují blikání stiskem A na jednom Micro:bitu.

### 4. Prezentace a sdílení (5 min)

Každý žák nebo dvojice ukáže svou animaci třídě. Hlasování o nejoriginálnější animaci.

## 📂 Podklady

- **MakeCode — LED:** [makecode.microbit.org](https://makecode.microbit.org) → kategorie LED → `vykreslit x y jas`
- **Inspirace — pixel art:** Připravte rastrové papíry 5×5 pro ruční návrh vzorů před programováním
- **Projekt — vánoční karta (EN):** microbit.org/projects → Christmas Card
- **RGB LED rozšíření:** Neopixel pásky se připojují přes piny — pro školy s vybavením spektakulární efekt
- **Sdílení výsledků:** QR kód na MakeCode projekt lze sdílet s rodiči přes třídní stránku

!!! tip "Tip pro učitele"
    Tato hodina je záměrně volnější — po intenzivních projektových týdnech 12–13 potřebují žáci i učitel prostor pro tvůrčí hru. Nehodnoťte obsah, ale přítomnost a zapojení. Pokud zbývá čas, propojte animace více Micro:bitů přes rádio — synchronizovaná světelná show celé třídy je nezapomenutelný zážitek.
