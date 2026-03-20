"""
MkDocs hook: Automaticky vloží hlavičku hodiny z YAML front matter.

Každý soubor tyden-*.md nemusí obsahovat žádné HTML pro lesson-meta, RVP sekci,
time-budget bar, goals nebo friday-tip — vše se vyrenderuje z front matter.

Minimální front matter pro hodinu:
---
grade: 6
week: 1
time: 45
area: Oblast RVP
rvp_codes:
  - code: INF-INF-004-ZV9-013
    text: "Žák navrhne..."
goals:
  - "Žák **zná** pravidla..."
time_budget:
  - type: board
    minutes: 10
  - type: pc
    minutes: 20
friday_tip: "Tip pro pátek..."   # nepovinné
---
"""

import re

# Barvy a popisky pro typy aktivit
SEG_COLORS = {
    'pc':         '#1976d2',
    'unplugged':  '#388e3c',
    'discussion': '#7b1fa2',
    'board':      '#f57c00',
    'review':     '#880e4f',
}
SEG_LABELS = {
    'pc':         'PC',
    'unplugged':  'Bez počítače',
    'discussion': 'Diskuse',
    'board':      'Tabule/výuka',
    'review':     'Reflexe',
}


def _md_bold(text: str) -> str:
    """Převede **text** na <strong>text</strong> pro použití v HTML blocích."""
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)


def _time_label(minutes: int) -> str:
    hours = minutes // 45
    if hours <= 1:
        return f"1 hod = {minutes} min"
    return f"{hours} hod = {minutes} min"


def generate_lesson_html(meta: dict) -> str:
    """Vygeneruje kompletní HTML hlavičku hodiny z front matter metadat."""
    parts = []

    # ── Lesson meta header ──────────────────────────────────────────────────
    grade = meta.get('grade')
    week = meta.get('week')
    time = meta.get('time', 45)
    area = meta.get('area', '')

    if grade:
        time_lbl = _time_label(int(time))
        parts.append(
            f'<div class="lesson-meta">\n'
            f'  <span class="lm-badge lm-grade">📚 {grade}. ročník</span>\n'
            f'  <span class="lm-badge lm-week">📅 Týden {week}</span>\n'
            f'  <span class="lm-badge lm-time">⏱️ {time_lbl}</span>\n'
            + (f'  <span class="lm-badge lm-area">🗂️ Oblast: {area}</span>\n' if area else '')
            + '</div>'
        )

    # ── RVP sekce ───────────────────────────────────────────────────────────
    rvp_codes = meta.get('rvp_codes', [])
    if rvp_codes:
        rvp_items = []
        for entry in rvp_codes:
            code = entry.get('code', '')
            text = entry.get('text', '')
            rvp_items.append(
                f'<span class="rvp-tag">'
                f'<span class="rvp-code">{code}</span>'
                f'<span class="rvp-desc">{text}</span>'
                f'</span>'
            )
        parts.append(
            '## 📋 Vazba na RVP ZV\n\n' + '\n'.join(rvp_items)
        )
        parts.append('---')

    # ── Tip pro pátek (nepovinné) ───────────────────────────────────────────
    # markdown="1" zajistí zpracování **bold** a dalšího markdownu uvnitř divu
    friday_tip = meta.get('friday_tip', '')
    if friday_tip:
        parts.append(
            f'<div class="friday-tip" markdown="1">\n'
            f'<span class="friday-tip-label">💬 Tip pro pátek</span>\n\n'
            f'{friday_tip}\n\n'
            f'</div>'
        )

    # ── Cíle hodiny ─────────────────────────────────────────────────────────
    # markdown="1" zajistí zpracování **bold** a odrážkového seznamu
    goals = meta.get('goals', [])
    if goals:
        goal_items = '\n'.join(f'- {g}' for g in goals)
        parts.append(
            f'<div class="goals" markdown="1">\n'
            f'<div class="goals-title">🎯 Cíle hodiny</div>\n\n'
            f'{goal_items}\n\n'
            f'</div>'
        )

    # ── Time budget bar ─────────────────────────────────────────────────────
    time_budget = meta.get('time_budget', [])
    if time_budget:
        total = sum(int(s.get('minutes', 0)) for s in time_budget)
        if total > 0:
            segments_html = ''
            legend_html = ''
            seen_types = []
            for seg in time_budget:
                seg_type = seg.get('type', 'board')
                seg_min = int(seg.get('minutes', 0))
                pct = round(seg_min / total * 100)
                segments_html += (
                    f'    <div class="time-segment seg-{seg_type}" style="width: {pct}%">'
                    f'{seg_min} min</div>\n'
                )
                if seg_type not in seen_types:
                    seen_types.append(seg_type)
                    color = SEG_COLORS.get(seg_type, '#888')
                    label = SEG_LABELS.get(seg_type, seg_type)
                    legend_html += (
                        f'    <span class="time-legend-item">'
                        f'<span class="time-legend-dot" style="background:{color}"></span>'
                        f' {label}</span>\n'
                    )
            parts.append(
                f'<div class="time-budget">\n'
                f'  <div class="time-budget-title">⏱️ Rozložení {total} minut</div>\n'
                f'  <div class="time-budget-bar">\n'
                f'{segments_html}'
                f'  </div>\n'
                f'  <div class="time-legend">\n'
                f'{legend_html}'
                f'  </div>\n'
                f'</div>'
            )

    if parts:
        parts.append('---')

    return '\n\n'.join(parts)


def on_page_markdown(markdown, page, **kwargs):
    """Hook: vloží HTML hlavičku hodiny do markdown obsahu za h1 nadpis."""
    # Zpracovávat pouze stránky tyden-*.md
    src = page.file.src_path.replace('\\', '/')
    if not re.search(r'\d+-rocnik/tyden-\d+', src):
        return markdown

    meta = page.meta
    if not meta.get('grade'):
        return markdown

    lesson_html = generate_lesson_html(meta)
    if not lesson_html:
        return markdown

    # Vložit za první h1 nadpis
    lines = markdown.split('\n')
    insert_idx = 1  # fallback: za první řádek
    for i, line in enumerate(lines):
        if line.startswith('# '):
            insert_idx = i + 1
            break

    result = lines[:insert_idx] + ['', lesson_html, ''] + lines[insert_idx:]
    output = '\n'.join(result)

    # Přidej markdown="1" ke všem custom divům, které ještě nemají
    # (opravuje soubory migr. před tímto patchem nebo ručně vytvořené)
    output = re.sub(
        r'<div class="(resources|goals|friday-tip)"(?!\s+markdown)',
        r'<div class="\1" markdown="1"',
        output,
    )
    return output
