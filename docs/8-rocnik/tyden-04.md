---
grade: 8
week: 4
time: 45
area: "Data, informace a modelování"
rvp_codes:
  - code: INF-INF-001-ZV9-002
    text: Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.
goals:
  - "**Rozlišuje** základní typy grafů a jejich účel."
  - "**Zvolí** správnou vizualizaci pro konkrétní datovou sadu."
  - "**Vytvoří** v tabulkovém procesoru grafy včetně popisků a legendy."
  - "**Kriticky posoudí**, zda graf předává informaci srozumitelně."
time_budget:
  - type: discussion
    minutes: 10
  - type: board
    minutes: 10
  - type: board
    minutes: 18
  - type: pc
    minutes: 7
---

# Vizualizace: Který graf pro jaká data?

## 💡 Metodický postup

### 1. Rychlý přehled: Kdy co použít?

<span class="act discussion">💬 Diskuse — 10 min</span>

| Typ grafu | Hlavní účel | Příklad z praxe |
| :--- | :--- | :--- |
| **Sloupcový / Pruhový** | Porovnání kategorií | Prodeje podle měsíců |
| **Spojnicový** | Vývoj v čase (trendy) | Teploty v průběhu roku |
| **Výsečový (Koláč)** | Podíly z celku (max 5-6) | Rozdělení rozpočtu |
| **Bodový (Scatter)** | Vztah dvou proměnných | Výška vs. Váha |
| **Teplotní mapa** | Intenzita v mřížce | Aktivita uživatelů v týdnu |

**⚠️ Zlatá pravidla:**
* **Koláč:** Nikdy pro časový vývoj!
* **Spojnice:** Pouze pokud má osa X logické pořadí (čas, posloupnost).
* **Pruhy:** Lepší než sloupce, pokud máte více než 6 kategorií nebo dlouhé názvy.

---

### 2. Aktivita: „Najdi správný graf“

<span class="act board">🖊️ Tabule — 10 min</span>

* **Doprava do školy** (autobus / auto / pěšky) $\rightarrow$ **Koláčový**
* **Průměrná teplota** každý měsíc $\rightarrow$ **Spojnicový**
* **Přečtené knihy** (porovnání tříd) $\rightarrow$ **Sloupcový**
* **Spánek vs. známky** $\rightarrow$ **Bodový**

---

### 3. Praktická tvorba na PC

<span class="act board">🖊️ Tabule — 18 min</span>

<div class="zadani-pc" markdown="1">

**Dataset A — Sloupcový graf**
* *Data:* Návštěvnost jídelny (Po: 312, Út: 298, St: 321, Čt: 305, Pá: 267)
* *Cíl:* Vytvořte sloupcový graf se správným měřítkem osy Y a popisky dnů

**Dataset B — Koláčový / Pruhový graf**
* *Data:* Oblíbené předměty (Informatika 38 %, TV 27 %, VV 18 %, M 17 %)
* *Cíl:* Vytvořte přehledný graf s popisky hodnotami přímo v grafu

</div>

---

### 4. Reflexe a peer-review

<span class="act pc">💻 PC — 7 min</span>

<div class="zadani-pc" markdown="1">

1.  Je zvolený typ grafu logický vzhledem k datům?
2.  Má graf název a popsané osy?
3.  Pochopím hlavní informaci do 5 sekund bez vysvětlování?

</div>

---

## 📂 Zdroje a podklady

* **Online nástroje:** [Datawrapper](https://www.datawrapper.de) (profesionální výstupy), [Flourish](https://flourish.studio) (interaktivita).
* **Inspirace:** Hledejte termín **"Chart Chooser"** pro přehledné plakáty do učebny.
* **Rozšíření:** Google Looker Studio pro tvorbu pokročilých dashboardů.

---

!!! tip "Tip pro učitele"
    Ukažte žákům reálnou infografiku z médií a nechte je hádat: *„Proč grafik vybral zrovna tento typ?“* Vizuální diskuze funguje lépe než suchá teorie.
    > ❗ **Pozor na koláče:** Žáci je milují, ale v praxi jsou často nevhodné. Ukažte jim stejná data v koláči a v pruhovém grafu vedle sebe. Sami uvidí, že v pruhu se hodnoty porovnávají mnohem přesněji.
