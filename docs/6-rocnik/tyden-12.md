---
grade: 6
week: 12
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-005
    text: "Po přečtení jednotlivých kroků algoritmu vysvětlí celý postup a určí problém, který je daným algoritmem řešen."
  - code: INF-INF-003-ZV9-010
    text: Pro řešení problému vytvoří tabulku evidence dat a stanoví pravidla pro práci se záznamy.
goals:
  - Žák přidá do Scratch projektu zvuk ze knihovny nebo nahraje vlastní
  - "Žák použije bloky `řekni` a `přemýšlej` pro vytvoření bublin s textem"
  - Žák synchronizuje zvuk s pohybem nebo změnou kostýmu
  - Žák vytvoří krátký příběh pomocí sekvence zvuků a bublinových dialogů
time_budget:
  - type: pc
    minutes: 10
  - type: pc
    minutes: 20
friday_tip: "Pátky jsou ideální pro **\"Dabingové studio\"**. Pokud mají žáci k dispozici mikrofony (nebo stačí i jeden u učitele), nechte je nahrát legrační věty pro jejich postavičky. Práce s vlastním hlasem v 6. třídě spolehlivě zvedne energii v hodině a žáci se naučí pracovat s editorem zvuku (oříznutí ticha, zrychlení/zpomalení hlasu), což je skvělý bonus k programování."
---

# 

## 💡 Metodický postup

### 1. Úvod: Němý film vs. film se zvukem (5 min)

Učitel ukáže žákům svůj projekt z minulé hodiny (tančící sprite) — nejprve bez zvuku, pak se zvukem. Otázka: „Jaký je rozdíl? Co zvuk přidává?"

Diskuse o tom, jak zvuk doplňuje vizuální obsah — jako v animovaném filmu.

### 2. Průzkum zvuků a bublin

<span class="act pc">💻 PC — 10 min</span>

Učitel na tabuli ukáže:

**Zvuky:**
- Záložka **Zvuky** u spritu → Vyber zvuk (ikona reproduktoru)
- Blok `přehraj zvuk [meow] dokud neskončí`
- Blok `nastav hlasitost na [50]%`

**Bubliny:**
- Z palety **Vzhled**: `řekni [Ahoj!] po dobu [2] sekund` → bílá bublina s textem
- `přemýšlej [Hmm...] po dobu [2] sekund` → oblačná bublina

Žáci si 5 minut hrají sami — prozkoumají možnosti.

### 3. Aktivita: Zpívající zvíře

<span class="act pc">💻 PC — 20 min</span>

Žáci vytvoří projekt „Zpívající zvíře" — krátký příběh se zvuky a dialogy:

**Struktura příběhu (3 scény):**
```
Scéna 1:
  Po kliknutí na vlajku:
    řekni [Ahoj! Já jsem Kocour Pepa.] 2s
    přehraj zvuk [meow] dokud neskončí

Scéna 2:
  přejdi na pozici [-100, 0]
  přemýšlej [Co budu dneska dělat?] 2s
  změň kostým na [další]

Scéna 3:
  pohni se o 50 kroků
  řekni [Jdu na procházku! Čau!] 2s
  přehraj zvuk [pop] dokud neskončí
```

**Volné téma:** Žáci si vymyslí vlastní příběh — zvíře, robot, hvězda...

### 4. Prezentace a reflexe (5 min)

2–3 žáci sdílí svůj projekt na tabuli. Třída hodnotí:
- Sedí zvuk k situaci?
- Rozumíme příběhu bez dalšího vysvětlení?

**Klíčové pojmy:** zvuková knihovna, `řekni`, `přemýšlej`, synchronizace

## 📂 Podklady

- **Scratch zvuková knihovna:** Zabudovaná v editoru — kategorie: Zvířata, Efekty, Hudba, Příroda atd.
- **Freesound.org:** [freesound.org](https://freesound.org) — volné zvuky ke stažení (nutná registrace), lze nahrát jako vlastní zvuk do Scratche
- **Scratch — nahrávání hlasu:** V záložce Zvuky klikněte na mikrofon → žáci mohou nahrát vlastní hlas
- **Scratch Activity Card — „Add a Soundtrack":** [scratch.mit.edu/ideas](https://scratch.mit.edu/ideas) → karta č. 5
- **Rozšíření:** Přidejte změnu pozadí (backdrop) při přechodu mezi scénami — základ budoucí story animace

!!! tip "Tip pro učitele"
    Nahrávání vlastního hlasu je pro žáky velmi motivující — jsou nadšení, když slyší svůj hlas z postavičky. Upozorněte na pravidla netikety — nenahrávat spolužáky bez svolení. Pokud nemáte mikrofony, použijte vestavěnou zvukovou knihovnu Scratche.
