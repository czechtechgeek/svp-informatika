# 🔒 Protokoly: HTTP vs. HTTPS

> **Stav:** `⬜ Nekontrolováno`

### 📋 Kontext a cíle
> **RVP ZV (Informatika):** Digitální bezpečnost / Sítě
> **Kód:** `INF-INF-004-ZV9-013` – *Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje, na základě posouzení rizik ztráty, poškození či zneužití dat.*
> **Kód:** `INF-INF-004-ZV9-014` – *Diskutuje o fungování digitálních technologií určujících trendy ve světě.*

**Po hodině žák:**
* **Vysvětlí** rozdíl mezi protokoly HTTP a HTTPS vlastními slovy.
* **Popíše**, co je SSL/TLS certifikát a k čemu slouží.
* **Identifikuje** vizuální znaky zabezpečeného spojení v prohlížeči.
* **Posoudí** bezpečnost webu a rozhodne, zda mu svěřit citlivé údaje.

---

### 💡 Metodický postup (45 min)

#### 1. Motivační úvod: Co se děje, když zadáte heslo? (7 min)
*Tabule — výklad.*

Učitel nakreslí na tabuli jednoduchý diagram: žák u počítače → internet (oblak) → server. Položí otázku: „Kdo všechno vidí, co posíláme přes internet?" Žáci hádají. Učitel vysvětlí, že data putují přes desítky zařízení (routery, servery ISP) a každý mezičlánek může data číst — pokud nejsou šifrovaná.

Klíčové pojmy na tabuli:
- **Protokol** = pravidla komunikace (jako jazyk, kterým si počítače povídají)
- **HTTP** = HyperText Transfer Protocol — data jdou v čitelném textu
- **HTTPS** = HTTP + Secure — data jsou šifrovaná

---

#### 2. Přímé srovnání: HTTP vs. HTTPS (12 min)
*Tabule — přehled.*

Učitel projde tabulku srovnání, žáci si zapisují:

| Vlastnost | HTTP | HTTPS |
|-----------|------|-------|
| Šifrování | Ne — data jdou jako otevřený text | Ano — data jsou zašifrovaná |
| Adresa | Začíná `http://` | Začíná `https://` |
| Zámek v prohlížeči | Chybí nebo varování | Zobrazí se zámek 🔒 |
| Certifikát | Není potřeba | Vyžaduje SSL/TLS certifikát |
| Použití dnes | Zastaralé, vzácné | Standard pro všechny weby |
| Riziko | Útočník vidí vše (hesla, čísla karet) | Útočník vidí jen šifrovaný chaos |

**Analogie pro žáky:** HTTP je jako pohlednice — poštovní doručovatel ji může přečíst. HTTPS je jako dopis v zalepené obálce se speciálním zámkem, který umí otevřít jen příjemce.

Co je SSL/TLS certifikát? Je to digitální doklad totožnosti webu, vydaný důvěryhodnou autoritou (jako průkaz totožnosti). Certifikát říká: „Opravdu jsi na webu Google.com, ne na podvrhnuté kopii."

---

#### 3. Praktická aktivita: Průzkumník prohlížeče (18 min)
*Práce na PC — průzkum webu.*

Žáci pracují samostatně na počítačích. Úkol: prozkoumat 5 různých webů a vyplnit tabulku.

Weby k prozkoumání (žáci je otevřou v prohlížeči):
1. `https://www.csas.cz` (banka)
2. `https://www.seznam.cz` (vyhledávač)
3. `https://www.alza.cz` (e-shop)
4. Libovolný web, který sami navštěvují
5. Libovolný web, který sami navštěvují

Co zaznamenat pro každý web:
- Má HTTPS? (ano/ne)
- Kde najdu zámek? (popište/screenshot)
- Kdo vydal certifikát? (kliknout na zámek → Certifikát → Vydavatel)
- Svěřil bych mu heslo/číslo karty? (ano/ne/proč)

Bonusový úkol: Zkuste najít web, který ještě používá HTTP — co prohlížeč zobrazí?

---

#### 4. Reflexe a shrnutí: Kdy HTTPS nestačí (8 min)
*Diskuze.*

Diskuse: „Znamená HTTPS, že je web bezpečný?" Odpověď: NE — HTTPS zajišťuje jen šifrované spojení, ne důvěryhodnost obsahu. Phishingový web může mít HTTPS a certifikát.

Shrnutí pravidel pro žáky:
1. Vždy zkontroluj HTTPS před zadáním hesla nebo čísla karty
2. Klikni na zámek a zkontroluj, komu certifikát patří
3. HTTPS je nutná podmínka, ale ne záruka bezpečnosti webu
4. Prohlížeč tě varuje červenou barvou nebo „Není zabezpečeno" — nikdy tato varování ignoruj

---

### 🛠️ Zdroje a nástroje

* **Web — Mozilla Observatory:** [observatory.mozilla.org](https://observatory.mozilla.org) — nástroj pro kontrolu bezpečnosti webů, žáci mohou zadat libovolný web
* **Video (CZ):** YouTube — „Jak funguje HTTPS" nebo „SSL TLS šifrování česky" — dobré vizuální vysvětlení handshake
* **Web — SSL Labs:** [ssllabs.com/ssltest](https://www.ssllabs.com/ssltest/) — pokročilý test SSL certifikátu webu
* **Propojení s praxí:** Bankovní aplikace, e-shopy, školní systémy — vše, co žáci denně používají

---

> 💡 **Tip pro učitele:**
> Nejsilnější moment hodiny je, když žáci sami v prohlížeči kliknou na zámek a zjistí, kdo certifikát vydal. Ukažte jim také, jak vypadá varování prohlížeče při HTTP webu (nebo při expirovaném certifikátu) — v Chromu je to červený výkřičník. Pokud škola používá vlastní systém (Bakaláři, Moodle), prověřte s žáky i jeho certifikát — žáci to ocení jako reálný kontext.

> 💬 **Tip pro pátek:** Otevřete v hodině několik reálných webů (e-shop, banka, zpravodajský web) a nechte žáky hledat zámek a HTTPS v adresním řádku. Okamžitě propojíte teorii s praxí, kterou žáci každý den používají.
