# 5. Umělá inteligence — Nauč počítač

<div class="lesson-meta">
  <span class="lm-badge lm-grade">🎯 Kroužek</span>
  <span class="lm-badge lm-week">💻 PC aktivita</span>
  <span class="lm-badge lm-time">⏱️ 60–90 min</span>
  <span class="lm-badge lm-area">🗂️ AI a strojové učení</span>
</div>

---

## 🎯 Co se naučíš?

- Co je umělá inteligence a jak se "učí"
- Jak natrénovat jednoduchý AI model bez programování
- Proč AI dělá chyby a jak je opravit (více a lepších dat!)

---

## 🤖 Co je strojové učení?

Normální program říká počítači přesně **co má dělat** (krok po kroku).
Strojové učení funguje jinak: místo příkazů dáváme počítači **příklady** a on si pravidla **najde sám**.

> **Příklad:** Chceme, aby počítač poznal kočku na fotce.
> → Ukážeme mu 1000 fotek koček (a 1000 fotek NE-koček)
> → Počítač si "vybuduje vzor" — co mají kočky společného
> → Teď pozná kočku i na nové fotce, kterou nikdy neviděl

---

## 🚀 Začínáme

**Otevři prohlížeč a přejdi na:**
👉 [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com)

Klikni na **Začít** (Get Started) — žádná registrace není potřeba!

---

## 📋 Postup

### Krok 1 — Vyber typ projektu

Teachable Machine nabízí tři typy:

| Typ | Popis |
|-----|-------|
| **Image Project** | Počítač rozpoznává obrázky z kamery 📸 |
| **Audio Project** | Počítač rozpoznává zvuky nebo slova 🎤 |
| **Pose Project** | Počítač rozpoznává polohu těla 🕺 |

👉 **Doporučujeme začít s Image Project** (nejjednodušší a nejzábavnější)

---

### Krok 2 — Vyber si, co budete rozpoznávat

Vymysli **dvě nebo tři třídy** (skupiny věcí), které chceš naučit počítač rozlišovat.

Nápady:

| Třída 1 | Třída 2 | Třída 3 |
|---------|---------|---------|
| Palec nahoru 👍 | Palec dolů 👎 | — |
| Otevřená ruka ✋ | Pěst ✊ | Mírumilovné „V" ✌️ |
| Pero 🖊️ | Guma | Pravítko |
| Tvář s úsměvem 😊 | Tvář bez úsměvu | — |
| Papír | Nůžky | Kámen ✊ |

---

### Krok 3 — Nasbírej data (tréninkové příklady)

1. Pojmenuj třídy (klikni na **Class 1**, **Class 2**)
2. U každé třídy klikni na **Webcam** (nebo **Upload**)
3. Drž tlačítko **Nahrát** a pohybuj se / měň polohu — nasbírej **aspoň 50–100 obrázků** na každou třídu

!!! warning "Důležité pro dobré výsledky"
    - Nahrávej z různých úhlů a vzdáleností
    - Zkus různé osvětlení
    - Čím více obrázků, tím chytřejší AI!

---

### Krok 4 — Trénink

- Klikni na **Trénovat model** (Train Model)
- Počkej — může to trvat 30–60 sekund
- Sleduj, jak se snižuje chyba (číslo **Loss** klesá)

---

### Krok 5 — Testování

- V sekci **Náhled** (Preview) otestuj svůj model kamerou
- Zkus různé podmínky — jiné světlo, jiná vzdálenost
- **Funguje to?** Co ho plete?

!!! info "AI dělá chyby — a to je normální"
    Pokud model nefunguje dobře, zkus: přidat více trénovacích obrázků, nebo nahrát různější polohy.

---

### Krok 6 — Export a sdílení

- Klikni na **Exportovat model**
- Zvolte **Nahrát na cloud** (Upload) — dostanete odkaz, který lze sdílet

---

## ✅ Co ukázat učiteli

- Ukázka modelu v akci (živé rozpoznávání kamerou)
- Vysvětli: **Co jsi naučil/a počítač rozpoznávat?** **Co mu dělalo problémy?**

---

## 🏆 Bonusové výzvy

1. **Audio model:** Zkus Audio Project — nauč počítač rozpoznat tvé jméno vs. jiné slovo
2. **Pose model:** Nauč počítač rozeznat dřep, stoj a výpon
3. **Scratch + AI:** Na stránce Teachable Machine lze exportovat model do Scratche (Extensions → Teachable Machine) — postava v Scratchi reaguje na gesta!
4. **Výzkumná otázka:** Co se stane, když jednu třídu natrénoješ s 10 obrázky a druhou s 200? Je výsledek spravedlivý?

---

<div class="resources" markdown="1">
<div class="resources-title">📂 Zdroje</div>

  - **Teachable Machine:** [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com) — hlavní nástroj (Google, zdarma)
  - **Machine Learning for Kids (CZ/EN):** [machinelearningforkids.co.uk](https://machinelearningforkids.co.uk) — textové hry a Scratch projekty s AI
  - **Quick, Draw! (Google):** [quickdraw.withgoogle.com](https://quickdraw.withgoogle.com) — zahraj si hru s AI, která hádá tvé kresby
  - **AI Experiments:** [experiments.withgoogle.com/collection/ai](https://experiments.withgoogle.com/collection/ai) — sbírka AI experimentů od Googlu

</div>

!!! tip "Tip pro učitele"
    Teachable Machine nepotřebuje žádný účet a běží v prohlížeči — stačí kamera (integrovaná v noteboocích). Nejlepší zážitek mají žáci, když model trénují ve skupině a pak ho navzájem "hackují" (zkouší, jak model zmást). Machine Learning for Kids nabízí předpřipravené projekty s textovými modely — vhodné pokud kamery nejsou k dispozici.
