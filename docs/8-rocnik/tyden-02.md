# 🔀 Pokročilé tabulky: Funkce IF

> **Stav:** `⬜ Nekontrolováno`

### 📋 Kontext a cíle
> **RVP ZV (Informatika):** Data, informace a modelování
> **Kód:** `INF-INF-001-ZV9-002` – *Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.*

**Po hodině žák:**
* **Vysvětlí** logiku podmínkové funkce IF (když platí podmínka, pak X, jinak Y).
* **Napíše** jednoduchou funkci IF pro hodnocení dat (splnil/nesplnil, sleva/bez slevy).
* **Rozlišuje** různé podmínkové operátory: `>`, `<`, `=`, `>=`, `<=`, `<>`.
* **Propojí** funkci IF s vědomostmi o podmínkách z programování (Scratch, 7. ročník).

---

### 💡 Metodický postup (45 min)

#### 1. Propojení se Scratchem (7 min)
*Diskuze u tabule.*

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

---

#### 2. Syntaxe IF — krok za krokem (10 min)
*Tabule — výklad.*

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

---

#### 3. Praktická úloha: Hodnocení žáků (20 min)
*Práce na PC.*

Učitel sdílí nebo žáci vytvoří tabulku s výsledky testu:

| Jméno | Body | Hodnocení |
|-------|------|-----------|
| Anna | 85 | ? |
| Petr | 52 | ? |
| Jana | 91 | ? |
| Tomáš | 38 | ? |

<div class="zadani-pc">

**Úloha 1:** Do sloupce C napište IF, který vypíše „Prospěl" pokud body ≥ 60, jinak „Neprospěl".

**Úloha 2:** Rozšiřte na tři kategorie pomocí vnořeného IF:
```
=IF(B2>=90; "Výborně"; IF(B2>=60; "Prospěl"; "Neprospěl"))
```

**Úloha 3 (pro rychlé):** Přidejte sloupec „Bonus" — kdo má ≥ 90 bodů, dostane „5 % bonus", ostatní „—".

</div>

---

#### 4. Kontrola a diskuse (8 min)
*Tabule — sdílení výsledků.*

Jeden žák sdílí výsledek na projektoru, třída kontroluje. Diskuse:
- „Co se stane, když buňka B2 bude prázdná?"
- „Jak bychom IF zkombinovali s SUM nebo AVERAGE?"
- Ukázka IF s textem vs. číslem (chyby při záměně)

---

### 🛠️ Zdroje a nástroje

* **Google Sheets — nápověda k IF:** [support.google.com](https://support.google.com/docs/answer/3093364) — kompletní dokumentace s příklady
* **Vzorová tabulka:** Připravte sdílený Google Sheet nebo Excel soubor s daty pro cvičení — ušetří čas
* **Video (CZ):** YouTube — „funkce IF Excel česky" — několik kvalitních tutoriálů od českých tvůrců
* **Rozšíření — IFS:** V novějších verzích Excel/Sheets existuje funkce `IFS` pro více podmínek bez vnořování — pro rychlé žáky
* **Propojení s praxí:** Mzdový list (přesčasy IF hodiny>8), e-shop (sleva IF objednávka>1000 Kč)

---

> 💡 **Tip pro učitele:**
> Nejčastější chyby žáků: záměna středníku a čárky (závisí na nastavení jazyka), chybějící uvozovky u textu, záměna `=` (rovná se) s přiřazením. Nechejte žáky záměrně udělat chybu a přečíst chybovou hlášku — tím se naučí debugovat. Vnořené IF (úloha 2) je kognitivně náročné — nedotahujte pokud třída nestíhá, to přijde přirozeně v dalších hodinách.

> 💬 **Tip pro pátek:** Ukaž žákům reálné použití: mzdový systém, vysvědčení nebo slevový kalkulator — všechny používají IF. „To, co se učíte dnes, opravdu někdo napsal a platí mu za to."
