---
grade: 7
week: 19
time: 45
area: Digitální technologie
rvp_codes:
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - "Žák vysvětlí, co je počítačová síť a proč ji potřebujeme"
  - "Žák rozlišuje základní síťová zařízení: router, switch, přístupový bod (AP)"
  - Žák popíše cestu datového paketu od odesílatele k příjemci
  - Žák rozlišuje wired (kabelové) a wireless (WiFi) připojení a uvede výhody každého
time_budget:
  - type: discussion
    minutes: 8
  - type: board
    minutes: 10
  - type: unplugged
    minutes: 15
  - type: board
    minutes: 7
friday_tip: "Fyzická ukázka: přineste do třídy starý kabelový síťový kabel (RJ-45), router (starý domácí) nebo přepínač. Žáci si je mohou prohlédnout, zeptat se na konektory. Fyzický kontakt s technologií zvyšuje zájem."
---

# Počítačová síť: Router a kabel

## 💡 Metodický postup

### 1. Úvod: Proč sítě existují?

<span class="act discussion">💬 Diskuse — 8 min</span>

Učitel se ptá: „Jak sdílíte soubory ve třídě? Jak se dostanete na internet?" Žáci odpovídají.

Historické propojení: První počítačové sítě sloužily armádě (ARPANET, 1969) — propojení 4 počítačů. Dnes: miliarda zařízení.

Klíčové pojmy:
- **LAN** (Local Area Network): síť v místnosti/budově
- **WAN** (Wide Area Network): síť přes velké vzdálenosti (internet je WAN)
- **Router**: zařízení, které propojuje LAN s WAN (internetu) a přiděluje adresy

### 2. Schéma sítě: Jak vypadá školní síť?

<span class="act board">🖊️ Tabule — 10 min</span>

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

### 3. Aktivita: Simulace síťové komunikace

<span class="act unplugged">✋ Bez počítače — 15 min</span>

**Rolová hra — „Žáci jsou pakety":**

Třída se rozdělí na skupiny: Odesílatel, Router, Switch, Příjemce.

Odesílatel napíše zprávu na papírek a předá Routeru. Router „rozhodne" (losování), kudy zpráva jde. Switch ji nasměruje na správný PC. Příjemce přijme.

Klíčové otázky po aktivitě:
- „Co se stane, pokud router ‚havaruje'?" (výpadek internetu)
- „Jak router ví, kam paket poslat?" (IP adresa — preview na týden 20)
- „Proč jsou pakety rozděleny na menší části, ne jeden velký soubor?"

### 4. Kabelové vs. WiFi — diskuse

<span class="act board">🖊️ Tabule — 7 min</span>

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
