# Lambda Add-On for NVDA #

* Author: Alberto Zanella and the lambda-nvda team.
* Preuzmi[stabilnu verziju][1]
* Preuzmi[razvojnu verziju][2]

Ovaj projekat je dodatak za LAMBDA aplikaciju. Inspirisan je radom Peter Lecky u Comenius univerzitetu. 
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) je program koji pomaže slepim osobama u pisanju i čitanju matematičkog sadržaja korišćenjem brajevog reda ili sintetizatora govora.
LAMBDA je rezultat EU-projekta. Za više informacija o aplikaciji LAMBDA posetite[https://www.lambdaproject.org/](https://www.lambdaproject.org/).  
The current version of the addon has braille tables for Italian and Spanish
languages and its interface is available in most of the NVDA's official
languages, because it is translated by the NVDA translations community.  If
you are a non-italian user of LAMBDA and you would like to contribute with
the porting of the braille table in your language, feel free to contact the
author (see below) or subscribe the project mailing list.

**Napomena:** Ovaj dodatak je razvijen od strane autora Alberto Zanella kao volonterska aktivnost. Niti autor niti drugi saradnici imaju veze sa prodajom ili korišćenjem programa Lambda. Ako želite više informacija o programu Lambda, ili vam treba podrška za korišćenje, kontaktirajte vašeg lokalnog distributera. Ako imate poteškoća u korišćenju ili instalaciji ovog dodatka, kontaktirajte autora ili koristite"link za probleme" na Github stranici projekta.

### [Official Github Repository](https://github.com/lambda-nvda/lambdaNvda/)

## Karakteristike dodatka:

### Govorna podrška:

* Dijalozi i meniji se ispravno prijavljuju;
* Prirodna podrška za matematičke formule, tj"compound root 3 sep compound
  root 3 x plus 24, close compound root, minus 3 equals 0";
* Uključeno čitanje po znakovima, rečima i izgovori sve režim;
* Izgovara kada je deo teksta izabran ili proširen(komandama Kontrol+b i
  kontrol+šift+b);
* Izgovara kada uređujete tekst Windows ili Lambda komandama;
* Proširen i kratak režim govora su podržani(možete ih izabrati iz menija
  alati programa Lambda);
* Posebni dijalozi kao što su režim strukture kalkulator i matriks prozor se
  ispravno prijavljuju;
* Izgovor znaka koristi Lambda processor tako da se specijalni znakovi
  ispravno prijavljuju;

### Brajeva podrška:

* Dodatak instalira(u folderu korisničkog profila) i aktivira prilagođenu
  brajevu tabelu. Ova tabela se može razlikovati za različite
  jezike. Prilagođene brajeve tabele su napravljene iz Lambda dodatka za
  Jaws(jbt datoteka). a zatim se specijalni simboli prikazuju koristeći iste
  oblike tačaka;
* Dodatak instalira poseban profil. Zbog toga, prilagođene brajeve tabele su
  aktivne samo kada se koristi Lambda aplikacija;
* Dijalozi i meniji se ispravno prikazuju na brajevom pismu;
* Sadržaj uređivanja se ispravno učitava i možete se kretati po njemu
  korišćenjem tastera za prebacivanje kursora i brajevog reda;
* Od verzije dodatka 1.1.0, postoje dva načina na koji se tekst u uređivaču
  učitava: "Ravan režim" i"Ne-ravan režim". Kada je"ravan režim" uključen,
  NVDA će koristiti model brajevog reda kako bi prepoznao poziciju
  kursora. Ovo je korisno kada korisnik želi da se kreće po ekranu, čak i u
  belom prostoru. Kada je"ravan režim" podešen na"isključen", učitavanje
  teksta na brajevom redu je stabilnije, zbog toga što NVDA koristi Windows
  API da ga učita. Ali kada je kursor na praznom prostoru nakon kraja reda,
  brajev red ne prati kursor sve dok se nešto ne doda od strane korisnika.

"Ravan režim" je aktiviran po podrazumevanim podešavanjima. Možete uključiti
i isključiti"Ravan režim" pritiskanjem NVDA+ŠIFT+F.

Preporučujemo da onemogućite ravan režim ako koristite prilagođena
podešavanja DPI u Windowsu(prilagođena veličina), pogotovo kada je
podešavanje veće od 96 dpi (veće od 100%).

* Struktura dijaloga je lakša jer su informacije koje se ponavljaju
  uklonjene;
* Izbor je ispravno označen tačkama 7 i 8 kada koristite Windows
  komande(Šift i strelice) kao i Lambda komande(Kontrol+b i Kontrol+Šift+b)

## Pre nego što počnete da koristite ovaj dodatak.

Ovaj dodatak pravi NVDA profil sa imenom"lambda" koji je podešen
za"lambda.exe" aplikaciju. Profil automatski podešava brajeva podešavanja:
Prilagođenu brajevu tabelu, vezivanje fokusa i ravan režim.

Ako profil sa istim imenom postoji na sistemu, dodatak ga neće zameniti i
morate urediti vaša podešavanja.

Da sprečite ovu situaciju, ako imate podešavanja koja želite da sačuvate,
možete koristiti"Revert LAMBDA Profile čarobnjak". prečica je NVDA+alt+r
(kada ste u aplikaciji Lambda).

Lakša opcija je takođe da obrišete stare verzije"lambda" profila nakon
instalacije dodatka. Da biste to uradili, otvorite NVDA meni,
izaberite"profili podešavanja" i pritisnite enter.

U ovom dijalogu, moćićete da pronađete i obrišete "lambda" profil. Profil će
ponovo biti napravljen kada se Lambda aplikacija pokrene.

Brisanje"lambda" profila je takođe lako rešenje kada dodatak ima neki
problem. Na primer, ako brajeva tabela nije ispravno podešena, umesto da
ručno podešavate profil, možete ga jednostavno obrisati. Dodatak će
napraviti novi sledeći put kada učitate Lambda editor.

Svaki put kada se Lambda editor pokrene, ovaj dodatak proverava da li profil
sa imenom "lambda" postoji. Ako ne postoji, automatski pravi sledeći profil:

```
filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Gde:

* path-to-the-addon-brailleTable-dir : Je adresa do foldera dodatka+
  "\brailleTables"
* tableName : Zavisi od aktivnog NVDA jezika. Trenutno samo Italijanske i
  Španske tabele, "lambda-ita.utb" i"lambda-esp.utb" postoje.

## Prečice dodatka:

* **NVDA+Šift+f**: Uključi ili isključi ravan brajev mod;
* **NVDA+alt+r**: Open the "Revert LAMBDA Profile Wizard";
* **NVDA+d**: Duplicate lines (use this instad of control+d).

## Known issues:

Due to a bug present in LAMBDA, the add-on provides an extra-logic that
reports white spaces. This logic may fail in the following situations:

* When words like "space", "spazio" "Espacio" etc. are inserted into the
  text, they may be reported by NVDA as the local NVDA language translation.
* Blank lines are not reported by the LAMBDA speech engine. The user will
  hear the translation of the word "space" instead. This could be both a
  blank line or a line containing only the word "space".

## Useful tips

This is a set of tips that will help you on using the addon in a more
eficient way.

* Character-by-character reporting: Normally, when working with maths you
  would like NVDA to report things you're writing character by character. To
  do this, there are a couple of simple steps: ensure to have the focus on
  the LAMBDA's window or one of its variants (the six dots representation,
  for example); press NVDA+2 (number two) or navigate to NVDA
  menu>Preferences>Keyboard settings and check the box to Speak typed
  characters; go to LAMBDA>Options>Voice paramethers and ensure the checkbox
  "echo" is ON, otherwhise NVDA won't receive anything from the speech
  engine while you are typing. And done, NVDA will speak written characters,
  but don't worry, only in LAMBDA or its special windows, the settings for
  the rest of applications will be left as they were.

## Mejling lista dodatka:

To report bugs, suggestions or if you want to contribute you can subscribe
the Addon Group (in English).  You can subscribe from the website:
<https://groups.io/g/lambda-nvda>.

## Change log

Below is a list of changes between the different add-on versions. Next to
the version number, between parentheses, is the development status. The
current development release isn't included as it could have changes until it
is flagged as stable or discarded as candidate.

### Version 1.3.0 (stable)

* Support for newer version of NVDA (Support for Python 3)
* Solved an issue while pressing duplicate line command NVDA+d in a blank
  line caused clipboard content to be pasted. Now when you press NVDA+d and
  you are in a blank line, a new blank line appears as expected.

### Version 1.2.2 (stable)

* Improved compatibility with WX Python version 4 (introduced with NVDA
  2018.3). Warning related with wx.NewId() is no longer displayed in debug
  log.
* Implemented guiHelper to enhance dialogs's appearance.
* New languages. Updated translations.

### Version 1.2.1a (stable)

This update is intended to be a long-term support release. It means that
until, at least, june 2018, it won't be released a version as stable as
this. We do it to provide students maximum stability and to minimize the
changes during the academical year.

* New languages. Updated translations.

### Version 1.2.1 (stable)

* Added compatibility with the way that NVDA 2017.3 uses to manage
  braille. Backwards compatibility kept.
* fixed many braille issues.

### Version 1.2.0 (development)

This version was not published as stable because the version 1.2.1 included
major fixes.

* New locales. Updated localizations.

### Version 1.1.8 (stable)

* Initial stable release.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=lambda

[2]: https://addons.nvda-project.org/files/get.php?file=lambda-dev
