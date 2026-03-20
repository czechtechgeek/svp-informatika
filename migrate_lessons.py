#!/usr/bin/env python3
"""
Migrační skript: přepíše všechny tyden-*.md soubory do nového formátu.

Každý soubor dostane YAML front matter s metadaty hodiny.
HTML bloky (lesson-meta, RVP sekce, goals, friday-tip, time-budget) se
odstraní z těla souboru — hook lesson_meta.py je vyrenderuje automaticky.

Formáty vstupních souborů:
  A – lesson-meta div + rvp-tag spans (původně správný formát)
  B – curriculumTag divs + section headers (7., 9. ročník + část 6.)
  C – markdown blockquoty + #### headers (8. ročník)

Záloha: každý soubor je před přepsáním uložen jako <file>.bak
"""

import re
import os
import glob
from pathlib import Path

# ── Konstanty ────────────────────────────────────────────────────────────────

ACT_EMOJI = {
    'pc':         '💻',
    'unplugged':  '✋',
    'discussion': '💬',
    'board':      '🖊️',
    'review':     '🔍',
}
ACT_LABEL = {
    'pc':         'PC',
    'unplugged':  'Bez počítače',
    'discussion': 'Diskuse',
    'board':      'Tabule',
    'review':     'Reflexe',
}

# ── Pomocné funkce ────────────────────────────────────────────────────────────

def detect_activity_type(hint: str) -> str:
    """Odhadne typ aktivity z textového nápovědy (z nadpisu nebo kurzívy)."""
    h = hint.lower()
    if 'bez počítače' in h or 'unplugged' in h:
        return 'unplugged'
    if re.search(r'\bpc\b', h) or 'počítač' in h:
        return 'pc'
    if 'diskus' in h or 'reflexe' in h or 'diskuze' in h:
        return 'discussion'
    if 'kvíz' in h or 'kviz' in h or 'opakování' in h or 'test' in h:
        return 'review'
    if 'tabule' in h or 'výuka' in h or 'výklad' in h:
        return 'board'
    return 'board'  # výchozí


def extract_text_from_tags(html: str, outer_class: str = None) -> str:
    """Extrahuje čistý text z HTML tagu (bez tagů)."""
    text = re.sub(r'<[^>]+>', '', html)
    return text.strip()


def strip_emoji_prefix(text: str, prefixes: list) -> str:
    """Odstraní emoji prefix a 'Oblast:' z textu oblasti."""
    for p in prefixes:
        if text.startswith(p):
            text = text[len(p):]
    return text.strip()


def yaml_str(s: str) -> str:
    """Escapuje string pro YAML (používá uvozovky pokud potřeba)."""
    s = s.strip()
    # Pokud obsahuje znaky vyžadující uvozovky
    if any(c in s for c in [':', '#', '[', ']', '{', '}', ',', '&', '*', '!', '|', '>', "'", '"', '%', '@', '`']):
        # Použij dvojité uvozovky a escapuj existující
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    return s


def make_front_matter(meta: dict) -> str:
    """Vytvoří YAML front matter string z metadat."""
    lines = ['---']
    lines.append(f'grade: {meta["grade"]}')
    lines.append(f'week: {meta["week"]}')
    lines.append(f'time: {meta.get("time", 45)}')
    if meta.get('area'):
        lines.append(f'area: {yaml_str(meta["area"])}')
    if meta.get('rvp_codes'):
        lines.append('rvp_codes:')
        for entry in meta['rvp_codes']:
            lines.append(f'  - code: {entry["code"]}')
            lines.append(f'    text: {yaml_str(entry["text"])}')
    if meta.get('goals'):
        lines.append('goals:')
        for g in meta['goals']:
            lines.append(f'  - {yaml_str(g)}')
    if meta.get('time_budget'):
        lines.append('time_budget:')
        for seg in meta['time_budget']:
            lines.append(f'  - type: {seg["type"]}')
            lines.append(f'    minutes: {seg["minutes"]}')
    if meta.get('friday_tip'):
        lines.append(f'friday_tip: {yaml_str(meta["friday_tip"])}')
    lines.append('---')
    return '\n'.join(lines)


def grade_from_path(path: str) -> int:
    """Extrahuje číslo ročníku z cesty souboru."""
    m = re.search(r'(\d+)-rocnik', path)
    return int(m.group(1)) if m else 0


def week_from_path(path: str) -> int:
    """Extrahuje číslo týdne z názvu souboru."""
    m = re.search(r'tyden-(\d+)', path)
    return int(m.group(1)) if m else 0


# ── Detekce formátu ───────────────────────────────────────────────────────────

def detect_format(content: str) -> str:
    """
    A – má <div class="lesson-meta"> → původní správný formát
    B – má curriculumTag nebo ## 📋 Vazba na RVP ZV → sekce-heading formát
    C – má > **Stav:** nebo ### 📋 Kontext → blockquote formát (8. ročník)
    """
    if '<div class="lesson-meta">' in content:
        return 'A'
    if '> **Stav:**' in content or '### 📋 Kontext' in content or '> **RVP ZV' in content or '> **Kód:**' in content:
        return 'C'
    return 'B'


# ── Parsování formátu A ───────────────────────────────────────────────────────

def parse_format_a(content: str, grade: int, week: int) -> tuple:
    """
    Parsuje soubory s <div class="lesson-meta"> a <span class="rvp-tag">.
    Vrátí (meta_dict, body_str).
    """
    meta = {'grade': grade, 'week': week, 'time': 45}

    # grade z lesson-meta
    m = re.search(r'lm-grade[^>]*>📚\s*(\d+)\.\s*ročník', content)
    if m:
        meta['grade'] = int(m.group(1))

    # week z lesson-meta
    m = re.search(r'lm-week[^>]*>📅\s*Týden\s*(\d+)', content)
    if m:
        meta['week'] = int(m.group(1))

    # time z lesson-meta (1 hod = 45 min nebo 2 hod = 90 min)
    m = re.search(r'lm-time[^>]*>⏱️\s*(\d+)\s*hod\s*=\s*(\d+)\s*min', content)
    if m:
        meta['time'] = int(m.group(2))

    # area z lesson-meta (s nebo bez "Oblast:" prefixu)
    m = re.search(r'lm-area[^>]*>🗂️\s*(?:Oblast:\s*)?([^<]+)', content)
    if m:
        meta['area'] = m.group(1).strip()

    # RVP kódy (rvp-tag formát)
    rvp_codes = []
    for m in re.finditer(
        r'<span class="rvp-tag"><span class="rvp-code">([^<]+)</span><span class="rvp-desc">([^<]+)</span></span>',
        content
    ):
        rvp_codes.append({'code': m.group(1).strip(), 'text': m.group(2).strip()})
    meta['rvp_codes'] = rvp_codes

    # friday-tip
    m = re.search(
        r'<div class="friday-tip">\s*<span class="friday-tip-label">[^<]*</span>\s*([\s\S]*?)\s*</div>',
        content
    )
    if m:
        tip = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        tip = re.sub(r'\s+', ' ', tip)
        meta['friday_tip'] = tip

    # goals
    m = re.search(
        r'<div class="goals">[\s\S]*?<div class="goals-title">[^<]*</div>([\s\S]*?)</div>',
        content
    )
    if m:
        goals_text = m.group(1)
        goals = re.findall(r'-\s+(.+)', goals_text)
        meta['goals'] = [g.strip() for g in goals if g.strip()]

    # time-budget
    time_budget = []
    tb_block = re.search(r'<div class="time-budget">([\s\S]*?)</div>\s*\n\s*---', content)
    if tb_block:
        for seg_m in re.finditer(
            r'class="time-segment seg-(\w+)"[^>]*>(\d+)\s*min',
            tb_block.group(1)
        ):
            time_budget.append({'type': seg_m.group(1), 'minutes': int(seg_m.group(2))})
    meta['time_budget'] = time_budget

    # Tělo: od ## 💡 Metodický postup dál
    body_match = re.search(r'(## 💡 Metodický postup[\s\S]*)', content)
    body = body_match.group(1).strip() if body_match else ''

    return meta, body


# ── Parsování formátu B ───────────────────────────────────────────────────────

def parse_format_b(content: str, grade: int, week: int) -> tuple:
    """
    Parsuje soubory s curriculumTag divy a section headings.
    Vrátí (meta_dict, body_str).
    """
    meta = {'grade': grade, 'week': week, 'time': 45}

    # area z - **Oblast:** text
    m = re.search(r'-\s*\*\*Oblast:\*\*\s*(.+)', content)
    if m:
        meta['area'] = m.group(1).strip()

    # RVP kódy z curriculumTag data-code + poslední span
    rvp_codes = []
    for m in re.finditer(
        r'data-code="([^"]+)"[\s\S]*?<span style="color: #374151;">([^<]+)</span>',
        content
    ):
        rvp_codes.append({'code': m.group(1).strip(), 'text': m.group(2).strip()})
    meta['rvp_codes'] = rvp_codes

    # friday-tip z ## 💬 Tip pro pátek sekce
    m = re.search(
        r'##\s+💬\s+Tip pro pátek\s*\n+([\s\S]*?)(?=\n##\s|\Z)',
        content
    )
    if m:
        tip = m.group(1).strip()
        tip = re.sub(r'\s+', ' ', tip)
        meta['friday_tip'] = tip

    # goals z ## 🎯 Cíle hodiny sekce
    m = re.search(
        r'##\s+🎯\s+Cíle hodiny\s*\n+([\s\S]*?)(?=\n##\s|\Z)',
        content
    )
    if m:
        goals_text = m.group(1)
        goals = re.findall(r'^[-*]\s+(.+)$', goals_text, re.MULTILINE)
        meta['goals'] = [g.strip() for g in goals if g.strip()]

    # time-budget z nadpisů ### N. Title (X min) — hint
    time_budget = []
    for m in re.finditer(
        r'^###\s+\d+\.\s+.+?\((\d+)\s+min\)\s*[—–-]\s*(.+)$',
        content, re.MULTILINE
    ):
        minutes = int(m.group(1))
        hint = m.group(2).strip()
        act_type = detect_activity_type(hint)
        time_budget.append({'type': act_type, 'minutes': minutes})
    meta['time_budget'] = time_budget

    # Tělo: od ## 💡 Metodický postup dál
    body_match = re.search(r'(## 💡 Metodický postup[\s\S]*)', content)
    body = body_match.group(1).strip() if body_match else ''

    # Přidej <span class="act"> badge za každý activity nadpis (pokud tam není)
    body = _add_act_badges_format_b(body)

    return meta, body


def _add_act_badges_format_b(body: str) -> str:
    """
    V těle formátu B přidá <span class="act"> badge za každý nadpis aktivity.
    Vzor: ### N. Title (X min) — hint  →  ### N. Title\n\n<span class="act TYPE">EMOJI Label — X min</span>
    """
    def replace_header(m):
        num = m.group(1)
        title = m.group(2).strip()
        minutes = int(m.group(3))
        hint = m.group(4).strip()
        act_type = detect_activity_type(hint)
        emoji = ACT_EMOJI.get(act_type, '📌')
        label = ACT_LABEL.get(act_type, hint)
        return (
            f'### {num}. {title}\n\n'
            f'<span class="act {act_type}">{emoji} {label} — {minutes} min</span>'
        )

    pattern = r'^(###\s+(\d+)\.\s+)(.+?)\s*\((\d+)\s+min\)\s*[—–-]\s*(.+)$'

    def replacer(m):
        prefix = m.group(1)
        title = m.group(3).strip()
        minutes = int(m.group(4))
        hint = m.group(5).strip()
        num_m = re.match(r'###\s+(\d+)\.\s+', prefix)
        num = num_m.group(1) if num_m else '?'
        act_type = detect_activity_type(hint)
        emoji = ACT_EMOJI.get(act_type, '📌')
        label = ACT_LABEL.get(act_type, hint)
        return (
            f'### {num}. {title}\n\n'
            f'<span class="act {act_type}">{emoji} {label} — {minutes} min</span>'
        )

    return re.sub(
        r'^(###\s+(\d+)\.\s+)(.+?)\s*\((\d+)\s+min\)\s*[—–-]\s*(.+)$',
        replacer,
        body,
        flags=re.MULTILINE
    )


# ── Parsování formátu C ───────────────────────────────────────────────────────

def parse_format_c(content: str, grade: int, week: int) -> tuple:
    """
    Parsuje soubory 8. ročníku s blockquote formátem.
    Vrátí (meta_dict, body_str).
    """
    meta = {'grade': grade, 'week': week, 'time': 45}

    # area z > **RVP ZV (Informatika):** Oblast
    m = re.search(r'>\s*\*\*RVP ZV[^:]*:\*\*\s*(.+)', content)
    if m:
        meta['area'] = m.group(1).strip()

    # RVP kódy z > **Kód:** `CODE` – text
    rvp_codes = []
    for m in re.finditer(r'>\s*\*\*Kód:\*\*\s*`([^`]+)`\s*[–-]\s*\*?([^*\n]+)\*?', content):
        text = m.group(2).strip().strip('*').strip()
        rvp_codes.append({'code': m.group(1).strip(), 'text': text})
    meta['rvp_codes'] = rvp_codes

    # friday-tip z > 💬 **Tip pro pátek:** text
    m = re.search(r'>\s*💬\s*\*\*Tip pro pátek[:\*]*\*?\*?\s*([^\n]+)', content)
    if m:
        tip = m.group(1).strip().strip('*').strip(':').strip()
        meta['friday_tip'] = tip

    # goals z **Po hodině žák:** bullet list
    m = re.search(
        r'\*\*Po hodině žák:\*\*\s*\n([\s\S]*?)(?=\n---|\n###|\n##|\Z)',
        content
    )
    if m:
        goals_text = m.group(1)
        goals = re.findall(r'^[*-]\s+(.+)$', goals_text, re.MULTILINE)
        meta['goals'] = [g.strip() for g in goals if g.strip()]

    # time z ### 💡 Metodický postup (X min) nadpisu
    m = re.search(r'###\s+💡\s+Metodický postup\s*\((\d+)\s*min\)', content)
    if m:
        meta['time'] = int(m.group(1))

    # time-budget z #### N. Title (X min) + *hint* na dalším řádku
    time_budget = []
    lines = content.split('\n')
    for i, line in enumerate(lines):
        m = re.match(r'^####\s+\d+\.\s+.+?\((\d+)\s+min\)', line)
        if m:
            minutes = int(m.group(1))
            # Hledáme type hint na dalším neprázdném řádku (italic)
            hint = 'board'
            for j in range(i + 1, min(i + 4, len(lines))):
                next_line = lines[j].strip()
                if next_line:
                    # Zkusíme parsovat kurzívu *hint*
                    hint_m = re.match(r'^\*([^*]+)\*\.?$', next_line)
                    if hint_m:
                        hint = hint_m.group(1)
                    break
            act_type = detect_activity_type(hint)
            time_budget.append({'type': act_type, 'minutes': minutes})
    meta['time_budget'] = time_budget

    # Tělo: od ### 💡 Metodický postup dál, přejmenuj na ## 💡
    body_match = re.search(r'(###\s+💡\s+Metodický postup[\s\S]*)', content)
    if not body_match:
        body_match = re.search(r'(## 💡 Metodický postup[\s\S]*)', content)
    body = body_match.group(1).strip() if body_match else ''

    # Normalizuj tělo formátu C
    body = _normalize_format_c_body(body)

    return meta, body


def _normalize_format_c_body(body: str) -> str:
    """Normalizuje tělo formátu C na standardní formát."""

    # ### 💡 Metodický postup (X min) → ## 💡 Metodický postup
    body = re.sub(
        r'^###\s+(💡\s+Metodický postup).*$',
        r'## \1',
        body, flags=re.MULTILINE
    )

    # ### 🛠️ Zdroje a nástroje → ## 📂 Zdroje a podklady (standard)
    body = re.sub(
        r'^###\s+🛠️\s+Zdroje a nástroje',
        '## 📂 Zdroje a podklady',
        body, flags=re.MULTILINE
    )

    # #### N. Title (X min) + *hint* → ### N. Title + <span class="act">
    body = _add_act_badges_format_c(body)

    # > 💡 **Tip pro učitele:**\n> text → !!! tip "Tip pro učitele"\n    text
    body = re.sub(
        r'>\s*💡\s*\*\*Tip pro učitele[:\*]*\*?\*?\s*\n((?:>.*\n?)*)',
        _convert_tip_block,
        body
    )

    # Odstraň > 💬 **Tip pro pátek:** (je v front matter)
    body = re.sub(r'\n>\s*💬\s*\*\*Tip pro pátek[^*]*\*+[^\n]*', '', body)

    # Odstraň inline tip pro pátek na konci
    body = re.sub(r'\n>\s*💬[^\n]*Tip pro pátek[^\n]*', '', body)

    # Odstraň zbývající blockquote tipy pro učitele (alternativní formát)
    body = re.sub(
        r'\n>\s*💡\s*\*\*Tip pro učitele[^\n]*\n((?:>[^\n]*\n)*)',
        _convert_tip_fallback,
        body
    )

    return body.strip()


def _convert_tip_block(m):
    """Převede > 💡 **Tip pro učitele:** blockquote na !!! tip admonition."""
    lines_raw = m.group(1)
    tip_lines = re.findall(r'^>\s?(.*)$', lines_raw, re.MULTILINE)
    indented = '\n'.join(f'    {l}' for l in tip_lines)
    return f'!!! tip "Tip pro učitele"\n{indented}\n'


def _convert_tip_fallback(m):
    """Alternativní převod tipu pro učitele."""
    lines_raw = m.group(1)
    tip_lines = re.findall(r'^>\s?(.*)$', lines_raw, re.MULTILINE)
    indented = '\n'.join(f'    {l}' for l in tip_lines)
    return f'\n!!! tip "Tip pro učitele"\n{indented}\n'


def _add_act_badges_format_c(body: str) -> str:
    """
    Nahradí #### N. Title (X min) + *hint* za ### N. Title + <span class="act">.
    """
    lines = body.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^####\s+(\d+)\.\s+(.+?)\s*\((\d+)\s+min\)\s*$', line)
        if m:
            num = m.group(1)
            title = m.group(2).strip()
            minutes = int(m.group(3))
            # Hledej type hint na dalším neprázdném řádku
            hint = 'board'
            skip_next = False
            for j in range(i + 1, min(i + 4, len(lines))):
                next_line = lines[j].strip()
                if next_line:
                    hint_m = re.match(r'^\*([^*]+)\*\.?$', next_line)
                    if hint_m:
                        hint = hint_m.group(1)
                        skip_next = True
                    break
            act_type = detect_activity_type(hint)
            emoji = ACT_EMOJI.get(act_type, '📌')
            label = ACT_LABEL.get(act_type, hint)
            result.append(f'### {num}. {title}')
            result.append('')
            result.append(f'<span class="act {act_type}">{emoji} {label} — {minutes} min</span>')
            i += 1
            if skip_next:
                # Přeskočíme prázdné řádky a hint řádek
                while i < len(lines) and not lines[i].strip():
                    i += 1
                if i < len(lines):
                    i += 1  # přeskočíme hint řádek
        else:
            result.append(line)
            i += 1
    return '\n'.join(result)


# ── Detekce souborů, které jsou již migrovány ─────────────────────────────────

def has_front_matter(content: str) -> bool:
    """Zjistí, zda soubor již má YAML front matter (začíná ---)."""
    return content.startswith('---\n') or content.startswith('---\r\n')


def get_first_h1(content: str) -> str:
    """Vrátí první h1 nadpis ze souboru (bez # prefixu)."""
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else ''


def clean_h1(title: str) -> str:
    """Odstraní emoji ze začátku nadpisu."""
    return re.sub(r'^[\U00010000-\U0010ffff\U00002600-\U000027BF\s]+', '', title).strip()


# ── Hlavní migrace ────────────────────────────────────────────────────────────

def migrate_file(filepath: str, dry_run: bool = False) -> dict:
    """
    Migruje jeden soubor hodiny do nového formátu s front matter.
    Vrátí info dict s výsledkem.
    """
    path = Path(filepath)
    grade = grade_from_path(str(filepath))
    week = week_from_path(str(filepath))

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Přeskoč soubory, které již mají front matter
    if has_front_matter(content):
        return {'file': filepath, 'status': 'skipped', 'reason': 'already has front matter'}

    fmt = detect_format(content)

    try:
        if fmt == 'A':
            meta, body = parse_format_a(content, grade, week)
        elif fmt == 'B':
            meta, body = parse_format_b(content, grade, week)
        elif fmt == 'C':
            meta, body = parse_format_c(content, grade, week)
        else:
            return {'file': filepath, 'status': 'error', 'reason': f'neznámý formát: {fmt}'}
    except Exception as e:
        return {'file': filepath, 'status': 'error', 'reason': str(e), 'format': fmt}

    if not body:
        return {'file': filepath, 'status': 'skipped', 'reason': 'žádná sekce Metodický postup (prázdniny?)'}

    # Získej nadpis z původního souboru
    title = get_first_h1(content)

    # Sestav výsledný obsah
    fm = make_front_matter(meta)
    # Odstraň emoji ze začátku h1 (pokud tam je)
    new_content = f'{fm}\n\n# {clean_h1(title)}\n\n{body}\n'

    # Přidej markdown="1" ke custom divům (md_in_html extension to vyžaduje)
    new_content = re.sub(
        r'<div class="(resources)"(?!\s+markdown)',
        r'<div class="\1" markdown="1"',
        new_content,
    )

    if not dry_run:
        # Záloha
        backup_path = str(filepath) + '.bak'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        # Zapis nový obsah
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return {
        'file': filepath,
        'status': 'migrated',
        'format': fmt,
        'grade': grade,
        'week': week,
        'rvp_count': len(meta.get('rvp_codes', [])),
        'goals_count': len(meta.get('goals', [])),
        'time_budget_count': len(meta.get('time_budget', [])),
        'has_friday_tip': bool(meta.get('friday_tip')),
    }


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Migruje tyden-*.md soubory do front matter formátu')
    parser.add_argument('--dry-run', action='store_true', help='Pouze zobraz co by se udělalo, nepíše soubory')
    parser.add_argument('--rocnik', type=int, choices=[6, 7, 8, 9], help='Migruj jen daný ročník')
    parser.add_argument('--tyden', type=int, help='Migruj jen daný týden (kombinuj s --rocnik)')
    args = parser.parse_args()

    base = Path(__file__).parent / 'docs'

    if args.rocnik:
        if args.tyden:
            pattern = str(base / f'{args.rocnik}-rocnik' / f'tyden-{args.tyden:02d}.md')
            files = glob.glob(pattern)
        else:
            files = sorted(glob.glob(str(base / f'{args.rocnik}-rocnik' / 'tyden-*.md')))
    else:
        files = sorted(glob.glob(str(base / '*-rocnik' / 'tyden-*.md')))

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Nalezeno {len(files)} souborů\n")

    stats = {'migrated': 0, 'skipped': 0, 'error': 0}
    errors = []

    for filepath in files:
        result = migrate_file(filepath, dry_run=args.dry_run)
        status = result['status']
        stats[status] = stats.get(status, 0) + 1

        rel = os.path.relpath(filepath, base)
        if status == 'migrated':
            fmt = result.get('format', '?')
            rvp = result.get('rvp_count', 0)
            goals = result.get('goals_count', 0)
            tb = result.get('time_budget_count', 0)
            print(f'  ✓ [{fmt}] {rel}  (RVP: {rvp}, goals: {goals}, time_budget: {tb})')
        elif status == 'skipped':
            print(f'  – {rel}  (přeskočeno: {result.get("reason", "")})')
        elif status == 'error':
            reason = result.get('reason', '')
            fmt = result.get('format', '?')
            print(f'  ✗ [{fmt}] {rel}  CHYBA: {reason}')
            errors.append(result)

    print(f'\n── Výsledek ──')
    print(f'  Migrováno:   {stats.get("migrated", 0)}')
    print(f'  Přeskočeno:  {stats.get("skipped", 0)}')
    print(f'  Chyby:       {stats.get("error", 0)}')

    if errors:
        print('\n── Soubory s chybou ──')
        for e in errors:
            print(f'  {e["file"]}: {e.get("reason", "")}')


if __name__ == '__main__':
    main()
