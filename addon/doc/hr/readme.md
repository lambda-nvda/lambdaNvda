# Lambda Add-On for NVDA #

* Autor: Alberto Zanella i lambda-nvda tim.
* Preuzmi [stable version][1]
* Preuzmi [development version][2]

Ovaj projekt je appModul za Lambda Softver. Inspiriran je radom Petera Leckya sa sveučilišta Comenius. 
Lambda (Linearni Pristup Matematici za Brajeve Zaslone i Zvučne sinteze) je softver koji pomaže slijepim osobama da čitaju i pišu matematiku koristeći brajev zaslon i/ili govornu sintezu.\LAMBDA je rezultat EU-Projekta. Za više informacija posjetite [https://www.lambdaproject.org/](https://www.lambdaproject.org/).  
Trenutačna inačica dodatka sadrži brajeve tablice za talijanski i španjolski
jezik, a sučelje je dostupno na većini službenih jezika NVDA jer ga prevodi
zajednica prevoditelja NVDA. Ako ste ne talijanski korisnik LAMBDA i želite
pridonijeti prijenosu brajeve tablice na vaš jezik, slobodno se obratite
autoru (vidi dolje) ili se prijavite na mailing listu projekta.

Napomena: Ovaj je dodatak dobrovoljno razvio Alberto Zanella. Niti autor niti suradnici nisu uključeni u prodaju i / ili razvoj softvera Lambda. Ako trebate više informacija o Lambda ili vam je potrebna podrška o korištenju, obratite se lokalnom distributeru. Ako naiđete na poteškoće prilikom korištenja ili instaliranja ovog dodatka, kontaktirajte autora ili upotrijebite vezu \ "Problemi " na Github stranici projekta.

### Službeni repozitorij na Githubu[(https://github.com/lambda-nvda/lambdaNvda/)

## Značajke dodatka:

### Govorna podrška:

* Dijaloški okviri i izbornici se ispravno prikazuju;
* Podrška za prirodni izgovor matematičkih formula; 
* Implementirano čitanje znak po znak, riječi, linija i Reci Sve; 
* Govori kada je blok teksta označen ili proširen (koristeći CTRl+B i
  SHIFT+CTRL+B);
* Govori dok se krećete u programu za uređivanje teksta korištenjem
  standardnih Windowsovih naredbi i Lambda-specifičnih naredbi; 
* Podržan je dulji i kraći način izgovora (možete ih odabrati korištenjem
  izbornika Alati u Lambda);
* Posebni dijaloški okviri poput strukturnog načina, kalkulatora i matričnog
  prozora sada se ispravno prikazuju i NVDA ispravno čita dok pomičete
  kursor uokolo ili dok tipkate novi tekst ;
* Povratni zvuk tipkanja koristi Lambda tekstualni procesor, tako da će se
  simboli i oznake ispravno prikazivati.

### Podrška za brajicu:

* Dodatak instalira (unutar mape korisničkog profila) i aktivira prilagođenu
  brajevu tablicu. Ta tablica može biti različita za različite
  jezike. Prilagođene brajeve tablice napravljene su od onih u Lambda
  dodatku za JAWS (jbt datoteka). Tako se simboli i oznake prikazuju istim
  točkicama.
* Dodatak kreira NVDA profil za standardnu brajevu konfiguraciju. Time se
  izlaz postavlja na prilagođenu brajevu tablicu samo kada je aplikacija
  Lambda aktivna..
* Dijaloški okviri i izbornici su ispravno prikazani na brajici; 
* Sadržaj se ispravno prikazuje na brajici i korisnik je u mogućnosti
  kretati se pomoću brajevih tipki za navigaciju ili tipki za pomicanje
  kursora;
* Starting from the addon version 1.1.0, there are two ways in which the
  text in the Lambda editor is rendered: "Flat mode" and "non-Flat
  Mode". When the "Flat mode" is on, NVDA will use the Display Model to
  retrieve information from the editor and to determine the caret
  position. This is specially beneficial when the user needs to move around
  on the screen, even in white spaces. When the "Flat Mode" is set to "off",
  text rendering on the braille display is more stable, since NVDA uses
  Windows API to retrieve it. However when the the caret is moved in white
  spaces next to the end of the line of text, the braille display does not
  follow the real cursor as long as a non-white space is added by the user.

Flat mod je aktivan prema zadanim postavkama. Možete ga uključivati i
isključivati koristeći naredbu NVDA+SHIFT+F. 

Strogo preporučamo da onemogućite flat mod ako koristite prilagođeni DPI u
Windowsima (opcija prilagođenih dimenzija), posebno kada imate postavke
zaslona sa više od 96 dsi (veće od 100%).

* Struktura dijaloških okvira je jednostavnija, uklonjene su informacije
  koje su se ponavljale. 
* Odabir će biti korektno prikazan točkicama 7 i 8, a označavanje se
  ispravno učitava standardnim Windows naredbama (SHIFT+STRELICE) ili Lambda
  specifičnim naredbama (CTRL+B, CTRL+B) su pritisnute.

## Prije početka korištenja ovog dodatka.

Ovaj dodatak stvara profil pod nazivom "lambda" koji je povezan s datotekom
"lambda.exe". Dodatak automatski postavlja sve mogućnosti brajice:
prilagođenu brajevu tablicu, fokus i način rada.

Ako je profil s istim imenom prisutan u vašem sustavu, dodatak ga neće
zamijeniti i morat ćete ručno prilagoditi konfiguracijski profil.

Da biste izbjegli ovu situaciju, ako imate određene postavke koje želite
sačuvati, možete upotrijebiti LAMBDA Čarobnjak za vraćanje postavki. Prečac
za pokretanje ovog alata je nvda+alt+r dok ste fokusirani u programu LAMBDA.

Također postoji jednostavna opcija za brisanje starih profila "lambda" nakon
instalacije dodatka. Da biste to učinili, otvorite NVDA izbornik, odaberite
izbornik Konfiguracijski profili i pritisnite ENTER. 

U dijaloškom okviru Konfiguracijski profili, moći ćete pronaći i obrisati
"lambda" profil. Profil će ponovno biti stvoren kada sljedeći put pokrenete
Lambda aplikaciju.

Brisanje profila "lambda" također bi trebalo biti jednostavno rješenje ako
postoji bilo koji problem u radu dodatka. Primjerice, ako brajeva tablica
nije ispravno postavljena, umjesto ručnog konfiguriranja profila jednostavno
je možete izbrisati. Dodatak će krirati novi profil kada drugi put pokrenete
Lambda urednik.

Svaki put kada pokrenete Lambda uređivač, ovaj dodatak provjerava postoji li
profil s nazivom "lambda". Ako ne postoji, automatski generira profil sa
sljedećim obrascem:

``` filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Gdje : 

* path-to-the-addon-brailleTable-dir : is the absolute path of the addon
  directory + "\brailleTables"
* Ime tablice: ovisi o aktivnom jeziku NVDA. Trenutno se prikazuju samo
  talijanske i španjolske brajeve tablice, lambda-ita.utb" i
  "lambda-esp.utb"

## Tipkovničke kratice za dodatak: 

* NVDA+Shift+f**: Uključi i isključi način brajice;
* NVDA+alt+r: Otvori čarobnjak za vraćanje LAMBDA profila; 
* NVDA+d: Dupliciraj linije (koristite ovo umjesto control+d).

## Poznate greške:

Zbog greške prisutne u LAMBDA-i, dodatak pruža dodatnu logiku koja
izvještava o bijelim prostorima. Ova logika možda neće uspjeti u sljedećim
situacijama:

* Kada su riječi poput "razmak", "spazio" "Espacio" umetnute u tekst, NVDA
  ih može prikazati kao lokalni NVDA prijevod.
* Prazne linije nisu prijavljene od strane LAMBDA govornog robota. Korisnik
  će umjesto toga čuti prijevod riječi razmak. To može biti i prazna linija
  ili linija koja sadrži riječ "razmak".

## Korisni trikovi 

Ovo je niz savjeta koji će vam pomoći u korištenju dodatka na učinkovitiji
način.

* Izgovaranje znak po znak: Uobičajeno, kada radite s programima za
  matematiku, NVDA bi trebao izgovarati stvari koje pišete znak po znak. Da
  biste to učinili, postoji nekoliko jednostavnih koraka: budite sigurni da
  ste u prozoru programa LAMBDA. Primjerice, pritisnite NVDA + 2 (broj dva)
  ili prijeđite na izbornik NVDA> Postavke> Postavke tipkovnice i označite
  okvir za izgovor znakova; idite na LAMBDA> Opcije> Glasovni parametri i
  provjerite je li potvrdni okvir "odjek" UKLJUČEN, u protivnom NVDA neće
  ništa primiti od govornog robota dok upisujete. Gotovo, NVDA će govoriti
  upisane znakove, ali ne brinite, samo u LAMBDA-u ili u posebnim prozorima,
  postavke za ostale aplikacije bit će netaknute.

## Mailing lista dodatka:

Da biste prijavili greške, iznijeli prijedloge ili ako želite doprinijeti,
možete se pretplatiti na grupu vezanu za ovaj dodatak (na engleskom
jeziku). Možete se pretplatiti sa web stranice:
<https://groups.io/g/lambda-nvda>.

## Popis izmjena

U nastavku je popis izmjena između različitih inačica dodatka. Pored broja
inačice, između zagrada, nalaze se informacije o statusu razvoja. Trenutno
razvojno izdanje nije uključeno jer može imati izmjene dok se ne označi kao
stabilno ili izbaci kao kandidat.

### Version 1.2.2 (stable)

* Improved compatibility with WX Python version 4 (introduced with NVDA
  2018.3). Warning related with wx.NewId() is no longer displayed in debug
  log.
* Implemented guiHelper to enhance dialogs's appearance.
* Novi jezici. Ažurirani prijevodi.

### Inačica 1.2.1a (stabilna) 

Ovo ažuriranje namijenjeno je za dugoročnu podršku. To znači da barem do
lipnja 2018. neće biti objavljena nova stabilna inačica. Želimo studentima
pružiti maksimalnu stabilnost i minimizirati promjene tijekom akademske
godine.

* Novi jezici. Ažurirani prijevodi.

### Inačica 1.2.1 (stabilna)

* Dodana je kompatibilnost s načinom na koji NVDA 2017.3 upravlja
  brajicom. Zadržana je kompatibilnost sa starijim inačicama.
* Ispravljene mnoge greške u brajici.

### Inačica 1.2.0 (razvojna) 

Ova inačica nije objavljena kao stabilna zbog toga što inačica 1.2.1
uključuje značajnije ispravke.

* Nove lokacije. Ažurirane lokalizacije.

### Inačica 1.1.8 (stabilna)

* Inicijalno stabilno izdanje.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=lambda

[2]: https://addons.nvda-project.org/files/get.php?file=lambda-dev
