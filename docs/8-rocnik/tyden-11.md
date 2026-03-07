# Radiová komunikace: Posílání zpráv

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování / Digitální technologie
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje algoritmus v programovacím jazyce</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-3-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-3-01</span><span style="color: #374151;">Žák vysvětlí princip fungování digitálních technologií a sítí</span></div>

## 💬 Tip pro pátek
Nastavte ve třídě dva „tábory" — tým A a tým B si posílají zprávy přes rádio. Soutěžní formát (kdo pošle správnou zprávu první) silně motivuje.

## 🎯 Cíle hodiny

- Žák naprogramuje bezdrátovou komunikaci mezi dvěma Micro:bity pomocí rádia
- Žák nastaví skupinový kanál pro selektivní příjem zpráv
- Žák rozliší princip vysílání (broadcast) a adresovaného přenosu
- Žák propojí téma s fungováním WiFi a Bluetooth v reálném světě

## 💡 Metodický postup

### 1. Radiová komunikace — princip (8 min) — tabule

Micro:bit obsahuje rádiový modul (2,4 GHz — stejná frekvence jako WiFi a Bluetooth). Funguje jako malá vysílací stanice.

Klíčové pojmy:
- **Kanál (skupina):** Číslo 0–255 — Micro:bity na stejném kanálu se „slyší", ostatní ne
- **Broadcast:** Zpráva je poslána všem na stejném kanálu
- **Payload:** Obsah zprávy — číslo nebo text (max. 19 znaků)

Propojení: WiFi router pracuje podobně — vysílá na frekvenci, zařízení s heslem (kanál) ho „slyší".

### 2. Demo: Odesílatel a příjemce (10 min) — PC + Micro:bit

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

### 3. Projekt: Třídní chatovací systém (20 min) — Micro:bit

Žáci ve dvojicích naprogramují obousměrnou komunikaci:

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

**Rozšíření:** Přidejte tlačítko A+B pro odeslání čísla 3 = „Možná".

Různé skupiny mají různá čísla skupiny — zprávy se nemíchají.

### 4. Diskuse: Bezpečnost bezdrátové komunikace (7 min) — diskuse

Otázka: „Může někdo odposlouchat naše zprávy?" → ANO — kdokoli na stejném kanálu zprávu přijme.

Reálné zabezpečení:
- **WiFi:** Heslo (šifrování WPA2/3) — kanál je šifrovaný
- **Bluetooth:** Párování — „spárované" zařízení mají sdílený klíč
- **Micro:bit:** Žádné šifrování — pouze kanál jako „slabá ochrana"

Přechod k tématu 8. ročníku: šifrování (týdny 19 a 23).

## 📂 Podklady

- **MakeCode — Rádio:** [makecode.microbit.org](https://makecode.microbit.org) → kategorie Rádio
- **Projekt — Walkie Talkie (EN):** microbit.org/projects → „Walkie Talkie"
- **Projekt — Rock Paper Scissors (EN):** microbit.org/projects → „Rock Paper Scissors" — využívá rádio pro multiplayer
- **Video (CZ):** YouTube — „Micro:bit radio komunikace"
- **Bezpečnost:** Připomeňte propojení s bezpečnostní tématikou 2. pololetí

!!! tip "Tip pro učitele"
    Radiová komunikace je nejspektakulárnější funkce Micro:bitu — žáci jsou nadšeni bezdrátovým přenosem. Ujistěte se, že každá dvojice má jiné číslo skupiny (1–30), jinak se zprávy z různých párů mísí. Hra „Kámen, nůžky, papír" přes rádio (projekt na microbit.org) je skvělý motivační projekt po základním demo.
