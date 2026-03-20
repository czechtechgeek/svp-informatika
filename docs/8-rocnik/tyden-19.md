# 🔐 Šifrování: Od Caesarovy šifry po RSA

> **Stav:** `⬜ Nekontrolováno`

### 📋 Kontext a cíle
> **RVP ZV (Informatika):** Bezpečnost / Kryptografie
> **Kód:** `INF-INF-004-ZV9-013` – *Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje, na základě posouzení rizik ztráty, poškození či zneužití dat.*
> **Kód:** `INF-INF-002-ZV9-006` – *Rozdělí problém na jednotlivě řešitelné části a navrhne postupy a algoritmy pro jeho řešení.*

**Po hodině žák:**
* **Vysvětlí** princip šifrování a dešifrování vlastními slovy.
* **Ručně zašifruje** a dešifruje zprávu pomocí Caesarovy šifry.
* **Porovná** symetrické a asymetrické šifrování a uvede příklad použití.
* **Popíše**, proč je RSA důležité pro bezpečnost internetu.

---

### 💡 Metodický postup (45 min)

#### 1. Úvod: Proč lidé šifrovali zprávy? (7 min)
*Tabule — výklad.*

Učitel stručně představí historický kontext: Julius Caesar posílal vojenské zprávy tak, aby je nepřítel nerozuměl. Každé písmeno posunul v abecedě o 3 místa (A→D, B→E, C→F…). Zpráva „AHOJ" se stala „DKRM". Stejný princip — posun — je klíč.

Na tabuli ukázkový převodník:

```
Originál: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Šifrovaně (posun 3): D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

Otázka pro třídu: „Co je slabina Caesarovy šifry?" — Žáci hádají: je jen 25 různých posunů, metodou pokus-omyl se dá prolomit za pár minut.

---

#### 2. Praktická aktivita: Luštění a šifrování (15 min)
*Aktivita bez počítače.*

**Část A — Zašifruj zprávu (5 min):** Každý žák dostane list s abecedním klíčem (posun 5). Úkol: zašifrovat svou zprávu (větu o 4–6 slovech, třeba „DNES MÁM HODINU INFORMATIKY").

**Část B — Předej a rozluštěj (5 min):** Žáci si vymění papíry se sousedem. Soused musí zprávu rozluštit — ale nezná posun! Musí ho uhodnout (je to algoritmus: zkus posun 1, 2, 3… dokud nedává smysl).

**Část C — Diskuse (5 min):** Jak rychle jste uhodli posun? Co by pomohlo (znalost jazyka, nejčastější písmena)? Toto se jmenuje frekvenční analýza — útok na jednoduché šifry.

---

#### 3. Od Caesara k modernímu šifrování (13 min)
*Tabule — přehled evoluce šifrování.*

Učitel přehledně vysvětlí evoluci šifrování:

| Typ šifrování | Příklad | Princip | Problém |
|---------------|---------|---------|---------|
| Substituční (historické) | Caesarova šifra | Jeden klíč, jednoduchý posun | Snadno prolomitelné |
| Symetrické | AES (Wi-Fi, ZIP) | Jeden klíč pro šifrování i dešifrování | Jak bezpečně předat klíč? |
| Asymetrické | RSA (HTTPS, e-mail) | Veřejný klíč (šifruje) + soukromý klíč (dešifruje) | Pomalejší, ale bezpečné |

**Analogie pro RSA:** Veřejný klíč je jako poštovní schránka — každý může hodit dopis dovnitř (zašifrovat). Soukromý klíč je jako klíč od schránky — jen majitel ho má a může dopis vytáhnout (dešifrovat).

Konkrétní příklad použití: Když se přihlásíte do Google, váš prohlížeč použije veřejný klíč Googlu, aby zašifroval vaše heslo. Jen Google (s soukromým klíčem) ho může přečíst.

---

#### 4. Kvíz a shrnutí (10 min)
*Kvíz.*

Rychlý kvíz (ústně nebo na papíře — 5 otázek):

1. Caesarova šifra s posunem 3 — co je šifrované slovo pro „KOT"? (odpověď: NRW)
2. Kolik různých posunů má Caesarova šifra? (25)
3. Který typ šifrování používá dva různé klíče? (asymetrické / RSA)
4. Co znamená „veřejný klíč"? (klíč, který může mít kdokoli — slouží k šifrování)
5. Proč je Caesarova šifra nebezpečná? (malý počet kombinací, frekvenční analýza)

Závěrečné shrnutí: Šifrování je matematika aplikovaná na bezpečnost. Princip je starý tisíce let, ale moderní šifry (AES-256, RSA-2048) jsou na dnešních počítačích prakticky neprolomitelné.

---

### 🛠️ Zdroje a nástroje

* **Online nástroj:** [cryptii.com](https://cryptii.com) — interaktivní šifrování/dešifrování včetně Caesarovy šifry, Vigenerovy šifry i moderních algoritmů
* **Video (CZ):** YouTube — „Jak funguje asymetrické šifrování" nebo „RSA šifrování jednoduše" — dobré vizuální vysvětlení
* **Web (EN):** Khan Academy sekce Cryptography — výborné interaktivní lekce zdarma
* **Pracovní list:** Připravte list s abecedním klíčem (posun 5) pro každého žáka — ušetří čas při aktivitě

---

> 💡 **Tip pro učitele:**
> Žáci bývají překvapeni, že šifrování je v podstatě matematika — sčítání a násobení čísel. Nebojte se zmínit, že prolomení RSA-2048 by trvalo i nejrychlejšímu počítači světa miliardy let. To žáky obvykle zaujme. Pokud máte čas, zkuste online nástroj cryptii.com společně promítat — žáci mohou v reálném čase vidět, jak se zpráva šifruje.

> 💬 **Tip pro pátek:** Nechte žáky napsat zprávu Caesarovou šifrou (posunutí o 3) a předejte ji sousedovi k luštění — fyzická aktivita bez počítače funguje výborně jako icebreaker a žáci si princip zapamatují lépe než z výkladu.
