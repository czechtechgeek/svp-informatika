---
grade: 8
week: 21
time: 45
area: Kybernetická bezpečnost
rvp_codes:
  - code: INF-INF-004-ZV9-013
    text: "Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje, na základě posouzení rizik ztráty, poškození či zneužití dat."
  - code: INF-INF-004-ZV9-014
    text: Diskutuje o fungování digitálních technologií určujících trendy ve světě.
goals:
  - "**Definuje** pojem phishing a popíše jeho cíle."
  - "**Identifikuje** nejméně 5 varovných znaků (red flags) v podvodném e-mailu."
  - "**Analyzuje** vzorový e-mail a zdůvodní, proč je nebo není podvodný."
  - "**Navrhne** správný postup, když obdrží podezřelý e-mail."
time_budget:
  - type: board
    minutes: 8
  - type: pc
    minutes: 20
  - type: discussion
    minutes: 10
  - type: review
    minutes: 7
friday_tip: "Přineste do hodiny vytištěný nebo promítnutý reálný phishingový e-mail (z vlastní schránky, se zakrytými osobními údaji) — žáci okamžitě vidí, jak přesvědčivě mohou podvody vypadat. Tato aktivita je nejsilnější, když je příklad co nejreálnější."
---

# Phishing: Analýza podvodných e-mailů

## 💡 Metodický postup

### 1. Úvod: Co je phishing a proč funguje?

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel vysvětlí původ slova: „phishing" = fishing (rybaření) — útočník „hodí návnadu" a čeká, kdo se chytí. Phishing je nejčastější způsob kybernetického útoku — přes 90 % úspěšných útoků začíná phishingovým e-mailem nebo SMS.

Proč phishing funguje? Útočníci využívají psychologické spouštěče:
- **Strach:** „Váš účet bude zablokován do 24 hodin!"
- **Spěch:** „Akce končí dnes — klikněte hned!"
- **Autorita:** „Česká pošta / Česká spořitelna / Microsoft vám posílá..."
- **Zvědavost:** „Podívejte se, kdo vás hledal na internetu"
- **Chamtivost:** „Vyhráli jste iPhone 15!"

Varianty phishingu: e-mail, SMS (smishing), telefon (vishing), sociální sítě.

---

### 2. Detektiv podvodů: Rozbor vzorových e-mailů

<span class="act pc">💻 PC — 20 min</span>

<div class="zadani-pc" markdown="1">

Pro každý z níže uvedených e-mailů zkontrolujte checklist a rozhodněte: **PODVOD** nebo **LEGITIMNÍ**?

**Checklist červených vlajek:**
- [ ] Odesílatel — odpovídá doména skutečné organizaci? (podvod: `info@ceska-posta-doruceni.cz`)
- [ ] Oslovení — je e-mail osobní nebo obecný? („Vážený zákazník" místo jména)
- [ ] Jazyk — jsou překlepy, špatná gramatika, podivné věty?
- [ ] Urgentnost — tlačí e-mail na okamžitou akci pod hrozbou?
- [ ] Odkaz — kam skutečně vede? (najedu myší, neklikám — zobrazí se skutečná URL)
- [ ] Příloha — očekával jsem tento soubor? Je přípona podezřelá? (.exe, .zip)
- [ ] Požadavek — chce e-mail heslo, číslo karty, osobní údaje?

---

**E-mail č. 1:**
> *Od:* support@ceska-sporitelna-online.net
> *Předmět:* ⚠️ Váš účet byl pozastaven — okamžitá akce nutná!
> *Text:* Vážený zákazníku, detekovali jsme podezřelou aktivitu na Vašem účtu. Pro obnovu přístupu klikněte ZDE do 24 hodin, jinak bude Váš účet trvale zablokován. Česka spořitelna, bezpečnostní tým.

**E-mail č. 2:**
> *Od:* newsletter@alza.cz
> *Předmět:* Vaše objednávka č. 2847163 byla odeslána
> *Text:* Dobrý den, Martine, Vaše objednávka byla předána přepravci DPD. Sledovat zásilku můžete na alza.cz v sekci Moje objednávky. S pozdravem, tým Alza.cz

**E-mail č. 3:**
> *Od:* noreply@microsoft-security.com
> *Předmět:* Neobvyklé přihlášení z Ruska do vašeho Microsoft účtu
> *Text:* Zjistili jsme přihlášení z IP adresy v Rusku. Pokud jste to nebyli vy, okamžitě ověřte svůj účet: [Zabezpečit účet]. Váš token vyprší za 30 minut.

</div>

*(Klíč: E-mail 1 = PODVOD, E-mail 2 = LEGITIMNÍ, E-mail 3 = PODVOD)*

---

### 3. Správná reakce: Co dělat s podezřelým e-mailem

<span class="act discussion">💬 Diskuse — 10 min</span>

Třída společně projde správný postup:

1. **NEklikat** na žádné odkaz v podezřelém e-mailu
2. **NEotevírat** přílohy od neznámých nebo podezřelých odesílatelů
3. **Ověřit** odesílatele přes jiný kanál (zavolat bance přímo, přejít na web ručně)
4. **Nahlásit** phishing — v Gmailu tlačítko „Nahlásit phishing", v Outlooku „Report"
5. **Smazat** e-mail ze schránky i z koše
6. Pokud jste klikli: **okamžitě změnit heslo** a informovat správce nebo rodiče

Žáci diskutují: „Co byste udělali, kdybychom dostali takový e-mail od 'ředitele školy'?"

---

### 4. Reflexe a shrnutí

<span class="act review">🔍 Reflexe — 7 min</span>

Rychlý kvíz — „Pravda nebo lež?":
1. E-mail s logem banky je vždy od banky. *(Lež)*
2. Překlepy v e-mailu jsou varující znak. *(Pravda)*
3. Pokud e-mail zná mé jméno, je legitimní. *(Lež — spear phishing)*
4. Správná reakce na podezřelý e-mail je zavolat odesílateli přes číslo z e-mailu. *(Lež — číslo může být také podvodné)*
5. HTTPS na webu zaručuje, že web není phishingový. *(Lež — i podvodné weby mohou mít HTTPS)*

---

## 📂 Zdroje a podklady

* **Online kvíz:** [phishingquiz.withgoogle.com](https://phishingquiz.withgoogle.com) — Google test „jste schopni rozeznat phishing?" (8 e-mailů, CZ/EN)
* **Web — NÚKIB materiály:** [nukib.cz/cs/kyberneticka-bezpecnost/pro-verejnost](https://www.nukib.cz) — tipy a příklady phishingu v češtině
* **Web — Hoax.cz:** [hoax.cz](https://www.hoax.cz) — databáze podvodných e-mailů a řetězových zpráv
* **Pracovní list:** Vytiskněte vzorové e-maily s checklistem — žáci pracují s tužkou, není potřeba PC

---

!!! tip "Tip pro učitele"
    Google phishing quiz je skvělý doplněk — žáci ho mohou vyplnit online a okamžitě vidí výsledek. Upozorněte žáky, že i zkušení dospělí občas phishing nepoznají — to není ostuda, proto existují technické filtry a antispam. Hlavní je znát postup, co dělat PO kliknutí (rychlá změna hesla, oznámení). Spear phishing (cílený phishing se jménem oběti) je pokročilé téma pro rychlejší žáky.
