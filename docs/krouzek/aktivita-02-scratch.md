# 2. Scratch — Animace a hry

<div class="lesson-meta">
  <span class="lm-badge lm-grade">🎯 Kroužek</span>
  <span class="lm-badge lm-week">💻 PC aktivita</span>
  <span class="lm-badge lm-time">⏱️ 60–90 min</span>
  <span class="lm-badge lm-area">🗂️ Tvorba animací a her</span>
</div>

---

## 🎯 Co se naučíš?

- Jak tvořit vlastní animace a jednoduché hry
- Jak přidat zvuky, pohyb a interakci s myší nebo klávesnicí
- Základy programovací logiky (smyčky, události, podmínky)

---

## 🚀 Začínáme

**Otevři prohlížeč a přejdi na:**
👉 [scratch.mit.edu](https://scratch.mit.edu)

Klikni na **Začít tvořit** — nemusíš se registrovat (ale pokud se zaregistruješ, tvoje projekty se uloží!).

---

## 📋 Postup

### Krok 1 — Prohlídka prostředí

Scratch má tři hlavní části:

| Část | Co tam je |
|------|-----------|
| **Scéna** (vlevo) | Kde se odehrává tvůj projekt — postavy a pozadí |
| **Bloky** (uprostřed) | Barevné bloky = příkazy (přetahuj na plochu vpravo) |
| **Skript** (vpravo) | Tady skládáš bloky dohromady = tvůj program |

---

### Krok 2 — Vyber si projekt

Vyber **jednu** z těchto miniprojectů:

=== "🐱 Animace — Kočka tančí"
    **Cíl:** Udělej animaci, kde kočka tančí na hudbu

    1. Klikni na kočku (Sprite1)
    2. Přidej blok **Události → Když klepnu na 🚩**
    3. Přidej **Zvuk → Přehraj zvuk** — vyber hudbu
    4. Přidej **Pohyb → Jdi na x:0 y:0** (střed scény)
    5. Přidej smyčku **Ovládání → Opakuj stále**
    6. Dovnitř smyčky přidej:
       - **Vzhled → Příští kostým** (přepíná animaci)
       - **Ovládání → Čekej 0.3 sekund**
    7. Klikni na 🚩 a sleduj!

=== "🎮 Jednoduchá hra — Chytej hvězdy"
    **Cíl:** Pohybuj postavou a sbírej hvězdy

    1. Smaž kočku a přidej jinou postavu (tlačítko ➕ vpravo dole)
    2. Přidej **hvězdu** jako druhou postavu
    3. Pro **hráče** nastav pohyb klávesnicí:
       - Blok: **Události → Když stisknuto tlačítko [šipka vpravo]**
       - Přidej: **Pohyb → Změň x o 10**
       - Opakuj pro všechny šipky (vlevo, nahoru, dolů)
    4. Pro **hvězdu** přidej:
       - **Když klepnu na 🚩 → Opakuj stále → Čekej do (dotýká se [hráč]?) → Jdi na náhodnou pozici**
    5. Přidej proměnnou **Skóre** a přičítej +1 při dotyku

=== "🎨 Interaktivní kresba"
    **Cíl:** Nakresli cokoliv pohybem myši

    1. Vyber prázdnou scénu (černé pozadí)
    2. Na kočku přidej:
       - **Události → Když klepnu na 🚩**
       - **Ovládání → Opakuj stále**
       - Dovnitř: **Pohyb → Jdi na [pozice myši]**
       - Dovnitř: **Pero → Pero dolů** + **Pero → Nastav barvu pera na [náhodná barva]**
    3. Přidej tlačítko pro smazání kreslení (**Pero → Vymaž vše**)
    4. Experimentuj s tloušťkou a barvou!

---

### Krok 3 — Úpravy a vylepšení

- Zkus přidat **vlastní pozadí** (klikni na ikonku hor vpravo dole)
- Přidej **vlastní zvuky** (záložka Zvuky u postavy)
- Přejmenuj projekt a klikni na **Sdílet** (pokud máš účet)

---

## ✅ Co ukázat učiteli

- Ukaž projekt živě (klikni na 🚩)
- Vysvětli: **Co tvůj projekt dělá?** **Jaký blok byl nejzajímavější?**

---

## 🏆 Bonusové výzvy

1. **Přidej level systém:** Po dosažení 10 bodů se scéna změní
2. **Multiplayer:** Přidej druhého hráče ovládaného jinými klávesami (WASD)
3. **Zvukový vizualizér:** Postava mění velikost podle hlasitosti mikrofonu (blok **Hlasitost**)
4. **Remix:** Najdi cizí projekt na Scratch.mit.edu, klikni "Podívat se dovnitř" a uprav ho po svém

---

<div class="resources" markdown="1">
<div class="resources-title">📂 Zdroje</div>

  - **Scratch (CZ):** [scratch.mit.edu](https://scratch.mit.edu) — přepni na češtinu v levém dolním rohu
  - **Tutoriály:** Na Scratchi klikni na **Tutoriály** (záložka nahoře) — jsou v češtině
  - **Scratch Wiki:** [en.scratch-wiki.info](https://en.scratch-wiki.info) — podrobné vysvětlení každého bloku
  - **Inspirace:** [scratch.mit.edu/explore/projects/games](https://scratch.mit.edu/explore/projects/games) — hotové projekty k prozkoumání

</div>

!!! tip "Tip pro učitele"
    Scratch funguje v prohlížeči bez instalace. Nejlepší je vytvořit sdílenou třídu (scratch.mit.edu/educators) — žáci se přihlásí a jejich projekty jsou viditelné. Alternativně žáci sdílejí odkaz na projekt nebo ho exportují jako soubor .sb3.
