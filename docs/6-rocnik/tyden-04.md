---
grade: 6
week: 4
time: 45
area: "Data, informace a modelování"
rvp_codes:
  - code: INF-INF-001-ZV9-002
    text: Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - "Žák vysvětlí, proč počítač ukládá text jako čísla"
  - "Žák použije jednoduchou substituční šifru (A=1, B=2 … Z=26) k zakódování slova"
  - Žák přečte zprávu zašifrovanou spolužákem pomocí stejné tabulky
  - Žák pochopí princip ASCII jako standardu pro kódování textu
  - Žák zapíše své jméno v číselném kódu
time_budget:
  - type: discussion
    minutes: 5
  - type: unplugged
    minutes: 15
  - type: pc
    minutes: 15
friday_tip: "Pro \"páteční efekt\" ukažte žákům **ASCII Art**. Stačí do vyhledávače zadat \"Star Wars ASCII Art\" nebo použít generátor obrázků z textu. Ukazuje to kreativní využití standardu, který se žáci právě naučili, a je to vizuálně velmi vděčné."
---

# 

## 💡 Metodický postup

### 1. Úvod: Jak počítač čte text?

<span class="act discussion">💬 Diskuse — 5 min</span>

Učitel se zeptá: „Pokud počítač pracuje jen s čísly, jak může zobrazit písmeno A?"

Krátká diskuse → žáci hádat. Učitel vysvětlí: každé písmeno má přiřazené číslo — to je princip kódování. Ukáže na tabuli jednoduchou tabulku A=1, B=2 ... Z=26.

### 2. Aktivita: Zašifruj své jméno

<span class="act unplugged">✋ Bez počítače — 15 min</span>

Každý žák dostane nebo si opíše tabulku:

```
A=1   B=2   C=3   D=4   E=5   F=6   G=7
H=8   I=9   J=10  K=11  L=12  M=13  N=14
O=15  P=16  Q=17  R=18  S=19  T=20  U=21
V=22  W=23  X=24  Y=25  Z=26
```

Úkol:
1. Zakódujte své křestní jméno jako čísla oddělená pomlčkami
2. Napište kód na lísteček a předejte sousedovi
3. Soused dekóduje jméno zpět na písmena

Příklad: `ADAM = 1-4-1-13`

### 3. Aktivita: ASCII detektiv

<span class="act pc">💻 PC — 15 min</span>

<div class="zadani-pc" markdown="1">

Otevři [ascii.cl](https://ascii.cl) a prozkoumej skutečnou ASCII tabulku.

**Úloha 1:** Odpověz na tyto otázky (zapiš odpovědi do sešitu nebo poznámkového bloku):
- Jaké číslo má velké písmeno **A**? A malé **a**? Proč jsou jiná?
- Co znamená číslo **32**?

**Úloha 2:** Napiš libovolnou větu (aspoň 5 slov) jako ASCII čísla v desítkové soustavě — každé písmeno nahraď jeho číslem z tabulky, čísla odděl mezerami.

**Úloha 3:** Svou zakódovanou zprávu předej spolužákovi (na papíře nebo přes chat). Spolužák ji rozluští pomocí ASCII tabulky — pak si role vyměňte.

**Pro rychlé žáky:** Zjisti, jaké číslo odpovídá emoji 😀 (nápověda: hledej „Unicode code point"). Porovnej s ASCII — proč ASCII emoji neobsahuje?

</div>

### 4. Shrnutí (5 min)

Učitel otevře Poznámkový blok, napíše slovo, uloží a řekne: „Tento soubor je jen čísla v paměti počítače — ASCII kód."

**Klíčové pojmy:** kódování, ASCII, standard, byte

## 📂 Podklady

- **ASCII tabulka online:** [ascii.cl](https://ascii.cl) — přehledná tabulka s dec/hex/char
- **ASCII tabulka alternativa:** [asciitable.com](https://www.asciitable.com)
- **Kódování a šifrování (CZ):** [umimeinformatiku.cz](https://www.umimeinformatiku.cz) — česká platforma s interaktivními cvičeními na kódování a šifrování, sekce „Informace a data"
- **Pracovní list:** Připravte tabulku A=1…Z=26 pro každého žáka + 3 předpřipravené zprávy k dekódování jako tištěný list

!!! tip "Tip pro učitele"
    Pro rozšíření ukažte rozdíl mezi ASCII (128 znaků) a Unicode (miliony znaků) — jak se zapíše emoji 😀? Odpověď je číslo 128512. Žáci jsou nadšeni, když zjistí, že i emoji je „jen číslo".
