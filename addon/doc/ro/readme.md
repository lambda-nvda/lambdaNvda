# Suplimentul Lambda pentru NVDA #

* Autor: Alberto Zanella și echipa lambda-nvda.
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltarre][2]

Acest proiect este un modul de aplicație pentru programul LAMBDA. A fost inspirat de munca lui Peter Lecky la universitatea Comenius. 
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) este un soft care ajută persoanele nevăzătoare să citească și să scrie matematică utilizând un afișaj braille și/sau o sinteză vocală.
LAMBDA este rezultatul unui proiect european. Pentru mai multe informații despre el vă rugăm să vizitați [http://www.lambdaproject.org/](http://www.lambdaproject.org/).  
Versiunea actuală a suplimentului are tabele braille pentru limbile italiană
și spaniolă, iar interfața sa este disponibilă în majoritatea limbilor
oficiale ale NVDA-ului, deoarece este tradusă de comunitatea de traduceri a
acestuia.  Dacă nu sunteți un utilizator italian al LAMBDA-ului și doriți să
contribuiți cu portarea tabelului braille în limba dumneavoastră, contactați
autorul (îl vedeți mai jos) sau abonați-vă la lista de mailing a
proiectului.

Vă rugăm să rețineți:** Acest supliment a fost dezvoltat de Alberto Zanella ca o activitate de voluntariat. Nici autorul sau colaboratorii nu sunt implicați în vânzarea și / sau dezvoltarea programului Lambda. Dacă aveți nevoie de mai multe informații despre Lambda, sau aveți nevoie de sprijin în utilizarea lui, vă rugăm să contactați distribuitorul dumneavoastră local. Dacă întâmpinați vreo problemă la utilizarea sau instalarea acestui supliment, vă rugăm să contactați autorul sau utilizați link-ul „Issues” pe pagina proiectului de pe Github.

### [Depozitul oficial de Github](https://github.com/lambda-nvda/lambdaNvda/)

## Caracteristicile suplimentului:

### Suport pentru vorbire:

* Dialogurile și meniurile sunt anunțate corespunzător;
* Suport în vorbirea naturală pentru formulele matematice care utilizează
  motorul matematic Lambda, adică "rădăcină compusă rădăcină 3 rădăcină
  combinată 3 x plus 24, rădăcină apropiată a compusului, minus 3 este egală
  cu 0";
* este implementată citirea prin caractere, cuvinte, rânduri și Spune tot;
* Vorbește când un bloc de text este selectat sau extins;
* Vorbește la deplasarea în editorul de text folosind comenzile Windows-ului
  sau comenzile specifice ale Lambda-ului;
* Atât modul extins de vorbire cât și cel scurt sunt suportate (îl puteți
  selecta folosind meniul de unelte în Lambda);
* Dialoguri speciale precum modul de structurare, calculator și fereastra
  matrix sunt anunțate corect, iar NVDA-ul citește corect la deplasarea
  cursorului în jur sau când un nou text este scris ;
* Tastarea ecoului utilizează procesorul de text Lambda, așa că simbolurile
  și marcajele vor fi corect raportate.

### Suport braille:

* Suplimentul se instalează (în directorul profilului de utilizator) și
  activează un tabel braille personalizat. Acest tabel poate fi diferit
  pentru diferite limbi. Tabelele personalizate braille au fost create din
  cele din pluginul Lambda pentru JAWS (fișier jbt). Apoi, simbolurile și
  marcajele sunt reprezentate folosind aceleași modele de puncte;
* Suplimentul crează un profil NVDA pentru o configurație standard
  braille. Prin aceasta, ieșirea este setată la tabelul personalizat braille
  numai atunci când aplicația Lambda este activă;
* Dialogurile și meniurile sunt raportate corespunzător în braille;
* Conținutul editorului este redat corect în braille, iar utilizatorul poate
  să se deplaseze folosind tastele de deplasare braille sau tastele de
  rotire a cursorului;
* Începând cu versiunea 1.1.0, există două modalități prin care textul din
  editorul Lambda este redat: modul „Flat” și Modul „Non-flat”. Atunci când
  modul ”Flat” este activat, NVDA va folosi Modelul de afișare pentru a
  prelua informații de la editor și pentru a determina poziția
  îngustă. Acest lucru este deosebit de benefic când utilizatorul trebuie să
  se deplaseze pe ecran, chiar și în spații albe. Atunci când modul „Flat”
  este setat pe "off", redarea textului pe afișajul braille este mai
  stabilă, deoarece NVDA folosește Windows API pentru a o prelua. Cu toate
  acestea, atunci când carul este mutat în spații albe de lângă sfârșitul
  liniei de text, afișajul braille nu urmează cursorul real atâta timp cât
  un utilizator nu adaugă un spațiu alb.

În mod implicit, modurile „Flat” și „Non-flat” sunt activate. Puteți activa
sau dezactiva modul „Flat” apăsând NVDA+SHIFT+F.

Vă recomandăm cu insistență să dezactivați modul „Flat”, dacă utilizați
DPI-ul personalizat în Windows (opțiunea Personalizare Dimensiune), mai ales
când aveți setări de ecran cu o rezoluție mai mare de 96 dpi (mai mare de
100%).

* Structura casetelor de dialog este mai ușoară, informația repetată a fost
  eliminată;
* Selectarea va fi marcată corect cu ajutorul punctelor 7 și 8, iar marcajul
  este corect reîmprospătat în timp ce sunt apăsate comenzile standard ale
  Windows-ului (SHIFT + săgeți) sau cele specifice ale Lambda-ului (CTRL+B,
  CTRL+SHIFT+B).

## Înainte de a începe să utilizați acest supliment.

El crează un profil NVDA numit „lambda” care este asociat cu aplicația
„lambda.exe”. Profilul setează automat toate opțiunile braille: tabelul
braille personalizat, legarea focalizării și setările modului Flat.

Dacă în sistemul dumneavoastră există un profil anterior cu același nume,
suplimentul nu îl va înlocui, iar dumneavoastră va trebui să ajustați manual
profilul de configurare.

Pentru a evita această situație, dacă aveți setări specifice pe care doriți
să le păstrați, puteți utiliza expertul de restabilire al profilului
LAMBDA. Comanda rapidă pentru pornirea acestui instrument este NVDA+alt+r
(când sunteți focalizat pe LAMBDA).

Ar mai fi o variantă, să ștergeți versiunile vechi ale profilului „lambda”
după instalarea suplimentului. Pentru a face astfel, deschideți meniul NVDA,
selectați opțiunea „Configurarea profilurilor” și apăsați Enter.

În dialogul de configurare al profilurilor, veți putea să localizați și să
ștergeți profilul „lambda”. Profilul va fi recreat data viitoare când
aplicația Lambda este pornită.

Ștergerea profilului "lambda" ar trebui să fie o soluție ușoară, de
asemenea, în cazul în care suplimentul se confruntă cu vreo problemă. De
exemplu, dacă tabelul braille nu este setat corect, în loc să configurați
manual profilul, puteți să îl ștergeți pur și simplu. Adăugarea va crea unul
nou data viitoare când veți încărca editorul Lambda.

De fiecare dată când editorul Lambda este pornit, acest supliment verifică
dacă există un profil cu numele „lambda”. Dacă nu există un astfel de
profil, el generează automat un profil cu următoarea formă:

``` filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = calea către dosarul suplimentului brailleTable\nume tabel

[lambda]
	brailleFlatMode = True

```

Unde :

* calea către dosarul suplimentului brailleTable : este calea absolută a
  dosarului suplimentului + "\brailleTables"
* nume tabel : depinde de limba activă a NVDA-ului. Momentan, doar tabelele
  braille italian și spaniol, "lambda-ita.utb" și "lambda-esp.utb" sunt
  prezente.

## Comenzile rapide ale suplimentului:

* **NVDA+Shift+f**: Activează sau dezactivează modul flat braille;
* **NVDA+alt+r**: Deschide expertul de recuperare a profilului LAMBDA.
* **NVDA+D: Duplică liniile (utilizați asta în loc de control+d).

## Probleme cunoscute:

Datorită unei erori prezente în LAMBDA, suplimentul oferă un extra-logic
care raportează spațiile albe. Acest logic poate eșua în următoarele
situații:

* Când cuvintele ca „space”, „spazio”, „espacio” etc. sunt inserate în text,
  pot fi raportate de NVDA ca o traducere în limba în care acesta este
  setat.
* Liniile goale nu sunt raportate de motorul de vorbire LAMBDA. Utilizatorul
  va auzi în schimb traducerea cuvântului „space”. Aceasta poate fi atât o
  linie goală, cât și una care conține doar cuvântul „space”.

## Sfaturi utile

Acesta este un set de sfaturi care vă vor ajuta să utilizați suplimentul
într-un mod mai eficient.

* Raportarea caracter cu caracter: Atunci când vă folosiți de matematică în
  viața de zi cu zi, v-ați dori ca NVDA-ul să raporteze ceea ce scrieți
  caracter cu caracter. Pentru a face asta, există câțiva pași simpli:
  asigurați-vă că aveți focalizarea pe fereastra LAMBDA sau pe una dintre
  variantele sale (reprezentarea cu șase puncte, de exemplu); apăsați NVDA+2
  (numărul doi) sau navigați la meniul NVDA>Preferințe>Setări tastatură și
  bifați caseta „Pronunță caracterele tastate”; mergeți la
  Lambda>Opțiuni>Parametri voce și asigurați-vă că caseta de bifat „ecou”
  este bifată, în caz contrar NVDA nu va primi nimic de la motorul de
  vorbire în timp ce tastați. Și gata, NVDA va pronunța caracterele scrise,
  dar nu vă faceți griji, doar în LAMBDA și în ferestrele sale speciale,
  setările pentru restul aplicațiilor vor rămâne așa cum erau.

## Lista de mailing a suplimentului:

To report bugs, suggestions or if you want to contribute you can subscribe
the Addon Group (in English).  You can subscribe from the website:
<https://groups.io/g/lambda-nvda>.

## Change log

Below is a list of changes between the different add-on versions. Next to
the version number, between parentheses, is the development status. The
current development release isn't included as it could have changes until it
is flagged as stable or discarded as candidate.

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

[1]: http://addons.nvda-project.org/files/get.php?file=lambda

[2]: http://addons.nvda-project.org/files/get.php?file=lambda-dev
