---
grade: 9
week: 22
time: 45
area: "Data, informace a modelování / Digitální společnost"
rvp_codes:
  - code: INF-INF-004-ZV9-014
    text: Diskutuje o fungování digitálních technologií určujících trendy ve světě.
  - code: INF-INF-001-ZV9-001
    text: "Získá z dat informace, interpretuje data získaná pro řešení konkrétního problému."
goals:
  - Žák vysvětlí princip distribuovaného záznamu (blockchain) vlastními slovy
  - "Žák popíše, jak probíhá transakce s kryptoměnou od odeslání po potvrzení"
  - Žák uvede alespoň dvě výhody a dvě rizika kryptoměn oproti tradičním penězům
  - Žák posoudí ekologický dopad těžby (miningu) kryptoměn
time_budget:
  - type: unplugged
    minutes: 10
  - type: board
    minutes: 10
  - type: discussion
    minutes: 15
  - type: review
    minutes: 10
friday_tip: "Přineste na hodinu vytištěný QR kód „peněženky\" s nulovou hodnotou a ukažte žákům, jak vypadá adresa v blockchainu. Abstraktní technologie okamžitě dostane vizuální podobu. Téma kryptoměn žáky silně motivuje — využijte to, ale dbejte na to, aby odcházeli s kritickým pohledem, ne s touhou investovat."
---

# 

## 💡 Metodický postup

### 1. Co je blockchain? Analogie s třídní knihou

<span class="act unplugged">✋ Bez počítače — 10 min</span>

Učitel vysvětlí blockchain pomocí analogie:

> Představte si, že každý žák v celé škole má stejný sešit, do kterého se zapisují všechny transakce (kdo komu co dal). Nikdo nemůže záznam smazat, protože všichni ostatní mají stejnou kopii. Kdo by chtěl podvádět, musel by změnit sešity u každého žáka najednou — to je prakticky nemožné.

**Klíčové pojmy:**
- **Blok** = skupina potvrzených transakcí (záznam v sešitu)
- **Řetěz (chain)** = každý blok odkazuje na předchozí, nelze ho vložit bez změny všech ostatních
- **Distribuovanost** = tisíce počítačů (nodes) uchovávají stejnou kopii
- **Neměnnost** = jednou zapsaná transakce nelze smazat

Učitel nakreslí na tabuli schéma: blok → blok → blok s šipkami a hash hodnotami.

### 2. Jak funguje transakce?

<span class="act board">🖊️ Tabule — 10 min</span>

Učitel provede žáky příkladem transakce Bitcoin:

1. **Vytvoření transakce:** Petr chce poslat 0,01 BTC Janě. Použije svou soukromou peněženku.
2. **Vysílání do sítě:** Transakce se odešle do sítě tisíců počítačů (peer-to-peer).
3. **Ověření (mining):** Speciální počítače (těžaři) soutěží o potvrzení bloku — řeší výpočetně náročný matematický úkol.
4. **Zapsání do blockchainu:** Vítěz blok zapíše a dostane odměnu (nové BTC). Transakce je potvrzena.
5. **Finalizace:** Po 6 potvrzeních (dalších blocích) je transakce zcela bezpečná (~1 hodina u Bitcoinu).

**Pojmy k zápisu:** peněženka (wallet), veřejný a soukromý klíč, mining, hash, node

### 3. Výhody, rizika a kritické myšlení

<span class="act discussion">💬 Diskuse — 15 min</span>

Žáci ve dvojicích vyplní tabulku (5 min), pak se diskutuje společně (10 min):

| Výhody kryptoměn | Rizika kryptoměn |
|------------------|-----------------|
| Bez zprostředkovatele (banky) | Extrémní cenová volatilita |
| Anonymita transakcí | Používání pro nelegální obchody |
| Celosvětové platby bez poplatků | Ztráta přístupu = ztráta peněz navždy |
| Odolnost vůči cenzuře | Obrovská spotřeba energie (mining) |
| Transparentnost — každý vidí historii | Podvody, Ponziho schémata, falešné projekty |

**Ekologický dopad — fakta k diskusi:**
- Bitcoin spotřebuje ročně tolik elektřiny jako celé Finsko nebo Argentina
- Důvod: mining vyžaduje miliony počítačů počítajících 24/7
- Alternativa: Ethereum přešlo v roce 2022 na Proof of Stake — spotřeba klesla o 99,95 %

Otázky pro diskusi:
- „Myslíte, že kryptoměny nahradí běžné peníze?"
- „Byl/a byste ochotný/á investovat úspory do Bitcoinu? Proč ano/ne?"

### 4. Kvíz — pravda nebo mýtus?

<span class="act review">🔍 Reflexe — 10 min</span>

Učitel čte tvrzení, žáci hlasují:

1. „Bitcoin je anonymní — nikdo nemůže sledovat moje transakce." → Mýtus (pseudoanonymita — transakce jsou veřejné, adresa lze dohledat)
2. „Blockchain lze snadno hacknut a data smazat." → Mýtus (prakticky nemožné kvůli distribuci)
3. „Kryptoměny jsou regulované českou vládou." → Pravda (od 2023 podléhají daňové povinnosti)
4. „Mining škodí životnímu prostředí." → Pravda (enormní spotřeba energie)
5. „Ztratím-li soukromý klíč peněženky, přijdu o všechny kryptoměny." → Pravda

## 📂 Podklady

- **Interaktivní demo blockchainu:** [andersbrownworth.com/blockchain](https://andersbrownworth.com/blockchain) — vizuální simulace hashování a tvorby bloků
- **Video (EN, CZ titulky):** YouTube — „But how does bitcoin actually work?" (3Blue1Brown)
- **Statistiky spotřeby energie:** [digiconomist.net/bitcoin-energy-consumption](https://digiconomist.net/bitcoin-energy-consumption)
- **ČNB o kryptoměnách (CZ):** cnb.cz — sekce pro spotřebitele, rizika kryptoměn
- **Nástroj pro simulaci:** Bitaddress.org — ukázka generování peněženky (pouze pro demonstraci)

!!! tip "Tip pro učitele"
    Nejsilnějším momentem hodiny bývá demo na andersbrownworth.com — žáci sami zkusí změnit jeden znak v bloku a vidí, jak se změní hash a celý řetěz se „rozbije". To je mnohem účinnější než jakékoliv vysvětlování. Dejte si pozor na to, aby hodina neskončila jako návod k investování — zdůrazněte, že velká část projektů jsou podvody a volatilita je obrovská.
