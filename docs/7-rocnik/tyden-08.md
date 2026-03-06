# Interakce: Ovládání postavy šipkami

## 🎯 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje algoritmus v programovacím jazyce</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-04" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-04</span><span style="color: #374151;">Žák navrhne a realizuje komplexnější projekt</span></div>

## 💡 Metodický tip pro pátky
Dejte žákům k dispozici gamepad nebo klávesnici a nechejte je „naučit" virtuálního žáka pohyb — kdo zvládne ovládat postavu čtyřmi šipkami bez kouknutí do kódu, má solidní intuici pro vstupní události.

## 🎯 Cíle hodiny

- Žák použije bloky událostí `když stisknuta klávesa` pro ovládání spritu
- Žák implementuje pohyb do čtyř směrů pomocí šipkových kláves
- Žák přidá animaci kostýmu reagující na směr pohybu
- Žák rozlišuje dva přístupy k ovládání (polling v cyklu vs. event-driven)

## 💡 Metodický postup

### 1. Analýza: Jak funguje ovládání ve hře? (8 min) — tabule

Učitel se zeptá: „Jak počítač ví, že stiskujete klávesu?" Žáci hádají.

Vysvětlení dvou přístupů:

**Přístup 1 — Pollování (testování v cyklu):**
```
opakuj dokola:
  pokud klávesa ↑ stisknuta? pak: pohni se nahoru
  pokud klávesa ↓ stisknuta? pak: pohni se dolů
```

**Přístup 2 — Událost (event-driven):**
```
když stisknuta klávesa [↑]:
  pohni se nahoru
```

Diskuse: Který je přehlednější? Který lépe reaguje na rychlé stisky? (Pollování reaguje hladčeji, events jsou přehlednější.)

### 2. Demo: Postava ovládaná šipkami (12 min) — tabule

Učitel postupně staví hráčský sprite na projektoru:

**Krok 1 — Základní pohyb:**
```
když stisknuta klávesa [šipka vpravo]: změň x o 10
když stisknuta klávesa [šipka vlevo]:  změň x o -10
když stisknuta klávesa [šipka nahoru]: změň y o 10
když stisknuta klávesa [šipka dolů]:   změň y o -10
```

**Krok 2 — Omezení obrazovkou:**
```
pokud x > 230 pak: nastav x na 230
pokud x < -230 pak: nastav x na -230
```

**Krok 3 — Animace směru:**
```
když stisknuta klávesa [šipka vpravo]: nastav směr na 90; změn kostým na "chůze-vpravo"
```

### 3. Kodování: Hráčův sprite + prostředí (20 min) — PC

Žáci vytvoří hráčský sprite a alespoň jedno z prostředí:

**Základ (povinný):**
- Sprite ovladatelný čtyřmi šipkami
- Nesmí přejít přes okraj obrazovky

**Prostředí — vyberte jedno:**
- **A:** Sběratelská hra — náhodně se objevují hvězdy, hráč je sbírá dotykem (zmizí)
- **B:** Labyrint — pozadí je labyrint (nakreslený v editoru), hráč nesmí přejít přes stěny (detekce barvy)
- **C:** Dva hráči — druhý sprite ovládá hráč 2 klávesami WASD

### 4. Showcase (5 min)

Dva žáci ukáží svůj projekt. Třída hodnotí:
- Reaguje sprite plynule?
- Kde by přidal/a nepřítele nebo překážku?

Učitel naznačí: „Příští týden přidáme **skóre** — proměnná, která počítá, co hráč sesbíral."

## 📂 Podklady

- **Scratch — snímání klávesy:** Blok `klávesa [_] stisknuta?` je v kategorii **Snímání** (světle modrá)
- **Scratch — změna x/y:** Kategorie **Pohyb** (modrá) — `změň x o`, `změň y o`, `nastav x na`, `nastav y na`
- **Detekce barvy:** Kategorie **Snímání** — `dotýkám se barvy [_]?` — pro labyrint nastavit barvu stěny
- **Tutoriál (EN):** Hledejte „Scratch arrow key movement tutorial" — Griffpatch nebo ScratchJr YouTube kanál
- **Inspirace — hra:** Pac-Man je čistě arrow-key hra — ukažte žákům jako motivaci, co se dá postavit

!!! tip "Tip pro učitele"
    Nejčastější chyba: sprite „skáče" přes okraj nebo „propíchne" zeď labyrintu. Ukažte žákům, že `změň x o 10` = teleportace o 10 pixelů, ne plynulý pohyb. Pro hladší pohyb použijte polling v cyklu s hodnotou 3–5 kroků. Detekce barvy pro labyrint (varianta B) je obtížnější — doporučte ji pouze rychlejším žákům.
