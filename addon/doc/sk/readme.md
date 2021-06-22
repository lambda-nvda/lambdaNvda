# Lambda #

* Autor: Alberto Zanella a ďalší.
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [vývojovú verziu][2]

Doplnok zlepšuje prístupnosť matematického editora Lambda. Ide o upravenú verziu pôvodného kódu od Petra Leckého z Univerzity Komenského.
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) je matematický editor špeciálne vyvinutý tak, aby uľahčoval zapisovanie matematických výpočtov nevidiacim s použitím braillovského riadka alebo hlasového výstupu.
Program LAMBDA vznikol vďaka podpore z fondou Európskej únie. Viac sa dočítate na [https://www.lambdaproject.org (anglicky)](https://www.lambdaproject.org/).  
Aktuálna verzia doplnku obsahuje Taliansku a Španielsku braillovskú tabuľku
(Slovenská zatiaľ nie je súčasťou). Doplnok je preložený do viacerých
jazykov (vrátane slovenčiny). Ak by ste chceli prispieť a napríklad viete
pomôcť s pridaním slovenskej tabuľky, kontaktujte autorov, alebo sa
prihláste do mailinglistu (V Taliančine alebo Angličtine).

**Upozorňujeme:** Doplnok vznikol vo voľnom čase a jeho autorom je Alberto Zanella. Autor ale nie je vývojárom samotného editora LAMBDA. V prípade problémov s editorom LAMBDA sa prosím obráďte na vášho dodávateľa. Ak máte priamo problémy s doplnkom, kontaktujte autora doplnku alebo hláste chybu cez odkaz "Issues" cez Github.

### [Repozitár na Github](https://github.com/lambda-nvda/lambdaNvda/)

## Vlastnosti:

### Podpora pre hlasové výstupy:

* Správne oznamovanie položiek v menu a dialógov;
* Pridaná podpora pre prirodzené čítanie zápisu;
* Pridaná možnosť čítania po znakoch, slovách, riadkoch a tiež plynulé
  čítanie;
* Pridané oznamovanie výberu a zmeny výberu bloku (CTRL+B a SHIFT+CTRL+B);
* Pridané oznamovanie pri pohybe kurzorom príkazmi Windows a Lambda;
* Podporované všetky režimi reči (nastavíte v menu nástroje);
* Pridané správne interpretovanie dialógov (kalkulačka, Matrix, štruktúra);
* Pridané správne oznamovanie symbolov pri zapnutom oznamovaní napísaných
  znakov;

### Podpora pre braillovské riadky:

* Doplnok nainštaluje a aktivuje braillovskú tabuľku. Pre rôzne jazyky je
  možné použiť rôzne tabuľky. Tabuľky boli vyrobené z tabuliek pre JAWS
  (súbory jbt);
* Doplnok vytvorí samostatný profil, v ktorom nastaví braillovskú
  tabuľku. Takto sa zaistí, že tabuľka sa načíta len pri aktívnom okne
  LAMBDA;
* Pridané správne oznamovanie dialógov a menu na braillovskom riadku;
* Obsah editačných polí sa správne zobrazuje na riadku a na posúvanie je
  možné použiť tlačidlá braillovského riadka;
* Od verzie 1.1.0 je možné zobrazovať výstup na braillovskom riadku dvoma
  spôsobmi. Ak je aktívna funkcia "použiť display model", na zobrazenie sa
  použije tzv. display model. Toto je užitočné, ak potrebujete presne
  sledovať kurzor na obrazovke, vrátane bielych znakov. Ak vypnete použitie
  display modelu, NVDA bude používať Windows api. Zobrazenie bude
  stabilnejšie, ale nedokáže správne interpretovať biele znaky. Preto kurzor
  nesleduje zobrazenie v prípade, že prechádzate cez biele znaky.

Predvolene je aktívny tzv. display model. Môžete ho vypnúť skratkou
nvda+shift+f.

Odporúčame ho vypnúť, ak používate vlastné rozlíšenie obrazovky.

* Zjednodušená štruktúra dialógov a odstránené nadbytočné opakovanie;
* Pridané správne oznamovanie vybratých blokov bodmi 7 a 8 a správne sa
  aktualizujú vybraté bloky pri zmene pomocou skratiek ctrl+b a
  ctrl+shift+b.

## Prvé spustenie.

Doplnok pri prvom spustení vytvorí profil "lambda" pre aplikáciu
"lambda.exe". V profile je nastavená výstupná braillovská tabuľka, zviazanie
braillovského kurzora s prezeracím kurzorom a aktivovanie display modelu.

Ak takýto profil existuje, doplnok ho neupraví a je potrebné upraviť
nastavenia ručne.

Situáciu môžete vyriešiť použitím sprievodcu nastavením profilu. Sprievodcu
vyvoláte skratkou nvda+alt+r z okna LAMBDA.

Riešením je tiež odstránenie profilu LAMBDA. Otvorte menu NVDA a aktivujte
položku konfiguračné profily.

Tu odstráňte profil LAMBDA. Profil sa automaticky nanovo vytvorí pri
nasledujúcom spustení LAMBDA editora.

Zmazanie profilu môže pomôcť aj vtedy, ak sa doplnok správa
neštandardne. Napríklad ak sa nenastaví správna tabuľka.

Pri každom spustení LAMBDA editora doplnok overí, či existuje profil. Ak
nie, vytvorí ho a nastaví tieto parametre:

```
filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Vysvetlenie:

* path-to-the-addon-brailleTable-dir : je absolútna cesta doplnku +
  "\brailleTables"
* Názov tabuľky: V súčasnosti sú v doplnku tabuľky pre Taliančinu
  lambda-ita.utb a Španielčinu lambda-esp.utb.

## Klávesové skratky:

* **NVDA+Shift+f**: Zapína a vypína použitie display modelu;
* **NVDA+alt+r**: Otvorí sprievodcu nastavením konfiguračného profilu;
* **NVDA+d**: skopíruje vybratý riadok (odporúčame použiť namiesto
  predvolenej skratky LAMBDA ctrl+d).

## Známe problémy:

Pre chybu v LAMBDA editore NVDA nesprávne oznamuje medzery v týchto
situáciách:

* Ak vložíte slová ako "space" alebo "Espacio", NVDA ich bude čítať v
  nastavenom jazyku NVDA.
* Rozhranie reči LAMBDA neoznamuje správne prázdne riadky. Namiesto toho
  oznamuje slovo "medzera". Toto môže zahŕňať prázdny riadok, ale aj riadok
  so slovom "medzera".

## Tipy

Toto sú odporúčania pre lepšie použitie doplnku.

* Ak chcete v LAMBDE oznamovať napísané znaky pri písaní, otvorte okno
  editora. Následne aktivujte čítanie napísaných znakov skratkou nvda+2
  (alebo z nastavení NVDA > klávesnica). V LAMBDE v menu nástroje aktivujte
  funkciu echo. Takto zaistíte oznamovanie napísaných znakov v LAMBDE a
  súčasne to neovplyvní nastavenie pre iné aplikácie.

## mailing list:

Ak chcete nahlásiť chyby, alebo máte nápady na vylepšenia, môžete sa
prihlásiť do nášho mailinglistu (anglicky). Stránka na prihlásenie je
<https://groups.io/g/lambda-nvda>.

## Zmeny

Nasleduje zoznam zmien. V zátvorkách uvádzame aj stav vývoja. Aktuálna
vývojová verzia nie je označená, keďže môže byť zahodená.

### Verzia 1.3.0 (stabilná)

* Pridaná podpora pre nové verzie NVDA (podpora pre Python 3)
* Skratka NVDA+D viac po stlačení na prázdnom riadku neprilepí obsah
  schránky. Vytvorí nový prázdny riadok.

### Verzia 1.2.2 (stabilná)

* Upravené pre WX Python version 4 (predstavené v NVDA 2018.3). Do logu sa
  viac nezapisujú upozornenia wx.NewId().
* Upravené zobrazenie dialógov.
* Nové a aktualizované preklady.

### Version 1.2.1a (stabilná)

Toto je stabilná verzia a neplánujeme vydať novú verziu do júna 2018, aby
sme zaistili funkčnosť pre študentov do konca semestra.

* Nové a aktualizované preklady.

### Verzia 1.2.1 (stabilná)

* Pridaná podpora pre braillovský výstup predstavený v NVDA 2017.3. Funguje
  aj na starších verziách NVDA.
* Opravené problémy so zobrazením na braillovských riadkoch.

### Verzia 1.2.0 (vývojová)

Nebola vydaná ako stabilná, lebo verzia 1.2.1 obsahovala výrazné úpravy.

* Nové a aktualizované preklady.

### Verzia 1.1.8 (stabilná)

* Prvé stabilné vydanie.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=lambda

[2]: https://addons.nvda-project.org/files/get.php?file=lambda-dev
