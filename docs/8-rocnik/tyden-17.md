# DNS: Telefonní seznam internetu

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Digitální technologie
- **Výstup:** <div class="curriculumTag" data-code="I-9-3-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-3-01</span><span style="color: #374151;">Žák vysvětlí princip fungování digitálních technologií a sítí</span></div>

## 💬 Tip pro pátek
Demo: změňte DNS server v nastavení počítače na 8.8.8.8 (Google) nebo 1.1.1.1 (Cloudflare) a otestujte rychlost načítání. Žáci vidí, že abstraktní nastavení má reálný dopad.

## 🎯 Cíle hodiny

- Žák vysvětlí, co je DNS a proč existuje (mapování doménových jmen na IP adresy)
- Žák popíše postup DNS dotazu (rekurzivní resolver → root → TLD → autoritativní server)
- Žák vysvětlí pojem DNS cache a TTL
- Žák uvede příklady, jak může být DNS zneužit (DNS spoofing, DNS poisoning)

## 💡 Metodický postup

### 1. Problém: Pamatujeme si adresy? (7 min) — diskuse

Učitel se ptá: „Jaká je IP adresa Googlu?" (Nikdo neví.) „Ale víte, jak se jmenuje?" (google.com)

DNS = překlad jmen na čísla — jako telefonní seznam, kde hledáte jméno a dostanete číslo.

Bez DNS by každý musel pamatovat číselné IP adresy. DNS umožňuje lidsky čitelné názvy.

### 2. Jak DNS dotaz funguje (15 min) — tabule

Krok za krokem:

```
Uživatel zadá: www.google.com
        ↓
[Rekurzivní resolver] ← obvykle DNS server vašeho ISP nebo 8.8.8.8
        ↓ (dotaz: co je .com?)
[Root nameserver] → "zeptej se TLD serveru pro .com"
        ↓
[TLD server .com] → "zeptej se Google autoritativního serveru"
        ↓
[Google autoritativní server] → IP: 142.250.185.78
        ↓
[Resolver vrátí IP uživateli] → prohlížeč se připojí
```

**Cache:** Výsledek se uloží na určitou dobu (TTL = Time To Live) — příště se ptát nemusíme.

### 3. Aktivita: DNS v příkazové řádce (15 min) — PC

Žáci otevřou příkazovou řádku / terminál:

**Windows:**
```
nslookup google.com
nslookup youtube.com
nslookup seznam.cz
```

**Alternativa (web):** [mxtoolbox.com/DNSLookup.aspx](https://mxtoolbox.com/DNSLookup.aspx) — online DNS lookup

Žáci si zapíší IP adresy populárních webů a porovnají — proč má Google více IP adres? (Load balancing — více serverů pro miliardy uživatelů.)

### 4. DNS a bezpečnost (8 min) — tabule

**DNS spoofing / poisoning:**
- Útočník podstrčí falešnou IP adresu pro legitimní doménu
- Uživatel zadá `banka.cz`, dostane falešnou IP → phishingový web
- Obrana: DNSSEC (ověřování digitálním podpisem), HTTPS (certifikát webu nesedí)

**DNS over HTTPS (DoH):**
- Šifrování DNS dotazů — ISP nevidí, jaké weby navštěvujete
- Dostupné v moderních prohlížečích a OS

## 📂 Podklady

- **Animace DNS (EN):** [howdns.works](https://howdns.works) — krásná komiksová animace celého DNS procesu
- **Online DNS lookup:** [mxtoolbox.com](https://mxtoolbox.com/DNSLookup.aspx) nebo [dnschecker.org](https://dnschecker.org)
- **Video (CZ):** YouTube — „DNS vysvětlení česky jak funguje"
- **Veřejné DNS servery:** 8.8.8.8 (Google), 1.1.1.1 (Cloudflare), 9.9.9.9 (Quad9 — zaměřen na bezpečnost)
- **Propojení s bezpečností:** DNS spoofing propojuje s phishingovým týdnem 21

!!! tip "Tip pro učitele"
    nslookup je mocný nástroj a žáci jsou překvapeni, že „vidí" za kulis webu. Pokud škola blokuje příkazovou řádku, použijte webový DNS lookup — funguje stejně. Zmínka o Cloudflare 1.1.1.1 jako o soukromějším DNS otevírá diskusi o soukromí online — kdo vidí vaše DNS dotazy? Váš ISP? Alternativně Google? Otázka bez jednoznačné odpovědi — ale cenná pro kritické myšlení.
