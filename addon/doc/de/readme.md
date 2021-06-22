# Lambda-Erweiterung für NVDA #

* Authoren: Alberto Zanella und das Lambda-NVDA-Team.
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Dieses Projekt ist ein AppModul für die LAMBDA-Software. Es wurde durch die Arbeit von Peter Lecky an der Comenius Universität inspiriert.
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) ist eine Software, die blinden Menschen das Lesen und Schreiben mathematischer Inhalte mit Hilfe einer Braillezeile und/oder eines Bildschirmlesers ermöglicht. LAMBDA ist das Ergebnis eines durch Fördermittel der EU durchgeführten Projektes. Weitere Informationen über LAMBDA finden Sie unter [https://www.lambdaproject.org/](https://www.lambdaproject.org/).  
Die aktuelle Version der Erweiterung verfügt über Braille-Tabellen für
italienische und spanische Sprachen und seine Benutzeroberfläche ist in den
meisten Sprachen der NVDA-Oberfläche verfügbar, da sie von der
NVDA-Übersetzungscommunity übersetzt wird.  Wenn Sie ein nicht-italienischer
Benutzer von LAMBDA sind und mit der Portierung der Braille-Tabelle in Ihrer
Sprache beitragen möchten, wenden Sie sich bitte an den Autor (siehe unten)
oder abonnieren Sie die Projekt-Mailingliste.

**Bitte beachten Sie:** Diese Erweiterung wurde von Alberto Zanella ehrenamtlich entwickelt. Weder der Autor noch die Mitwirkenden sind am Verkauf und / oder an der Weiterentwicklung der Software Lambda beteiligt. Für weitere Informationen über Lambda oder wenn Sie Unterstützung bei der Verwendung benötigen, wenden Sie sich bitte an Ihren lokalen Händler. Wenn Sie Schwierigkeiten bei der Verwendung oder Installation dieser Erweiterung haben, kontaktieren Sie bitte den Autor oder verwenden Sie den Link "Issues" auf der Github-Projektseite.

### [Offizielles Github-Repository](https://github.com/lambda-nvda/lambdaNvda/)

## Funktionen:

### Vorlesefunktionen:

* Menüs und dialoge werden richtig angesagt;
* Natürliche Sprachunterstützung für mathematische Formel basierend auf der
  Lambda-Mathematik-Platform, z.B. "zusammengesetzte Wurzel 3 sep
  zusammengesetzte Wurzel 3 x plus 24, zusammengesetzte Wurzel geschlossen,
  minus 3 gleich 0";
* Die Lesemodi Zeichen, Worte, Zeile und alles lesen werden unterstützt;
* Es wird angesagt, wenn ein Textblock ausgewählt oder erweitert wurde
  (durch Drücken von STRG+B und Umschalt+STRG+B);
* Das Navigieren durch den Texteditor mit Windows- und LAMBDA-spezifischen
  Befehlen wird angesagt;
* Im Bereich Werkzeuge (Tools) in der LAMBDA-Erweiterung können ausführliche
  oder einfache Sprachmodi ausgewählt werden;
* Spezielle Dialoge wie Strukturmodus, Taschenrechner und Matrixfenster
  werden nun korrekt angezeigt und NVDA liest korrekt vor, wenn der Cursor
  bewegt oder wenn neuer Text eingegeben wird;
* Das Eingabenecho nutzt den Lambda-Text-Prozessor. Somit werden Symbole und
  Markierungen richtig angesagt.

### Braille-Unterstützung:

* Die Erweiterung installiert und aktiviert innerhalb des
  Benutzerprofilverzeichnisses eine eigene Braille-Tabelle. Diese Tabelle
  kann für verschiedene Sprachen unterschiedlich sein. Es wurden
  benutzerdefinierte Braille-Tabellen aus dem Lambda-Plugin für JAWS
  (jbt-Datei) erstellt. Somit werden Symbole und Marker mit den gleichen
  Punktmustern dargestellt;
* Die Erweiterung erstellt ein NVDA-Profil für eine
  Standard-Braille-Konfiguration. Dadurch wird die Ausgabe nur dann auf die
  benutzerdefinierte Braille-Tabelle gesetzt, wenn die Lambda-Anwendung
  aktiv ist;
* Menüs und Dialoge werden in Braille korrekt angezeigt;
* Der Inhalt des Editors wird korrekt in Brailleschrift wiedergegeben und
  der Benutzer kann sich mit Hilfe von Braille-Scrolling-Tasten oder
  Cursor-Routing-Tasten durch die Elemente bewegen;
* Ab der Erweiterungsversion 1.1.0 gibt es zwei Möglichkeiten, wie der Text
  im Lambda-Editor angezeigt wird: "Flächenmodus ein" (Flat mode) und
  "Flächenmodus aus" (non-flat mode). Wenn der "Flächenmodus" eingeschaltet
  ist, wird NVDA das Bildschirmlayout benutzen, um Informationen vom Editor
  abzurufen und die Position des Cursors zu bestimmen. Dies ist besonders
  vorteilhaft, wenn der Benutzer sich auf dem Bildschirm auch in weißen
  Bereichen bewegen muss. Wenn der"Flächenmodus" auf "aus" eingestellt ist,
  ist die Textdarstellung auf der Braillezeile stabiler. Dies liegt daran,
  dass NVDA für die Bestimmung der Cursorposition die Windows-Schnittstelle
  verwendet. Wenn der Cursor jedoch in weißen Feldern neben dem Ende der
  Textzeile bewegt wird, folgt die Braillezeile nicht dem tatsächlichen
  Cursor, solange der Benutzer ein nicht-weißes Leerzeichen hinzufügt.

Der Flächenmodus ist standardmäßig aktiv. Sie können ihn mit NVDA + Umschalt
+ f deaktivieren oder erneut aktivieren.

Wir empfehlen den Flächenmodus zu deaktivieren, wenn Sie benutzerdefinierte
DPI in Windows verwenden (Custom Sizing Option), insbesondere wenn Sie
Bildschirmeinstellungen mit mehr als 96 dpi (größer als 100%) haben.

* Die Struktur von Dialogfenstern ist einfacher, wiederholte Informationen
  wurden entfernt;
* Die Auswahl wird mit den Punkten 7 und 8 richtig markiert und die
  Markierung wird korrekt aktualisiert, während die Standard-Windows-Befehle
  (Umschalt+Pfeiltasten) oder Lambda-spezifische Befehle (STRG+B,
  STRG+Umschalt+B) gedrückt werden.

## Bevor Sie diese Erweiterung verwenden.

Diese Erweiterung erstellt ein NVDA-Profil mit dem Namen"Lambda", das mit
der Anwendung"Lambda.exe" verbunden ist. Das Profil stellt automatisch alle
Braille-Optionen ein: die benutzerdefinierte Braille-Tabelle, die
Fokus-Befestigung und die Flächenmodus-Einstellungen.

Wenn ein vorheriges Profil mit dem gleichen Namen in Ihrem System vorhanden
ist, wird die Erweiterung es nicht überschreiben. Sie müssen Ihr
Konfigurationsprofil manuell anpassen.

Wenn Sie bestimmte Einstellungen haben, die Sie beibehalten möchten, können
Sie den "Revert LAMBDA Profile Wizard" (Widerherstellungsassistent für
LAMBDA-Profile) verwenden. Die Tastenkombination für dieses Werkzeug ist
NVDA+alt+r. Der Fokus muss sich dabei im LAMBDA befinden.

Eine einfache Möglichkeit ist es auch, alte Versionen des "Lambda"-Profils
nach der Installation der Erweiterung zu löschen. Öffnen Sie dazu das
NVDA-Menü, wählen Sie den Menüpunkt"Konfigurationsprofile" und drücken Sie
ENTER.

Im Dialog Konfigurationsprofile können Sie das Lambda-Profil lokalisieren
und löschen. Das Profil wird beim nächsten Start der Lambda-Anwendung neu
erstellt.

Das Löschen des Lambda-Profils ist eine einfache Lösung, auch wenn die
Erweiterung auf irgendein Problem stößt. Wenn z.B. die Braille-Tabelle nicht
richtig eingestellt ist, können Sie das Profil einfach löschen, anstatt das
Profil manuell zu konfigurieren. Die Erweiterung erstellt beim nächsten
Laden des Lambda-Editors ein neues Profil.

Jedes Mal, wenn der Lambda-Editor gestartet wird, prüft diese Erweiterung,
ob ein Profil mit dem Namen "Lambda" existiert. Ist dies nicht der Fall,
wird automatisch ein Profil mit dem folgenden Formular erstellt:

```
Dateiname: userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = Pfad-zur-Brailletabellen-Ordner-der-Erweiterung\Brailletabellenname

[lambda]
	brailleFlatMode = True

```

Wo:

* path-to-the-addon-brailleTable-dir : ist der absolute Pfad des
  Erweiterungsordners + "\Braille-Tabellen"
* tableName : hängt von der gerade aktiven NVDA-Sprache ab. Zurzeit sind nur
  die italienischen und spanischen Braille-Tabellen, "lambda-ita.utb" und
  "lambda-esp.utb", vorhanden.

## Erweiterungsspezifische Tastaturbefehle:

* **NVDA+Shift+f**: Schaltet Braille-Flächenmodus ein oder aus;
* **NVDA+alt+r**: Öffnet den "Revert LAMBDA Profile Wizard"
  (Wiederherstellungsassistent für LAMBDA-Profile);
* **NVDA+d**: Zeilen duplizieren (nutzen Sie diesen Befehl statt STRG+d).

## Bekannte Probleme:

Aufgrund eines Fehlers in LAMBDA bietet die Erweiterung eine Extra-Logik,
die geschützte Leerzeichen meldet. Diese Logik kann in den folgenden
Situationen versagen:

* Wenn Wörter wie "space", "spazio" "Espacio" etc. im Text eingefügt werden,
  könnten Sie in der lokalen NVDA-Sprache ausgesprochen werden.
* Leere Zeilen werden von der LAMBDA-Sprach-Platform nicht gemeldet. Der
  Benutzer wird stattdessen die Übersetzung des Wortes "Leerzeichen"
  hören. Das könnte sowohl eine Leerzeile als auch eine Zeile sein, die nur
  das Wort "Leerzeichen" enthält.

## Nützliche Tipps

Hier sind einige Tipps, die Ihnen eine effizientere Arbeitsweise mit der
Erweiterung ermöglichen werden.

* Zeichenweise lesen: Normalerweise möchten Sie bei der Arbeit mit
  Mathematischen Inhalten, dass NVDA die Eingaben Zeichen für Zeichen
  meldet. Um dies zu ermöglichen, gibt es ein paar einfache Schritte:
  Stellen Sie sicher, dass der Fokus auf das Fenster des LAMBDA oder eine
  seiner Varianten (z.B. die Sechs-Punkte-Darstellung) gerichtet ist;
  drücken Sie NVDA+2 (Zahl zwei) oder navigieren Sie zum
  NVDA-Menü/Einstellungen/Tastatur-Einstellungen und aktivieren Sie das
  Kontrollkästchen für Zeichen ansagen; gehen Sie zu
  LAMBDA>Einstellungen>Voice paramethers (Stimmparameter) und stellen Sie
  sicher, dass das Kontrollkästchen "echo" eingeschaltet ist, andernfalls
  wird NVDA beim Tippen nichts von der Sprach-Platform empfangen. Danach
  wird NVDA geschriebene Zeichen aussprechen! Aber keine Sorge, dies gilt
  nur in LAMBDA oder seinen speziellen Fenstern. Ansonsten werden die
  Einstellungen für den Rest der Anwendungen nicht verändert.

## Mailliste für die LAMBDA-Erweiterung:

Um Fehler oder Vorschläge mittzuteilen oder wenn Sie mitwirken möchten,
können Sie die englische Lambda-Entwicklungsgruppe abonnieren.  Sie können
sich auf der folgenden Website anmelden: <https://groups.io/g/lambda-nvda>.

## Änderungsnotizen

Nachfolgend finden Sie eine Liste der Änderungen zwischen den verschiedenen
Erweiterungsversionen. Neben der Versionsnummer steht in Klammern der
Entwicklungsstand. Die aktuelle Entwicklerversion ist nicht enthalten, da
sie weitere Änderungen haben könnte, bevor sie als stabil gekennzeichnet
oder als Kandidat verworfen wird.

### Version 1.3.0 (stabil)

* Unterstützung für neuere Version von NVDA (Unterstützung für Python 3)
* Problem behoben, wenn mittels NVDA+d eine leere Zeile dupliziert wurde,
  wurde die Zwischenablage eingefügt. Nun wird die leere Zeile wie erwartet
  dupliziert.

### Version 1.2.2 (stable)

* Verbesserte Kompatibilität mit wxPython 4 (eingeführt mit NVDA
  2018.3). Warnung bezüglich mit wx.NewId() wird nicht länger mehr angezeigt
  im Debug-Protokoll.
* GuiHelper wurde implementiert, um das Erscheinungsbild der Dialoge zu
  verbessern.
* Neue Sprachen. Aktualisierte Übersetzungen.

### Version 1.2.1a (stabil)

Diese Aktualisierung ist als langfristiges Support-Release gedacht. Das
bedeutet, dass es bis mindestens Juni 2018 keine andere stabile Version als
diese geben wird. Wir handhaben es so, um den Studenten maximale Stabilität
zu bieten und die Veränderungen während des akademischen Jahres zu
minimieren.

* Neue Sprachen. Aktualisierte Übersetzungen.

### Version 1.2.1 (stabil)

* Die Kompatibilität mit der Art und Weise, wie NVDA 2017.3 die
  Brailleschrift verwaltet, wurde hinzugefügt. Abwärtskompatibilität bleibt
  bestehen.
* Viele Braille-Probleme wurden behoben.

### Version 1.2.0 (Testversion)

Diese Version wurde nicht als Stabil veröffentlicht, da die Version 1.2.1
viele signifikante Verbesserungen beinhaltete.

* Neue und aktualisierte Lokalisierungen.

### Version 1.1.8 (stabil)

* Erste stabile Version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=lambda

[2]: https://addons.nvda-project.org/files/get.php?file=lambda-dev
