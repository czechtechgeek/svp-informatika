---
grade: 9
week: 7
time: 45
area: Programování / Algoritmické myšlení
rvp_codes:
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
  - code: INF-INF-002-ZV9-006
    text: Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.
goals:
  - "Žák importuje modul `turtle` a ovládá základní příkazy pohybu"
  - "Žák využívá `for` cyklus pro kreslení opakujících se tvarů"
  - "Žák propojuje matematiku (úhly, počet stran) s programováním"
  - Žák vytvoří vlastní kreativní obrázek pomocí želví grafiky
time_budget:
  - type: board
    minutes: 8
  - type: board
    minutes: 15
  - type: board
    minutes: 17
  - type: discussion
    minutes: 5
friday_tip: "Želví grafika je skvělá pro páteční hodinu – výsledky jsou okamžitě viditelné a esteticky zajímavé. Pusťte žákům na začátku inspiraci: výstup spirálového programu. „Chcete vědět, jak se to napíše?\" Garantovaně ano."
---

# Python III: Želví grafika

## 💡 Metodický postup

### 1. Úvod do modulu turtle

<span class="act board">🖊️ Tabule — 8 min</span>

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

### 2. Čtverce a pravidelné mnohoúhelníky

<span class="act board">🖊️ Tabule — 15 min</span>

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

### 3. Kreativní tvorba

<span class="act board">🖊️ Tabule — 17 min</span>

Žáci si vyberou výzvu dle svých schopností:

**Základní:** Nakreslit libovolný barevný tvar

**Střední:** Nakreslit spirálu nebo hvězdu:
```python
for i in range(50):
    t.forward(i * 3)
    t.right(91)
```

**Pokročilé:** Nakreslit sněhovou vločku nebo vlastní vzor s více barvami a tvary.

### 4. Galerie a reflexe

<span class="act discussion">💬 Diskuse — 5 min</span>

Žáci ukáží svůj obrázek sousedovi. Vyberou 2–3 zajímavé výsledky k sdílení s celou třídou. Diskuse: Jaký matematický vzorec stojí za spirálou?

## 📂 Podklady

- **Online turtle:** trinket.io/python (funguje v prohlížeči bez instalace)
- **Dokumentace turtle:** docs.python.org/3/library/turtle.html
- **Inspirace:** YouTube „Python turtle art" – nádherné příklady generativního umění
- **Výzva pro rychlé:** Nakreslení hodinového ciferníku nebo Sierpińského trojúhelníku

!!! tip "Tip pro učitele"
    Nechejte žáky experimentovat – nemusí sledovat přesně váš kód. Zelví grafika je ideální pro „co se stane, když změním toto číslo?" Chyby jsou vizuálně viditelné a oprava je okamžitě ověřitelná. Propojte s matematikou: zeptejte se na úhel vnitřní/vnější u různých mnohoúhelníků.
