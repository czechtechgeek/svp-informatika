# 📖 NÁVOD NA VYPLNĚNÍ PROJEKTU

Zde je praktický návod, jak vyplnit obsah jednotlivých týdnů v souladu se spirálovitým modelem.

---

## 1️⃣ STRUKTURA JEDNOHO TÝDNE

Každý soubor `tyden-XX.md` má následující strukturu:

```markdown
# [Téma - např. "Úvod: Pravidla učebny, digitální identita"]

## 🎯 Cíle hodiny

[Zde napište 3-5 konkrétních cílů, které by měl žák zvládnout]

Příklad:
- Pochopit pravidla práce v učebně
- Vytvořit si bezpečné heslo
- Vytvořit profil s digitální identitou
- Chápat základy bezpečnosti online

## 💡 Metodický postup

[Zde popište kroky realizace hodiny]

Příklad:
1. **Úvod (5 min)** - Seznámení s pravidly
2. **Aktivita 1 (15 min)** - Bezpečné heslo (unplugged)
3. **Aktivita 2 (15 min)** - Tvorba profilu
4. **Shrnutí (5 min)** - Diskuse o bezpečnosti

## 📂 Podklady

[Zde přidejte odkaz na materiály]

Příklad:
- **Prezentace:** [odkaz na prezentaci]
- **Pracovní list:** [odkaz na PDF]
- **Interaktivní prvky:** [odkaz na web]
- **Zdrojový kód:** [odkaz na GitHub]
```

---

## 2️⃣ PŘÍKLADY PRO JEDNOTLIVÉ ROČNÍKY

### 📌 6. ROČNÍK - Príklad vyplnění (tyden-01.md)

```markdown
# Úvod: Pravidla učebny, digitální identita

## 🎯 Cíle hodiny

- Pochopit pravidla práce s IT v učebně
- Vytvořit si bezpečné heslo (nebo je znát)
- Pochopit, co je digitální identita
- Zajistit si bezpečný přístup k datům
- Poznat základy online bezpečnosti

## 💡 Metodický postup

1. **Vstupní diskuse (5 minut)**
   - Co je bezpečné heslo?
   - Proč hesla nesmíme sdílet?

2. **Aktivita: Tvorba hesla (10 minut)**
   - Žáci si napíší heslo na papír
   - Cvičí se používáním "silného hesla"
   - Diskuse: co dělá heslo bezpečným?

3. **Aktivita: Digitální identita (15 minut)**
   - Jaké informace o mě jsou online?
   - Co je OK a co není?
   - Vytvoření seznamu osobních údajů

4. **Shrnutí (5 minut)**
   - Opakování klíčových pravidel
   - Domácí úkol: Zkontrolujte svá hesla doma

5. **Reflektivní otázky:**
   - Která pravidla jsou pro vás nejdůležitější?
   - Co byste dodali vy?

## 📂 Podklady

- **Prezentace:** `Digitální identita a bezpečnost` (PowerPoint)
- **Pracovní list:** `Tvorba silného hesla` (PDF)
- **Interaktivní hra:** [Password Game](https://passwords.google/)
- **Videa:**
  - [Bezpečné heslo](https://youtu.be/...)
  - [Ochrana osobních údajů](https://youtu.be/...)

**Domácí příprava:**
- Přečtěte si kapitolu o bezpečnosti v učebnici
- Zkontrolujte svá hesla
```

### 📌 7. ROČNÍK - Příklad vyplnění (tyden-06.md)

```markdown
# Podmínky I: "Když narazíš na hranu, odraz se"

## 🎯 Cíle hodiny

- Pochopit logiku podmínky (IF-THEN)
- Využít podmínky v Scratch (blok "Když")
- Vytvořit jednoduchou logiku pro hru
- Zvládnout rozhodování v kódu
- Debuggovat problém s podmínkami

## 💡 Metodický postup

1. **Úvod: Podmínky v reálném životě (5 minut)**
   - Když zazvonís zvonek → otevřu dveře
   - Když prší → vezmu si deštník
   - Demonstrace na postavě v Scratchi

2. **Aktivita 1: Seznámení s blokem Když (10 minut)**
   - Blok "Když" (if)
   - Porovnávání: =, <, >
   - Příkazy uvnitř bloku

3. **Aktivita 2: Odraz od okraje (15 minut)**
   ```
   Když se stane [dotyk barvy]
   Pak změň směr o 180 stupňů
   ```
   - Žáci naprogramují pohyb postavy
   - Budou testovat v emulátoru

4. **Aktivita 3: Vlastní logika (15 minut)**
   - Žáci si vytvoří svou vlastní podmínku
   - Např. "Když stisknu klávesu, změň kostým"

5. **Shrnutí (5 minut)**
   - Kde se používají podmínky?

## 📂 Podklady

- **Scratch projekt:** [Projekt - Odraz od okraje](https://scratch.mit.edu/projects/...)
- **Pracovní list:** Procvičování podmínek (PDF)
- **Videa tutoriály:**
  - [Pokročilé podmínky v Scratchi](https://youtu.be/...)
  - [IF-THEN logika pro začátečníky](https://youtu.be/...)
- **Obrázky:** Schémata rozhodovacích bloků

**Pro učitele:**
- Testujte projekt před hodinou
- Připravte si 2-3 příklady chyb, které se mohou stát
```

### 📌 8. ROČNÍK - Příklad vyplnění (tyden-16.md)

```markdown
# Jak funguje internet: Cesta paketu

## 🎯 Cíle hodiny

- Pochopit základní koncept přenosu dat
- Vysvětlit, co je balíček (packet)
- Znát roli routeru a DNS
- Simulovat cestu paketu
- Pochopit, proč je internet distribuovaný

## 💡 Metodický postup

1. **Úvod: Analýza (5 minut)**
   - Kde je informace, kterou právě posílám?
   - Jak se dostane do počítače kamaráda?
   - Živá demonstrace: ping příkaz

2. **Aktivita 1: Simulace bez počítače (15 minut)**
   - Třída jako internet: žáci jsou routery
   - Jeden žák pošle zprávu druhému
   - Zpráva se roztrhá na kousky (pakety)
   - Každý kousek jde jinou cestou
   - Diskuse: co se mohlo stát?

3. **Aktivita 2: Reálný internet - Wireshark (15 minut)**
   - Analýza pravé komunikace
   - Kde vidíme IPv4 adresu?
   - Kde vidíme DNS dotaz?

4. **Aktivita 3: Tracert příkaz (10 minut)**
   ```
   tracert google.com
   ```
   - Kolik hopů do Google?
   - Jaké IP adresy vidíme?

5. **Diskuse (5 minut)**
   - Bezpečnost: vidíme, co posílají ostatní?
   - HTTPS - ochrana dat

## 📂 Podklady

- **Simulátor:** [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer)
- **Nástroj:** Wireshark - analýza paketů
- **Videa:**
  - [Jak funguje DNS](https://youtu.be/...)
  - [IP adresy a routování](https://youtu.be/...)
- **Schémata:** Diagram cesty paketu internetu
- **Bezpečnostní aspekt:** HTTPS vs HTTP

**Domácí projekt:**
- Napište tracert pro 5 různých serverů
- Analyzujte výsledky
```

### 📌 9. ROČNÍK - Příklad vyplnění (tyden-05.md)

```markdown
# Python I: Print, proměnné, input

## 🎯 Cíle hodiny

- Pracovat s proměnnými v Pythonu
- Zvládnout příkaz print() pro výstup
- Zvládnout příkaz input() pro vstup
- Vytvořit jednoduchý program s interakcí
- Pochopit datové typy (string, int)

## 💡 Metodický postup

1. **Úvod: Co je proměnná? (5 minut)**
   - Analogie: krabice s etiketou
   - Kde se používají?
   - Python vs Scratch

2. **Aktivita 1: První program (10 minut)**
   ```python
   print("Ahoj světe!")
   jméno = "Petr"
   print("Jmenuju se", jméno)
   ```
   - Spuštění v PyCharm / Online IDE
   - Úprava a otestování

3. **Aktivita 2: Vstup od uživatele (10 minut)**
   ```python
   jméno = input("Jaké máš jméno? ")
   print("Ahoj", jméno)
   ```
   - Interakce s programem
   - Práce s proměnnými
   - Debugging: co se stalo?

4. **Aktivita 3: Věk a narození (10 minut)**
   ```python
   jméno = input("Tvé jméno: ")
   věk = input("Tvůj věk: ")
   print(jméno, "má", věk, "let")
   ```
   - Kombinování proměnných
   - Datové typy: string vs int

5. **Aktivita 4: Věk v budoucnosti (5 minut)**
   ```python
   věk = int(input("Tvůj věk: "))
   věk_za_10_let = věk + 10
   print("Za 10 let ti bude", věk_za_10_let)
   ```
   - Konverze typů (int)
   - Matematické operace

## 📂 Podklady

- **Online IDE:** [Replit.com](https://replit.com) nebo [Python.org](https://www.python.org/shell/)
- **IDE lokálně:** PyCharm Community Edition
- **Tutoriály:**
  - [Codecademy - Python kurz](https://www.codecademy.com/)
  - [W3Schools Python](https://www.w3schools.com/python/)
- **Ukázkové programy:** 
  - ahoj_svet.py
  - interaktivni_program.py
  - kalkulacka.py
- **Videa:** [Python pro začátečníky](https://youtu.be/...)

**Domácí úkol:**
- Vytvořte program, který se zeptá na vaše jméno a věk
- Program vypočítá, ve kterém roce se narodíte
- Sdílení přes GitHub
```

---

## 3️⃣ ŠABLONA PRO COPY-PASTE

```markdown
# [TÉMA Z OSNOVY]

## 🎯 Cíle hodiny

- Cíl 1
- Cíl 2
- Cíl 3
- Cíl 4
- Cíl 5

## 💡 Metodický postup

1. **Úvod (5 minut)**
   - Aktivita / diskuse

2. **Hlavní aktivita 1 (15 minut)**
   - Popis
   - Postup
   - Očekávaný výsledek

3. **Hlavní aktivita 2 (15 minut)**
   - Popis
   - Postup
   - Očekávaný výsledek

4. **Shrnutí (5 minut)**
   - Opakování
   - Reflexe

5. **Reflektivní otázky:**
   - Otázka 1
   - Otázka 2

## 📂 Podklady

- **Prezentace:** [odkaz]
- **Pracovní listy:** [odkaz]
- **Videa:** [odkaz]
- **Zdrojové kódy:** [odkaz]
- **Interaktivní prvky:** [odkaz]

**Domácí příprava / úkol:**
- Úkol 1
- Úkol 2
```

---

## 4️⃣ TIPY PRO VYPLNĚNÍ

### 🎓 Co dělá dobrou hodinu?

✅ **Cíle** - měřitelné, konkrétní, dosažitelné  
✅ **Aktivní učení** - co dělají žáci, ne co říkáte vy  
✅ **Sekvence** - od jednoduchého ke složitému  
✅ **Zpětná vazba** - jak víte, že žáci pochopili?  
✅ **Reflexe** - co jsme se naučili?  

### 🔄 Spirálový model

Pamatujte, že se témata vrací:

- **6. třída:** "Co je to data?" → Porozumění
- **7. třída:** "Jak data organizuji?" → Aplikace
- **8. třída:** "Jak data analyzuji?" → Analýza
- **9. třída:** "Jak data použiji v kontextu?" → Syntéza

### 📚 Kde najít inspiraci?

- **Code.org** - hotové lekce
- **Codecademy** - interaktivní kurzy
- **Khan Academy** - videa a cvičení
- **GitHub** - příklady projektů
- **Scratch komunita** - hotové projekty
- **YouTube edukační kanály** - tutoriály

---

## 5️⃣ PŘÍKLAD KOMPLETNÍHO ŘETĚZCE (Datové záhady)

Zde vidíte, jak se **jedno téma** vrací během 4 let:

### 6. ročník - Tyden 04: Kódování textu
- 🎯 Cíl: Pochopit ASCII
- 💡 Aktivita: Každé písmeno má číslo
- 📂 Pracovní list: Zašifruj svou zprávu

### 7. ročník - Tyden 07: Složené podmínky
- 🎯 Cíl: Pochopit AND, OR
- 💡 Aktivita: Rozhodování s více podmínkami
- 📂 Projekt: Tvorba hry s logikou

### 8. ročník - Tyden 19: Šifrování
- 🎯 Cíl: Od ASCII k RSA
- 💡 Aktivita: Analýza moderního šifrování
- 📂 Projekt: Vlastní šifra

### 9. ročník - Tyden 21: Digitální právo
- 🎯 Cíl: GDPR a šifrování osobních údajů
- 💡 Aktivita: Analýza bezpečnosti v praxi
- 📂 Projekt: Bezpečnostní audit

---

**Nyní máte vše, co potřebujete! Vyberte si týden a začněte psát! 🚀**

