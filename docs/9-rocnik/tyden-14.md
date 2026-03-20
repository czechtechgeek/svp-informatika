# Vánoce: Generativní umění

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování / Digitální tvorba
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-009" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-009</span><span style="color: #374151;">Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-004-ZV9-014" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-004-ZV9-014</span><span style="color: #374151;">Diskutuje o fungování digitálních technologií určujících trendy ve světě.</span></div>

## 💬 Tip pro pátek
Předvánoční hodina je skvělá příležitost pro kreativitu bez hodnocení — dejte žákům volnost experimentovat a sdílet výsledky. Pusťte vánoční hudbu na pozadí a nechte hodinu plynout v uvolněné atmosféře.

## 🎯 Cíle hodiny

- Žák vytvoří vánoční grafiku pomocí Python turtle nebo online nástroje
- Žák pochopí princip generativního umění — kód jako tvůrčí nástroj
- Žák modifikuje existující kód a prozkoumá efekt změny parametrů
- Žák sdílí svůj výtvor se třídou a popíše, jak ho vytvořil

## 💡 Metodický postup

### 1. Úvod: Co je generativní umění (7 min) — tabule / diskuse

Učitel ukáže příklady generativního umění na projektoru:
- Sněhové vločky generované kódem
- Fraktály (Kochova vločka, Sierpińského trojúhelník)
- Generativní vánoční stromy

Klíčová myšlenka: „Umění vytvořené algoritmem — počítač kreslí podle pravidel, ale výsledek je unikátní."

Propojení: Stejný přístup používají architekti, designéři log, tvůrci her.

### 2. Demo: Vánoční strom v Python Turtle (8 min) — Python

Učitel živě naprogramuje základní vánoční strom:

```python
import turtle
import random

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("navy")

def vetev(delka, uroven):
    if uroven == 0 or delka < 5:
        return
    # nakreslí větev
    t.color("darkgreen")
    t.forward(delka)
    # levá větev
    t.left(30)
    vetev(delka * 0.7, uroven - 1)
    t.right(30)
    # pravá větev
    t.right(30)
    vetev(delka * 0.7, uroven - 1)
    t.left(30)
    # vrátí se zpět
    t.backward(delka)

# Nakreslí strom
t.left(90)
t.penup()
t.goto(0, -200)
t.pendown()
vetev(150, 6)

# Hvězda nahoře
t.penup()
t.goto(0, 100)
t.color("gold")
t.write("★", align="center", font=("Arial", 30, "bold"))

turtle.done()
```

Učitel ukáže, co se stane, když změní číslo `0.7` na `0.8` nebo úhel `30` na `45`.

### 3. Kreativní práce (25 min) — Python

Žáci si vyberou jeden ze tří přístupů dle úrovně:

**Varianta A — Začátečník (Python Turtle):**
Modifikovat vzorový kód stromu: změnit barvy, přidat „ozdoby" (barevné tečky), změnit tvar.

```python
# Přidání ozdob (barevné kruhy na konci větví)
def vetev_s_ozdobami(delka, uroven):
    if uroven == 0 or delka < 5:
        # nakreslí ozdobu
        barvy = ["red", "gold", "silver", "blue"]
        t.color(random.choice(barvy))
        t.dot(8)
        return
    t.color("darkgreen")
    t.forward(delka)
    t.left(30)
    vetev_s_ozdobami(delka * 0.7, uroven - 1)
    t.right(60)
    vetev_s_ozdobami(delka * 0.7, uroven - 1)
    t.left(30)
    t.backward(delka)
```

**Varianta B — Pokročilý (Python Turtle):**
Nakreslit sněhovou vločku pomocí fraktálu (Kochova křivka):

```python
import turtle

def kochova_krivka(delka, uroven):
    if uroven == 0:
        turtle.forward(delka)
        return
    kochova_krivka(delka / 3, uroven - 1)
    turtle.left(60)
    kochova_krivka(delka / 3, uroven - 1)
    turtle.right(120)
    kochova_krivka(delka / 3, uroven - 1)
    turtle.left(60)
    kochova_krivka(delka / 3, uroven - 1)

turtle.speed(0)
turtle.color("skyblue")
turtle.bgcolor("navy")

# Nakreslit 6 ramen vločky
for _ in range(6):
    kochova_krivka(150, 3)
    turtle.right(60)

turtle.done()
```

**Varianta C — Online nástroj (p5.js):**
Otevřít [editor.p5js.org](https://editor.p5js.org) a vytvořit padající sníh:

```javascript
// p5.js: Padající sníh
let vlocky = [];

function setup() {
  createCanvas(400, 400);
  for (let i = 0; i < 100; i++) {
    vlocky.push({x: random(width), y: random(height), r: random(2, 6)});
  }
}

function draw() {
  background(10, 10, 50);
  fill(255);
  noStroke();
  for (let v of vlocky) {
    ellipse(v.x, v.y, v.r);
    v.y += v.r / 2;
    if (v.y > height) { v.y = 0; v.x = random(width); }
  }
}
```

### 4. Sdílení a závěr (5 min) — diskuse

Žáci ukáží svou tvorbu na projektoru nebo pošlou screenshot do skupiny. Učitel ukončí pololetní blok: „Za chvíli jsou vánoce — příští rok pokračujeme tématem AI."

## 📂 Podklady

- **Python Turtle dokumentace:** docs.python.org/3/library/turtle.html
- **p5.js editor online:** [editor.p5js.org](https://editor.p5js.org) — nepotřebuje instalaci, vhodné jako záloha
- **Inspirace — generativní umění:** openprocessing.org — galerie hotových projektů
- **Vzorové kódy:** Připravte soubory ke stažení/zkopírování pro žáky, kteří zaostávají
- **Fraktály — vysvětlení:** YouTube — „fractal art Python turtle" pro vizuální inspiraci

!!! tip "Tip pro učitele"
    Rekurzivní funkce (vetev volá sama sebe) může žáky zaskočit — nemusíte ji plně vysvětlovat, stačí říct „funkce se volá sama a tím se větví". Pokud nemáte nainstalovaný Python s Turtle, p5.js v prohlížeči je plnohodnotná alternativa. Výsledky žáků sdílejte na třídní nástěnce nebo pošlete rodičům — je to skvělý způsob ukázat, co informatika opravdu umí.
