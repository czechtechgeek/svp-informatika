---
grade: 7
week: 5
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - "Žák bez nápovědy sestaví program využívající pohyb, události, cykly a zvuky"
  - "Žák identifikuje kategorii bloků v paletě a ví, k čemu každá kategorie slouží"
  - "Žák opraví chybný program (debugging) pomocí logické analýzy, ne náhodného klikání"
  - "Žák připraví scénu pro nadcházející témata (podmínky, proměnné)"
time_budget:
  - type: unplugged
    minutes: 8
  - type: board
    minutes: 10
  - type: pc
    minutes: 20
friday_tip: "Scratch nejlépe funguje jako volná tvorba — dejte žákům 10 min na konci hodiny bez zadání: „Udělejte v Scratch cokoliv, na co máte chuť.\" Výsledky jsou vždy překvapivé a odhalí, co žáky skutečně zajímá."
---

# Scratch V: Opakování bloků

## 💡 Metodický postup

### 1. Rozcvička: Bingo kategorií

<span class="act unplugged">✋ Bez počítače — 8 min</span>

Každý žák dostane kartičku bingo (3×3 nebo 4×4) s názvy bloků (např. `pohni se`, `přehraj zvuk`, `opakuj`, `když stisknuta klávesa`, `nastav x`, `čekej`, `řekni`, `změň kostým`).

Učitel popisuje, co blok dělá — žáci škrtají na kartičce. Kdo má celou řadu, volá „Scratch!".

Cíl: rychlá diagnostika paměti z minulého roku, zábavnou formou.

### 2. Opakování bloků: Rychlé demo

<span class="act board">🖊️ Tabule — 10 min</span>

Učitel otevře Scratch na projektoru a projde skupiny bloků:

| Skupina | Barva | Příklady |
|---------|-------|---------|
| Pohyb | Modrá | pohni se, nastav x, otočení |
| Vzhled | Fialová | řekni, změň kostým, ukaž/skryj |
| Zvuk | Růžová | přehraj zvuk, zastav zvuky |
| Události | Žlutá | po kliknutí na vlajku, stisknuta klávesa |
| Řízení | Oranžová | opakuj, čekej, pokud... pak |
| Snímání | Světle modrá | dotýkám se, vzdálenost od |

U každé skupiny žáci navrhnou, k čemu ji použijí v herním projektu.

### 3. Kódovací výzvy

<span class="act pc">💻 PC — 20 min</span>

<div class="zadani-pc" markdown="1">

Pracuj individuálně. Splň alespoň dvě ze tří výzev:

**Výzva 1 — Lehká:** Animovaný pozdrav
- Sprite přijde z levého okraje
- Řekne „Vítej v 7. třídě!" po dobu 2 sekund
- Odejde na pravý okraj
- Přehraje zvuk při příchodu

**Výzva 2 — Střední:** Tančící postavička
- Sprite střídá kostýmy (tanec) v cyklu
- Hudba hraje na pozadí
- Stisknutím mezerníku se zastaví/spustí

**Výzva 3 — Těžká:** Odraz od stěn
- Sprite se pohybuje konstantní rychlostí
- Po nárazu na okraj se odrazí (blok `odraz od okraje`)
- Stopa zanechávána pohybem (pero)

Hotový projekt ulož do svého Scratch účtu s názvem „7rocnik-rozcvicka".

</div>

### 4. Sdílení a reflexe (7 min)

Jeden žák z každé výzvy ukáže výsledek na projektoru. Třída identifikuje:
- Které bloky jsou použity?
- Co by přidal/a, aby byl program zajímavější?

Učitel oznamuje: „Příští hodinu přidáme podmínky — a vaše postavičky budou reagovat na okolí."

## 📂 Podklady

- **Scratch:** [scratch.mit.edu](https://scratch.mit.edu) — žáci se přihlásí existujícím účtem
- **Scratch referenční karta (CZ):** Hledejte „Scratch karta bloků CZ" — PDF s přehledem všech bloků ke stažení
- **Scratch tutoriály:** [scratch.mit.edu/ideas](https://scratch.mit.edu/ideas) — oficiální průvodci, mnoho jich má CZ lokalizaci
- **Debugging tipy:** Pokud program nefunguje — zkontrolujte: Je vlajka zelená? Jsou bloky propojeny? Je sprite ve správné poloze?

!!! tip "Tip pro učitele"
    Výzva 3 (odraz) je záměrně připravena pro týden 6, kde probereme podmínky — blok `odraz od okraje` je zjednodušení, které Scratch dělá za nás. Silnější žáci se mohou zeptat, jak to funguje „uvnitř" — je to dobrá příležitost k preview podmínek. Pokud někteří žáci nemají Scratch účet, využijte režim „bez přihlášení" a projekty uložte jako soubory .sb3.
