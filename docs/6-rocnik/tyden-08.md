---
grade: 6
week: 8
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-005
    text: "Po přečtení jednotlivých kroků algoritmu vysvětlí celý postup a určí problém, který je daným algoritmem řešen."
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - Žák zapíše přesnou sekvenci příkazů pro navigaci robota přes překážkový terén
  - "Žák odladí program, když robot neskončí tam, kde má (debugging)"
  - Žák ovládá Ozobota pomocí barevných kódů nakreslených na papíře
  - "Žák pochopí, že i malá nepřesnost v instrukci způsobí špatný výsledek"
time_budget:
  - type: board
    minutes: 25
  - type: pc
    minutes: 10
friday_tip: "Páteční hodiny s roboty bývají hlučné a nadšené. Využijte to pro **\"Robotí závody\"**. Vytvořte na zemi velký labyrint z lepicí pásky a nechte skupiny soutěžit, čí Ozobot projde trasu nejrychleji s využitím \"turbo\" kódů. Motivuje to žáky k preciznímu kreslení a rychlému ladění chyb."
---

# 

## 💡 Metodický postup

### 1. Úvod: Roboti v praxi (5 min)

Učitel ukáže krátký klip nebo obrázky reálných robotů (Amazon warehouse robot, chirurgický robot, Curiosity na Marsu). Otázka: „Co mají všichni společného?"

Odpověď: Všichni dostávají přesné instrukce — nemohou improvizovat.

### 2. Aktivita: Ozobot — barevné kódy

<span class="act board">🖊️ Tabule — 25 min</span>

Učitel rozdá bílé papíry a fixy. Žáci nakreslí dráhu pro Ozobota a používají barevné kódy pro příkazy.

**Základní Ozobot barevné kódy:**
- `Červená-Zelená-Červená` = Zastav
- `Červená-Červená-Modrá` = Zrychli
- `Zelená-Modrá-Zelená` = Zpomal
- `Modrá-Červená-Modrá` = Točit se

Úkoly (postupně od nejjednodušší):
1. Nakreslete přímou dráhu s jedním zatáčením vlevo
2. Přidejte příkaz „zrychli" uprostřed dráhy
3. Nakreslete dráhu ve tvaru čtverce — Ozobot musí projít celý obvod

#### Pokud není k dispozici Ozobot

Alternativa — žák hraje robota. Jeden žák zavře oči, druhý mu dává příkazy slovně (krok vpřed, otočit vlevo 90°, krok vpřed...) pro průchod labyrintem z lavic.

### 3. Aktivita: Ozobot v digitálním prostředí

<span class="act pc">💻 PC — 10 min</span>

<div class="zadani-pc">

Otevři [OzoBlockly editor](https://ozoblockly.com) a naprogramuj sekvenci pohybů v blokovém prostředí.

**Úkol:** Naprogramuj Ozobota tak, aby nakreslil čtverec (4× „pohyb vpřed + otočení o 90°").

</div>

### 4. Shrnutí (5 min)

Diskuse:
- Co bylo nejtěžší na psaní instrukcí?
- Kdy se váš robot choval jinak, než jste čekali? Proč?

**Propojení s minulou hodinou:** Algoritmus z týdne 07 teď vidíme v praxi — instrukce musí být přesné, jinak robot selže.

## 📂 Podklady

- **Ozobot barevné kódy:** [ozobot.com/app-and-color-codes](https://ozobot.com/stem-education/color-codes) — kompletní přehled kódů ke stažení (PDF)
- **Ozobot online editor:** [ozoblockly.com](https://ozoblockly.com) — blokový programovací editor pro Ozobota
- **Alternativní aktivita:** [Code.org — Labyrint](https://studio.code.org/s/course1) — online labyrint pro programování bez robota (nastavte jazyk „Čeština" v menu vpravo nahoře)
- **Video — Ozobot tutorial (CZ):** Na YouTube vyhledejte „Ozobot návod" nebo „Ozobot tutorial česky" — existují české i slovenské návody
- **Pracovní listy:** Vytiskněte šablony drah pro Ozobota — jednoduchý labyrint a čtvercová dráha

!!! tip "Tip pro učitele"
    Ozobot funguje nejlépe na hladkém bílém papíře s tlustšími fixy. Tenké čáry nebo šedý papír robot nečte spolehlivě. Každá skupina by měla mít vlastního robota — sdílení zpomaluje hodinu. Pokud máte jen 2–3 Ozoboty, pracujte ve skupinách po 3–4.
