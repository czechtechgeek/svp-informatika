# Algoritmus v kuchyni: Recept jako posloupnost kroků

## 🎯 Cíle hodiny

- Žák definuje pojem algoritmus jako přesnou posloupnost kroků vedoucích k cíli
- Žák zapíše algoritmus pro jednoduchou každodenní činnost (recept, ranní příprava)
- Žák rozpozná chybu v algoritmu a opraví ji
- Žák pochopí, proč musí být instrukce jednoznačné a v správném pořadí

## 💡 Metodický postup

### 1. Úvod: Robot v kuchyni (5 min) — unplugged

Učitel přinese (nebo nakreslí) obrázek robota kuchaře a řekne:

> „Tento robot umí jen přesně to, co mu napíšeme. Nerozumí výrazům jako ‚trochu', ‚podle chuti' nebo ‚zamíchej to'. Jak mu napíšeme recept?"

Krátká diskuse — žáci zjistí, že robot potřebuje přesné, jednoznačné instrukce.

### 2. Aktivita: Recept pro robota (20 min) — unplugged

**Varianta A — PB&J sendvič** (klasická CS aktivita):
Učitel hraje roli robota. Jeden žák mu diktuje instrukce jak udělat sendvič — učitel instrukce doslovně plní (záměrně špatně, pokud nejsou přesné).

Příklady nejednoznačných instrukcí a co robot udělá:
- „Vezmi chléb" → robot vezme celý bochník i s obalem
- „Natři máslo na chleba" → robot hodí máslo na chleba bez rozetření
- „Přilož druhou vrstvu" → robot přiloží celý chleba vedle, ne na sendvič

Třída diskutuje a opravuje instrukce.

**Varianta B — Napiš algoritmus pro ranní rutinu:**
Každý žák napíše minimálně 10 kroků svého rána (vstát, čistit zuby, snídat...) tak, aby tomu rozuměl robot. Sousedé si navzájem instrukce zkontrolují.

### 3. Aktivita: Flowchart — vývojový diagram (15 min) — PC nebo papír

Žáci nakreslí jednoduchý vývojový diagram pro algoritmus „Jak připravit čaj?":

```
Začátek
  ↓
Naplň konvici vodou
  ↓
Zapni konvici
  ↓
Voda je horká? → NE → Počkej 1 minutu → zpět na otázku
  ↓ ANO
Vlož čajový sáček do hrníčku
  ↓
Zalijte horkou vodou
  ↓
Počkej 3 minuty
  ↓
Vyhoď sáček → Konec
```

Nástroj: [draw.io](https://app.diagrams.net) nebo tužka a papír.

### 4. Shrnutí (5 min)

**3 vlastnosti dobrého algoritmu:**
1. **Konečnost** — musí někdy skončit
2. **Jednoznačnost** — každý krok má přesně jeden výsledek
3. **Správné pořadí** — kroky musí jít za sebou logicky

## 📂 Podklady

- **Aktivita PB&J:** [CS Unplugged — Algorithms](https://csunplugged.org/en/topics/sorting-algorithms/) — aktivity o algoritmech bez PC
- **Vývojový diagram online:** [app.diagrams.net](https://app.diagrams.net) — zdarma, bez registrace, ukládá do Google Drive
- **Video (EN):** „Algorithm — Crash Course Computer Science #13" na YouTube (~12 min)
- **Video (CZ):** Vyhledejte „algoritmus pro děti" na YouTube — kanál KhanAcademy CZ
- **Rozšíření:** Žáci naprogramují recept jako sekvenci bloků v [Scratch](https://scratch.mit.edu) — každý příkaz = jeden blok

!!! tip "Tip pro učitele"
    Aktivita s robotem-kuchařem je velmi zábavná a zapamatovatelná — žáci ji citují ještě v 9. třídě při debuggingu. Čím doslovněji hrajete robota, tím lépe pochopí potřebu přesnosti. Pokud máte reálný sendvič k dispozici, je to ještě efektnější.

