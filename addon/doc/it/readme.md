# Componente aggiuntivo Lambda per NVDA #
[[!meta title="Lambda Add-On for NVDA"]]

* Autori: Alberto Zanella e il team Lambda-NVDA
* Download [stable version][1]
* Download [development version][2]

Questo add-on permette di utilizzare il software LAMBDA con NVDA. Deriva da un lavoro precedente di Peter Lecky della Comenius University ed è stato studiato e realizzato per rendere l'accesso all'ambiente LAMBDA il più semplice e simile a ciò che già avviene con altri screen reader.
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) è un programma che aiuta i non vedenti a leggere  e scrivere matematica utilizzando o un display braille, o la sintesi vocale, o entrambi contemporaneamente.
Per maggiori informazioni sul software LAMBDA si invita a consultare: http://www.lambdaproject.org/it/ e http://veia.it/
L'attuale versione del componente aggiuntivo dispone di tabelle braille
adattate per l'uso con Lambda sia per l'Italiano che per lo Spagnolo. La
traduzione delll'addon è disponibile in svariate lingue grazie al team di
traduzione internazionale. Se non sei un utente italiano e vorresti
includere il porting della tua tabella braille nel progetto, contatta
l'autore (vedi sotto), oppure iscriviti alla mailing list del progetto.-

**Nota**: Si precisa che lo sviluppo di questo add-on è avvenuto in maniera volontaria e del tutto indipendente dall'azienda rivenditore del prodotto LAMBDA, con la quale l'autore non intrattiene alcun rapporto di lavoro e/o di collaborazione. Per richieste in merito al prodotto si invita pertanto a contattare il servizio di supporto tecnico messo a disposizione dal fornitore del prodotto.
Per ulteriori informazioni sull'addon, richieste o altro è possibile contattare l'autore tramite email o su GitHub.

### [Repository Github ufficiale: ](https://github.com/lambda-nvda/lambdaNvda/)

## Caratteristiche principali:

### accesso in sintesi vocale:

* Vocalizza correttamente le finestre di dialogo ed i menù;
* Vocalizza le formule matematiche utilizzando il sistema di processamento
  di testi di LAMBDA, quindi legge correttamente ed in modo naturale il
  testo matematico (ad esempio "radice 3 di 3x più 24, fine radice");
* Permette di leggere per carattere, riga, o con il leggi-tutto;
* Vocalizza correttamente la selezione dei blocchi, usando ctrl-b o
  shift-ctrl-b;
* Vocalizza correttamente gli spostamenti all'interno del testo utilizzando
  i principali tasti standard di Windows e quelli specifici di LAMBDA;
* Vocalizza sia in maniera compatta che estesa, funzione modificabile dal
  menu strumenti di Lambda;
* Vocalizza le finestre di esplorazione struttura, la calcolatrice e la
  finestra di esplorazione delle matrici;
* Il riscontro in scrittura avviene usando il sistema di processamento testi
  di LAMBDA, di modo da annunciare correttamente i simboli e i marcatori.

### Supporto Braille:

* The addon installs (inside the user profile directory) and activates a
  custom braille table. This table may be different for different
  languages. Custom braille tables were made from ones in the Lambda plugin
  for JAWS (jbt file). Then symbols and markers are represented using the
  same dots patterns;
* The addon creates an NVDA profile for a standard braille configuration. By
  this, the output is set to the custom braille table only when the Lambda
  application is active;
* Le finestre di dialogo e i menu vengono mostrati in braille in maniera
  appropriata;
* The content of the editor is correctly rendered in braille and the user is
  able to move using braille scrolling keys or cursor routing keys;
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

The "flat mode" is active by default. You can toggle "flat mode" on or off
by pressing NVDA+SHIFT+F.

We strongly recommend to disable the Flat Mode if you are using custom DPI
in Windows (Custom sizing option), especially when you have screen settings
with more than 96 dpi (larger than 100%).

* The structure of dialog boxes is easier, repeated information has been
  removed;
* The selection will be marked properly using dots 7 and 8, and marking is
  properly refreshed while standard Windows commands (SHIFT+ARROWS) or
  Lambda specific commands (CTRL+B, CTRL+SHIFT+B) are pressed.

## Prima di iniziare ad utilizzare questo componente aggiuntivo.

This addon creates an NVDA profile named "lambda" which is associated with
the "lambda.exe" application. The profile automatically sets all braille
options: the custom braille table, the focus tethering and flat mode
settings.

If a previous profile with the same name is present in your system, the
addon will not override it and you have to manually adjust your
configuration profile.

To stave off this situation, if you have specific settings you'd like to
preserve, you can use the "Revert LAMBDA Profile Wizard". The shortcut to
start this tool is NVDA+alt+r (when focused in LAMBDA).

An easy option is also to delete old versions of the "lambda" profile after
the installation of the addon. To do so, open the NVDA menu, select the
"Configuration profiles" menu Item and press ENTER.

In the Configuration profiles dialog, you'll be able to locate and delete
the "lambda" profile. The profile will be re-created the next time the
Lambda application is started.

Deleting the "lambda" profile should be an easy solution also when the addon
runs into any problem. For instance, if the braille table is not properly
set, instead of manually configuring the profile, you can simply delete
it. The addon will create a new one the next time you'll load the Lambda
editor.

Each time the Lambda editor is started, this addon checks if a profile with
the name "lambda" exists. If it doesn't, it automatically generates a
profile with the following form:

``` filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Dove :

* path-to-the-addon-brailleTable-dir : is the absolute path of the addon
  directory + "\brailleTables"
* tableName : depends on the active NVDA language. Currently only the
  italian and Spanish braille tables, "lambda-ita.utb" and "lambda-esp.utb"
  respectively, is present.

## Comandi rapidi da tastiera per il componente:

* **NVDA+Shift+f**: Toggle braille flat mode on or off;
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

## Suggerimenti utili

Questo è un insieme di consigli che aiuterà ad utilizzare il componente in
maniera più efficiente.

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

## Addon mailing list:

Per segnalare bug, suggerimenti o se si desidera contribuire è possibile
iscriversi al gruppo relativo a questo componente aggiuntivo (in inglese). È
possibile iscriversi dal sito internet: https://groups.io/g/lambda-nvda.

[[!tag dev stable]]
[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=lambda[1]:
http://addons.nvda-project.org/files/get.php?file=lambda

[2]: http://addons.nvda-project.org/files/get.php?file=lambda-dev[2]:
http://addons.nvda-project.org/files/get.php?file=lambda-dev
