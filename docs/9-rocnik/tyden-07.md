# Python III: Želví grafika

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Programování / Algoritmické myšlení
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-009" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-009</span><span style="color: #374151;">Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-002-ZV9-006" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-002-ZV9-006</span><span style="color: #374151;">Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.</span></div>

## 💬 Tip pro pátek
Želví grafika je skvělá pro páteční hodinu – výsledky jsou okamžitě viditelné a esteticky zajímavé. Pusťte žákům na začátku inspiraci: výstup spirálového programu. „Chcete vědět, jak se to napíše?" Garantovaně ano.

## 🎯 Cíle hodiny

- Žák importuje modul `turtle` a ovládá základní příkazy pohybu
- Žák využívá `for` cyklus pro kreslení opakujících se tvarů
- Žák propojuje matematiku (úhly, počet stran) s programováním
- Žák vytvoří vlastní kreativní obrázek pomocí želví grafiky

## 💡 Metodický postup

### 1. Úvod do modulu turtle (8 min) — tabule

Učitel ukáže a vysvětlí základní příkazy:

```python
import turtle

t = turtle.Turtle()   # Vytvoří želvu
t.forward(100)        # Pohyb dopředu o 100 pixelů
t.right(90)           # Otočení doprava o 90 stupňů
t.left(45)            # Otočení doleva o 45 stupňů
t.penup()             # Zvedne pero (nepíše při pohybu)
t.pendown()           # Spustí pero
t.color("red")        # Barva čáry
t.speed(5)            # Rychlost 1–10
```

Analogie: Želva je robot s perem – říkáte jí, kam jít a o kolik se otočit.

### 2. Čtverce a pravidelné mnohoúhelníky (15 min) — Python

**Čtverec bez cyklu:**
```python
import turtle
t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
```

**Čtverec s cyklem:**
```python
for i in range(4):
    t.forward(100)
    t.right(90)
```

**Šestiúhelník:**
```python
for i in range(6):
    t.forward(100)
    t.right(60)   # 360 / 6 = 60
```

Klíč: Pro N-úhelník je vnější úhel `360 / N`. Žáci zjistí sami.

### 3. Kreativní tvorba (17 min) — Python

Žáci si vyberou výzvu dle svých schopností:

**Základní:** Nakreslit libovolný barevný tvar

**Střední:** Nakreslit spirálu nebo hvězdu:
```python
for i in range(50):
    t.forward(i * 3)
    t.right(91)
```

**Pokročilé:** Nakreslit sněhovou vločku nebo vlastní vzor s více barvami a tvary.

### 4. Galerie a reflexe (5 min) — diskuse

Žáci ukáží svůj obrázek sousedovi. Vyberou 2–3 zajímavé výsledky k sdílení s celou třídou. Diskuse: Jaký matematický vzorec stojí za spirálou?

## 📂 Podklady

- **Online turtle:** trinket.io/python (funguje v prohlížeči bez instalace)
- **Dokumentace turtle:** docs.python.org/3/library/turtle.html
- **Inspirace:** YouTube „Python turtle art" – nádherné příklady generativního umění
- **Výzva pro rychlé:** Nakreslení hodinového ciferníku nebo Sierpińského trojúhelníku

!!! tip "Tip pro učitele"
    Nechejte žáky experimentovat – nemusí sledovat přesně váš kód. Zelví grafika je ideální pro „co se stane, když změním toto číslo?" Chyby jsou vizuálně viditelné a oprava je okamžitě ověřitelná. Propojte s matematikou: zeptejte se na úhel vnitřní/vnější u různých mnohoúhelníků.
