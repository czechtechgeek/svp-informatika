# Proměnné I: Skóre ve hře

## 🎯 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák implementuje algoritmus v programovacím jazyce</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-03" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-03</span><span style="color: #374151;">Žák pracuje s proměnnými a datovými typy</span></div>

## 💡 Metodický tip pro pátky
Živý model proměnné: vezmte krabičku a kartičku s názvem „skóre". Do krabičky vložte lístek s číslem 0. Při každém „bodu" vyměňte lístek za vyšší číslo. Žáci vidí proměnnou fyzicky — má jméno, má hodnotu, hodnota se mění.

## 🎯 Cíle hodiny

- Žák vysvětlí, co je proměnná, a odliší ji od konstanty
- Žák vytvoří proměnnou ve Scratch a nastaví její počáteční hodnotu
- Žák používá bloky `nastav [skóre] na 0`, `změň [skóre] o 1` a zobrazí hodnotu na scéně
- Žák propojí proměnnou s podmínkou — skóre > 10 → konec hry

## 💡 Metodický postup

### 1. Co je proměnná? (8 min) — tabule

Učitel napíše:

```
skóre = 0
skóre = skóre + 1
skóre = skóre + 1
skóre = ?   →  skóre = 2
```

Analogie: Proměnná je jako **jmenovka na šuplíku**. Jmenovka se nemění (název), ale obsah šuplíku ano (hodnota).

Typy proměnných (základní přehled):
- **Číslo:** skóre, čas, životy, věk
- **Text:** jméno hráče, zpráva
- **Pravda/Nepravda:** hraje? splněno?

Ve Scratch: všechny proměnné jsou viditelné na scéně jako displej — to je výhoda pro výuku.

### 2. Demo: Přidání skóre do hry (12 min) — tabule

Učitel vezme projekt z minulé hodiny (hráč sbírá hvězdy) a přidá skóre:

**Krok 1 — Vytvoření proměnné:**
- Kategorie **Proměnné** → „Vytvořit proměnnou" → název: `skóre`
- Automaticky se přidají bloky: `nastav [skóre] na 0`, `změň [skóre] o 1`

**Krok 2 — Inicializace na startu:**
```
po kliknutí na vlajku:
  nastav [skóre] na 0
```

**Krok 3 — Přidání bodu při kolizi:**
```
opakuj dokola:
  pokud dotýkám se [hvězda]? pak:
    změň [skóre] o 1
    skryj hvězdu (nebo přesuň na nové místo)
```

**Krok 4 — Podmínka pro výhru:**
```
pokud [skóre] = 10 pak:
  řekni "Výhra!" po dobu 2 sekund
  zastav vše
```

### 3. Kodování: Hra se skóre (20 min) — PC

Žáci přidají proměnnou `skóre` do svého projektu z minulé hodiny nebo začnou nový projekt:

**Minimální požadavky:**
- Proměnná `skóre` inicializovaná na 0 při startu
- Skóre se zvyšuje při určité události (kolize, kliknutí, stisk klávesy)
- Skóre je viditelné na scéně

**Rozšíření:**
- **Životy:** druhá proměnná `životy` (začíná na 3, snižuje se při chybě)
- **Nejvyšší skóre:** proměnná `rekord` — aktualizuje se, pokud `skóre > rekord`
- **Hladiny:** po dosažení 10 bodů se zvýší obtížnost (rychlejší pohyb nepřátel)

### 4. Shrnutí (5 min)

Žáci odpoví ústně:
- „Proměnná je..."
- „Rozdíl mezi `nastav` a `změň` je..."
- „Kdybych přidal/a životy, co bych použil/a?"

## 📂 Podklady

- **Scratch — proměnné:** Kategorie **Proměnné** (oranžová, tmavší) — `nastav [_] na`, `změň [_] o`, `zobraz proměnnou`
- **Scratch tutoriál — proměnné:** [scratch.mit.edu/ideas](https://scratch.mit.edu/ideas) — hledejte „variables" nebo „score"
- **Analogie pro žáky:** Proměnná = schránka s názvem (krabičky, šuplíky, kontejnery)
- **Rozšíření — seznam (list):** Pro pokročilé žáky ukažte, že Scratch má i **Listy** (seznamy) — pro uložení více hodnot najednou (highscore tabulka)

!!! tip "Tip pro učitele"
    Nejčastější chyba: žáci zapomenou inicializovat proměnnou na 0 při startu — skóre pak pokračuje od minulého spuštění. Zdůrazněte, že blok `nastav [skóre] na 0` patří vždy k události `po kliknutí na vlajku`. Druhá častá chyba: záměna `nastav` (přepíše hodnotu) a `změň o` (přidá k hodnotě). Nechejte žáky si oba bloky vyzkoušet a pozorovat rozdíl.
