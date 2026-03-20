---
grade: 7
week: 16
time: 45
area: Digitální technologie
rvp_codes:
  - code: INF-INF-003-ZV9-010
    text: Pro řešení problému vytvoří tabulku evidence dat a stanoví pravidla pro práci se záznamy.
  - code: INF-INF-003-ZV9-009
    text: "Posoudí účel a užitečnost vybraného informačního systému, popíše jeho vnitřní fungování."
goals:
  - "Žák vysvětlí, co je cloudové úložiště a jak se liší od lokálního disku"
  - Žák se orientuje v rozhraní Google Drive nebo OneDrive (dle vybavení školy)
  - "Žák nahraje soubor do cloudu, vytvoří složky a organizuje dokumenty"
  - "Žák pochopí, proč je cloud výhodný pro zálohu a přístup z více zařízení"
time_budget:
  - type: unplugged
    minutes: 8
  - type: board
    minutes: 12
  - type: pc
    minutes: 20
friday_tip: "Analogie pro cloud: „Vaše fotky v mobilu jsou jako peněženka — máte je u sebe. Cloud je jako bankovní trezor — data jsou jinde, ale dostanete se k nim odkudkoliv.\" Žáci tuto analogii okamžitě pochopí."
---

# Cloud: Google Drive/OneDrive

## 💡 Metodický postup

### 1. Diskuse: Kde jsou vaše data?

<span class="act unplugged">✋ Bez počítače — 8 min</span>

Učitel se ptá:
- „Kam si ukládáte fotky z telefonu?"
- „Co se stane, když ztratíte mobil? Přijdete o fotky?"
- „Jak si posíláte soubory ze školy domů?"

Typické odpovědi: USB flash disk, e-mail sám sobě, přes Bluetooth, cloud (Google Foto, iCloud, OneDrive).

Učitel nakreslí schéma:
```
[PC škola] → USB disk → [PC doma]     (tradiční)
[PC škola] → Cloud   → [PC doma]     (cloud)
                     ↗ [Tablet]
                     ↗ [Mobil]
```

Výhoda cloudu: přístup odkudkoliv, automatická záloha, sdílení bez přenosu souboru.

### 2. Demo: Navigace v Google Drive

<span class="act board">🖊️ Tabule — 12 min</span>

Učitel otevře Drive na projektoru a ukáže:

1. **Domovská obrazovka:** Nedávné, Sdílené se mnou, Koš
2. **Vytvoření složky:** Pravý klik → Nová složka → pojmenovat
3. **Nahrání souboru:** Přetáhnout soubor nebo tlačítko „+ Nový"
4. **Typy dokumentů:** Docs (text), Sheets (tabulky), Slides (prezentace) — Google alternativy k MS Office
5. **Uložení:** „V Drive se ukládá automaticky — žádné Ctrl+S není třeba!"

Klíčový bod: dokument je uložen na serveru Google, ne na PC — proto funguje i po zavření karty.

### 3. Praktická aktivita: Uspořádejte složky

<span class="act pc">💻 PC — 20 min</span>

<div class="zadani-pc">

Přihlas se do svého školního Google účtu a splň tyto úkoly v Google Drive:

**Úkol 1:** Vytvoř strukturu složek:
```
Informatika 7. ročník/
├── 1. pololetí/
│   ├── Modelování/
│   └── Scratch projekty/
└── 2. pololetí/
```

**Úkol 2:** Nahraj alespoň jeden soubor (screenshot projektu, PDF, obrázek…) do příslušné složky.

**Úkol 3:** Vytvoř nový Google Doc s názvem „Moje poznámky — 7. třída" a napiš alespoň první větu.

**Úkol 4:** Ověř, že cloud opravdu funguje: otevři Google Drive na jiném zařízení nebo v anonymním okně a zkontroluj, že tvůj soubor tam je.

**Pro rychlé žáky:** Zkus zjistit, kolik úložného místa máš v Drive k dispozici a kolik z něj využíváš. Kde to najdeš?

</div>

### 4. Reflexe (5 min)

Diskuse:
- „Co se stane, pokud Google zanikne? (riziko závislosti na jedné platformě)"
- „Kdy byste raději data neukládali do cloudu?"
- „Kolik místa je zdarma? (Google: 15 GB, OneDrive: 5 GB)"

## 📂 Podklady

- **Google Drive:** [drive.google.com](https://drive.google.com) — přihlášení školním G-Suite účtem
- **OneDrive:** [onedrive.live.com](https://onedrive.live.com) — alternativa pro školy s Microsoft 365
- **Video (CZ):** Hledejte „Google Drive pro začátečníky CZ" — krátké tutoriály 5–8 min
- **Propojení s bezpečností (preview):** Cloud = data na cizím serveru → čí jsou vlastně? (téma týden 22)
- **Šablona struktury složek:** Připravte screenshot doporučené struktury složek jako vzor

!!! tip "Tip pro učitele"
    Pokud škola nemá G-Suite for Education ani Microsoft 365, je cloud obtížné prakticky ukázat — žáci nemají školní účty. V tom případě použijte simulaci: ukažte rozhraní na projektoru a nechejte žáky kreslit strukturu složek na papír. Alternativně mohou žáci použít osobní Google účet (rodiče musí souhlasit pro žáky pod 13 let — ověřte GDPR podmínky vaší školy).
