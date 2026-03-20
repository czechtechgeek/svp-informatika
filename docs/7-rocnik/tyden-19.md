# Počítačová síť: Router a kabel

## 📋 Vazba na RVP ZV (Informatika)
- **Oblast:** Digitální technologie
- **Výstup:** <div class="curriculumTag" data-code="INF-INF-003-ZV9-009" style="display: inline-flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px 10px; background-color: #f0f7ff; border: 1px solid #1975FE; border-radius: 6px; font-size: 13px; margin: 2px 4px 2px 0; user-select: none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1975FE" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span style="color: #1975FE; font-weight: 500;">INF-INF-003-ZV9-009</span><span style="color: #374151;">Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování.</span></div>

## 💬 Tip pro pátek
Fyzická ukázka: přineste do třídy starý kabelový síťový kabel (RJ-45), router (starý domácí) nebo přepínač. Žáci si je mohou prohlédnout, zeptat se na konektory. Fyzický kontakt s technologií zvyšuje zájem.

## 🎯 Cíle hodiny

- Žák vysvětlí, co je počítačová síť a proč ji potřebujeme
- Žák rozlišuje základní síťová zařízení: router, switch, přístupový bod (AP)
- Žák popíše cestu datového paketu od odesílatele k příjemci
- Žák rozlišuje wired (kabelové) a wireless (WiFi) připojení a uvede výhody každého

## 💡 Metodický postup

### 1. Úvod: Proč sítě existují? (8 min) — diskuse

Učitel se ptá: „Jak sdílíte soubory ve třídě? Jak se dostanete na internet?" Žáci odpovídají.

Historické propojení: První počítačové sítě sloužily armádě (ARPANET, 1969) — propojení 4 počítačů. Dnes: miliarda zařízení.

Klíčové pojmy:
- **LAN** (Local Area Network): síť v místnosti/budově
- **WAN** (Wide Area Network): síť přes velké vzdálenosti (internet je WAN)
- **Router**: zařízení, které propojuje LAN s WAN (internetu) a přiděluje adresy

### 2. Schéma sítě: Jak vypadá školní síť? (10 min) — tabule

Učitel kreslí na tabuli:

```
[Internet (WAN)]
       |
   [Router]     ← Brána mezi LAN a WAN
       |
   [Switch]     ← Rozdělovač pro více PC
   /  |  \
[PC1][PC2][PC3]  ← Stanice

     WiFi AP    ← Bezdrátový přístupový bod
   /    \
[Tablet][Mobil]
```

Žáci hádají: Kde v tomto schématu je vaše mobilní data (4G)? → Mobilní síť = jiný typ WAN.

### 3. Aktivita: Simulace síťové komunikace (15 min) — bez počítače

**Rolová hra — „Žáci jsou pakety":**

Třída se rozdělí na skupiny: Odesílatel, Router, Switch, Příjemce.

Odesílatel napíše zprávu na papírek a předá Routeru. Router „rozhodne" (losování), kudy zpráva jde. Switch ji nasměruje na správný PC. Příjemce přijme.

Klíčové otázky po aktivitě:
- „Co se stane, pokud router ‚havaruje'?" (výpadek internetu)
- „Jak router ví, kam paket poslat?" (IP adresa — preview na týden 20)
- „Proč jsou pakety rozděleny na menší části, ne jeden velký soubor?"

### 4. Kabelové vs. WiFi — diskuse (7 min) — tabule

| Vlastnost | Kabel (Ethernet) | WiFi |
|-----------|-----------------|------|
| Rychlost | Velmi vysoká (1 Gbps+) | Nižší (100–600 Mbps) |
| Stabilita | Výborná | Závisí na prostředí |
| Mobilita | Žádná | Plná |
| Bezpečnost | Vyšší | Nižší (odposlech) |
| Cena | Kabel + konektor | Levnější zařízení |

Diskuse: „Kdy byste použili kabel? Kdy WiFi?" (herní PC = kabel; mobil = WiFi)

## 📂 Podklady

- **Simulátor sítě (CZ/EN):** [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer) — zdarma po registraci, simulace sítí pro výuku
- **Video (CZ):** Hledejte „jak funguje internet CZ" nebo „počítačová síť vysvětlení" — ČT edu nebo YouTube
- **Fyzická ukázka:** Síťový kabel RJ-45 k prohlédnutí, starý router (vypnutý)
- **Interaktivní (EN):** [howdnsworks.com](https://howdns.works) — krásně animovaná vysvětlení DNS a sítí (pro pokročilé)
- **Propojení s bezpečností:** WiFi je snadněji odposlouchatelná — proto HTTPS a VPN (témata bezpečnosti)

!!! tip "Tip pro učitele"
    Síťová témata jsou abstraktní — fyzické předměty a rolová hra pomáhají. Pokud máte ve škole možnost zajít do serverovny nebo technické místnosti se síťovými prvky, je to cenná exkurze. Žáci, kteří hrají online hry, mají intuitivní pochopení pojmů ping (latence) a rychlost stahování — využijte jejich zkušenost jako vstupní bod.
