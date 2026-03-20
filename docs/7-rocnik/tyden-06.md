---
grade: 7
week: 6
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - "Žák vysvětlí, co je podmínka v programování, a uvede příklady z reálného života"
  - "Žák použije blok `pokud... pak` ve Scratch pro reakci na dotyk okraje"
  - Žák implementuje odrážení objektu od stěn pomocí podmínek (bez spoléhání na zabudovaný blok)
  - Žák odliší stav (dotýkám se okraje?) od akce (otoč se)
time_budget:
  - type: discussion
    minutes: 7
  - type: board
    minutes: 12
  - type: pc
    minutes: 20
friday_tip: "Živá demonstrace podmínky: stoupněte si na kraj třídy a kráčejte rovně — když narazíte na zeď, otočte se. Nechejte žáky říct „podmínku\" nahlas: „POKUD narazíš na zeď, PAK se otoč.\" Fyzické prožití konceptu urychlí porozumění o 30 %."
---

# Podmínky I: Když narazíš, odraz se

## 💡 Metodický postup

### 1. Podmínky v reálném světě

<span class="act discussion">💬 Diskuse — 7 min</span>

Učitel zapíše na tabuli schéma:

```
POKUD [podmínka] PAK [akce]
```

Žáci navrhují příklady:
- „POKUD prší, PAK vezmi deštník"
- „POKUD je červená, PAK stůj"
- „POKUD je skóre > 10, PAK zobraz gratulaci"
- „POKUD je baterka < 20 %, PAK zapni šetrný režim"

Učitel zdůrazní: podmínka je vždy **otázka s odpovědí ANO nebo NE** (boolean — termín pro pokročilé).

### 2. Demo: Odraz od stěny krok za krokem

<span class="act board">🖊️ Tabule — 12 min</span>

Učitel staví program na projektoru, žáci říkají postup nahlas:

**Cíl: Sprite letí přes obrazovku, odrazí se od všech čtyř stěn.**

Krok 1 — pohyb v cyklu:
```
po kliknutí na vlajku
opakuj dokola:
  pohni se o 5 kroků
```

Krok 2 — podmínka pro okraj:
```
  pokud dotýkám se okraje? pak:
    otoč se o 180 stupňů
```

Krok 3 — náhodný úhel na startu:
```
nastav směr na (číslo 1 až 360)
```

Učitel záměrně udělá chybu (zapomene `opakuj dokola`) — žáci ji odhalí a opraví.

### 3. Kodování: Bouncing Ball s rozšířeními

<span class="act pc">💻 PC — 20 min</span>

<div class="zadani-pc">

Otevři [scratch.mit.edu](https://scratch.mit.edu) a vytvoř nový projekt. Naprogramuj sprite, který se pohybuje a odráží od stěn.

**Základní úkol (povinný):**
- Vyber si libovolný sprite
- Sprite se pohybuje a odráží od všech čtyř stěn jeviště
- Rychlost pohybu: 5–8 kroků (ne příliš rychle ani pomalu)
- Použij blok `pokud dotýkám se okraje? pak: otoč se o 180 stupňů` uvnitř cyklu `opakuj dokola`

**Přidej aspoň 2 rozšíření:**
- **A:** Při každém odrazu sprite změní barvu (blok `změň barvu o 25`)
- **B:** Při odrazu přehraje zvuk
- **C:** Přidej druhý sprite pohybující se jiným směrem — kolize způsobí výbuch (skrytí a zvuk)
- **D:** Šipkami nahoru/dolů se mění rychlost pohybu
- **E:** Počítej, kolikrát se sprite odrazil (použij proměnnou)

Svůj projekt pojmenuj a ulož. Sdílej odkaz přes Google Classroom nebo ulož do svého Scratch profilu.

</div>

### 4. Reflexe a propojení (6 min)

Žáci odpoví na kartičce (nebo ústně):
- „Podmínka je jako…"
- „Bez podmínky by se stalo…"
- „Chci příště přidat…"

Učitel oznamuje: „Příště přidáme POKUD–JINAK a složené podmínky (AND, OR)."

## 📂 Podklady

- **Scratch:** [scratch.mit.edu](https://scratch.mit.edu)
- **Scratch blok referenční přehled:** Blok `pokud... pak` je v kategorii **Řízení** (oranžová); `dotýkám se...` je v kategorii **Snímání** (světle modrá)
- **Video tutorial — podmínky ve Scratch (EN):** Hledejte „Scratch if then tutorial" na YouTube — CS Dojo nebo Griffpatch kanál
- **Inspirace — jednoduché hry:** Pong, Breakout — obě hry jsou postaveny čistě na podmínkách a odrazu
- **Rozšíření pro rychlé žáky:** Nechejte je pokusit se naprogramovat jednoduché Pong (dva hráči, míček, dvě pálky)

!!! tip "Tip pro učitele"
    Podmínky jsou první kognitivně náročný koncept v programování. Nezkoušejte ho vysvětlit abstraktně — vždy začněte konkrétním příkladem (odraz, semafor, výběr jídla). Blok `pokud... pak` ve Scratch vizuálně zobrazuje „kapsu" pro příkazy — žáci to intuitivně chápou lépe než textový kód. Pokud někdo skončí rychle, navrhněte: „Přidej druhý sprite, který se odráží v opačném směru."
