---
grade: 8
week: 23
time: 45
area: Kybernetická bezpečnost / Digitální gramotnost
rvp_codes:
  - code: INF-INF-004-ZV9-013
    text: "Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje, na základě posouzení rizik ztráty, poškození či zneužití dat."
  - code: INF-INF-004-ZV9-014
    text: Diskutuje o fungování digitálních technologií určujících trendy ve světě.
goals:
  - "**Vysvětlí** princip dvoufázového ověření a proč heslo samotné nestačí."
  - "**Rozliší** různé metody 2FA (SMS, aplikace, hardwarový klíč) a zhodnotí jejich bezpečnost."
  - "**Samostatně projde** procesem nastavení 2FA na reálné službě."
  - "**Argumentuje**, proč by měli 2FA používat i ostatní členové rodiny."
time_budget:
  - type: board
    minutes: 8
  - type: board
    minutes: 10
  - type: pc
    minutes: 20
  - type: discussion
    minutes: 7
friday_tip: "Nechte žáky na konci hodiny zkontrolovat, zda mají 2FA zapnuté na Googlu nebo Discordu — mnoho z nich to udělá poprvé v životě a ocení praktický výstup hodiny. Je to dovednost, kterou si odnesou domů."
---

# Dvoufázové ověření (2FA)

## 💡 Metodický postup

### 1. Úvod: Co kdyby někdo znal vaše heslo?

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel položí otázku: „Kolik hesel používáte? Jsou všechna unikátní?" Statistika pro žáky: průměrný uživatel má přes 100 online účtů. Každý rok uniknou miliardy hesel z napadených databází. Žáci mohou zkontrolovat na [haveibeenpwned.com](https://haveibeenpwned.com), zda jejich e-mail figuruje v uniklých datech.

Klíčová myšlenka: Heslo je jen **jeden faktor** ověření. Pokud útočník heslo zná (nebo uhádne, nebo ho ukradne), má plný přístup k účtu. Řešení: přidat druhý faktor.

Tři kategorie faktorů ověření:
- **Co víte** — heslo, PIN
- **Co máte** — telefon, hardwarový klíč
- **Kdo jste** — otisk prstu, obličej (biometrie)

**2FA = ověření dvěma různými kategoriemi faktorů.** I když útočník zná heslo, bez vašeho telefonu se nepřihlásí.

---

### 2. Přehled metod 2FA

<span class="act board">🖊️ Tabule — 10 min</span>

| Metoda | Jak funguje | Bezpečnost | Příklad |
|--------|-------------|------------|---------|
| **SMS kód** | Jednorázový kód přijde SMSkou | Střední — SMS lze přesměrovat (SIM swap) | Většina bank, státní portály |
| **Authenticator app** | Aplikace generuje 6místný kód každých 30 s | Vysoká — kód je offline, vázán na zařízení | Google Authenticator, Authy, Microsoft Authenticator |
| **E-mailový kód** | Kód přijde e-mailem | Nízká až střední — závisí na bezpečnosti e-mailu | Méně časté |
| **Push notifikace** | Aplikace se zeptá „Jste to vy?" | Vysoká — ale pozor na MFA fatigue útok | Duo Security, Microsoft Authenticator |
| **Hardwarový klíč** | USB/NFC klíč (YubiKey) | Nejvyšší — fyzický předmět nelze vzdáleně ukrást | Google účty, firemní přístupy |

Doporučení: Authenticator aplikace je nejlepší poměr bezpečnosti a pohodlí pro běžného uživatele.

---

### 3. Praktická aktivita: Nastavení 2FA

<span class="act pc">💻 PC — 20 min</span>

<div class="zadani-pc">

Zapněte 2FA na jedné ze služeb, na které máte účet:

**Možnost A — Google účet (Gmail):**
1. Přejděte na myaccount.google.com
2. Bezpečnost → Dvoufázové ověření → Začít
3. Projděte průvodcem (SMS nebo aplikace)
4. Uložte záložní kódy na bezpečné místo

**Možnost B — Discord:**
1. Nastavení uživatele (ozubené kolo) → Moje účet
2. Dvoufázové ověření → Zapnout
3. Naskenujte QR kód v aplikaci Authenticator
4. Zadejte ověřovací kód

**Možnost C — Instagram / TikTok:**
1. Nastavení → Zabezpečení → Dvoufázové ověření
2. Vyberte metodu (SMS nebo aplikace)

*Nemáte vlastní zařízení nebo účet? Pracujte ve dvojici nebo sledujte demonstraci na projektoru.*

</div>

Po aktivitě: ruka nahoru — kdo 2FA úspěšně nastavil?

---

### 4. Diskuse: Kdy 2FA nestačí a jak dál

<span class="act discussion">💬 Diskuse — 7 min</span>

Diskuse: „Může útočník obejít 2FA?" Ano — v případech:
- **SIM swapping** — útočník přesvědčí operátora, aby přenesl vaše číslo na jeho SIM
- **MFA fatigue** — útočník pošle desítky push notifikací, dokud uživatel z únavy nepotvrdí
- **Phishing v reálném čase** — podvodný web přeposílá kód útočníkovi okamžitě

Proto: Authenticator aplikace je lepší než SMS, a hardwarový klíč je nejbezpečnější. A vždy dávejte pozor, co potvrzujete v push notifikaci.

Závěrečné shrnutí — 3 věci pro domov:
1. Zapnout 2FA na e-mailu (to je nejdůležitější účet)
2. Stáhnout si Authenticator aplikaci
3. Uložit záložní kódy na bezpečné offline místo (vytisknout, schránka)

---

## 📂 Zdroje a podklady

* **Web — Have I Been Pwned:** [haveibeenpwned.com](https://haveibeenpwned.com) — žáci zkontrolují, zda jejich e-mail figuruje v uniklých datech
* **Aplikace — Google Authenticator:** zdarma na Android i iOS — nejrozšířenější authenticator
* **Aplikace — Authy:** alternativa s cloudovou zálohou — vhodná pro méně zkušené uživatele
* **Web — 2fa.directory:** [2fa.directory](https://2fa.directory) — přehled všech webů a aplikací, které podporují 2FA

---

!!! tip "Tip pro učitele"
    Praktické nastavení 2FA je nejhodnotnější část hodiny — snažte se, aby co nejvíce žáků skutečně 2FA zapnulo ještě v hodině. Upozorněte, že záložní kódy jsou kritické — bez nich se uživatel může ze svého účtu navždy vyloučit (například při ztrátě telefonu). Téma propojte s rodinnou bezpečností: žáci mohou pomoci rodičům nebo prarodičům nastavit 2FA na bankovním účtu nebo e-mailu.
