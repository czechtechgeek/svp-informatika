# 🌡️ Senzory III: Teploměr a světelný senzor

> **Stav:** `⬜ Nekontrolováno`

### 📋 Kontext a cíle
> **RVP ZV (Informatika):** Algoritmizace a programování / Data, informace a modelování
> **Kód:** `INF-INF-002-ZV9-007` – *V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné.*
> **Kód:** `INF-INF-001-ZV9-001` – *Získá z dat informace, interpretuje data získaná pro řešení konkrétního problému.*

**Po hodině žák:**
* **Přečte** hodnotu z vestavěného teploměru a světelného senzoru Micro:bitu.
* **Naprogramuje** podmíněnou reakci na překročení prahové hodnoty (alarm).
* **Zaznamená** naměřená data a porovná je s fyzickým teploměrem.
* **Kriticky zhodnotí** přesnost vestavěných senzorů.

---

### 💡 Metodický postup (45 min)

#### 1. Přehled environmentálních senzorů (8 min)
*Tabule — výklad.*

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

---

#### 2. Demo a měření (12 min)
*PC + Micro:bit — demonstrace a měření.*

Žáci napíší jednoduchý program pro monitoring:

```
opakovat stále:
  zobrazit číslo → teplota (°C)
  pauza 2000 ms
  zobrazit číslo → úroveň světla
  pauza 2000 ms
```

Aktivita: Proměřte teplotu na různých místech — u okna, u radiátoru, na chodbě. Zapište výsledky do tabulky. Porovnejte s fyzickým teploměrem — jak velká je odchylka?

---

#### 3. Projekt: Teplotní alarm (18 min)
*Práce s Micro:bitem.*

<div class="zadani-pc">

Naprogramujte alarm překročení teploty:

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

**Rozšíření *(pro rychlé)*:** Spojte oba senzory — zobrazujte různé ikony pro různé kombinace teploty a světla (ráno/odpoledne/noc, léto/zima).

</div>

---

#### 4. Diskuse: Přesnost a kalibrace (7 min)
*Diskuze.*

Klíčové otázky:
- „Proč se Micro:bit teploměr liší od skutečné teploty?" (Zahřívání procesoru)
- „Jak bychom zvýšili přesnost?" (Kalibrace = odečtení konstanty)
- „Jaký senzor byste přidali, kdybyste mohli?" (Vlhkost, CO₂, hluk...)

Propojení s praxí: Profesionální senzory jsou přesnější, ale stojí více. Micro:bit je ukázka principu — v IoT zařízeních se používají dedikované senzorové moduly.

---

### 🛠️ Zdroje a nástroje

* **MakeCode — Vstup → Teplota:** [makecode.microbit.org](https://makecode.microbit.org) → Vstup → `teplota (°C)` a `úroveň světla`
* **Projekt — meteorologická stanice:** microbit.org/projects → „Weather Station" — komplexnější verze dnešního projektu
* **Kalibrace teploměru:** Empiricky zjistěte offset (naměřená − skutečná teplota) a odečtěte ho ve vzorci
* **Rozšíření — external senzory:** DHT11/DHT22 teplotní a vlhkostní senzor, připojitelný přes piny
* **Video (CZ):** YouTube — „Micro:bit teploměr projekt česky"

---

> 💡 **Tip pro učitele:**
> Přesnost teploměru závisí na konkrétním kusu Micro:bitu a prostředí — nevadí, pokud se žáci ptají, proč se liší od fyzického teploměru. To je cenná vědecká diskuse o přesnosti měřicích přístrojů a kalibraci. Pokud máte přístup k DHT11 senzoru (cena cca 30 Kč), lze hodinu rozšířit na přesné měření vlhkosti — velmi vhodné pro propojení s přírodovědou.

> 💬 **Tip pro pátek:** Měření teploty ve třídě vs. na chodbě: žáci přirozeně diskutují o rozdílech a přesnosti — skvělá propojení s fyzikálním měřením a přesností přístrojů.
