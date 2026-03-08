# Kryptoměny a Blockchain

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Data, informace a modelování / Digitální společnost
- **Výstup:** <div class="curriculumTag" data-code="I-9-4-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-4-01</span><span style="color: #374151;">Žák kriticky hodnotí digitální obsah a dokáže posoudit věrohodnost a dopad digitálních technologií</span></div>
- **Výstup:** <div class="curriculumTag" data-code="I-9-1-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-1-01</span><span style="color: #374151;">Žák popíše způsoby reprezentace a kódování dat v digitálních systémech</span></div>

## 💬 Tip pro pátek
Přineste na hodinu vytištěný QR kód „peněženky" s nulovou hodnotou a ukažte žákům, jak vypadá adresa v blockchainu. Abstraktní technologie okamžitě dostane vizuální podobu. Téma kryptoměn žáky silně motivuje — využijte to, ale dbejte na to, aby odcházeli s kritickým pohledem, ne s touhou investovat.

## 🎯 Cíle hodiny

- Žák vysvětlí princip distribuovaného záznamu (blockchain) vlastními slovy
- Žák popíše, jak probíhá transakce s kryptoměnou od odeslání po potvrzení
- Žák uvede alespoň dvě výhody a dvě rizika kryptoměn oproti tradičním penězům
- Žák posoudí ekologický dopad těžby (miningu) kryptoměn

## 💡 Metodický postup

### 1. Co je blockchain? Analogie s třídní knihou (10 min) — bez počítače

Učitel vysvětlí blockchain pomocí analogie:

> Představte si, že každý žák v celé škole má stejný sešit, do kterého se zapisují všechny transakce (kdo komu co dal). Nikdo nemůže záznam smazat, protože všichni ostatní mají stejnou kopii. Kdo by chtěl podvádět, musel by změnit sešity u každého žáka najednou — to je prakticky nemožné.

**Klíčové pojmy:**
- **Blok** = skupina potvrzených transakcí (záznam v sešitu)
- **Řetěz (chain)** = každý blok odkazuje na předchozí, nelze ho vložit bez změny všech ostatních
- **Distribuovanost** = tisíce počítačů (nodes) uchovávají stejnou kopii
- **Neměnnost** = jednou zapsaná transakce nelze smazat

Učitel nakreslí na tabuli schéma: blok → blok → blok s šipkami a hash hodnotami.

### 2. Jak funguje transakce? (10 min) — tabule

Učitel provede žáky příkladem transakce Bitcoin:

1. **Vytvoření transakce:** Petr chce poslat 0,01 BTC Janě. Použije svou soukromou peněženku.
2. **Vysílání do sítě:** Transakce se odešle do sítě tisíců počítačů (peer-to-peer).
3. **Ověření (mining):** Speciální počítače (těžaři) soutěží o potvrzení bloku — řeší výpočetně náročný matematický úkol.
4. **Zapsání do blockchainu:** Vítěz blok zapíše a dostane odměnu (nové BTC). Transakce je potvrzena.
5. **Finalizace:** Po 6 potvrzeních (dalších blocích) je transakce zcela bezpečná (~1 hodina u Bitcoinu).

**Pojmy k zápisu:** peněženka (wallet), veřejný a soukromý klíč, mining, hash, node

### 3. Výhody, rizika a kritické myšlení (15 min) — diskuse

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

### 4. Kvíz — pravda nebo mýtus? (10 min) — kvíz

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
