---
grade: 8
week: 17
time: 45
area: Digitální technologie
rvp_codes:
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - "**Vysvětlí**, co je DNS a proč existuje (mapování doménových jmen na IP adresy)."
  - "**Popíše** postup DNS dotazu (rekurzivní resolver → root → TLD → autoritativní server)."
  - "**Vysvětlí** pojem DNS cache a TTL."
  - "**Uvede** příklady, jak může být DNS zneužit (DNS spoofing, DNS poisoning)."
time_budget:
  - type: discussion
    minutes: 7
  - type: board
    minutes: 15
  - type: pc
    minutes: 15
  - type: board
    minutes: 8
friday_tip: "Demo: změňte DNS server v nastavení počítače na 8.8.8.8 (Google) nebo 1.1.1.1 (Cloudflare) a otestujte rychlost načítání. Žáci vidí, že abstraktní nastavení má reálný dopad."
---

# ️ DNS: Telefonní seznam internetu

## 💡 Metodický postup

### 1. Problém: Pamatujeme si adresy?

<span class="act discussion">💬 Diskuse — 7 min</span>

Učitel se ptá: „Jaká je IP adresa Googlu?" (Nikdo neví.) „Ale víte, jak se jmenuje?" (google.com)

DNS = překlad jmen na čísla — jako telefonní seznam, kde hledáte jméno a dostanete číslo.

Bez DNS by každý musel pamatovat číselné IP adresy. DNS umožňuje lidsky čitelné názvy.

---

### 2. Jak DNS dotaz funguje

<span class="act board">🖊️ Tabule — 15 min</span>

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

---

### 3. Aktivita: DNS v příkazové řádce

<span class="act pc">💻 PC — 15 min</span>

<div class="zadani-pc">

Otevřete příkazovou řádku (Windows: `Win+R` → `cmd`) a spusťte:

```
nslookup google.com
nslookup youtube.com
nslookup seznam.cz
```

**Alternativa (web):** [mxtoolbox.com/DNSLookup.aspx](https://mxtoolbox.com/DNSLookup.aspx) — online DNS lookup

Zapište si IP adresy zjištěných webů a porovnejte. Proč má Google více IP adres?

</div>

*(Load balancing — více serverů pro miliardy uživatelů.)*

---

### 4. DNS a bezpečnost

<span class="act board">🖊️ Tabule — 8 min</span>

**DNS spoofing / poisoning:**
- Útočník podstrčí falešnou IP adresu pro legitimní doménu
- Uživatel zadá `banka.cz`, dostane falešnou IP → phishingový web
- Obrana: DNSSEC (ověřování digitálním podpisem), HTTPS (certifikát webu nesedí)

**DNS over HTTPS (DoH):**
- Šifrování DNS dotazů — ISP nevidí, jaké weby navštěvujete
- Dostupné v moderních prohlížečích a OS

---

## 📂 Zdroje a podklady

* **Animace DNS (EN):** [howdns.works](https://howdns.works) — krásná komiksová animace celého DNS procesu
* **Online DNS lookup:** [mxtoolbox.com](https://mxtoolbox.com/DNSLookup.aspx) nebo [dnschecker.org](https://dnschecker.org)
* **Video (CZ):** YouTube — „DNS vysvětlení česky jak funguje"
* **Veřejné DNS servery:** 8.8.8.8 (Google), 1.1.1.1 (Cloudflare), 9.9.9.9 (Quad9 — zaměřen na bezpečnost)
* **Propojení s bezpečností:** DNS spoofing propojuje s phishingovým týdnem 21

---

!!! tip "Tip pro učitele"
    nslookup je mocný nástroj a žáci jsou překvapeni, že „vidí" za kulis webu. Pokud škola blokuje příkazovou řádku, použijte webový DNS lookup — funguje stejně. Zmínka o Cloudflare 1.1.1.1 jako o soukromějším DNS otevírá diskusi o soukromí online — kdo vidí vaše DNS dotazy? Váš ISP? Alternativně Google? Otázka bez jednoznačné odpovědi — ale cenná pro kritické myšlení.
