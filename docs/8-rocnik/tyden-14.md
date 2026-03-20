---
grade: 8
week: 14
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
goals:
  - "**Naprogramuje** animovanou světelnou sekvenci na LED matici Micro:bitu."
  - "**Využije** cykly a pauzy pro kontrolu rytmu animace."
  - "**Volitelně synchronizuje** více Micro:bitů přes rádio."
  - "**Tvůrčím způsobem aplikuje** znalosti z 1. pololetí."
time_budget:
  - type: board
    minutes: 5
  - type: pc
    minutes: 10
  - type: board
    minutes: 25
  - type: board
    minutes: 5
friday_tip: Skvělá hodina pro sdílení s rodiči nebo jinou třídou — pozvěte publikum a nechejte žáky předvést světelné show. Motivace exploduje.
---

# Vánoce: Světelná show

## 💡 Metodický postup

### 1. Inspirace: Co je světelná show?

<span class="act board">🖊️ Tabule — 5 min</span>

Učitel ukáže příklady:
- Světelné rampouchy na domech (animace LED)
- Vánoční strom s programovatelnými světly (RGB LED pásky)
- Velké billboard displeje (matice LED panelů — jako váš Micro:bit, jen větší)

Propojení: Všechny tyto efekty jsou programy — posloupnosti příkazů se správným časováním.

---

### 2. Základní techniky světelné show

<span class="act pc">💻 PC — 10 min</span>

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

---

### 3. Vlastní světelná show

<span class="act board">🖊️ Tabule — 25 min</span>

<div class="zadani-pc">

Vytvořte vlastní vánoční animaci v MakeCode. Doporučené motivy (nebo vymyslete vlastní):

- Sněhová vločka (symetrie pomocí pixelů)
- Padající sníh (animace pohyblivého bodu shora dolů)
- Blikající hvězdička (střídání vzorů)
- Vánoční strom (vykreslení tvaru + blikání)
- Scroll textu „Veselé vánoce" (kategorie Základní → `zobrazit text`)

**Bonus — synchronizace přes rádio:** Skupiny nastaví stejný kanál a synchronizují blikání stiskem A na jednom Micro:bitu.

</div>

---

### 4. Prezentace a sdílení

<span class="act board">🖊️ Tabule — 5 min</span>

Každý žák nebo dvojice ukáže svou animaci třídě. Hlasování o nejoriginálnější animaci.

---

## 📂 Zdroje a podklady

* **MakeCode — LED:** [makecode.microbit.org](https://makecode.microbit.org) → kategorie LED → `vykreslit x y jas`
* **Inspirace — pixel art:** Připravte rastrové papíry 5×5 pro ruční návrh vzorů před programováním
* **Projekt — vánoční karta (EN):** microbit.org/projects → Christmas Card
* **RGB LED rozšíření:** Neopixel pásky se připojují přes piny — pro školy s vybavením spektakulární efekt
* **Sdílení výsledků:** QR kód na MakeCode projekt lze sdílet s rodiči přes třídní stránku

---

!!! tip "Tip pro učitele"
    Tato hodina je záměrně volnější — po intenzivních projektových týdnech 12–13 potřebují žáci i učitel prostor pro tvůrčí hru. Nehodnoťte obsah, ale přítomnost a zapojení. Pokud zbývá čas, propojte animace více Micro:bitů přes rádio — synchronizovaná světelná show celé třídy je nezapomenutelný zážitek.
