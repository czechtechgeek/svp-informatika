---
grade: 7
week: 11
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-008
    text: "Průběžně ověřuje správnost vytvářeného postupu, zkouší program, opravuje chyby, posoudí efektivitu postupu, programu."
  - code: INF-INF-001-ZV9-003
    text: "Modeluje situace různými způsoby, včetně grafů nebo obdobných schémat."
goals:
  - "Žák navrhne koncept vlastní hry včetně herní mechaniky, postav a cíle"
  - "Žák vytvoří papírový nebo digitální „game design dokument\" (GDD) ve zjednodušené formě"
  - "Žák identifikuje, které Scratch bloky bude potřebovat pro svůj návrh"
  - Žák se naučí realisticky odhadnout rozsah projektu a přizpůsobit ho dostupnému času
time_budget:
  - type: board
    minutes: 8
  - type: pc
    minutes: 30
friday_tip: "Krátké inspirační kolo: každý žák jmenuje jednu oblíbenou hru a jednu mechaniku z ní (skákání, sbírání, vyhýbání). Učitel zapisuje na tabuli. Vznikne „banka nápadů\", ze které slabší žáci mohou čerpat."
---

# Projekt Hra I: Návrh mechaniky

## 💡 Metodický postup

### 1. Úvod: Co je herní mechanika?

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel vysvětlí rozdíl:
- **Téma:** O čem hra je (vesmír, pohádka, sport)
- **Mechanika:** Co hráč dělá (skáče, střílí, sbírá, vyhýbá se, řeší puzzle)
- **Cíl:** Kdy hráč vyhraje nebo prohraje

Příklady:
| Hra | Téma | Mechanika | Cíl |
|-----|------|-----------|-----|
| Pac-Man | Bludiště | Pohyb + sbírání | Sebrat vše, nevyhnout se duchy |
| Flappy Bird | Létání | Kliknutí = skok | Projet co nejvíce překážek |
| Tetris | Puzzle | Otáčení tvarů | Vyplnit řady, nedosáhnout nahoru |

Diskuse: „Jakou mechaniku umíme ve Scratch udělat?" → Pohyb šipkami, skóre, časomíra, kolize.

### 2. Workshp: Návrh hry

<span class="act pc">💻 PC — 30 min</span>

<div class="zadani-pc" markdown="1">

Otevři **Google Docs** (nebo papír) a vyplň svůj **Game Design Dokument** pro hru, kterou budeš programovat v příštích hodinách ve Scratchi:

```
NÁZEV HRY: _______________

TÉMA: ___________________

HRÁČSKÁ POSTAVA:
  Jak vypadá: ___________
  Jak se ovládá: ________

PŘEKÁŽKY / NEPŘÁTELÉ:
  Co dělají: ____________
  Jak se pohybují: ______

CÍL HRY:
  Jak se vyhraje: _______
  Jak se prohraje: ______

PROMĚNNÉ:
  ☐ Skóre   ☐ Čas   ☐ Životy   ☐ Jiné: _____

NÁČRT SCÉNY (nakresli nebo popiš):
  [místo pro skicu nebo popis prostředí]

BLOKY SCRATCH, které budu potřebovat:
  ☐ Pohyb šipkami   ☐ Detekce kolize   ☐ Náhodná poloha
  ☐ Proměnné        ☐ Časomíra         ☐ Jiné: _____
```

⚠️ Pozor na rozsah — hra musí být hotová za 2 hodiny! Max. 3 sprity, max. 2 proměnné, 1 scéna.

Na závěr ukáže spolužákovi svůj plán a navzájem zkontrolujte, zda je hra realizovatelná.

</div>

Učitel chodí po třídě, konzultuje nápady, upozorňuje na příliš složité plány.

**Kritéria realizovatelnosti za 2 hodiny:**
- Max. 3 sprity
- Max. 2 proměnné
- 1 herní scéna
- Jasný cíl hry

### 3. Peer review (7 min)

Ve dvojicích si žáci vymění GDD a zkontrolují:
- Je jasné, jak se hra ovládá?
- Je cíl srozumitelný?
- Je to realizovatelné za 2 hodiny?

Každý napíše spolužákovi 1 konkrétní doporučení.

## 📂 Podklady

- **Šablona GDD:** Připravte tisknutelnou šablonu A4 nebo Google Docs dokument sdílený se třídou
- **Inspirace — Scratch komunita:** [scratch.mit.edu/explore/projects/games](https://scratch.mit.edu/explore/projects/games) — procházejte populární projekty pro inspiraci (ne kopírování)
- **Scratch — Starter Projects:** [scratch.mit.edu/starter-projects](https://scratch.mit.edu/starter-projects) — základní šablony pro různé herní žánry
- **Video (CZ):** Hledejte „jak navrhnout hru pro začátečníky" nebo „game design základy" — krátká videa 5–8 min

!!! tip "Tip pro učitele"
    Nejčastější problém v projektovém týdnu: přílišná ambice. Žáci chtějí vytvořit RPG s inventářem a save systémem. Jemně, ale důrazně veďte k jednoduchosti — lepší dokončená jednoduchá hra než nedokončená složitá. Připravte si ukázku jednoduché hry v Scratch (15 minut práce), která je přesto zábavná — demonstruje, že kvalita není o množství funkcí.
