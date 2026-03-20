---
grade: 7
week: 12
time: 45
area: Algoritmizace a programování
rvp_codes:
  - code: INF-INF-002-ZV9-008
    text: "Průběžně ověřuje správnost vytvářeného postupu, zkouší program, opravuje chyby, posoudí efektivitu postupu, programu."
  - code: INF-INF-002-ZV9-007
    text: "V blokově orientovaném programovacím jazyce vytvoří přehledný program, používá opakování, větvení programu, proměnné."
goals:
  - Žák realizuje herní projekt podle svého GDD z minulé hodiny
  - "Žák aplikuje všechny naučené koncepty: pohyb, podmínky, proměnné, kolize"
  - "Žák debugguje svůj program — identifikuje chybu, formuluje hypotézu, testuje opravu"
  - Žák uloží a sdílí rozpracovaný projekt pro pokračování v příštím týdnu
time_budget:
  - type: unplugged
    minutes: 5
  - type: pc
    minutes: 33
friday_tip: "Páteční programování je nejproduktivnější v tichu s hudbou na pozadí (instrumentální, bez textů). Žáci jsou soustředěnější. Zkuste zapnout ambientní hudbu a pozorujte rozdíl v atmosféře."
---

# Projekt Hra II: Programování

## 💡 Metodický postup

### 1. Zahájení: Krátká rekapitulace a plán

<span class="act unplugged">✋ Bez počítače — 5 min</span>

Každý žák si přečte svůj GDD z minulé hodiny a napíše na kartičku:
- „Dnes udělám…" (3 konkrétní věci)
- „Začnu s…"

Učitel upozorní: „Mějte otevřený GDD vedle Scratch — je to váš návod."

### 2. Samostatná práce na projektu

<span class="act pc">💻 PC — 33 min</span>

<div class="zadani-pc">

Otevři **Scratch** (scratch.mit.edu) a programuj svou hru podle GDD z minulé hodiny. Postupuj v tomto doporučeném pořadí:

1. ☐ Scéna — nastav pozadí a přidej sprity (postavičky)
2. ☐ Pohyb hráče — ovládání šipkami nebo myší
3. ☐ Pohyb překážek/nepřátel — náhodná poloha nebo automatický pohyb
4. ☐ Detekce kolize — co se stane při dotyku?
5. ☐ Proměnné — skóre, čas nebo životy
6. ☐ Podmínka výhry/prohry

Průběžně projekt ukládej (Ctrl+S nebo tlačítko Uložit). Projekt pojmenuj: `7rocnik-hra-[tvoje jméno]`.

🐛 Nefunguje? Zkontroluj:
- Je vybrán správný sprite (ne pozadí)?
- Jsou bloky propojené (ne volně plovoucí)?
- Začíná program `po kliknutí na vlajku`?

</div>

Žáci pracují individuálně na svých herních projektech. Učitel aktivně obchází třídu a pomáhá.

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
