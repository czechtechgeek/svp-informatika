# 🦠 Malware: Viry, trojské koně, ransomware

> **Stav:** `⬜ Nekontrolováno`

### 📋 Kontext a cíle
> **RVP ZV (Informatika):** Kybernetická bezpečnost
> **Kód:** `INF-INF-004-ZV9-013` – *Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje, na základě posouzení rizik ztráty, poškození či zneužití dat.*
> **Kód:** `INF-INF-004-ZV9-014` – *Diskutuje o fungování digitálních technologií určujících trendy ve světě.*

**Po hodině žák:**
* **Rozliší** základní typy malware (virus, červ, trojský kůň, ransomware, spyware) a popíše jejich chování.
* **Vysvětlí**, jak se malware šíří a jak mu lze předcházet.
* **Analyzuje** konkrétní scénář a identifikuje typ útoku a správnou reakci.
* **Vytvoří** osobní plán ochrany zařízení před malwarem.

---

### 💡 Metodický postup (45 min)

#### 1. Úvod: Co je malware a proč existuje? (7 min)
*Tabule — výklad.*

Učitel napíše na tabuli slovo „MALWARE" a žáci hádají, co znamená (malicious software = škodlivý software). Krátká diskuse: Kdo za malwarem stojí? (kyberzločinci, státní aktéři, hacktivisté) a proč? (peníze, špionáž, sabotáž, sláva).

Zajímavá čísla na tabuli:
- Každý den vzniká přibližně **450 000 nových vzorků malwaru**
- Ransomwarový útok na nemocnici nebo firmu může způsobit škody v **miliardách korun**
- Nejčastější způsob šíření: e-mailová příloha (phishing) — přes 90 % útoků

---

#### 2. Katalog malwaru: Přehled typů (13 min)
*Tabule — přehled typů.*

Učitel projde tabulku typů malwaru. Žáci si mohou dělat poznámky:

| Typ | Co dělá | Jak se šíří | Reálný příklad |
|-----|---------|-------------|----------------|
| **Virus** | Připojí se k souboru, šíří se spuštěním | Infikované soubory, USB | ILOVEYOU (2000) — 50 mld. $ škod |
| **Červ (Worm)** | Šíří se sám přes síť bez zásahu uživatele | Síťová zranitelnost | WannaCry (2017) — napadl nemocnice |
| **Trojský kůň** | Tváří se jako legitimní program | Stažení z internetu, e-mail | Vzdálený přístup útočníka k PC |
| **Ransomware** | Zašifruje soubory, požaduje výkupné | Phishing, zranitelnosti | Ryuk, Lockbit — útok na ČVUT 2021 |
| **Spyware** | Sleduje aktivitu uživatele, krade hesla | Bundleware, podvodné aplikace | Keyloggery, stalkerware |
| **Adware** | Zobrazuje nežádoucí reklamy | Instalace „zdarma" programů | Nepříjemné, ale obvykle neničí data |

**Analogie pro žáky:** Ransomware je jako kdybychom přišli domů a zjistili, že nám někdo zamknul vše v trezoru a žádá výkupné za klíč.

---

#### 3. Analýza scénářů (18 min)
*PC nebo papír — práce ve dvojicích.*

Žáci pracují ve dvojicích. Každá dvojice dostane 3 scénáře a musí odpovědět na 3 otázky:
1. Jaký typ malwaru je popsán?
2. Jak se do systému dostal?
3. Co by měl uživatel udělat?

**Scénář 1:** Jana stáhla z internetu „zdarma" program na střih videí. Po instalaci se na ploše začaly objevovat reklamy, prohlížeč přesměrovává na neznámé weby a počítač je pomalejší.
*(Odpověď: Adware/Bundleware. Stažení z nedůvěryhodného webu. Odinstalovat program, spustit antivirus.)*

**Scénář 2:** Petr dostal e-mail s přílohou „faktura_2024.pdf.exe". Po otevření se nic nestalo — ale za hodinu mu přišla zpráva, že všechny jeho soubory jsou zašifrované a má zaplatit 2 BTC.
*(Odpověď: Ransomware. Phishingový e-mail s podvodnou přílohou. NEPLATIT, odpojit od sítě, kontaktovat IT, obnovit ze zálohy.)*

**Scénář 3:** Školní server začal posílat spam na tisíce adres, aniž to kdokoli ze školy dělal. IT správce zjistil, že server komunikuje s adresami v Rusku.
*(Odpověď: Červ nebo botnet. Zranitelnost v serverovém softwaru. Izolovat server, záplatovat, prohledat.)*

---

#### 4. Obrana: Osobní bezpečnostní plán (7 min)
*Diskuze.*

Žáci navrhnou vlastní „top 5 pravidel" pro ochranu svého zařízení. Učitel je zapíše na tabuli a třída společně vybere nejlepší:

Správná pravidla (která by měla zaznít):
- Aktualizovat operační systém a programy (záplaty zranitelností)
- Mít funkční antivirus / Windows Defender
- Nestahovat software z nedůvěryhodných zdrojů
- Neotvírat přílohy od neznámých nebo podezřelých odesílatelů
- Zálohovat důležitá data (3-2-1 pravidlo: 3 kopie, 2 různá média, 1 mimo domov)

---

### 🛠️ Zdroje a nástroje

* **Web — Virustotal:** [virustotal.com](https://www.virustotal.com) — bezplatný nástroj pro kontrolu souborů a URL na malware (žáci mohou zkusit v hodině)
* **Web — NÚKIB:** [nukib.cz](https://www.nukib.cz) — Národní úřad pro kybernetickou a informační bezpečnost, materiály pro školy
* **Video (CZ):** YouTube — „WannaCry útok vysvětlení" nebo „jak funguje ransomware" — dobré reportáže ČT nebo Seznamu
* **Propojení s praxí:** Případ útoku na Fakultní nemocnici Brno (2020) nebo ČVUT — reálné české příklady

---

> 💡 **Tip pro učitele:**
> Zdůrazněte, že cílem hodiny není strašit žáky, ale vybavit je znalostmi. Žáci (ani dospělí) by NIKDY neměli platit výkupné za ransomware — platba nezaručuje obnovení dat a motivuje útočníky k dalším útokům. Zálohy jsou jediná spolehlivá obrana. Praktický tip: ukažte žákům, jak zkontrolovat, zda je Windows Defender aktivní — to zvládnou i sami doma.

> 💬 **Tip pro pátek:** Zeptejte se žáků na začátku, zda někdo z nich nebo z rodiny zažil napadení malwarem — většina tříd má zkušenosti z první nebo druhé ruky. Reálné příběhy jsou nejlepší motivace pro bezpečnostní témata.
