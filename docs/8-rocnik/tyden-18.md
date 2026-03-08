# Protokoly: HTTP vs. HTTPS

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Digitální bezpečnost / Sítě
- **Výstup:** <div class="curriculumTag" data-code="I-9-4-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-4-02</span><span style="color: #374151;">Žák chrání sebe i ostatní při práci v digitálním prostředí</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-4-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-4-01</span><span style="color: #374151;">Žák kriticky hodnotí digitální obsah a chování online</span></div>

## 💬 Tip pro pátek
Otevřete v hodině několik reálných webů (e-shop, banka, zpravodajský web) a nechte žáky hledat zámek a HTTPS v adresním řádku. Okamžitě propojíte teorii s praxí, kterou žáci každý den používají.

## 🎯 Cíle hodiny

- Žák vysvětlí rozdíl mezi protokoly HTTP a HTTPS vlastními slovy
- Žák popíše, co je SSL/TLS certifikát a k čemu slouží
- Žák identifikuje vizuální znaky zabezpečeného spojení v prohlížeči
- Žák posoudí bezpečnost webu a rozhodne, zda mu svěřit citlivé údaje

## 💡 Metodický postup

### 1. Motivační úvod: Co se děje, když zadáte heslo? (7 min) — tabule

Učitel nakreslí na tabuli jednoduchý diagram: žák u počítače → internet (oblak) → server. Položí otázku: „Kdo všechno vidí, co posíláme přes internet?" Žáci hádají. Učitel vysvětlí, že data putují přes desítky zařízení (routery, servery ISP) a každý mezičlánek může data číst — pokud nejsou šifrovaná.

Klíčové pojmy na tabuli:
- **Protokol** = pravidla komunikace (jako jazyk, kterým si počítače povídají)
- **HTTP** = HyperText Transfer Protocol — data jdou v čitelném textu
- **HTTPS** = HTTP + Secure — data jsou šifrovaná

### 2. Přímé srovnání: HTTP vs. HTTPS (12 min) — tabule

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

### 3. Praktická aktivita: Průzkumník prohlížeče (18 min) — PC

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

### 4. Reflexe a shrnutí: Kdy HTTPS nestačí (8 min) — diskuse

Diskuse: „Znamená HTTPS, že je web bezpečný?" Odpověď: NE — HTTPS zajišťuje jen šifrované spojení, ne důvěryhodnost obsahu. Phishingový web může mít HTTPS a certifikát.

Shrnutí pravidel pro žáky:
1. Vždy zkontroluj HTTPS před zadáním hesla nebo čísla karty
2. Klikni na zámek a zkontroluj, komu certifikát patří
3. HTTPS je nutná podmínka, ale ne záruka bezpečnosti webu
4. Prohlížeč tě varuje červenou barvou nebo „Není zabezpečeno" — nikdy tato varování ignoruj

## 📂 Podklady

- **Web — Mozilla Observatory:** [observatory.mozilla.org](https://observatory.mozilla.org) — nástroj pro kontrolu bezpečnosti webů, žáci mohou zadat libovolný web
- **Video (CZ):** YouTube — „Jak funguje HTTPS" nebo „SSL TLS šifrování česky" — dobré vizuální vysvětlení handshake
- **Web — SSL Labs:** [ssllabs.com/ssltest](https://www.ssllabs.com/ssltest/) — pokročilý test SSL certifikátu webu
- **Propojení s praxí:** Bankovní aplikace, e-shopy, školní systémy — vše, co žáci denně používají

!!! tip "Tip pro učitele"
    Nejsilnější moment hodiny je, když žáci sami v prohlížeči kliknou na zámek a zjistí, kdo certifikát vydal. Ukažte jim také, jak vypadá varování prohlížeče při HTTP webu (nebo při expirovaném certifikátu) — v Chromu je to červený výkřičník. Pokud škola používá vlastní systém (Bakaláři, Moodle), prověřte s žáky i jeho certifikát — žáci to ocení jako reálný kontext.
