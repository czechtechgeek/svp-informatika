# Příkazy pro robota: Přesnost instrukcí

## 🎯 Cíle hodiny

- Žák zapíše přesnou sekvenci příkazů pro navigaci robota přes překážkový terén
- Žák odladí program, když robot neskončí tam, kde má (debugging)
- Žák ovládá Ozobota pomocí barevných kódů nakreslených na papíře
- Žák pochopí, že i malá nepřesnost v instrukci způsobí špatný výsledek

## 🎯 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-03" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-03</span><span style="color: #374151;">Žák zapíše algoritmus v programovacím jazyce</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-3-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-3-01</span><span style="color: #374151;">Žák vysvětlí princip fungování technologií</span></div>

## 💡 Metodický tip pro pátky
Páteční hodiny s roboty bývají hlučné a nadšené. Využijte to pro **"Robotí závody"**. Vytvořte na zemi velký labyrint z lepicí pásky a nechte skupiny soutěžit, čí Ozobot projde trasu nejrychleji s využitím "turbo" kódů. Motivuje to žáky k preciznímu kreslení a rychlému ladění chyb.

## 💡 Metodický postup

### 1. Úvod: Roboti v praxi (5 min)

Učitel ukáže krátký klip nebo obrázky reálných robotů (Amazon warehouse robot, chirurgický robot, Curiosity na Marsu). Otázka: „Co mají všichni společného?"

Odpověď: Všichni dostávají přesné instrukce — nemohou improvizovat.

### 2. Aktivita: Ozobot — barevné kódy (25 min) — Ozobot + papír

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

**Pokud není k dispozici Ozobot:**
Alternativa — žák hraje robota. Jeden žák zavře oči, druhý mu dává příkazy slovně (krok vpřed, otočit vlevo 90°, krok vpřed...) pro průchod labyrintem z lavic.

### 3. Aktivita: Ozobot v digitálním prostředí (10 min) — PC

Žáci otevřou [OzoBlockly editor](https://ozoblockly.com) a naprogramují sekvenci pohybů v blokovém prostředí.

Úkol: Naprogramujte Ozobota tak, aby nakreslil čtverec (4× „pohyb vpřed + otočení o 90°").

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

