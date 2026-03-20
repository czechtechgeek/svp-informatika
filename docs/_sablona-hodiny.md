# NÁZEV HODINY
<!-- Nadpis = téma týdne. Stručně a výstižně. -->

<!-- ══════════════════════════════════════════════════════
     METADATA HODINY
     Zkopíruj tento blok a vyplň: ročník, číslo týdne
     a součet minut (1 vyuč. hodina = 45 min, 2 hodiny = 90 min).
     Typy aktivit v lm-area odpovídají oblastem RVP.
     ══════════════════════════════════════════════════════ -->
<div class="lesson-meta">
  <span class="lm-badge lm-grade">📚 X. ročník</span>
  <span class="lm-badge lm-week">📅 Týden XX</span>
  <span class="lm-badge lm-time">⏱️ 1 hod = 45 min</span>
  <!-- Pokud jsou 2 hodiny za sebou: -->
  <!-- <span class="lm-badge lm-time">⏱️ 2 hod = 90 min</span> -->
  <span class="lm-badge lm-area">🗂️ Oblast: NÁZEV OBLASTI RVP</span>
</div>

<!-- ══════════════════════════════════════════════════════
     VAZBA NA RVP ZV
     Uveď kódy výstupů z RVP (viz docs/data/rvp.yml a stránka RVP výstupy).
     Používej VÝHRADNĚ formát INF-INF-XXX-ZV9-YYY a přesné znění z rvp.yml.
     Nepoužívej starý formát I-9-X-XX.
     ══════════════════════════════════════════════════════ -->
## 📋 Vazba na RVP ZV

<!-- Kódy výstupů dle docs/data/rvp.yml — používejte POUZE formát INF-INF-XXX-ZV9-YYY -->
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-XXX-ZV9-YYY" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-XXX-ZV9-YYY</span><span style="color: #374151;">Přesné znění výstupu z rvp.yml</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-XXX-ZV9-YYY" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-XXX-ZV9-YYY</span><span style="color: #374151;">Druhý výstup (pokud je)</span></div>

---

<!-- ══════════════════════════════════════════════════════
     TIP PRO PÁTEK
     Krátká alternativní aktivita pro "línou" hodinu
     nebo hodinu v pátek odpoledne. Nepovinné.
     ══════════════════════════════════════════════════════ -->
<div class="friday-tip">
  <span class="friday-tip-label">💬 Tip pro pátek</span>
  Pokud je konec týdne a třída je unavená, zkuste...
  <!-- Napiš konkrétní aktivitu, hru nebo diskusi. -->
</div>

<!-- ══════════════════════════════════════════════════════
     CÍLE HODINY
     Co žák zvládne na konci hodiny?
     Pište ve tvaru "Žák [sloveso] ..."
     Doporučený počet: 3–5 cílů.
     ══════════════════════════════════════════════════════ -->
<div class="goals">
  <div class="goals-title">🎯 Cíle hodiny</div>

  - Žák **[sloveso]** ...
  - Žák **[sloveso]** ...
  - Žák **[sloveso]** ...
  <!-- Přidej nebo odeber cíle podle potřeby -->

</div>

---

<!-- ══════════════════════════════════════════════════════
     PŘEHLED ČASU — TIME BUDGET BAR
     Vizuální koláč minut. Šířka každého segmentu
     = (minuty / celkem) * 100 %

     Příklad pro 45 min:
       Aktivita 1: 10 min → width: 22.2%
       Aktivita 2: 15 min → width: 33.3%
       Aktivita 3: 15 min → width: 33.3%
       Závěr:       5 min → width: 11.1%

     Barvy tříd (act / seg):
       pc          = modrá   → práce na PC
       unplugged   = zelená  → bez počítače
       discussion  = fialová → diskuse / reflexe
       board       = oranžová→ tabule / výuka
       review      = růžová  → opakování / test
     ══════════════════════════════════════════════════════ -->
<div class="time-budget">
  <div class="time-budget-title">⏱️ Rozložení 45 minut</div>
  <div class="time-budget-bar">
    <div class="time-segment seg-board"      style="width: 22%">10 min</div>
    <div class="time-segment seg-pc"         style="width: 33%">15 min</div>
    <div class="time-segment seg-unplugged"  style="width: 33%">15 min</div>
    <div class="time-segment seg-discussion" style="width: 11%">5 min</div>
  </div>
  <div class="time-legend">
    <span class="time-legend-item"><span class="time-legend-dot" style="background:#f57c00"></span> Tabule/výuka</span>
    <span class="time-legend-item"><span class="time-legend-dot" style="background:#1976d2"></span> PC</span>
    <span class="time-legend-item"><span class="time-legend-dot" style="background:#388e3c"></span> Bez počítače</span>
    <span class="time-legend-item"><span class="time-legend-dot" style="background:#7b1fa2"></span> Diskuse</span>
  </div>
</div>

---

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

<span class="act pc">💻 PC — 15 min</span>

Popis aktivity. Postup práce na počítači.

---

### 3. Název třetí aktivity

<span class="act unplugged">✋ Bez počítače — 15 min</span>

Popis aktivity bez technologií.

---

### 4. Závěrečná reflexe

<span class="act discussion">💬 Diskuse — 5 min</span>

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
