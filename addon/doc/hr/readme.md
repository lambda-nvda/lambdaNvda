# Lambda dodatak za NVDA #

* Autor: Alberto Zanella i lambda-nvda tim.
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]

Ovaj projekt je aplikacijski modul za Lambda Softver. Inspiriran je radom Petera Leckya sa sveučilišta Comenius. 
Lambda (Linearni pristup matematici za brajeve uređaje i zvučno sintetiziranje glasa) je softver koji pomaže slijepim osobama čitati i pisati matematiku pomoću brajevog retka i ili govorne jedinice.
LAMBDA je rezultat jednog EU-Projekta. Za više informacija posjetite [https://www.lambdaproject.org/](https://www.lambdaproject.org/).  
Trenutačna verzija dodatka sadrži brajeve tablice za talijanski i španjolski
jezik, a sučelje je dostupno na većini službenih jezika NVDA čitača, jer ga
prevodi NVDA zajednica prevoditelja. Ako niste talijanski korisnik i želite
pridonijeti prijenosu brajeve tablice na vaš jezik, slobodno se obratite
autoru (vidi dolje) ili se prijavite na mailing listu projekta.

**Napomena:** Alberto Zanella je razvio ovaj dodatak za vrijeme dobrovoljnog rada. Niti autor niti suradnici nisu uključeni u prodaju ili razvoj softvera Lambda. Ako trebate više informacija o Lambda ili ako trebate pomoć, obratite se lokalnom distributeru. Ako naiđete na poteškoće prilikom korištenja ili instaliranja ovog dodatka, kontaktirajte autora ili upotrijebite poveznicu „Issues” (problemi) na Github stranici projekta.

### [Službeni Github repozitorij](https://github.com/lambda-nvda/lambdaNvda/)

## Funkcije dodatka:

### Podrška za govor:

* Ispravno izvještavanje o dijaloškim okvirima i izbornicima;
* Podrška za prirodni izgovor matematičkih formula korištenjem Lambda
  matematičke govorne jedinice, npr. „korijen iz 3 kroz korijen iz 3 x plus
  24, zatvori korijen, minus 3 jednako 0”;
* Implementirano je čitanje po znakovima, po riječima, po redcima i Izgovori
  sve;
* Govori kad je blok teksta odabran ili proširen (koristeći KONTROL+B i
  ŠIFT+KONTROL+B);
* Govori tijekom kretanja u uređivaču teksta, korišteći standardne Windows
  naredbe i Lambda-specifične naredbe;
* Podrška za dugi i kratki modus govora (moguće ih je odabrati korištenjem
  izbornika Alati u Lambda);
* Sada se ispravno izvještava o posebnim dijaloškim okvirima poput modus
  strukture, kalkulatora i matričnog prozora i NVDA ih ispravno čita tijekom
  pomicanja kursora ili tipkanja novog teksta;
* Povratni zvuk pri tipkanju koristi Lambdin procesor za tekst, tako da će
  se o simbolima i oznakama ispravno izvještavati.

### Podrška za brajicu:

* Dodatak instalira (unutar mape korisničkog profila) i aktivira prilagođenu
  brajevu tablicu. Ta tablica se može razlikovati za razne
  jezike. Prilagođene brajeve tablice su izrađene od onih u Lambda dodatku
  za JAWS (jbt datoteka). Nakon toga se simboli i oznake prikazuju istim
  točkicama;
* Dodatak izrađuje NVDA profil za standardnu brajevu konfiguraciju. Time se
  izlaz postavlja na prilagođenu brajevu tablicu samo kad je aplikacija
  Lambda aktivna;
* O dijaloškim okvirima i izbornicima se ispravno izvještava na brajevom
  retku;
* Sadržaj se ispravno iscrtava na brajevom retku i korisnik se može kretati
  pomoću brajevih tipki za navigaciju ili tipki za pomicanje kursora;
* Verzijom 1.1.0 ovog dodatka se u Lambda uređivaču uvodi iscrtavanje teksta
  na dva načina: „Flat modus” i „ne-Flat modus”. Kad je „Flat modus”
  uključen, NVDA će koristiti model brajevog retka za dohvaćanje podataka iz
  uređivača i za određivanje položaja kursora. To je posebno korisno kad se
  korisnik mora kretati po ekranu, čak i u praznim područjima. Kad je „Flat
  modus” postavljen na „isključeno”, iscrtavanje teksta na brajevom retku je
  stabilnije, budući da NVDA koristi Windows API za njegovo
  preuzimanje. Međutim, kad se kursor pomiče u prazna područja pored kraja
  retka teksta, brajev redak ne slijedi stvarni pokazivač sve dok korisnik
  nešto ne doda.

Flat modus je standardno aktivan. Moguće ga je uključiti ili isključiti
tipkama NVDA+ŠIFT+F.

Svakako preporučamo deaktivirati Flat modus, ako koristite prilagođene DPI
vrijednosti u Windowsima (opcija za prilagođene veličine), posebno kad se u
postavkama ekrana, DPI vrijednosti postave na više od 96 dpi (veće od 100%).

* Struktura dijaloških okvira je jednostavnija, uklonjene su informacije
  koje su se ponavljale;
* Odabir će biti ispravno prikazan točkicama 7 i 8, a označavanje se
  ispravno učitava pritiskanjem standardnih Windows naredbi (ŠIFT+STRELICE)
  ili određenih Lambda naredbi (KONTROL+B, KONTROL+B).

## Prije upotrebe ovog dodatka.

Ovaj dodatak stvara profil pod nazivom „lambda” koji je povezan s datotekom
„lambda.exe”. Dodatak automatski postavlja sve mogućnosti brajice:
prilagođenu brajevu tablicu, povezivanje s fokusom i postavke za flat modus.

Ako je profil s istim imenom prisutan u vašem sustavu, dodatak ga neće
zamijeniti i morat ćete ručno prilagoditi konfiguracijski profil.

Da biste izbjegli ovu situaciju, ako imate određene postavke koje želite
sačuvati, možete upotrijebiti čarobnjaka za vraćanje LAMBDA profila. Prečac
za pokretanje ovog alata je nvda+alt+r (kad je fokus u aplikaciji LAMBDA).

Također postoji jednostavna opcija za brisanje starih „lambda” profila nakon
instaliranja dodatka. Da biste to učinili, otvorite NVDA izbornik, odaberite
izbornik Konfiguracijski profili i pritisnite ENTER.

U dijaloškom okviru Konfiguracijski profili možete pronaći i obrisati
„lambda” profil. Profil će ponovo biti stvoren tijekom sljedećeg pokretanja
Lambda aplikacije.

Brisanje „lambda” profila također bi trebalo biti jednostavno rješenje, ako
dođe do problema u radu dodatka. Na primjer, ako brajeva tablica nije
ispravno postavljena, umjesto ručnog konfiguriranja profila, možete ga
jednostavno izbrisati. Dodatak će stvoriti novi profil tijekom sljedećeg
pokretanja Lambda uređivača.

Svaki put kad pokrenete Lambda uređivač, ovaj dodatak provjerava, postoji li
profil s nazivom „lambda”. Ako ne postoji, automatski izrađuje profil u
obliku:

```
filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Gdje :

* staza-do-mape-brajeveTablice-dodatka : je absolutna staza mape dodataka +
  „\brajeveTablice”
* imeTablice: ovisi o aktivnom jeziku NVDA čitača. Trenutačno postoje samo
  talijanske i španjolske brajeve tablice „lambda-ita.utb” i
  „lambda-esp.utb”.

## Tipkovnički prečaci za dodatak:

* **NVDA+šift+f**: Uključi ili isključi modus brajevog retka;
* **NVDA+alt+r**: Otvori čarobnjaka za vraćanje LAMBDA profila;
* **NVDA+d**: Dupliciraj retke (koristite ovo umjesto kontrol+d).

## Poznati problemi:

Zbog greške koja je prisutna u aplikaciji LAMBDA, dodatak pruža dodatnu
logiku koja izvještava o bjelinama (razmacima). Ova logika možda neće
uspjeti u sljedećim situacijama:

* Kad se riječi poput „razmak”, „spazio”, „Espacio” itd. umetnu u tekst,
  NVDA će o njima možda izvijestiti lokalnim NVDA prijevodom.
* LAMBDA govorna jedinica ne izvještava o praznim redcima. Korisnik će
  umjesto toga čuti prijevod za riječ „razmak”. To može biti prazni redak
  ili redak koji sadrži riječ „razmak”.

## Korisni savjeti

Ovo je niz savjeta koji će vam pomoći koristiti dodatak na učinkovitiji
način.

* Izvještavanje o znakovima pojedinačno: Uobičajeno, kad radite s programima
  za matematiku, NVDA bi trebao izvještavati o stvarima koje pišete znak po
  znak. Da biste to učinili, postoji nekoliko jednostavnih koraka: budite
  sigurni da ste u prozoru programa LAMBDA. Primjerice, pritisnite NVDA+2
  (broj dva) ili prijeđite na izbornik NVDA>Postavke>Postavke tipkovnice i
  označite okvir za govor utipkanih znakova; idite na LAMBDA>Opcije>Glasovni
  parametri i provjerite je li potvrdni okvir „odjek” UKLJUČEN, u protivnom
  NVDA neće ništa primiti od govorne jedinice dok tipkate. I gotovo! NVDA će
  govoriti upisane znakove, ali samo u LAMBDA aplikaciji ili u njenim
  posebnim prozorima. Postavke za ostale aplikacije se neće mijenjati.

## Mailing lista dodatka:

Da biste prijavili greške, iznijeli prijedloge ili ako želite doprinijeti,
možete se pretplatiti na grupu vezanu za ovaj dodatak (na engleskom
jeziku). Možete se pretplatiti s web stranice:
<https://groups.io/g/lambda-nvda>.

## Popis promjena

U nastavku se nalazi popis promjena između različitih verzija dodatka. Pored
broja verzije se u zagradama nalaze informacije o stanju razvoja. Trenutačno
razvojno izdanje nije uključeno. Ono bi moglo sadržati promjene sve dok se
ne označi kao stabilno izdanje ili dok se ne odbaci kao kandidat.

### Verzija 1.3.0 (stabilna)

* Podrška za noviju NVDA verziju (podrška za Python 3).
* Riješen je problem, pri kojem je pritiskanje tipki NVDA+d u praznom retku
  prouzročilo umetanje sadržaja međuspremnika. Kad sada pritisnete NVDA+d i
  nalazite se u praznom retku, pojavljuje se novi prazan redak kao što se i
  očekuje.

### Verzija 1.2.2 (stabilna)

* Poboljšana je kompatibilnost s WX Python verzija 4 (uveden u NVDA
  2018.3). Upozorenje vezano za wx.NewId() se više ne prikazuje u dnevniku
  ispravljanja grešaka.
* Implementiran je guiHelper za poboljšavanje prikaza dijaloških okvira.
* Novi jezici. Ažurirani prijevodi.

### Verzija 1.2.1a (stabilna)

Ova nadogradnja je namijenjena je za dugoročnu podršku. To znači, da se
barem do lipnja 2018. neće objavlti nova stabilna verzija. Želimo studentima
pružiti maksimalnu stabilnost i minimalne promjene tijekom akademske godine.

* Novi jezici. Ažurirani prijevodi.

### Verzija 1.2.1 (stabilna)

* Dodana je kompatibilnost s načinom na koji NVDA 2017.3 upravlja
  brajicom. Zadržana je kompatibilnost sa starijim verzijama.
* Ispravljene mnoge greške s brajicom.

### Verzija 1.2.0 (razvojna)

Ova verzija nije objavljena kao stabilna zbog toga što verzija 1.2.1
uključuje značajnije ispravke.

* Novi jezici. Ažurirani jezici.

### Verzija 1.1.8 (stabilna)

* Inicijalno stabilno izdanje.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=lambda

[2]: https://addons.nvda-project.org/files/get.php?file=lambda-dev
