---
grade: 6
week: 20
time: 45
area: Digitální technologie a společnost
rvp_codes:
  - code: INF-INF-004-ZV9-013
    text: "Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje, na základě posouzení rizik ztráty, poškození či zneužití dat."
  - code: INF-INF-004-ZV9-014
    text: Diskutuje o fungování digitálních technologií určujících trendy ve světě.
goals:
  - "Žák popíše vlastnosti silného hesla (délka, různé typy znaků, žádné osobní údaje)"
  - Žák vytvoří silné heslo pomocí techniky věty (passphrase)
  - "Žák vysvětlí, proč nepoužíváme stejné heslo pro více účtů"
  - "Žák ví, komu heslo nikdy neříká — ani kamarádům, ani učiteli"
time_budget:
  - type: board
    minutes: 8
  - type: unplugged
    minutes: 10
  - type: pc
    minutes: 15
friday_tip: "V pátek zkuste **„Slovní šifra\"** — žáci vymyslí heslo z první písmene každého slova v oblíbené větě (např. „Mám rád pizzu s extra sýrem!\" → `MrPsEs!`). Pak si navzájem ukazují jen tu větu, ne výsledné heslo — cvičení paměti a kreativity zároveň."
---

# Bezpečné heslo: Trezor v hlavě

## 💡 Metodický postup

### 1. Úvod: Jak hackeři lámou hesla?

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel ukáže (bez osobních dat!) statistiky nejpoužívanějších hesel v ČR:

```
1. 123456        5. qwerty
2. heslo         6. password
3. 123456789     7. abc123
4. 12345678      8. 111111
```

Diskuse: „Kolik čas by trvalo uhádnout heslo '123456'?" → Milisekund. „A heslo '7kR#mZ!9vL\$'?" → Stovky let.

### 2. Aktivita: Hodnotíme hesla

<span class="act unplugged">✋ Bez počítače — 10 min</span>

Žáci dostanou kartičky s hesly a hodnotí je stupnicí 1–5:

| Heslo | Hodnocení | Proč? |
|-------|-----------|-------|
| `petr123` | 1 | Jméno + číslo — velmi slabé |
| `Pes123` | 2 | Krátké, snadno prolomitelné |
| `Praha2010!` | 3 | Delší, ale obsahuje osobní údaj |
| `Tr0mb0n!Zel%42` | 5 | Délka + různé znaky + bez osobních dat |
| `MámRádSněhulákySÚsměvem` | 5 | Passphrase — snadno zapamatovatelná, dlouhá |

Klíčové principy silného hesla:
- Délka ≥ 12 znaků
- Malá + velká písmena + čísla + speciální znaky
- Žádné osobní údaje (jméno, datum narození, město)

### 3. Technika věty — passphrase

<span class="act pc">💻 PC — 15 min</span>

<div class="zadani-pc">

Vytvoř si vlastní silné heslo pomocí techniky věty (passphrase). Postup:

1. Vymysli zapamatovatelnou větu (o aspoň 6 slovech): např. „Moje kočka se jmenuje Micka a má 3 roky!"
2. Vezmi **první písmeno** každého slova: `MksjMam3r!`
3. Přidej aspoň jeden speciální znak (`!`, `$`, `#`, `%`) do středu hesla

**Ověř sílu svého cvičného hesla** na [howsecureismypassword.net](https://howsecureismypassword.net).

> ⚠️ **Důležité:** Vkládej POUZE vymyšlená cvičná hesla — nikdy své skutečné heslo!

Zapiš do sešitu:
- Svou vymyšlenou větu (tu větu, ne výsledné heslo!)
- Jak dlouho by trvalo prolomit tvé cvičné heslo podle webu?

**Pro rychlé žáky:** Vyzkoušej heslo z jednoho slova (např. `heslo123`) a porovnej s passphrase. Jaký je rozdíl v čase prolomení?

</div>

### 4. Shrnutí: Desatero hesel (7 min)

Žáci společně sepíší „Desatero hesel" na tabuli. Klíčové body:
- Nikdy nikomu nesdílím heslo (ani kamarádovi, ani učiteli)
- Pro každou službu jiné heslo
- Heslo si nepisuji na papír přilepený u monitoru
- Správce hesel (Bitwarden, KeePass) je bezpečná alternativa

## 📂 Podklady

- **Správce hesel (zdarma, CZ podpora):** [Bitwarden](https://bitwarden.com) — open source, bezplatný, dostupný v češtině
- **Testování síly hesla (jen cvičná!):** [howsecureismypassword.net](https://howsecureismypassword.net)
- **Bezpečnost online (CZ):** [e-bezpeci.cz](https://www.e-bezpeci.cz) — Centrum PRVoK, materiály pro školy
- **NÚKIB doporučení:** [nukib.cz](https://www.nukib.cz) — Národní úřad pro kybernetickou bezpečnost vydává rady pro uživatele v češtině
- **Video (CZ):** YouTube „silné heslo jak vytvořit" nebo „bezpečné heslo pro děti"

!!! tip "Tip pro učitele"
    Nikdy po žácích nežádejte, aby vám ukázali nebo řekli svá skutečná hesla — to by bylo v přímém rozporu s tím, co je učíme. Všechny ukázky dělajte s vymyšlenými hesly. Pokud škola používá Google Workspace, doporučte žákům zapnout dvoufázové ověření u rodinných Gmail účtů doma.
