# Pokročilé tabulky: Funkce IF

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Data, informace a modelování
- **Výstup:** <div class="curriculumTag" data-code="I-9-1-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-1-02</span><span style="color: #374151;">Žák zpracuje a interpretuje data pomocí vhodných nástrojů</span></div>

## 💬 Tip pro pátek
Ukaž žákům reálné použití: mzdový systém, vysvědčení nebo slevový kalkulator — všechny používají IF. „To, co se učíte dnes, opravdu někdo napsal a platí mu za to."

## 🎯 Cíle hodiny

- Žák vysvětlí logiku podmínkové funkce IF (když platí podmínka, pak X, jinak Y)
- Žák napíše jednoduchou funkci IF pro hodnocení dat (splnil/nesplnil, sleva/bez slevy)
- Žák rozlišuje různé podmínkové operátory: `>`, `<`, `=`, `>=`, `<=`, `<>`
- Žák propojí funkci IF s vědomostmi o podmínkách z programování (Scratch, 7. ročník)

## 💡 Metodický postup

### 1. Propojení se Scratchem (7 min) — tabule

Učitel napíše na tabuli pseudokód:

```
když skóre > 50
  pak řekni "Vyhrál jsi!"
  jinak řekni "Prohrál jsi."
```

Pak ukáže, jak to samé funguje v tabulkovém procesoru:

```
=IF(B2>50; "Vyhrál jsi!"; "Prohrál jsi.")
```

Žáci identifikují části: podmínka (`B2>50`), hodnota když pravda, hodnota když nepravda.

### 2. Syntaxe IF — krok za krokem (10 min) — tabule

Učitel zapíše obecný vzorec:

```
=IF(podmínka; hodnota_když_PRAVDA; hodnota_když_NEPRAVDA)
```

Příklady podmínek:
- `A1>100` — hodnota v A1 je větší než 100
- `B3="Praha"` — text v B3 je "Praha"
- `C5>=18` — hodnota v C5 je 18 nebo více
- `D2<>""` — buňka D2 není prázdná

Žáci zapisují do sešitu/poznámek.

### 3. Praktická úloha: Hodnocení žáků (20 min) — PC

Učitel sdílí nebo žáci vytvoří tabulku s výsledky testu:

| Jméno | Body | Hodnocení |
|-------|------|-----------|
| Anna | 85 | ? |
| Petr | 52 | ? |
| Jana | 91 | ? |
| Tomáš | 38 | ? |

**Úloha 1:** Do sloupce C napište IF, který vypíše „Prospěl" pokud body ≥ 60, jinak „Neprospěl".

**Úloha 2:** Rozšiřte na tři kategorie pomocí vnořeného IF:
```
=IF(B2>=90; "Výborně"; IF(B2>=60; "Prospěl"; "Neprospěl"))
```

**Úloha 3 (pro rychlé):** Přidejte sloupec „Bonus" — kdo má ≥ 90 bodů, dostane „5 % bonus", ostatní „—".

### 4. Kontrola a diskuse (8 min) — tabule

Jeden žák sdílí výsledek na projektoru, třída kontroluje. Diskuse:
- „Co se stane, když buňka B2 bude prázdná?"
- „Jak bychom IF zkombinovali s SUM nebo AVERAGE?"
- Ukázka IF s textem vs. číslem (chyby při záměně)

## 📂 Podklady

- **Google Sheets — nápověda k IF:** [support.google.com](https://support.google.com/docs/answer/3093364) — kompletní dokumentace s příklady
- **Vzorová tabulka:** Připravte sdílený Google Sheet nebo Excel soubor s daty pro cvičení — ušetří čas
- **Video (CZ):** YouTube — „funkce IF Excel česky" — několik kvalitních tutoriálů od českých tvůrců
- **Rozšíření — IFS:** V novějších verzích Excel/Sheets existuje funkce `IFS` pro více podmínek bez vnořování — pro rychlé žáky
- **Propojení s praxí:** Mzdový list (přesčasy IF hodiny>8), e-shop (sleva IF objednávka>1000 Kč)

!!! tip "Tip pro učitele"
    Nejčastější chyby žáků: záměna středníku a čárky (závisí na nastavení jazyka), chybějící uvozovky u textu, záměna `=` (rovná se) s přiřazením. Nechejte žáky záměrně udělat chybu a přečíst chybovou hlášku — tím se naučí debugovat. Vnořené IF (úloha 2) je kognitivně náročné — nedotahujte pokud třída nestíhá, to přijde přirozeně v dalších hodinách.
