# Senzory III: Teploměr a světelný senzor

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování / Data, informace a modelování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje algoritmus v programovacím jazyce</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-1-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-1-01</span><span style="color: #374151;">Žák porozumí pojmu data, jejich typům a způsobům reprezentace</span></div>

## 💬 Tip pro pátek
Měření teploty ve třídě vs. na chodbě: žáci přirozeně diskutují o rozdílech a přesnosti — skvělá propojení s fyzikálním měřením a přesností přístrojů.

## 🎯 Cíle hodiny

- Žák přečte hodnotu z vestavěného teploměru a světelného senzoru Micro:bitu
- Žák naprogramuje podmíněnou reakci na překročení prahové hodnoty (alarm)
- Žák zaznamená naměřená data a porovná je s fyzickým teploměrem
- Žák kriticky zhodnotí přesnost vestavěných senzorů

## 💡 Metodický postup

### 1. Přehled environmentálních senzorů (8 min) — tabule

Micro:bit obsahuje dva environmentální senzory:

**Teploměr:**
- Měří teplotu procesoru (ne okolí přímo) — přibližná přesnost ±2–3 °C
- Kategorie Vstup → `teplota (°C)`
- Reálné použití: monitoring serveroven, skleníků, skladu potravin

**Světelný senzor:**
- LED diody fungují jako fotodiody — měří okolní světlo
- Hodnota 0 (tma) až 255 (plné světlo)
- Kategorie Vstup → `úroveň světla`
- Reálné použití: automatické stmívání displeje, detektor přítomnosti

### 2. Demo a měření (12 min) — PC + Micro:bit

Žáci napíší jednoduchý program pro monitoring:

```
opakovat stále:
  zobrazit číslo → teplota (°C)
  pauza 2000 ms
  zobrazit číslo → úroveň světla
  pauza 2000 ms
```

Aktivita: Proměřte teplotu na různých místech — u okna, u radiátoru, na chodbě. Zapište výsledky do tabulky. Porovnejte s fyzickým teploměrem — jak velká je odchylka?

### 3. Projekt: Teplotní alarm (18 min) — Micro:bit

Žáci naprogramují alarm překročení teploty:

```
opakovat stále:
  pokud teplota(°C) > 30:
    zobrazit ikonu (srdce s výstrahou)
    zvuk "Da da da" (nebo blikání)
  jinak:
    zobrazit číslo → teplota
  pauza 1000 ms
```

**Varianta se světlem:**
```
pokud úroveň světla < 50:
  zobrazit text "TMA"
jinak:
  zobrazit text "SVĚTLO"
```

**Rozšíření (pro rychlé):** Spojte oba senzory — zobrazujte různé ikony pro různé kombinace teploty a světla (ráno/odpoledne/noc, léto/zima).

### 4. Diskuse: Přesnost a kalibrace (7 min) — diskuse

Klíčové otázky:
- „Proč se Micro:bit teploměr liší od skutečné teploty?" (Zahřívání procesoru)
- „Jak bychom zvýšili přesnost?" (Kalibrace = odečtení konstanty)
- „Jaký senzor byste přidali, kdybyste mohli?" (Vlhkost, CO₂, hluk...)

Propojení s praxí: Profesionální senzory jsou přesnější, ale stojí více. Micro:bit je ukázka principu — v IoT zařízeních se používají dedikované senzorové moduly.

## 📂 Podklady

- **MakeCode — Vstup → Teplota:** [makecode.microbit.org](https://makecode.microbit.org) → Vstup → `teplota (°C)` a `úroveň světla`
- **Projekt — meteorologická stanice:** microbit.org/projects → „Weather Station" — komplexnější verze dnešního projektu
- **Kalibrace teploměru:** Empiricky zjistěte offset (naměřená − skutečná teplota) a odečtěte ho ve vzorci
- **Rozšíření — external senzory:** DHT11/DHT22 teplotní a vlhkostní senzor, připojitelný přes piny
- **Video (CZ):** YouTube — „Micro:bit teploměr projekt česky"

!!! tip "Tip pro učitele"
    Přesnost teploměru závisí na konkrétním kusu Micro:bitu a prostředí — nevadí, pokud se žáci ptají, proč se liší od fyzického teploměru. To je cenná vědecká diskuse o přesnosti měřicích přístrojů a kalibraci. Pokud máte přístup k DHT11 senzoru (cena cca 30 Kč), lze hodinu rozšířit na přesné měření vlhkosti — velmi vhodné pro propojení s přírodovědou.
