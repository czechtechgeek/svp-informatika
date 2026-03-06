# PŘEHLED VYTVOŘENÉHO PROJEKTU
## Digitální kniha Informatiky - ŠVP pro 2. stupeň

---

## ✅ CO BYLO VYTVOŘENO

### 📁 Adresářová struktura
```
docs/
├── index.md                 (Hlavní vstupní stránka)
├── 6-rocnik/
│   ├── index.md             (Rozcestník 6. ročníku)
│   └── tyden-01.md až tyden-31.md
├── 7-rocnik/
│   ├── index.md             (Rozcestník 7. ročníku)
│   └── tyden-01.md až tyden-30.md
├── 8-rocnik/
│   ├── index.md             (Rozcestník 8. ročníku)
│   └── tyden-01.md až tyden-30.md
└── 9-rocnik/
    ├── index.md             (Rozcestník 9. ročníku)
    └── tyden-01.md až tyden-30.md
```

### 📊 STATISTIKA
- **Celkem souborů:** 125 Markdown souborů
  - 6. ročník: 32 souborů
  - 7. ročník: 31 souborů
  - 8. ročník: 31 souborů
  - 9. ročník: 31 souborů

### 🔧 KONFIGURAČNÍ SOUBOR
**mkdocs.yml** - Aktualizován s:
- Nastavením motivu Material Theme
- Aktivací navigačních prvků (tabs, sections, expand)
- Komplexní navigační strukturou (nav:) se všemi ročníky a pololetími
- Povolením rozšíření (tables, admonition, superfences, details)

### 📄 OBSAH SOUBORŮ

#### Hlavní index (`docs/index.md`)
- Úvodní představení projektu
- Popis spirálovitého modelu výuky
- Přehled všech 4 ročníků s odkazy
- Instrukce pro učitele

#### Indexy ročníků (`6-rocnik/index.md` atd.)
Každý obsahuje:
- Nadpis ročníku s cílem
- Tabulku s přehledem všech témata
- Relativní odkazů na jednotlivé týdny
- Diferenciaci do 1. a 2. pololetí

#### Šablony týdnů (`tyden-XX.md`)
Každý týden obsahuje:
- Nadpis s tématem z osnovy
- Sekci **🎯 Cíle hodiny** (prázdná - připravená na vyplnění)
- Sekci **💡 Metodický postup** (prázdná - připravená na vyplnění)
- Sekci **📂 Podklady** (prázdná - připravená na vyplnění)

---

## 🎯 CO OBSAHUJÍ JEDNOTLIVÉ ROČNÍKY

### 6. ROČNÍK: Objevitel (31 týdnů)
**Cíl:** Přechod od uživatelského ovládání k pochopení principů dat a algoritmů.

**1. Pololetí** (15 týdnů):
- Data, informace, kódování (obraz, text, binární)
- Souborový systém
- Algoritmy a instruktáž
- Scratch (základy - pohyb, události, cykly, zvuky)
- Vánoční projekt, opakování

**2. Pololetí** (16 týdnů):
- Hardware a software
- Internet (prohlížeč, vyhledávač)
- Bezpečnost (hesla, netiketa)
- Tabulky a grafy
- Autorská práva a vyhledávání
- Projektová práce

### 7. ROČNÍK: Tvůrce (30 týdnů)
**Cíl:** Modelování reality a interaktivní programování.

**1. Pololetí** (15 týdnů):
- Modelování (myšlenkové mapy, schémata, diagramy)
- Scratch (pokročilé bloky)
- Podmínky a interakce
- Proměnné
- Projekt: tvorba hry
- Vánoční pixel-art projekt

**2. Pololetí** (15 týdnů):
- Cloud a sdílení
- Počítačová síť a IP adresy
- HTML základy
- Bezpečnost (sociální sítě, kyberšikana, digitální stopa)
- Fotografie, video
- Projekt: digitální časopis

### 8. ROČNÍK: Analytik (31 týdnů)
**Cíl:** Práce s daty jako nástrojem a úvod do fyzického computingu.

**1. Pololetí** (15 týdnů):
- Data v 21. století
- Pokročilé tabulky (funkce IF, MIN, MAX)
- Vizualizace a klamání daty
- Micro:bit (program, tlačítka)
- Senzory (akcelerometr, teplota, světlo)
- Radiová komunikace
- Projekt: robot (návrh, programování)
- Vánoční světelná show

**2. Pololetí** (16 týdnů):
- Internet (cesta paketu, DNS, protokoly)
- Šifrování a bezpečnost
- Malware, phishing, sociální inženýrství
- Dvoufázové ověření a IoT
- E-commerce a bezpečné platby
- 3D modelování (Tinkercad)
- Projekt: chytrého města

### 9. ROČNÍK: Expert (30 týdnů)
**Cíl:** Syntéza znalostí, AI a příprava na realitu.

**1. Pololetí** (15 týdnů):
- Simulace (co se stane, když...?)
- Finanční gramotnost
- Python (print, proměnné, input, výpočty, želví grafika)
- Debugging a seznamy
- Funkce
- Projekt: závěrečný kódovací projekt
- Vánoční generativní umění

**2. Pololetí** (15 týdnů):
- Umělá inteligence (strojové učení, LLM)
- Prompt engineering
- AI a etika
- Budoucnost práce
- Digitální právo (GDPR, Creative Commons)
- Blockchain a kryptoměny
- Informační válka a dezinformace
- Kybernetická obrana
- Digitální wellbeing
- Projekt: digitální portfolio pro střední školu

---

## 🚀 NÁVOD NA SPUŠTĚNÍ (POKUD MÁTE MKDOCS NAINSTALOVÁN)

```bash
# 1. Instalace mkdocs (pokud není nainstalován)
pip install mkdocs mkdocs-material

# 2. Spuštění lokálního serveru
cd C:\Users\tichy\git\svp-informatika
mkdocs serve

# 3. Otevřete v prohlížeči: http://127.0.0.1:8000
```

## 📝 DALŠÍ KROKY

1. **Vyplnění obsahu:** Doplňte obsahy do sekcí:
   - 🎯 Cíle hodiny
   - 💡 Metodický postup
   - 📂 Podklady (odkazy na materiály, pracovní listy, atd.)

2. **Přidání médií:** Vytvořte podsložky pro:
   - `img/` - obrázky, schémata, diagramy
   - `files/` - pracovní listy, zdrojové kódy
   - `presentations/` - prezentace

3. **Úprava tématu:** V `mkdocs.yml` lze upravit:
   - Barvy (primary: teal, accent: deep orange)
   - Fonty a dalších stylů
   - Navigační funkce

4. **Publikování:** Pro zveřejnění webu:
   - GitHub Pages
   - Netlify
   - vlastní server s `mkdocs build`

---

## ✨ VLASTNOSTI PROJEKTU

✅ **Strukturovanost:** Spirálovitý model - témata se vrací v progresivně vyšší náročnosti  
✅ **Komplexnost:** 4 ročníky, 122 hodin výuky, 122 témat  
✅ **Flexibilita:** Snadno se přidávají nové materiály  
✅ **Dostupnost:** Volně šiřitelné pro potřeby vzdělávání  
✅ **Moderne:** Využívá aktuální technologie (Python, AI, IoT, blockchain)  

---

**Projekt je připraven k použití. Veškeré soubory byly vytvořeny a správně nakonfigurovány.**

