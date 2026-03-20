# 📱 IoT: Internet věcí – rizika

> **Stav:** `⬜ Nekontrolováno`

### 📋 Kontext a cíle
> **RVP ZV (Informatika):** Digitální bezpečnost / Technologie
> **Kód:** `INF-INF-004-ZV9-013` – *Navrhne základní způsoby zabezpečení zařízení a systémů, se kterými pracuje, na základě posouzení rizik ztráty, poškození či zneužití dat.*
> **Kód:** `INF-INF-004-ZV9-014` – *Diskutuje o fungování digitálních technologií určujících trendy ve světě.*

**Po hodině žák:**
* **Definuje** pojem IoT a uvede konkrétní příklady IoT zařízení ze svého okolí.
* **Pojmenuje** hlavní bezpečnostní a soukromostní rizika spojená s IoT.
* **Analyzuje** reálný případ IoT útoku a navrhne opatření, jak mu předejít.
* **Posoudí**, jaká data o něm sbírají chytrá zařízení a jak to omezit.

---

### 💡 Metodický postup (45 min)

#### 1. Úvod: Kolik zařízení je online? (8 min)
*Diskuze.*

Učitel požádá žáky, aby odhadli, kolik zařízení připojených k internetu je v jejich domácnosti. Zapíše čísla na tabuli. Celkový odhad pro celou třídu bude pravděpodobně stovky zařízení.

Definice IoT: **Internet of Things (Internet věcí)** = síť fyzických zařízení (věcí), které jsou připojeny k internetu a sbírají nebo sdílejí data.

Přehled kategorií IoT zařízení:

| Kategorie | Příklady |
|-----------|---------|
| Chytrá domácnost | Chytré žárovky, termostaty (Nest), zámky, alarm |
| Zábava | Chytré TV, herní konzole, chytré reproduktory (Alexa, Google Home) |
| Zdraví a sport | Fitness náramky (Fitbit), chytré hodinky, glukometry |
| Doprava | Chytré auto (GPS, OBD dongle), elektrokoloběžky |
| Průmysl | Senzory ve výrobě, chytré elektrárny, nemocniční přístroje |
| Škola | Interaktivní tabule, 3D tiskárny, Raspberry Pi, BBC Micro:bit |

Zajímavé číslo: V roce 2024 bylo na světě připojeno přes **17 miliard IoT zařízení**. Do roku 2030 se odhaduje přes 30 miliard.

---

#### 2. Rizika IoT: Co může jít špatně? (12 min)
*Tabule — přehled rizik.*

Učitel projde tři hlavní kategorie rizik s reálnými příklady:

**1. Bezpečnostní rizika — útočníci se dostanou do sítě přes IoT:**
- Výchozí hesla: Většina IoT zařízení má výchozí heslo „admin" nebo „1234". Útočník to ví.
- Botnet Mirai (2016): Virus napadl statisíce nezabezpečených webkamer a routerů. Použil je k masivnímu útoku, který vyřadil Twitter, Netflix a Amazon na několik hodin.
- Chytrá žárovka jako vstupní bod: Vědci prokázali, že přes špatně zabezpečenou žárovku lze proniknout do celé domácí sítě a dostat se k počítači.

**2. Soukromostní rizika — zařízení sbírají víc dat, než čekáme:**
- Chytré reproduktory (Alexa, Google Home) nahrávají konverzace i bez záměrné aktivace.
- Fitness náramky znají váš spánek, srdeční tep, pohyb — a tato data prodávají třetím stranám.
- Chytrá TV sleduje, co díváte, a posílá data výrobci (tzv. ACR — Automatic Content Recognition).

**3. Fyzická bezpečnostní rizika:**
- Hacknutý chytrý zámek = útočník může fyzicky vstoupit do domu.
- Hacknuté chytré auto = útočník může ovlivnit brzdění nebo navigaci.
- Hacknutý nemocniční přístroj = přímé ohrožení života pacienta.

---

#### 3. Analýza případu: Útok na nemocnici přes termostat (15 min)
*PC nebo papír — skupinová práce.*

Žáci pracují ve skupinách po 3–4. Dostanou popis případu a odpoví na otázky.

**Případ:** Severoamerické kasino bylo hackováno přes akvárium. Útočníci se dostali do sítě skrze chytrý teploměr v akváriu — zařízení mělo výchozí heslo a bylo připojeno do firemní sítě. Z akváriového termostatu pak útočníci prošli do databáze VIP zákazníků.

**Otázky pro skupiny:**
1. Jaká chyba umožnila útok? *(výchozí heslo, IoT zařízení v hlavní síti)*
2. Jak byste kasino poradili, aby se to neopakovalo? *(změna hesla, oddělená síť pro IoT)*
3. Jaká zařízení ve vaší škole by mohla být podobným rizikem?
4. Co sbírá váš telefon, chytré hodinky nebo fitness náramek? Je to v pořádku?

Skupiny sdílejí závěry — učitel zapisuje doporučení na tabuli.

---

#### 4. Jak se chránit: Pravidla pro bezpečné IoT (10 min)
*Diskuze.*

Žáci navrhnou pravidla, učitel doplní:

1. **Změňte výchozí heslo** každého IoT zařízení hned po instalaci
2. **Oddělená Wi-Fi síť** — doma nastavte zvláštní síť jen pro IoT zařízení (funkce „guest network")
3. **Aktualizujte firmware** — výrobci vydávají opravy bezpečnostních chyb
4. **Přemýšlejte, co kupujete** — nepotřebujete chytrou žárovku od výrobce, o kterém jste neslyšeli
5. **Zkontrolujte oprávnění** — proč potřebuje fitness náramek přístup k vašim kontaktům?
6. **Starý router = riziko** — přes 5 let starý router pravděpodobně nedostává bezpečnostní aktualizace

---

### 🛠️ Zdroje a nástroje

* **Web — Shodan:** [shodan.io](https://www.shodan.io) — vyhledávač nezabezpečených IoT zařízení na internetu (ukázkové použití pouze pro demonstraci, nepoužívat pro přístup k cizím zařízením)
* **Video (EN/CZ):** YouTube — „Mirai botnet explained" nebo „IoT security risks" — dobré vizuální vysvětlení; ČT dokument o chytrých domácnostech
* **Web — NÚKIB:** [nukib.cz](https://www.nukib.cz) — doporučení pro zabezpečení domácí sítě
* **Propojení s praxí:** Raspberry Pi a BBC Micro:bit jsou také IoT zařízení — propojte s praktickými hodinami programování

---

> 💡 **Tip pro učitele:**
> Téma IoT je ideální pro propojení s domácím prostředím žáků — většina z nich má doma alespoň chytrou TV nebo chytrý reproduktor. Nechte žáky přemýšlet, jaká data o nich tato zařízení sbírají. Shodan.io je fascinující nástroj — učitel může promítnout vyhledání „default password camera" a ukázat, kolik nezabezpečených kamer je viditelných z internetu. Zdůrazněte ale, že k cizím zařízením se přistupovat nesmí — je to trestný čin.

> 💬 **Tip pro pátek:** Zeptejte se žáků, kolik chytrých zařízení mají doma — spočítají telefony, tablety, chytrou TV, router, případně chytré reproduktory nebo žárovky. Výsledná čísla je vždy překvapí a okamžitě propojí téma s jejich vlastní realitou.
