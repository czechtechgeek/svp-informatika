# Algoritmus v kuchyni: Recept jako posloupnost kroků

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Algoritmizace a programování
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-01</span><span style="color: #374151;">Žák rozloží problém na podproblémy</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-2-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-2-02</span><span style="color: #374151;">Žák popíše algoritmus (grafické vyjádření)</span></div>

## 💬 Tip pro pátek
Pátky v 6. třídě snesou trochu humoru. Pokud děláte aktivitu s robotem-kuchařem, nechte žáky, aby vás "naprogramovali" i k tak jednoduché věci, jako je **otevření fixy nebo usednutí na židli**. Ukáže se, že i zdánlivě banální pohyby vyžadují desítky přesných instrukcí (uchop, stiskni, táhni směrem nahoru...).

## 🎯 Cíle hodiny

- Žák definuje pojem algoritmus jako přesnou posloupnost kroků vedoucích k cíli
- Žák zapíše algoritmus pro jednoduchou každodenní činnost (recept, ranní příprava)
- Žák rozpozná chybu v algoritmu a opraví ji
- Žák pochopí, proč musí být instrukce jednoznačné a v správném pořadí

## 💡 Metodický postup

### 1. Úvod: Robot v kuchyni (5 min) — bez počítače

Učitel přinese (nebo nakreslí) obrázek robota kuchaře a řekne:

> „Tento robot umí jen přesně to, co mu napíšeme. Nerozumí výrazům jako ‚trochu', ‚podle chuti' nebo ‚zamíchej to'. Jak mu napíšeme recept?"

Krátká diskuse — žáci zjistí, že robot potřebuje přesné, jednoznačné instrukce.

### 2. Aktivita: Recept pro robota (20 min) — bez počítače

#### Varianta A — PB&J sendvič (klasická CS aktivita)

Učitel hraje roli robota. Jeden žák mu diktuje instrukce jak udělat sendvič — učitel instrukce doslovně plní (záměrně špatně, pokud nejsou přesné).

Příklady nejednoznačných instrukcí a co robot udělá:
- „Vezmi chléb" → robot vezme celý bochník i s obalem
- „Natři máslo na chleba" → robot hodí máslo na chleba bez rozetření
- „Přilož druhou vrstvu" → robot přiloží celý chleba vedle, ne na sendvič

Třída diskutuje a opravuje instrukce.

#### Varianta B — Napiš algoritmus pro ranní rutinu

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

- **Aktivity o algoritmech (CZ):** [imysleni.cz](https://imysleni.cz) — sekce „Algoritmy a programování", aktivity bez PC pro ZŠ v češtině
- **Vývojový diagram online:** [app.diagrams.net](https://app.diagrams.net) — zdarma, bez registrace, ukládá do Google Drive, dostupné v češtině
- **Video (CZ):** [ČT edu — Programování a algoritmy](https://edu.ceskatelevize.cz/predmet/informatika) — hledejte „algoritmus" nebo „jak funguje program"
- **Rozšíření:** Žáci naprogramují recept jako sekvenci bloků v [Scratch](https://scratch.mit.edu) — každý příkaz = jeden blok

!!! tip "Tip pro učitele"
    Aktivita s robotem-kuchařem je velmi zábavná a zapamatovatelná — žáci ji citují ještě v 9. třídě při debuggingu. Čím doslovněji hrajete robota, tím lépe pochopí potřebu přesnosti. Pokud máte reálný sendvič k dispozici, je to ještě efektnější.

