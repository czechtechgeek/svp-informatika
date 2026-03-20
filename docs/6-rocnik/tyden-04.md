# Kódování textu: Každé písmeno má své číslo

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Data, informace a modelování
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-001-ZV9-002" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-001-ZV9-002</span><span style="color: #374151;">Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-009" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-009</span><span style="color: #374151;">Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.</span></div>

## 💬 Tip pro pátek
Pro "páteční efekt" ukažte žákům **ASCII Art**. Stačí do vyhledávače zadat "Star Wars ASCII Art" nebo použít generátor obrázků z textu. Ukazuje to kreativní využití standardu, který se žáci právě naučili, a je to vizuálně velmi vděčné.

## 🎯 Cíle hodiny

- Žák vysvětlí, proč počítač ukládá text jako čísla
- Žák použije jednoduchou substituční šifru (A=1, B=2 … Z=26) k zakódování slova
- Žák přečte zprávu zašifrovanou spolužákem pomocí stejné tabulky
- Žák pochopí princip ASCII jako standardu pro kódování textu
- Žák zapíše své jméno v číselném kódu

## 💡 Metodický postup

### 1. Úvod: Jak počítač čte text? (5 min) — diskuse

Učitel se zeptá: „Pokud počítač pracuje jen s čísly, jak může zobrazit písmeno A?"

Krátká diskuse → žáci hádat. Učitel vysvětlí: každé písmeno má přiřazené číslo — to je princip kódování. Ukáže na tabuli jednoduchou tabulku A=1, B=2 ... Z=26.

### 2. Aktivita: Zašifruj své jméno (15 min) — bez počítače

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

### 3. Aktivita: ASCII detektiv (15 min) — PC

Žáci otevřou [ascii.cl](https://ascii.cl) a prozkoumají skutečnou ASCII tabulku.

Úkoly:
- Jaké číslo má velké A? A malé a? Proč jsou jiná?
- Co znamená číslo 32? (mezera)
- Napište libovolnou větu (5 slov) jako ASCII čísla v desítkové soustavě
- Pošlete zakódovanou zprávu spolužákovi (na papíře nebo do chatu), ten ji rozluští

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

