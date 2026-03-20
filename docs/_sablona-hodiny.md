---
grade: X          # číslo ročníku (6, 7, 8, nebo 9)
week: XX          # číslo týdne (1–32)
time: 45          # délka hodiny v minutách (45 nebo 90)
area: NÁZEV OBLASTI RVP   # např. "Algoritmizace a programování"
rvp_codes:
  - code: INF-INF-XXX-ZV9-YYY
    text: "Přesné znění výstupu z docs/data/rvp.yml"
  # - code: INF-INF-XXX-ZV9-YYY    # druhý výstup (pokud je)
  #   text: "Druhý výstup"
goals:
  - "Žák **[sloveso]** ..."
  - "Žák **[sloveso]** ..."
  - "Žák **[sloveso]** ..."
time_budget:
  # Typy: pc | unplugged | discussion | board | review
  # Součet minut by měl odpovídat hodnotě time výše
  - type: board
    minutes: 10
  - type: pc
    minutes: 20
  - type: discussion
    minutes: 10
  - type: review
    minutes: 5
friday_tip: "Alternativní aktivita pro pátek nebo línou hodinu..."   # NEPOVINNÉ — smazat řádek pokud není
---

# NÁZEV HODINY
<!-- Nadpis = téma týdne. Stručně a výstižně. -->

<!-- ══════════════════════════════════════════════════════
     Vše výše (lesson-meta, RVP sekce, cíle, time-budget)
     se vyrenderuje automaticky z front matter výše.
     Tady začíná obsah hodiny — pouze metodika.
     ══════════════════════════════════════════════════════ -->

## 💡 Metodický postup

<!-- ──────────────────────────────────────────────────────
     AKTIVITA 1
     Nadpis: ### číslo. Název aktivity
     Za nadpisem hned štítek s typem a délkou:
       <span class="act TŘÍDA">EMOJI Typ — X min</span>
     Typy: pc, unplugged, discussion, board, review
     ────────────────────────────────────────────────────── -->
### 1. Název první aktivity

<span class="act board">🖊️ Tabule — 10 min</span>

Popis aktivity. Co dělá učitel, co dělají žáci.

- Krok 1
- Krok 2
- Krok 3

---

### 2. Název druhé aktivity

<span class="act pc">💻 PC — 20 min</span>

Popis aktivity. Postup práce na počítači.

---

### 3. Název třetí aktivity

<span class="act discussion">💬 Diskuse — 10 min</span>

Popis aktivity nebo reflexní otázky.

---

### 4. Závěrečná reflexe

<span class="act review">🔍 Reflexe — 5 min</span>

- Otázka k reflexi 1?
- Otázka k reflexi 2?

---

<!-- ══════════════════════════════════════════════════════
     ZDROJE A PODKLADY
     Přidej odkazy na materiály, weby, videa, nástroje.
     ══════════════════════════════════════════════════════ -->
<div class="resources">
  <div class="resources-title">📂 Zdroje a podklady</div>

  - **Název zdroje (CZ):** [odkaz.cz](https://odkaz.cz) — krátký popis
  - **Nástroj:** [nastroj.com](https://nastroj.com) — k čemu slouží
  - **Pracovní list:** Připrav... (popis, co si učitel vytiskne/připraví)

</div>

<!-- ══════════════════════════════════════════════════════
     TIP PRO UČITELE
     Praktická rada, upozornění nebo alternativa.
     Zobrazí se jako zelený info box.
     ══════════════════════════════════════════════════════ -->
!!! tip "Tip pro učitele"
    Konkrétní rada pro realizaci hodiny: co si připravit, na co si dát pozor, jak reagovat na problémy.
