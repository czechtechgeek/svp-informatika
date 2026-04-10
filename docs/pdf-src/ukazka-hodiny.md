---
grade: 8
week: 21
time: 45
area: Digitální technologie a společnost
rvp_codes:
  - code: INF-INF-004-ZV9-015
    text: "Posoudí důvěryhodnost digitálního obsahu; uvede příklady dezinformací a způsoby jejich šíření."
  - code: INF-INF-004-ZV9-013
    text: "Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje."
goals:
  - "Žák **rozezná** phishingový e-mail od legitimní komunikace (min. 4 ze 6 příkladů)"
  - "Žák **pojmenuje** 3 konkrétní znaky podvodné zprávy"
  - "Žák **sestaví** pravidla, jak ověřit pravost e-mailu nebo zprávy"
  - "Žák **procvičí** nahlášení phishingu v běžném poštovním klientovi"
time_budget:
  - type: board
    minutes: 8
  - type: discussion
    minutes: 10
  - type: pc
    minutes: 20
  - type: review
    minutes: 7
friday_tip: "Aktivita bez PC: Připravte 6 vytištěných e-mailů (3 legitimní, 3 phishing). Žáci v páru hodnotí každý e-mail a odůvodňují své rozhodnutí. Následuje třídní diskuse."
---

# Phishing: rozpoznání podvodné zprávy

<!--
  ╔══════════════════════════════════════════════════════════════════╗
  ║  UKÁZKA KOMPLETNÍ HODINY — pravidla integrity lekcí v PDF       ║
  ║                                                                  ║
  ║  Tato stránka slouží jako referenční vzor. Demonstruje:          ║
  ║  1. Správné použití front matter (generuje záhlaví automaticky)  ║
  ║  2. Strukturu aktivit s act tagy                                 ║
  ║  3. Zadání na PC (.zadani-pc) — nikdy na prázdné stránce         ║
  ║  4. Pravidla, která print.css používá k zachování integrity      ║
  ╚══════════════════════════════════════════════════════════════════╝

  PDF INTEGRITA — jak to funguje:

  • Každá hodina je obalena do <div class="lesson-unit"> hookem pdf_build.py.
    Ten dostane break-before: page → hodina vždy začíná na nové stránce.

  • h3 + .zadani-pc tvoří nerozlučný pár:
    h3 { break-after: avoid }  →  h3 nesmí být poslední na stránce
    .zadani-pc { break-before: avoid }  →  zadání nesmí začít bez nadpisu
    .zadani-pc { break-inside: avoid }  →  zadání se nesmí rozlomit uprostřed

  • .goals, .lesson-meta, .time-budget, .resources, .friday-tip:
    break-inside: avoid  →  nikdy se nerozdělí přes stránku

  • Odstavce: orphans: 3; widows: 3  →  žádné osamocené řádky
-->

## 💡 Metodický postup

### 1. Motivační příběh

<span class="act board">📋 Tabule/výuka — 8 min</span>

Učitel přečte krátký příběh (nebo zobrazí na projektoru):

> *Babičce Novákové přišel e-mail od "Česká spořitelna": „Vaše karta
> byla zablokována. Klikněte sem a ověřte své údaje do 24 hodin."
> Klikla. O tři dny později jí zmizelo 47 000 Kč.*

Otázky k zahájení diskuse:

- Co udělala babička špatně?
- Jak byste vy poznali, že jde o podvod?
- Proč útočníci posílají právě e-maily (a ne třeba dopisy)?

---

### 2. Analýza příkladu

<span class="act discussion">💬 Diskuse — 10 min</span>

Učitel promítne screenshot phishingového e-mailu (připravený předem)
a společně s žáky identifikují červené vlajky:

1. **Adresa odesílatele** — nekoresponduje s doménou banky
2. **Urgence** — „do 24 hodin", „ihned"
3. **Obecné oslovení** — „Vážený zákazníku" místo jménem
4. **Odkaz na jinou doménu** — URL v `<a href>` se liší od zobrazeného textu
5. **Jazykové chyby** — překlepy, strojový překlad
6. **Neobvyklá žádost** — banka po vás nikdy nepožaduje heslo e-mailem

Žáci zapisují znaky podvodu do sešitu (2 min).

---

### 3. Praktická identifikace

<span class="act pc">💻 PC — 20 min</span>

### Část A — Quiz (10 min)

Žáci otevřou připravený formulář (Google Forms / MS Forms) s 6 e-maily.
Pro každý e-mail označí: **Legitimní** / **Phishing** + zdůvodnění.

### Část B — Nahlášení (10 min)

Žáci se přihlásí do svého školního e-mailového klienta (Outlook, Gmail)
a vyzkouší funkci **„Nahlásit phishing / junk"**:

<div class="zadani-pc" markdown="1">

**Zadání: Nahlásit podezřelou zprávu**

1. Otevři školní e-mail (Outlook nebo Gmail)
2. V doručené poště najdi zprávu označenou „[TEST PHISHING]" — poslal ji učitel
3. Klikni pravým tlačítkem na zprávu (nebo na tři tečky ⋮)
4. Zvol možnost **„Nahlásit jako nevyžádanou"** nebo **„Nahlásit phishing"**
5. Do Google formuláře napiš: *Co se stalo? Zmizela zpráva? Přišlo potvrzení?*

💡 **Pozor:** V reálném světě phishing hlásíte přímo poskytovateli e-mailu
i na [phishing@cert.cz](mailto:phishing@cert.cz) (NÚKIB).

</div>

Učitel monitoruje postup přes učitelský přehled formuláře a poskytuje
zpětnou vazbu třídě jako celku.

---

### 4. Shrnutí a pravidlo 3×Ověř

<span class="act review">🔍 Reflexe — 7 min</span>

Třída společně sestaví **pravidlo 3×Ověř** (zapsat na tabuli, vyfotit):

1. **Ověř odesílatele** — podívej se na celou e-mailovou adresu, ne jen na jméno
2. **Ověř odkaz** — najeď myší (bez kliknutí!) a zkontroluj URL v levém dolním rohu
3. **Ověř kanálem** — zavolej přímo firmě/osobě a zeptej se

Závěrečná otázka pro dobrovolníka: *„Proč útočníci vytváří umělou urgenci?"*

---

<div class="resources" markdown="1">
<div class="resources-title">📂 Zdroje a podklady</div>

- **Phishing quiz (CZ):** [phishingquiz.withgoogle.com](https://phishingquiz.withgoogle.com) — Google interaktivní test
- **Hlášení incidentů:** [phishing@cert.cz](mailto:phishing@cert.cz) — NÚKIB CERT.cz
- **Metodika (CZ):** [e-bezpeci.cz](https://www.e-bezpeci.cz) — sekce Sociální inženýrství
- **Video (EN, 4 min):** „What is Phishing?" — Common Craft na YouTube
- **Materiály:** Připravte 6 screenshotů e-mailů (stáhnout z e-bezpeci.cz nebo vytvořit)
- **Šablona hodnocení:** Google Forms s 6 e-maily + sloupec „Zdůvodnění"

</div>

!!! warning "Bezpečnostní upozornění pro učitele"
    Při promítání reálných phishingových e-mailů **nikdy neklikejte na odkaz**
    ani nezobrazte obrázky — mohou obsahovat sledovací pixely.
    Vždy používejte screenshot se zakrytou nebo upravenou URL.

!!! tip "Diferenciace"
    **Rychlí žáci:** Vytvoří vlastní (falešný) phishingový e-mail v textovém
    editoru — poznat ho pak musí spolužák. Aktivita prohlubuje pochopení
    tím, že žák „přemýšlí jako útočník."

    **Pomalejší žáci:** Zaměřte se jen na Část A (quiz). Část B je rozšíření.
