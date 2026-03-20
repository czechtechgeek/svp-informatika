---
grade: 8
week: 11
time: 45
area: Algoritmizace a programování / Digitální technologie
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - "**Naprogramuje** bezdrátovou komunikaci mezi dvěma Micro:bity pomocí rádia."
  - "**Nastaví** skupinový kanál pro selektivní příjem zpráv."
  - "**Rozliší** princip vysílání (broadcast) a adresovaného přenosu."
  - "**Propojí** téma s fungováním WiFi a Bluetooth v reálném světě."
time_budget:
  - type: board
    minutes: 8
  - type: pc
    minutes: 10
  - type: board
    minutes: 20
  - type: discussion
    minutes: 7
friday_tip: "Nastavte ve třídě dva „tábory\" — tým A a tým B si posílají zprávy přes rádio. Soutěžní formát (kdo pošle správnou zprávu první) silně motivuje."
---

# Radiová komunikace: Posílání zpráv

## 💡 Metodický postup

### 1. Radiová komunikace — princip

<span class="act board">🖊️ Tabule — 8 min</span>

Micro:bit obsahuje rádiový modul (2,4 GHz — stejná frekvence jako WiFi a Bluetooth). Funguje jako malá vysílací stanice.

Klíčové pojmy:
- **Kanál (skupina):** Číslo 0–255 — Micro:bity na stejném kanálu se „slyší", ostatní ne
- **Broadcast:** Zpráva je poslána všem na stejném kanálu
- **Payload:** Obsah zprávy — číslo nebo text (max. 19 znaků)

Propojení: WiFi router pracuje podobně — vysílá na frekvenci, zařízení s heslem (kanál) ho „slyší".

---

### 2. Demo: Odesílatel a příjemce

<span class="act pc">💻 PC — 10 min</span>

Učitel naprogramuje 2 Micro:bity:

**Program A — Odesílatel:**
```
při spuštění:
  rádio nastav skupinu 7

při stisknutí A:
  rádio odešli text "AHOJ"
```

**Program B — Příjemce:**
```
při spuštění:
  rádio nastav skupinu 7

při přijetí rádio textové zprávy:
  zobrazit přijatý text
```

Žáci sledují, jak zpráva přejde z jednoho Micro:bitu na druhý bezdrátově.

---

### 3. Projekt: Třídní chatovací systém

<span class="act board">🖊️ Tabule — 20 min</span>

<div class="zadani-pc" markdown="1">

Ve dvojicích naprogramujte obousměrnou komunikaci (každá dvojice má jiné číslo skupiny 1–30):

```
při spuštění:
  rádio nastav skupinu 5  ← stejná skupina pro celou dvojici

při stisknutí A:
  rádio odešli číslo 1    ← signál "Ano"
  zobrazit text "ANO"

při stisknutí B:
  rádio odešli číslo 2    ← signál "Ne"
  zobrazit text "NE"

při přijetí čísla:
  pokud přijaté číslo = 1 → zobrazit ikonu (fajfka)
  pokud přijaté číslo = 2 → zobrazit ikonu (křížek)
```

**Rozšíření *(pro rychlé)*:** Přidejte tlačítko A+B pro odeslání čísla 3 = „Možná".

</div>

---

### 4. Diskuse: Bezpečnost bezdrátové komunikace

<span class="act discussion">💬 Diskuse — 7 min</span>

Otázka: „Může někdo odposlouchat naše zprávy?" → ANO — kdokoli na stejném kanálu zprávu přijme.

Reálné zabezpečení:
- **WiFi:** Heslo (šifrování WPA2/3) — kanál je šifrovaný
- **Bluetooth:** Párování — „spárované" zařízení mají sdílený klíč
- **Micro:bit:** Žádné šifrování — pouze kanál jako „slabá ochrana"

Přechod k tématu 8. ročníku: šifrování (týdny 19 a 23).

---

## 📂 Zdroje a podklady

* **MakeCode — Rádio:** [makecode.microbit.org](https://makecode.microbit.org) → kategorie Rádio
* **Projekt — Walkie Talkie (EN):** microbit.org/projects → „Walkie Talkie"
* **Projekt — Rock Paper Scissors (EN):** microbit.org/projects → „Rock Paper Scissors" — využívá rádio pro multiplayer
* **Video (CZ):** YouTube — „Micro:bit radio komunikace"
* **Bezpečnost:** Připomeňte propojení s bezpečnostní tématikou 2. pololetí

---

!!! tip "Tip pro učitele"
    Radiová komunikace je nejspektakulárnější funkce Micro:bitu — žáci jsou nadšeni bezdrátovým přenosem. Ujistěte se, že každá dvojice má jiné číslo skupiny (1–30), jinak se zprávy z různých párů mísí. Hra „Kámen, nůžky, papír" přes rádio (projekt na microbit.org) je skvělý motivační projekt po základním demo.
