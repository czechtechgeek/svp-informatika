# Jak funguje internet: Cesta paketu

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Digitální technologie
- **Výstup:** <div class="curriculumTag" data-code="I-9-3-01" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">I-9-3-01</span><span style="color: #374151;">Žák vysvětlí princip fungování digitálních technologií a sítí</span></div>

## 💬 Tip pro pátek
Pusťte žákům vizualizaci „Submarine Cable Map" — fyzické kabely pod oceánem, které propojují kontinenty. Fyzická realita internetu je překvapivá a fascinující.

## 🎯 Cíle hodiny

- Žák vysvětlí, co je datový paket a proč se data dělí na pakety
- Žák popíše cestu paketu od odesílatele k příjemci přes uzly sítě
- Žák vysvětlí funkci IP adresy a roli routeru při směrování paketů
- Žák rozlišuje TCP a UDP a uvede příklady použití obou protokolů

## 💡 Metodický postup

### 1. Analogie: Dopis rozdělený na pohlednice (8 min) — tabule

Učitel přinese velký list papíru a rozstříhá ho na 5 kousků:
- Každý kousek = paket
- Každý kousek má číslo (pořadí) a adresu příjemce
- Kousky mohou cestovat různými cestami a dorazit v jiném pořadí
- Příjemce složí zpět podle čísel

Proč pakety a ne jeden velký soubor? → Efektivita (více cest), odolnost (ztracený paket = jen malé zpomalení, ne ztráta celého souboru).

### 2. Cesta paketu — vrstvový model (12 min) — tabule

Zjednodušený model TCP/IP:

```
[Aplikace]          → HTTP, DNS, e-mail — „Co"
[Transport]         → TCP/UDP — „Jak spolehlivě"
[Síť/Internet]      → IP adresy, routing — „Kudy"
[Fyzická vrstva]    → kabel, WiFi, 4G — „Čím fyzicky"
```

**IP adresa** = adresa zařízení v síti (např. 192.168.1.1)
- IPv4: 4 čísla × 0–255 (cca 4 miliarda adres — nestačí)
- IPv6: hexadecimální, mnohem více adres

**Router** = „poštovní úřad" — přijme paket, rozhodne kudy dál.

### 3. Aktivita: Rolová hra „Jsem paket" (15 min) — bez počítače

Třída je síť:
- 4–5 „routerů" stojí uprostřed (mají tabulku směrování — papír)
- Zbývající žáci jsou „pakety" — mají lístek s IP adresou cíle
- Pakety se pohybují od routeru k routeru, každý router rozhodne, kam paket pošle
- Cíl: dostat paket na správnou „IP adresu" v místnosti

Diskuse: Co se stane, když jeden router „havaruje"? (Pakety hledají jinou cestu — robustnost internetu.)

### 4. TCP vs. UDP (10 min) — tabule

| Vlastnost | TCP | UDP |
|-----------|-----|-----|
| Spolehlivost | Potvrzení každého paketu | Žádné potvrzení |
| Rychlost | Pomalejší | Rychlejší |
| Pořadí | Garantováno | Nezaručeno |
| Použití | Web, e-mail, soubory | Video streaming, online hry, VoIP |

Příklad: YouTube — pokud ztratíme paket ve streamu, raději přeskočíme než čekáme na opakované zaslání.

## 📂 Podklady

- **Video — jak funguje internet (CZ):** YouTube „jak funguje internet animace" nebo „internet paket routing"
- **Vizualizace — Submarine Cable Map (EN):** [submarinecablemap.com](https://www.submarinecablemap.com) — fyzické kabely pod mořem
- **Interaktivní — howdnsworks (EN):** [howdns.works](https://howdns.works) — animované vysvětlení DNS
- **Simulátor sítě:** Cisco Packet Tracer (zdarma po registraci) — pro pokročilejší simulaci
- **Propojení s 7. ročníkem:** Router a LAN/WAN ze 7. ročníku — nyní jdeme hlouběji

!!! tip "Tip pro učitele"
    Rolová hra „jsem paket" je fyzická a žáci si ji pamatují. Připravte předem tabulky směrování pro routery (jednoduché: „pakety pro 192.168.1.X pošli doleva, ostatní doprava"). Pokud nemáte prostor pro pohyb, lze hru zjednodušit na sezení — žáci si předávají lístky v řadách. Propojení s fyzickým kabelem pod oceánem otevírá diskusi o geopolitice internetu (kdo vlastní kabely, co se stane při přerušení).
