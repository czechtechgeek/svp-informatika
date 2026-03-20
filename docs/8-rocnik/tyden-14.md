# 🎄 Vánoce: Světelná show

> **Stav:** `⬜ Nekontrolováno`

### 📋 Kontext a cíle
> **RVP ZV (Informatika):** Algoritmizace a programování
> **Kód:** `INF-INF-002-ZV9-007` – *V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné.*

**Po hodině žák:**
* **Naprogramuje** animovanou světelnou sekvenci na LED matici Micro:bitu.
* **Využije** cykly a pauzy pro kontrolu rytmu animace.
* **Volitelně synchronizuje** více Micro:bitů přes rádio.
* **Tvůrčím způsobem aplikuje** znalosti z 1. pololetí.

---

### 💡 Metodický postup (45 min)

#### 1. Inspirace: Co je světelná show? (5 min)
*Tabule — motivace.*

Učitel ukáže příklady:
- Světelné rampouchy na domech (animace LED)
- Vánoční strom s programovatelnými světly (RGB LED pásky)
- Velké billboard displeje (matice LED panelů — jako váš Micro:bit, jen větší)

Propojení: Všechny tyto efekty jsou programy — posloupnosti příkazů se správným časováním.

---

#### 2. Základní techniky světelné show (10 min)
*Práce na PC — demonstrace.*

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

#### 3. Vlastní světelná show (25 min)
*Práce s Micro:bitem — tvůrčí tvorba.*

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

#### 4. Prezentace a sdílení (5 min)

Každý žák nebo dvojice ukáže svou animaci třídě. Hlasování o nejoriginálnější animaci.

---

### 🛠️ Zdroje a nástroje

* **MakeCode — LED:** [makecode.microbit.org](https://makecode.microbit.org) → kategorie LED → `vykreslit x y jas`
* **Inspirace — pixel art:** Připravte rastrové papíry 5×5 pro ruční návrh vzorů před programováním
* **Projekt — vánoční karta (EN):** microbit.org/projects → Christmas Card
* **RGB LED rozšíření:** Neopixel pásky se připojují přes piny — pro školy s vybavením spektakulární efekt
* **Sdílení výsledků:** QR kód na MakeCode projekt lze sdílet s rodiči přes třídní stránku

---

> 💡 **Tip pro učitele:**
> Tato hodina je záměrně volnější — po intenzivních projektových týdnech 12–13 potřebují žáci i učitel prostor pro tvůrčí hru. Nehodnoťte obsah, ale přítomnost a zapojení. Pokud zbývá čas, propojte animace více Micro:bitů přes rádio — synchronizovaná světelná show celé třídy je nezapomenutelný zážitek.

> 💬 **Tip pro pátek:** Skvělá hodina pro sdílení s rodiči nebo jinou třídou — pozvěte publikum a nechejte žáky předvést světelné show. Motivace exploduje.
