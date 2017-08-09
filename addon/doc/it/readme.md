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

* Il componente aggiuntivo installa (all'interno della cartella profilo
  utente di NVDA) ed inseguito attiva una tabella braille
  personalizzata. Tale tabella può essere diversa in base alla lingua. Le
  tabelle personalizzate sono state adattate da quelle presenti nel plugin
  Lambda per Jaws, (file jbt). In seguito i simboli e i marcatori sono stati
  rappresentati servendosi degli stessi punti braille.
* Crea e configura un profilo applicativo apposito (in questo modo la
  tabella braille speciale per LAMBDA sarà attivata solo su questo software
  e non su altri);
* Le finestre di dialogo e i menu vengono mostrati in braille in maniera
  appropriata;
* Permette la navigazione nei menù e nelle finestre di dialogo in braille,
  servendosi dei tasti di scorrimento o dei cursor routing;
* A partire dalla versione 1.1.0 presenta una doppia modalità per il
  braille: "Flat Mode" e non "Flat Mode" (modalità in linea
  attiva/disattiva). Quando "Flat Mode" è attivata, NVDA userà
  l'intercettatore grafico per determinare cosa è presente a schermo. Questo
  è utile per poter spaziare con il braille anche in aree "bianche", dove
  non è presente testo. Con la modalità "Flat Mode" disattivata, si avrà
  maggior potenza nell'elaborazione del testo, in quanto NVDA utilizzerà le
  funzioni messe a disposizione dal sistema operativo Windows per
  determinare la presenza di testo. Di contro però, non sarà possibile
  esplorare in braille aree bianche, prive di alcun testo.

Di default la modalità "Flat Mode" è attiva. Per attivarla o disattivarla
usare il comando NVDA+SHIFT+F.

Si consiglia caldamente di disattivare la "Flat Mode" qualora si sia
cambiato il valore dei DPI dello schermo (da 100% ad un ingrandimento
maggiore).

* La struttura delle finestre di dialogo è più lineare, rimosse informazioni
  ripetute;
* Marca in braille in modo corretto quando il testo viene selezionato.

## Prima di iniziare ad utilizzare questo componente aggiuntivo.

L'addon provvede alla creazione automatica di un nuovo profilo di NVDA
chiamato "lambda" associato all'applicazione "lambda.exe". Questa operazione
viene effettuata automaticamente all'avvio dell'applicativo Lambda. In
particolare vengono correttamente impostate le preferenze relative alla
tabella braille, al tracciamento del cursore ed alla modalità flat del
braille.

Se è già presente un profilo chiamato "lambda", l'addon non lo sovrascriverà
e si dovrà provvedere manualmente alla configurazione.

Per rendere il compito più facile, se si desidera preservare alcune delle
impostazioni del precedente profilo, è possibile utilizzare la funzionalità
di "Ripristino guidato impostazioni di LAMBDA". Il comando rapido per questo
comando è NVDA+alt+r (quando la finestra di Lambda è attiva).

Una soluzione più semplice è quella di cancellare il precedente profilo
chiamato "lambda" accedendo al menù di NVDA, quindi andando in "Gestione
profili".

Nella finestra Configurazione profili, si potrà individuare ed eliminare il
profilo di "lambda". Il profilo verrà ricreato la prossima volta
l'applicazione Lambda verrà riavviata.

La rimozione del profilo può essere utile anche nel caso di problemi legati
alla configurazione di NVDA con LAMBDA; ad esempio nel caso in cui la
tabella braille non sembra corrispondere con quella impostata, è più rapido
eliminare il profilo piuttosto che cercare di risolvere a mano, tanto il
profilo verrà subito ricreato al riavvio dell'applicazione.

Ad ogni avvio dell'applicazione Lambda, questo componente aggiuntivo
controlla se un profilo chiamato "lambda" esiste. Se non esiste, procede
alla sua creazione automatica secondo questo formato:

``` filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Dove :

* * percorso-della-cartella-brailleTable-del-componente-aggiuntivo : è il
  percorso assoluto della directory dell'addon a cui segue "\brailleTables"
* * nomeTabella : dipende dalla lingua di NVDA.

## Comandi rapidi da tastiera per il componente:

* * **NVDA+Shift+f**: Abilita o disabilita la modalità braille flat;
* * **NVDA+alt+r**: Apre la finestra di dialogo "Ripristino guidato
  impostazioni di LAMBDA".
* * **NVDA+d**: Duplica la riga su cui è posizionato il cursore (usare
  questa combinazione di tasti invece di control+d).

## Problemi noti

Per risolvere un problema presente in LAMBDA, l'add-on contiene una miglior
gestione della vocalizzazione degli spazi vuoti. Questa strategia di lettura
può non funzionare correttamente nei seguenti casi:

* Se vengono inserite nel testo parole come "space", "spazio" "Espacio" ecc,
  queste vengono lette da NVDA come "spazio" (tradotto in Italiano) anche se
  sono scritti in altre lingue
* Normalmente le righe vuote non vengono lette da LAMBDA. Ora verrà detto
  "spazio": ciò può indicare che la riga è vuota, che nella riga è presente
  uno spazio o che vi sia effettivamente scritto "spazio".

## Suggerimenti utili

Questo è un insieme di consigli che aiuterà ad utilizzare il componente in
maniera più efficiente.

* Lettura carattere per carattere: Quando si manipolano formule matematiche,
  è desiderabile fare in modo che NVDA pronunci i caratteri quando vengono
  digitati. Per fare questo è possibile procedere in diversi modi: anzitutto
  assicurarsi che la finestra di Lambda (o una finestra del programma come
  la visualizzazione a 6 punti) sia attiva; premere NVDA+2 (non del
  tastierino) oppure attivare il menù di NVDA>Preferenze>Impostazioni
  tastiera, attivare la casella di controllo "Leggi i caratteri
  digitati". Infine assicurarsi di avere abilitato il pulsante radio
  "Jaws/virgo" e la casella di controllo  "Echo"  di LAMBDA aprendo il menù
  del programma Opzioni>Impostazioni Voce. In questo modo LAMBDA processerà
  correttamente i caratteri inseriti. Niente paura: queste impostazioni
  rimarranno attive soltanto quando viene usato il programma Lambda. Se un
  altro programma viene attivato le impostazioni di lettura ritorneranno
  quelle precedenti.

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
