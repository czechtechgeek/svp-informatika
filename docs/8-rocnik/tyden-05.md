---
grade: 8
week: 5
time: 45
area: "Data, informace a modelování / Digitální společnost"
rvp_codes:
  - code: INF-INF-001-ZV9-002
    text: Navrhuje a porovnává různé způsoby kódování dat s cílem jejich uložení a přenosu.
  - code: INF-INF-004-ZV9-014
    text: Diskutuje o fungování digitálních technologií určujících trendy ve světě.
goals:
  - "**Identifikuje** nejčastější techniky klamavé vizualizace dat (zkrácená osa, 3D efekty, cherry picking)."
  - "**Analyzuje** konkrétní příklady klamavých grafů a pojmenuje použitou manipulaci."
  - "**Vytvoří** vlastní „klamavý\" a „poctivý\" graf ze stejných dat."
  - "**Aplikuje** kritický přístup k datovým vizualizacím v médiích."
time_budget:
  - type: board
    minutes: 8
  - type: board
    minutes: 12
  - type: pc
    minutes: 18
  - type: discussion
    minutes: 7
friday_tip: "Prohlídka novin nebo zpravodajských webů: najděte s žáky jeden graf živě a analyzujte ho. Reálný případ z aktuálního dne je silnější než jakýkoli připravený příklad."
---

# Klamání daty: Grafy v médiích

## 💡 Metodický postup

### 1. Úvod: Může lhát pravdivé číslo?

<span class="act board">🖊️ Tabule — 8 min</span>

Učitel napíše na tabuli: „Nezaměstnanost klesla z 5,2 % na 5,0 %."

Otázka: „Je to dobrá zpráva?" Pak ukáže dva grafy ze stejných dat:

- **Graf A:** Osa Y začíná od 0 % — pokles je téměř neviditelný
- **Graf B:** Osa Y začíná od 4,8 % — pokles vypadá dramaticky (velký skok)

Závěr: Čísla jsou pravdivá. Graf lže způsobem, jakým je znázorní.

---

### 2. Katalog klamavých technik

<span class="act board">🖊️ Tabule — 12 min</span>

Učitel projde se třídou přehled technik:

| Technika | Jak funguje | Jak odhalit |
|----------|-------------|-------------|
| Zkrácená osa Y | Osa nezačíná od nuly — malé změny vypadají velké | Vždy zkontroluj začátek osy |
| 3D efekt | Perspektiva zkresluje plochy výsečí | Poptej 2D verzi nebo procenta |
| Cherry picking | Vybrané časové období podporuje požadovaný závěr | Zeptej se: „A co bylo předtím?" |
| Překrývající se kategorie | Kategorie se překrývají → součet > 100 % | Zkontroluj, zda součet dává smysl |
| Zavádějící měřítko | Obrázky nebo bubliny neodpovídají hodnotám | Porovnej hodnoty s vizuální velikostí |

---

### 3. Praktická aktivita: Oprav graf

<span class="act pc">💻 PC — 18 min</span>

Zadaná data — vývoj prodejů e-shopu:

| Měsíc | Prodeje (tis. Kč) |
|-------|-------------------|
| Říjen | 842 |
| Listopad | 856 |
| Prosinec | 871 |

<div class="zadani-pc" markdown="1">

**Část A:** Ze zadaných dat vytvořte záměrně **zavádějící graf** (zkraťte osu Y, vyberte vhodné časové okno) — ať vypadá jako dramatický růst.

**Část B:** Ze stejných dat vytvořte **poctivý graf** (osa od 0, korektní popis os a nadpis).

**Část C:** Vyměňte oba grafy se sousedem — pozná manipulaci? Diskutujte, co přesně dělá každý graf zavádějícím.

</div>

---

### 4. Reflexe: Jak se bránit?

<span class="act discussion">💬 Diskuse — 7 min</span>

Checklist pro analýzu grafu:
1. Kde začíná osa Y?
2. Jaký je časový rozsah?
3. Co chybí v legendě nebo popisu?
4. Kdo graf vytvořil a co z toho má?

---

## 📂 Zdroje a podklady

* **Web — Calling Bullshit (EN):** [callingbullshit.org](https://www.callingbullshit.org) — galerie klamavých vizualizací s vysvětlením
* **Kniha (CZ):** „Jak lhát se statistikou" — Darrell Huff; dostupná v knihovnách, čtivá a krátká
* **Web — Misleading graphs (EN):** hledejte „misleading graphs examples" — stovky reálných příkladů
* **Video (CZ):** YouTube — „klamavé grafy statistiky" nebo „jak lhát s čísly"
* **Propojení s matematikou:** Procenta a absolutní změny — stejné téma se jiným pohledem

---

!!! tip "Tip pro učitele"
    Tato hodina má velký potenciál pro debatu. Žáci se přirozeně ptají: „Dělají to novináři záměrně?" Odpověď: Někdy ano (politická agenda), někdy ne (neznalost vizualizace). Obojí je problém. Veďte žáky k tomu, že odhalení manipulace není o politickém přesvědčení — je to analytická dovednost. Příklady najdete v aktuálním tisku i na sociálních sítích.
