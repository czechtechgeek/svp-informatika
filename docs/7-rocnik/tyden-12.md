# Projekt Hra II: Programování

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-002-ZV9-008" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-002-ZV9-008</span><span style="color: #374151;">Průběžně ověřuje správnost vytvářeného postupu, zkouší program, opravuje chyby, posoudí efektivitu postupu, programu.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-002-ZV9-007" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-002-ZV9-007</span><span style="color: #374151;">V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné.</span></div>

## 💬 Tip pro pátek
Páteční programování je nejproduktivnější v tichu s hudbou na pozadí (instrumentální, bez textů). Žáci jsou soustředěnější. Zkuste zapnout ambientní hudbu a pozorujte rozdíl v atmosféře.

## 🎯 Cíle hodiny

- Žák realizuje herní projekt podle svého GDD z minulé hodiny
- Žák aplikuje všechny naučené koncepty: pohyb, podmínky, proměnné, kolize
- Žák debugguje svůj program — identifikuje chybu, formuluje hypotézu, testuje opravu
- Žák uloží a sdílí rozpracovaný projekt pro pokračování v příštím týdnu

## 💡 Metodický postup

### 1. Zahájení: Krátká rekapitulace a plán (5 min) — bez počítače

Každý žák si přečte svůj GDD z minulé hodiny a napíše na kartičku:
- „Dnes udělám…" (3 konkrétní věci)
- „Začnu s…"

Učitel upozorní: „Mějte otevřený GDD vedle Scratch — je to váš návod."

### 2. Samostatná práce na projektu (33 min) — PC

Žáci pracují individuálně na svých herních projektech. Učitel aktivně obchází třídu a pomáhá.

**Doporučené pořadí implementace:**
1. Scéna (pozadí + sprity) — vizuální základ
2. Pohyb hráčského spritu
3. Pohyb překážek/nepřátel (náhodná poloha, automatický pohyb)
4. Detekce kolize + reakce
5. Proměnné (skóre, čas, životy)
6. Podmínka výhra/prohra

**Časté problémy a řešení:**

| Problém | Řešení |
|---------|--------|
| Sprite neodpovídá na klávesy | Kliknout na sprite (ne pozadí) při programování |
| Kolize nefunguje | Zkontrolovat, zda sprity mají správné jméno v bloku `dotýkám se [_]` |
| Program se zastaví okamžitě | Chybí smyčka `opakuj dokola` |
| Skóre narůstá příliš rychle | Přidat `čekej 0.5 sekund` po detekci kolize |

### 3. Průběžný checkpoint (5 min)

Učitel zastaví práci: „Kdo má hotový pohyb hráče? Kdo má hotovou kolizi? Kdo má proměnnou skóre?"

Žáci zvedají ruce — učitel vidí, kdo potřebuje pomoc, a přesune se k nim.

### 4. Uložení a příprava na testování (2 min)

Žáci uloží projekt na Scratch s názvem formátu `7rocnik-hra-[jméno]`.

Pokud projekt není hotový: „Zapište si na kartičku, kde jste skončili a co zítra uděláte jako první."

## 📂 Podklady

- **Scratch:** [scratch.mit.edu](https://scratch.mit.edu) — projekt průběžně ukládat (Ctrl+S nebo tlačítko Uložit)
- **Debugging checklist:**
  1. Je sprite vybrán správně?
  2. Jsou bloky propojeny (ne volně plovoucí)?
  3. Začíná program `po kliknutí na vlajku`?
  4. Je v cyklu `opakuj dokola`?
  5. Jsou proměnné inicializovány na startu?
- **Scratch sprite editor:** Žáci mohou nakreslít vlastní sprity — připomeňte, že jednoduchý tvar funguje lépe než složitý obrázek
- **Free assets:** Na Scratch jsou zabudované sprity, pozadí a zvuky — není nutné nic stahovat

!!! tip "Tip pro učitele"
    Tato hodina je záměrně bez velké struktury — žáci potřebují nerušený čas na tvorbu. Vaše role je kouč, ne přednášející. Nebojte se říct „nevím, pojďme to zjistit spolu" — modelujete tím zdravý přístup k problémům. Identifikujte 1–2 žáky, kteří jsou napřed, a poprosit je, aby pomohli sousedovi — peer učení funguje v programování velmi efektivně.
