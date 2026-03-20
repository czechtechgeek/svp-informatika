---
grade: 7
week: 20
time: 45
area: Digitální technologie
rvp_codes:
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
  - code: INF-INF-004-ZV9-013
    text: "Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje, na základě posouzení rizik ztráty, poškození či zneužití dat."
goals:
  - "Žák vysvětlí, co je IP adresa a k čemu slouží"
  - "Žák rozlišuje IPv4 a IPv6 a ví, proč přecházíme na IPv6"
  - Žák rozlišuje soukromou a veřejnou IP adresu
  - "Žák chápe, že IP adresa odhaluje polohu a identitu — propojení s bezpečností"
time_budget:
  - type: board
    minutes: 8
  - type: board
    minutes: 10
  - type: pc
    minutes: 15
  - type: discussion
    minutes: 7
friday_tip: "Aktualizace IP: ukažte žákům na projektoru web „co je moje IP adresa\" (whatismyip.com nebo podobný) — okamžitě vidí svou veřejnou IP adresu. Je to „wow moment\", který otvírá diskusi o soukromí."
---

# IP adresa: Adresa bydliště počítače

## 💡 Metodický postup

### 1. Analogie: Adresa domu

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel kreslí analogii:

```
Poštovní adresa:         IP adresa:
Praha, Hlavní 42    =    192.168.1.42
Město | Ulice | číslo    Síť | podsíť | zařízení
```

Klíčový bod: Každé zařízení v síti potřebuje jedinečnou adresu, aby vědělo, komu je zpráva určena a odkud přišla.

**IPv4 vs. IPv6:**
- IPv4: 4 čísla 0–255, oddělenč tečkami (192.168.0.1) → max. 4 miliardy adres → skoro vyčerpány!
- IPv6: delší, hexadecimální (2001:0db8:85a3:0000:0000:8a2e:0370:7334) → 340 sextiliard adres

### 2. Soukromá vs. veřejná IP

<span class="act board">🖊️ Tabule — 10 min</span>

Učitel vysvětlí rozdíl:

| Typ | Příklady | Kdo ji vidí |
|-----|---------|-------------|
| **Soukromá** (privátní) | 192.168.x.x, 10.x.x.x | Jen zařízení v LAN |
| **Veřejná** | Přidělena poskytovatelem | Celý internet |

Analogie: Privátní IP = číslo pokoje v hotelu. Veřejná IP = adresa hotelu.

Všechna zařízení v domácnosti sdílí jednu veřejnou IP (od poskytovatele internetu), ale mají různé privátní IP (přiděleny routerem = NAT).

### 3. Praktická aktivita: Zjistěte svou IP

<span class="act pc">💻 PC — 15 min</span>

<div class="zadani-pc">

Proveď tyto úkoly a odpovědi zapiš do sešitu nebo Google Docs:

**Úkol 1 — Zjisti svou privátní IP:**
- Windows: otevři **Start → cmd** → napiš `ipconfig` → hledej „IPv4 adresa"
- Zapiš svou privátní IP. Mají všichni žáci ve třídě stejnou nebo různou privátní IP?

**Úkol 2 — Zjisti veřejnou IP:**
- Otevři prohlížeč a vyhledej „co je moje IP adresa" nebo přejdi na stránku pro zjištění IP
- Zapiš veřejnou IP. Je stejná jako u ostatních žáků v třídě? Proč?

**Úkol 3 — DNS lookup:**
- V příkazové řádce (cmd) napiš: `nslookup google.com`
- Jakou IP adresu má google.com? Co to znamená — proč stránka nemá jen jméno?

**Úkol 4 — Geolokace:**
- Vyhledej geolokaci veřejné IP naší školy. Kde říká, že se škola nachází? Je to přesné?

**Pro rychlé žáky:** Spusť příkaz `tracert google.com` (Windows). Co vidíš? Co jsou ta čísla a adresy?

</div>

### 4. Propojení s bezpečností

<span class="act discussion">💬 Diskuse — 7 min</span>

Klíčové otázky:
- „Pokud někdo zná vaši IP, co o vás ví?" (přibližnou polohu, poskytovatele)
- „Proč se VPN používá pro anonymitu?" (maskuje veřejnou IP)
- „Mohou vás podle IP dohledat?" (jen s pomocí policie a soudu — ne sami)

## 📂 Podklady

- **CMD příkazy:** `ipconfig` (Windows), `ifconfig` (Linux/Mac) — základní síťové nástroje
- **DNS vysvětlení:** [howdns.works](https://howdns.works) — krásná animace jak DNS funguje (EN)
- **IP geolokace demo:** Veřejné weby pro zjištění IP a přibližné polohy (vhodné pro demo, ne pro sledování)
- **Video (CZ):** Hledejte „IP adresa vysvětlení CZ" — Computerphile CZ nebo tutoriály na YouTube
- **Rozšíření — traceroute:** Příkaz `tracert google.com` (Windows) ukáže cestu paketu přes routery — vizuálně fascinující

!!! tip "Tip pro učitele"
    Příkaz `ipconfig` v cmd je pro žáky „magický" — vidí data, která normálně nevidí. Je to dobrý způsob, jak demystifikovat technologie. Zdůrazněte: IP adresa sama o sobě není nebezpečná — problém nastává v kombinaci s dalšími daty (uživatelské jméno, lokace, časy přihlášení). Tato hodina přirozeně připravuje na bezpečnostní témata v týdnech 22–25.
