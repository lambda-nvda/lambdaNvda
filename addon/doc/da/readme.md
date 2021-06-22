# Lambda tilføjelsespakke for NVDA #

* Forfatter: Alberto Zanella og Lambda-NVDA team.
* Download [stabil version][1]
* Download [udviklingsversion][2]

Dette projekt er et appModule for LAMBDA-Software. Det er inspireret af arbejdet af Peter Lecky på Comenius University. 
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) er software, der hjælper blinde mennesker med at læse og skrive matematik ved hjælp af et punktdisplay- og eller en talesyntese.
LAMBDA er resultatet af et EU-projekt. For mere information om LAMBDA besøg [https://www.lambdaproject.org/] (https://www.lambdaproject.org/).
Den aktuelle version af tilføjelsespakken har punkttabeller for det
italienske og spanske sprog og dens grænseflade er tilgængelig i de fleste
af NVDAS officielle sprog, fordi den er oversat af Fællesskabets
oversættere.  Hvis du er en ikke-italienske bruger af LAMBDA og du gerne vil
bidrage med portering af punkttabellen på dit sprog, er du velkommen til at
kontakte forfatteren (se nedenfor) eller Tilmeld dig projektets postliste.

** Bemærk venligst: ** Denne tilføjelse er blevet udviklet af Alberto Zanella som frivilligt arbejde. Ejeren eller bidragsyderen er heller ikke involveret i salg- og- eller udvikling af softwaren Lambda. Hvis du har brug for mere information om Lambda, eller du har brug for hjælp til, hvordan du bruger pakken, bedes du kontakte din lokale distributør. Hvis du støder på problemer, når du bruger eller installerer denne tilføjelse, bedes du kontakte forfatteren eller bruge linket "Issues" på Githubs projektside.

### [Officeielt Github Repository](https://github.com/lambda-nvda/lambdaNvda/)

## Funktioner i tilføjelsespakken:

### Understøttelse for tale:

* Dialoger og menuer rapporteres som forventet;
* Naturlig talestøtte til matematiske formler ved hjælp af Lambda Math
  Engine, dvs. "compound root 3 sep compound root 3 x plus 24, close
  compound root, minus 3 equals 0";
* Kan læse hvert tegn, ord, linjer eller sig alt;
* Taler, når en blok af tekst er valgt eller udvidet ved brug af Ctrl+B og
  Ctrl+Skift+B;
* Taler, når du bevæger dig rundt i tekstredigeringen ved brug af
  standard-Windowskommandoer og Lambda-specifikke kommandoer;
* Både detaljerede og kortfattede taletilstande er tilgængelige. Du kan
  vælge dette ved at benytte menuen "Tools" i Lambda.
* Særlige dialoger som struktur tilstand, lommeregner og matrix vindue er nu
  korrekt rapporteret og NVDA læser korrekt når du flytter markøren eller
  når ny tekst skrives.
* Indtastningsekko benytter tekstbehandlingen fundet i Lambda, så symboler
  og mærker vil blive rapporteret korrekt.

### Understøttelse af punkt

* Denne tilføjelsespakke vil blive installeret i mappen user profile, og
  aktivere en tilpasset punkttabel. Denne tabel er muligvis forskellig i
  forhold til andre sprog. Denne tabel er baseret på Lambda plugin for JAWS
  (jbt fil). Derfor er symboler og mærker repræsenteret af samme
  punktmønstre.
* Tilføjelsen opretter en NVDA-profile for en standardkonfiguration af
  punktskrift. Derfor er oversættelsestabellen kun indstillet til den
  tilpassede punkttabel, når Lambda er aktiv.
* Dialoger og menuer er korrekt rapporteret på punkt.
* Indholdet i redigeringsprogrammet er korrekt omsat til punkt. Derudover
  kan brugeren også navigere ved hjælp af panoreringsknapper eller
  markørsammenføringsknapper.
* Fra version 1.1.0 af tilføjelsen, vil det nu være muligt at gengive
  teksten i Lambda-editor på to måder: "Flad tilstand" og "ikke-flad
  tilstand". Når "flad tilstand" er slået til, vil NVDA benytte
  skærmmodellen til at hente information fra editoren samt bestemme
  markørens position. Dette er især nyttigt, når brugeren skal bevæge sig
  rundt på skærmen, selv når der er blanke tegn. Når "Flad tilstand" er
  slået fra, vil tekstgengivelse på punktdisplayet fremkomme mere stabilt,da
  NVDA i dette tilfælde benytter en Windows-API til at hente tilsvarende
  information. Hvis markøren dog flyttes hen på et blankt tegn i slutningen
  af en linje, vil punktdisplayet ikke følge den aktuelle markør, hvis et
  andet tegn end et blankt tegn er skrevet af brugeren.

"Flad tilstand" er som standard aktiv. Du kan slå dette til eller fra ved at
trykke på NVDA+Shift+F.

Vi anbefaler at du deaktivere "Flad tilstand", hvis du anvender
brugerdefineret DPI i Windows (brugerdefinerede
dimensioneringsindstillinger), især når du har skærmindstillinger med mere
end 96 DPI (større end 100%).

* Dialogboksenes struktur er nemmere, gentagne oplysninger er blevet
  fjernet;
* Det valgte vil blive markeret korrekt ved brug af punkt 7 og 8, og korrekt
  opdateret ved brug af Windows-kommandoer Skift-piletaster eller
  Lambda-specifikke kommandoer Ctrl+B og Ctrl+Skift+B.

## Før du bruger denne tilføjelse.

Denne tilføjelse opretter en NVDA-profil ved navn "Lambda". Denne profil er
associeret med filen "Lambda.exe". Profilen indstiller automatisk alle
punktindstillinger. Dette inkludere den tilpassede oversættelsestabel,
hvordan fokus følges og flad tilstand.

Hvis en eksisterende profil med samme navn befinder sig på dit system, skal
du selv erstatte den, da tilføjelsespakken ikke vil gøre dette.

For at undgå dette, skal du benytte "Guiden Gendan LAMBDA-profil", såfremt
du har indstillinger, som du ønsker at gemme. Du kan starte dette værktøj
ved at trykke NVDA+Alt+R, når du befinder dig i LAMBDA.

En nem mulighed er også at slette gamle versioner af lambda-profilen efter
installationen af tilføjelsen. For at gøre det skal du åbne NVDA-menuen,
vælge menupunktet "Indstillingsprofiler..." og trykke på ENTER.

I dialogboksen "Indstillingsprofiler" kan du finde og slette
Lambda-profilen. Profilen genoprettes næste gang Lambda-applikationen er
startet.

Sletning af profilen "lambda" bør også være en nem løsning, når tilføjelsen
løber ind i problemer. For eksempel, hvis punkttabellen ikke er indstillet
korrekt, kan du blot slette den  i stedet for at udføre en manuel
konfiguration af profilen. Tilføjelsen vil oprette en ny profil, næste gang
du indlæser Lambda Editor.

Hver gang Lambda-editoren er startet, kontrollerer denne tilføjelse, om der
findes en profil med navnet "lambda". Hvis det ikke er tilfældet, genererer
det automatisk en profil med følgende formular:

```
filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Hvor:

* path-to-the-addon-brailleTable-dir : er den fulde sti til
  tilføjelsespakkens mappen + "\brailleTables"
* tableName : afhænger af det aktive NVDA-sprog. I øjeblikket findes kun
  italienske og spanske oversættelsestabeller, henholdsvis "lambda-ita.utb"
  og "lambda-esp.utb".

## Tilføjelsens tastaturgenveje:

* **NVDA+Skift+F**: Slå flad tilstand for punkt til og fra;
* **NVDA+alt+r**: Åben værktøjet "Revert Lambda Profile Wizard";
* **NVDA+d**: Dupliker linjer (brug dette i stedet for Ctrl+D).)

## Kendte problemer

På grund af en fejl i LAMBDA giver tilføjelsen en ekstra logik, der
rapporterer blanktegn. Denne logik kan mislykkes i følgende situationer:

* Når ord som "space", "spazio" "Espacio" osv. indsættes i teksten, vil NDA
  muligvis rapportere dette i hendhold til den lokale NVDA-oversættelses der
  benyttes.
* Blanke Linjer er ikke rapporteret af Lambda når tale benyttes. Brugeren
  vil høre en oversættelse af ordet "space" i stedet. Dette kan være både en
  tom linje eller en linje som blot indeholder ordet "space".

## Nyttige råd

Dette er nogle råd, der hjælper dig med at bruge tilføjelsen på en mere
effektiv måde.

* Rapportering med tegn for tegn: Normalt, når du arbejder med matematik,
  vil du gerne NVDA rapportere ting, du skriver tegn for tegn. For at gøre
  dette er der et par enkle trin: Sørg for at have fokus på LAMBDA-vinduet
  eller en af ​​dets varianter (f.eks. Den sekspunktede repræsentation);
  tryk NVDA+2 (nummer to) eller naviger til NVDA-menuen> Indstillinger>
  Tastaturindstillinger og markér boksen der slår den tilsvarende
  indstilling til og fra; gå til LAMBDA>Options> Voice Parameters og sørg
  for, at check boxen "Echo" er markeret, elers vil NVDA ikke modtage talen,
  mens du skriver. Når dette er gjort, vil NVDA udtale tegn, men disse
  indstillinger vil kun påvirke LAMBDA eller dets specielle vinduer.

## Postliste for tilføjelsespakke:

For at rapportere fejl, eller hvis du har forslag eller hvis du vil bidrage,
kan du abonnere på Addon-gruppen (på engelsk). Du kan tilmelde dig på
hjemmesiden: <https://groups.io/g/lambda-nvda>.

## Ændringshistorik

Nedenfor er en liste over ændringer mellem de forskellige versioner. Ud for
versionen er nummer, mellem parenteser, der repræsentere status for
udvikling. Den aktuelle udgave af udviklingsversionen er ikke inkluderet
eftersom den kunne have ændringer, indtil den er markeret som stabil eller
kasseres som kandidat.

### Version 1.3.0 (stabil)

* Understøttelse for nyere versioner af NVDA (understøttelse fpr Python 3)
* Løst et problem, hvor et tryk på NVDA+D, hvilket er kommandoen til at
  duplikere en linje indsatte udklipsholderens indhold, hvis man befandt sig
  på en blank linje. Når du nu trykker på NVDA+D, og du befinder dig på en
  blank linje, vises en ny tom linje som forventet.

### Version 1.2.2 (stabil)

* Forbedret kompatibilitet med WX Python version 4 (introduceret i NVDA
  2018.3). Advarsel relateret til wx.NewId() vises ikke længere i debug log.
* Implementerede guiHelper for at forbedre dialogenes udseende.
* Nye sprog. Opdaterede oversættelser.

### Version 1.2.1a (stabil)

Denne opdatering er beregnet til at være en langsigtet udgave i henblik på
understøttelse. Det betyder, at indtil tidligst juni 2018, vil der ikke
blive frigivet en version der er ligeså stabil. Vi gør det for at give de
studerende maksimal stabilitet og for at minimere ændringerne i løbet af
skoleåret.

* Nye sprog. Opdaterede oversættelser.

### Version 1.2.1 (stabil)

* Tilføjet kompatibilitet med den måde, NVDA 2017.3 bruger til at styre
  punktskrift. Baglæns kompatibilitet vedligeholdes.
* Rettede mange fejl med punkt.

### Version 1.2.0 (udvikling)

Denne version var ikke offentliggjort som stabil, fordi version 1.2.1
inkluderet store rettelser.

* Nye landestandarder. Opdaterede lokaliseringer.

### Version 1.1.8 (stabil)

* Indledende stabil frigivelse.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=lambda

[2]: https://addons.nvda-project.org/files/get.php?file=lambda-dev
