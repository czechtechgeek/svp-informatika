# Dvoufázové ověření (2FA)

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Kybernetická bezpečnost / Digitální gramotnost
- **Výstup:** <div class="curriculumTag" data-code="I-9-4-02" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-4-02</span><span style="color: #374151;">Žák chrání sebe i ostatní při práci v digitálním prostředí</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-4-03" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-4-03</span><span style="color: #374151;">Žák komunikuje a spolupracuje digitálně s ohledem na etiku</span></div>

## 💬 Tip pro pátek
Nechte žáky na konci hodiny zkontrolovat, zda mají 2FA zapnuté na Googlu nebo Discordu — mnoho z nich to udělá poprvé v životě a ocení praktický výstup hodiny. Je to dovednost, kterou si odnesou domů.

## 🎯 Cíle hodiny

- Žák vysvětlí princip dvoufázového ověření a proč heslo samotné nestačí
- Žák rozliší různé metody 2FA (SMS, aplikace, hardwarový klíč) a zhodnotí jejich bezpečnost
- Žák samostatně projde procesem nastavení 2FA na reálné službě
- Žák argumentuje, proč by měli 2FA používat i ostatní členové rodiny

## 💡 Metodický postup

### 1. Úvod: Co kdyby někdo znal vaše heslo? (8 min) — tabule

Učitel položí otázku: „Kolik hesel používáte? Jsou všechna unikátní?" Statistika pro žáky: průměrný uživatel má přes 100 online účtů. Každý rok uniknou miliardy hesel z napadených databází. Žáci mohou zkontrolovat na [haveibeenpwned.com](https://haveibeenpwned.com), zda jejich e-mail figuruje v uniklých datech.

Klíčová myšlenka: Heslo je jen **jeden faktor** ověření. Pokud útočník heslo zná (nebo uhádne, nebo ho ukradne), má plný přístup k účtu. Řešení: přidat druhý faktor.

Tři kategorie faktorů ověření:
- **Co víte** — heslo, PIN
- **Co máte** — telefon, hardwarový klíč
- **Kdo jste** — otisk prstu, obličej (biometrie)

**2FA = ověření dvěma různými kategoriemi faktorů.** I když útočník zná heslo, bez vašeho telefonu se nepřihlásí.

### 2. Přehled metod 2FA (10 min) — tabule

| Metoda | Jak funguje | Bezpečnost | Příklad |
|--------|-------------|------------|---------|
| **SMS kód** | Jednorázový kód přijde SMSkou | Střední — SMS lze přesměrovat (SIM swap) | Většina bank, státní portály |
| **Authenticator app** | Aplikace generuje 6místný kód každých 30 s | Vysoká — kód je offline, vázán na zařízení | Google Authenticator, Authy, Microsoft Authenticator |
| **E-mailový kód** | Kód přijde e-mailem | Nízká až střední — závisí na bezpečnosti e-mailu | Méně časté |
| **Push notifikace** | Aplikace se zeptá „Jste to vy?" | Vysoká — ale pozor na MFA fatigue útok | Duo Security, Microsoft Authenticator |
| **Hardwarový klíč** | USB/NFC klíč (YubiKey) | Nejvyšší — fyzický předmět nelze vzdáleně ukrást | Google účty, firemní přístupy |

Doporučení: Authenticator aplikace je nejlepší poměr bezpečnosti a pohodlí pro běžného uživatele.

### 3. Praktická aktivita: Nastavení 2FA (20 min) — PC

Žáci pracují samostatně na počítačích nebo telefonech. Vyberou si jednu ze služeb, na které mají účet:

**Možnost A — Google účet (Gmail):**
1. Přejít na myaccount.google.com
2. Bezpečnost → Dvoufázové ověření → Začít
3. Projít průvodcem (SMS nebo aplikace)
4. Uložit záložní kódy na bezpečné místo

**Možnost B — Discord:**
1. Nastavení uživatele (ozubené kolo) → Moje účet
3. Dvoufázové ověření → Zapnout
4. Naskenovat QR kód v aplikaci Authenticator
5. Zadat ověřovací kód

**Možnost C — Instagram / TikTok:**
1. Nastavení → Zabezpečení → Dvoufázové ověření
2. Vybrat metodu (SMS nebo aplikace)

Žáci, kteří nemají vlastní zařízení nebo účet: pracují ve dvojici s kamarádem nebo sledují demonstraci na projektoru.

Učitel prochází třídou a pomáhá. Po aktivitě: ruka nahoru — kdo 2FA úspěšně nastavil?

### 4. Diskuse: Kdy 2FA nestačí a jak dál (7 min) — diskuse

Diskuse: „Může útočník obejít 2FA?" Ano — v případech:
- **SIM swapping** — útočník přesvědčí operátora, aby přenesl vaše číslo na jeho SIM
- **MFA fatigue** — útočník pošle desítky push notifikací, dokud uživatel z únavy nepotvrdí
- **Phishing v reálném čase** — podvodný web přeposílá kód útočníkovi okamžitě

Proto: Authenticator aplikace je lepší než SMS, a hardwarový klíč je nejbezpečnější. A vždy dávejte pozor, co potvrzujete v push notifikaci.

Závěrečné shrnutí — 3 věci pro domov:
1. Zapnout 2FA na e-mailu (to je nejdůležitější účet)
2. Stáhnout si Authenticator aplikaci
3. Uložit záložní kódy na bezpečné offline místo (vytisknout, schránka)

## 📂 Podklady

- **Web — Have I Been Pwned:** [haveibeenpwned.com](https://haveibeenpwned.com) — žáci zkontrolují, zda jejich e-mail figuruje v uniklých datech
- **Aplikace — Google Authenticator:** zdarma na Android i iOS — nejrozšířenější authenticator
- **Aplikace — Authy:** alternativa s cloudovou zálohou — vhodná pro méně zkušené uživatele
- **Web — 2fa.directory:** [2fa.directory](https://2fa.directory) — přehled všech webů a aplikací, které podporují 2FA

!!! tip "Tip pro učitele"
    Praktické nastavení 2FA je nejhodnotnější část hodiny — snažte se, aby co nejvíce žáků skutečně 2FA zapnulo ještě v hodině. Upozorněte, že záložní kódy jsou kritické — bez nich se uživatel může ze svého účtu navždy vyloučit (například při ztrátě telefonu). Téma propojte s rodinnou bezpečností: žáci mohou pomoci rodičům nebo prarodičům nastavit 2FA na bankovním účtu nebo e-mailu.
