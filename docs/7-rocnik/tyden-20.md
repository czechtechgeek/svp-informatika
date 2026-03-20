# IP adresa: Adresa bydliště počítače

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Digitální technologie
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-009" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-009</span><span style="color: #374151;">Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.</span></div>
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-004-ZV9-013" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-004-ZV9-013</span><span style="color: #374151;">Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje, na základě posouzení rizik ztráty, poškození či zneužití dat.</span></div>

## 💬 Tip pro pátek
Aktualizace IP: ukažte žákům na projektoru web „co je moje IP adresa" (whatismyip.com nebo podobný) — okamžitě vidí svou veřejnou IP adresu. Je to „wow moment", který otvírá diskusi o soukromí.

## 🎯 Cíle hodiny

- Žák vysvětlí, co je IP adresa a k čemu slouží
- Žák rozlišuje IPv4 a IPv6 a ví, proč přecházíme na IPv6
- Žák rozlišuje soukromou a veřejnou IP adresu
- Žák chápe, že IP adresa odhaluje polohu a identitu — propojení s bezpečností

## 💡 Metodický postup

### 1. Analogie: Adresa domu (8 min) — tabule

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

### 2. Soukromá vs. veřejná IP (10 min) — tabule

Učitel vysvětlí rozdíl:

| Typ | Příklady | Kdo ji vidí |
|-----|---------|-------------|
| **Soukromá** (privátní) | 192.168.x.x, 10.x.x.x | Jen zařízení v LAN |
| **Veřejná** | Přidělena poskytovatelem | Celý internet |

Analogie: Privátní IP = číslo pokoje v hotelu. Veřejná IP = adresa hotelu.

Všechna zařízení v domácnosti sdílí jednu veřejnou IP (od poskytovatele internetu), ale mají různé privátní IP (přiděleny routerem = NAT).

### 3. Praktická aktivita: Zjistěte svou IP (15 min) — PC

#### Úkol 1 — Privátní IP

- Windows: Start → cmd → `ipconfig` → hledat „IPv4 adresa"
- macOS/Linux: Terminál → `ifconfig` nebo `ip addr`
- Žáci zapíší svou privátní IP. Mají všichni stejnou nebo různou?

#### Úkol 2 — Veřejná IP

- Otevřít browser → vyhledat „co je moje IP adresa" nebo navštívit veřejný checker
- Zapsat veřejnou IP. Mají všichni ve třídě stejnou veřejnou IP? (Ano — sdílí školní router)

#### Úkol 3 — DNS lookup

- Vyhledat „IP adresa google.com" nebo v cmd: `nslookup google.com`
- Zjistit, jakou IP má google.com — vysvětlení DNS (jméno → IP)

#### Úkol 4 — Geolokace IP

- Vyhledat geolokaci veřejné IP školy — kde říká, že se škola nachází? Je to přesné?

### 4. Propojení s bezpečností (7 min) — diskuse

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
