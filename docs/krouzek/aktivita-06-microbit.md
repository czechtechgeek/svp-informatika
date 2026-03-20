# 6. Micro:bit — Mini počítač v prohlížeči

<div class="lesson-meta">
  <span class="lm-badge lm-grade">🎯 Kroužek</span>
  <span class="lm-badge lm-week">💻 PC aktivita</span>
  <span class="lm-badge lm-time">⏱️ 60–90 min</span>
  <span class="lm-badge lm-area">🗂️ Fyzické programování (simulátor)</span>
</div>

---

## 🎯 Co se naučíš?

- Jak funguje mini počítač Micro:bit a k čemu slouží
- Jak programovat v blokovém prostředí MakeCode
- Jak pracovat se senzory (tlačítka, akcelerometr, LED displej) — v simulátoru!

---

## 💡 Co je Micro:bit?

Micro:bit je **miniaturní počítač** velikosti vizitky. Má:

- 🟡 25 LED diod (displej 5×5)
- 🔘 2 tlačítka (A a B)
- 📐 Akcelerometr (pozná naklonění)
- 🧭 Kompas
- 📡 Bluetooth (komunikace mezi Micro:bity)

Dnes budeme Micro:bit **simulovat v prohlížeči** — takže ho nepotřebujeme fyzicky mít!

---

## 🚀 Začínáme

**Otevři prohlížeč a přejdi na:**
👉 [makecode.microbit.org](https://makecode.microbit.org)

Klikni na **Nový projekt** — žádná registrace není potřeba.

---

## 📋 Postup

### Krok 1 — Prohlídka MakeCode

| Část | Co dělá |
|------|---------|
| **Simulátor** (vlevo) | Virtuální Micro:bit — ihned vidíš výsledek |
| **Bloky** (uprostřed) | Kategorie bloků — klikni a přetahuj |
| **Pracovní plocha** (vpravo) | Tady skládáš svůj program |

Klikni na **▶ Přehrát** v simulátoru — měl by se spustit jakýkoliv program, který napíšeš.

---

### Krok 2 — Vyber si projekt

=== "😃 Animované smajlíky"
    **Cíl:** Micro:bit zobrazuje různé smajlíky při stisku tlačítek

    1. Z kategorie **Vstup** přetáhni blok **"když je stisknuto tlačítko A"**
    2. Dovnitř vlož **Základní → zobraz ikonu** — vyber šťastný smajlík 😊
    3. Přidej druhý blok **"když je stisknuto tlačítko B"**
    4. Dovnitř vlož smutný smajlík 😞
    5. Klikni na tlačítka A a B v simulátoru — funguje to?
    6. **Rozšíření:** Přidej blok **"při zatřesení"** (kategorie Vstup) — zobraz překvapený obličej nebo symbol ❗

=== "🎲 Elektronická kostka"
    **Cíl:** Zatřesení Micro:bitem zobrazí náhodné číslo 1–6

    1. Z kategorie **Vstup** přetáhni **"při zatřesení"**
    2. Dovnitř vlož **Základní → zobraz číslo**
    3. Místo pevného čísla vlož **Matematika → vybrat náhodně od 1 do 6**
    4. Výsledek by měl vypadat takto:
       ```
       při zatřesení
         zobraz číslo [vybrat náhodně od 1 do 6]
       ```
    5. V simulátoru klikni na symbol 🤝 (zatřesení) — hodí kostka!
    6. **Rozšíření:** Přidej animaci před zobrazením čísla — 3× blikni tečkou, pak zobraz výsledek

=== "🌡️ Teploměr + krokoměr"
    **Cíl:** Micro:bit sleduje teplotu a počítá kroky při pohybu

    **Teploměr:**
    1. Přidej blok **Základní → při startu** → **zobraz řetězec "Ahoj!"**
    2. Přidej **Vstup → tlačítko A** → **zobraz číslo [Vstup → teplota (°C)]**
    3. V simulátoru stiskni A — zobrazí se teplota prostředí

    **Krokoměr:**
    4. Přidej **Proměnné → vytvoř proměnnou** → pojmenuj ji `kroky`
    5. Nastav: **"při zatřesení → změň kroky o 1 → zobraz číslo [kroky]"**
    6. Klikej v simulátoru na zatřesení — kroky se počítají!
    7. Přidej tlačítko B pro reset: **"při B → nastav kroky na 0"**

---

### Krok 3 — Stáhnout nebo sdílet

- Klikni na **Stáhnout** (vpravo dole) — dostaneš soubor `.hex`
- Pokud máš fyzický Micro:bit, překopíruj ho na zařízení jako USB disk
- Nebo klikni na **Sdílet** → zkopíruj odkaz

---

## ✅ Co ukázat učiteli

- Předveď projekt v simulátoru (klikej na tlačítka / zatřesení)
- Vysvětli: **Co tvůj program dělá?** **Jaký senzor používá?**

---

## 🏆 Bonusové výzvy

1. **Kámen nůžky papír:** Při zatřesení se náhodně zobrazí kámen, nůžky nebo papír (jako ikona)
2. **Odpočítávač:** Stiskni A → začne odpočítávat 10…9…8… → zobrazí "START!"
3. **Kompas:** Kategorie **Vstup → kompas (°)** → zobraz světovou stranu (N, S, E, W) při stisku tlačítka
4. **Rádiová komunikace:** Zkus záložku **Rádio** — simulátor podporuje vysílání zpráv mezi dvěma Micro:bity v jednom prohlížeči!

---

<div class="resources" markdown="1">
<div class="resources-title">📂 Zdroje</div>

  - **MakeCode:** [makecode.microbit.org](https://makecode.microbit.org) — hlavní nástroj (Microsoft, zdarma)
  - **Micro:bit web (CZ):** [microbit.org/cs-cz](https://microbit.org/cs-cz) — oficiální stránky s projekty v češtině
  - **Projekty pro začátečníky:** [microbit.org/projects/make-it-code-it](https://microbit.org/projects/make-it-code-it/) — desítky projektů s návodem
  - **MakeCode Python:** V MakeCode lze přepnout na textový Python (záložka Python nahoře) — skvělé pro pokročilé žáky

</div>

!!! tip "Tip pro učitele"
    MakeCode simulátor je plně funkční — nepotřebujete fyzické Micro:bity. Pokud je ale máte k dispozici, stačí stáhnout .hex soubor a překopírovat na Micro:bit (připojí se jako USB disk). Doporučujeme projekt Elektronická kostka jako první — je rychlý a okamžitě přináší "wow" efekt. Rádio funkce v simulátoru umožňuje simulovat komunikaci dvou zařízení v jednom okně prohlížeče.
