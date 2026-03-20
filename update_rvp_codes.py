#!/usr/bin/env python3
"""
Update RVP codes and descriptions across all lesson files.
Replaces old I-9-X-XX codes with official INF-INF-XXX-ZV9-XXX codes.
"""

import os
import re
import glob

# Official RVP outcomes mapping
# Format: old_code -> (new_code, official_description)
MAPPING = {
    "I-9-1-01": ("INF-INF-001-ZV9-001", "Získá z dat informace, interpretuje data získaná pro řešení konkrétního problému."),
    "I-9-1-02": ("INF-INF-001-ZV9-002", "Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu."),
    "I-9-1-03": ("INF-INF-001-ZV9-003", "Modeluje situace různými způsoby, včetně grafů nebo obdobných schémat."),
    "I-9-2-01": ("INF-INF-002-ZV9-006", "Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení."),
    "I-9-2-02": ("INF-INF-002-ZV9-007", "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."),
    "I-9-2-03": ("INF-INF-002-ZV9-005", "Po přečtení jednotlivých kroků algoritmu vysvětlí celý postup a určí problém, který je daným algoritmem řešen."),
    "I-9-2-04": ("INF-INF-002-ZV9-008", "Průběžně ověřuje správnost vytvářeného postupu, zkouší program, opravuje chyby, posoudí efektivitu postupu, programu."),
    "I-9-3-01": ("INF-INF-003-ZV9-009", "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."),
    "I-9-3-02": ("INF-INF-003-ZV9-010", "Pro řešení problému vytvoří tabulku evidence dat a stanoví pravidla pro práci se záznamy."),
    "I-9-4-01": ("INF-INF-004-ZV9-014", "Diskutuje o fungování digitálních technologií určujících trendy ve světě."),
    "I-9-4-02": ("INF-INF-004-ZV9-013", "Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje, na základě posouzení rizik ztráty, poškození či zneužití dat."),
    "I-9-4-03": ("INF-INF-004-ZV9-014", "Diskutuje o fungování digitálních technologií určujících trendy ve světě."),
    "I-9-4-04": ("INF-INF-004-ZV9-014", "Diskutuje o fungování digitálních technologií určujících trendy ve světě."),
}

# Standard curriculumTag SVG (book icon)
BOOK_SVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'

CURRICULUM_TAG_STYLE = 'display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;'


def make_curriculum_tag(code, desc):
    """Generate a curriculumTag div with the given code and description."""
    return (
        f'<div class="curriculumTag" data-code="{code}" style="{CURRICULUM_TAG_STYLE}">'
        f'{BOOK_SVG}'
        f'<span style="color: #1975FE; font-weight: 500;">{code}</span>'
        f'<span style="color: #374151;">{desc}</span>'
        f'</div>'
    )


def make_rvp_tag(code, desc):
    """Generate a rvp-tag span with the given code and description (for legacy format)."""
    return f'<span class="rvp-tag"><span class="rvp-code">{code}</span><span class="rvp-desc">{desc}</span></span>'


def update_curriculum_tags(content):
    """Replace curriculumTag divs using old codes with new official codes."""
    def replacer(m):
        old_code = m.group(1)
        if old_code in MAPPING:
            new_code, new_desc = MAPPING[old_code]
            return f'- **Výstup:** {make_curriculum_tag(new_code, new_desc)}'
        return m.group(0)  # Leave unchanged if not in mapping

    # Match the full "- **Výstup:** <div...>" pattern including old code
    pattern = r'- \*\*Výstup:\*\* <div class="curriculumTag" data-code="(I-9-\d-\d+)"[^>]*>.*?</div>'
    content = re.sub(pattern, replacer, content)
    return content


def update_rvp_tags(content):
    """Replace old-style rvp-tag spans with new official codes and descriptions."""
    def replacer(m):
        old_code = m.group(1)
        if old_code in MAPPING:
            new_code, new_desc = MAPPING[old_code]
            return make_rvp_tag(new_code, new_desc)
        return m.group(0)

    pattern = r'<span class="rvp-tag"><span class="rvp-code">(I-9-\d-\d+)</span><span class="rvp-desc">[^<]*</span></span>'
    content = re.sub(pattern, replacer, content)
    return content


def update_backtick_codes(content):
    """Replace old codes in the 8th grade backtick format: > **Kód:** `I-9-X-XX` – *description*"""
    def replacer(m):
        old_code = m.group(1)
        if old_code in MAPPING:
            new_code, new_desc = MAPPING[old_code]
            return f'> **Kód:** `{new_code}` – *{new_desc}*'
        return m.group(0)

    pattern = r'> \*\*Kód:\*\* `(I-9-\d-\d+)` – \*[^*]+\*'
    content = re.sub(pattern, replacer, content)
    return content


def update_file(filepath):
    """Update a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    updated = update_curriculum_tags(original)
    updated = update_rvp_tags(updated)
    updated = update_backtick_codes(updated)

    if updated != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated)
        return True
    return False


def main():
    docs_dir = os.path.join(os.path.dirname(__file__), 'docs')
    md_files = glob.glob(os.path.join(docs_dir, '**', '*.md'), recursive=True)

    changed = 0
    unchanged = 0
    for filepath in sorted(md_files):
        if update_file(filepath):
            print(f"  UPDATED: {os.path.relpath(filepath)}")
            changed += 1
        else:
            unchanged += 1

    print(f"\nDone. Updated: {changed}, Unchanged: {unchanged}")


if __name__ == '__main__':
    main()
