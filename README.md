<!---
This is not the source for the readme file of NVDA Addon. This is just for the Github repository. The source for the NVDA Addon build is readme-src.md. Thanks!
-->

# Lambda Add-On for NVDA

* [Download latest stable release](https://github.com/nvdaaddons/lambda/releases/download/latest/lambda.nvda-addon)
* [Download latest development release](https://github.com/nvdaaddons/lambda/releases/download/dev/lambda-dev.nvda-addon)

Se sei un utente italiano vista [questa pagina](https://github.com/nvdaaddons/lambda/wiki/Benvenuto)

This project is an appModule for the LAMBDA Software. It has been inspired by the work of Peter Lecky at the Comenius University. 
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) is a software that helps blind people to read and write math using a braille display and/or a speech synthesizer.
LAMBDA is the result of an EU-Project. For more information about LAMBDA please visit [http://www.lambdaproject.org/](http://www.lambdaproject.org/).  
The current version of the addon has braille tables for Italian and Spanish languages and has been included on the official NVDA translations system, so its interface is being translated into many languages.
If you are a non-italian user of LAMBDA and you would like to contribute with translations in your language, feel free to contact the author (see below) or fork this project.

**Please note:** This addon has been developed by Alberto Zanella as a voluntary activity. Nor the author or the contributors are involved in selling and / or development of the software Lambda. If you need more information about Lambda, or you need support on how to use it, please contact your local distributor. If you are encountering any difficulties when using or installing this addon, please contact the author or use the "Issues" link on the Github project page.

## Addon Features:

### Speech support:

* Dialogs and menus are properly reported;
* Natural speech support for math formulas using the Lambda math engine, i.e. "compound root 3 sep compound root 3 x plus 24, close compound root, minus 3 equals 0";
* implemented the Reading by character, words, lines and Say All;
* Speaks when a block of text is selected or extended (using CTRL+B and SHIFT+CTRL+B);
* Speaks when moving in the text editor using standard Windows commands and Lambda-specific commands;
* Both Extended and Short speech modes are supported (you can select it using the Tools menu in Lambda);
* Special dialogs like structure mode, calculator, and matrix window are now correctly reported and NVDA reads correctly when moving the cursor around or when new text is typed ;
* Typing echo uses the Lambda text processor, so symbols and markers will be correctly reported.

### Braille support:

* The addon installs (inside the user profile directory) and activates a custom braille table. This table may be different for different languages. Custom braille tables were made from ones in the Lamba plugin for JAWS (jbt file). Then symbols and markers are represented using the same dots patterns;
* The addon creates an NVDA profile for a standard braille configuration. By this, the output is set to the custom braille table only when the Lambda application is active;
* Dialogs and menus are properly reported in braille;
* The content of the editor is correctly rendered in braille and the user is able to move using braille scrolling keys or cursor routing keys;
* Starting from the addon version 1.1.0, there are two ways in which the text in the Lambda editor is rendered: "Flat mode" and "non-Flat Mode". When the "Flat mode" is on, NVDA will use the Display Model to retrieve information from the editor and to determine the caret position. This is especially beneficial when the user needs to move around on the screen, even in white spaces. When the  "Flat Mode" is set to "off", text rendering on the braille display is more stable, since NVDA uses Windows API to retrieve it. However when the the caret is moved in white spaces next to the end of the line of text, the braille display does not follow the real cursor as long as a non-white space is added by the user. 

The "flat mode" is active by default. You can toggle "flat mode" on or off by pressing NVDA+SHIFT+F.

We strongly recommend to disable the Flat Mode if you are using custom DPI in Windows (Custom sizing option), especially when you have screen settings with more than 96 dpi (larger than 100%).
* The structure of dialog boxes is easier, repeated information has been removed;
* The selection will be marked properly using dots 7 and 8, and marking is properly refreshed while standard Windows commands (SHIFT+ARROWS) or Lambda specific commands (CTRL+B, CTRL+SHIFT+B) are pressed.

## Setup

You can get the addon by navigating to the "Releases" link in the Github repository page and activating it, then jump to the Downloads heading. Open the first link you'll locate, which is named "lambda.nvda-addon". Download it and run it using your NVDA Screen Reader. The setup will be automatically performed.

## Before starting to use this addon.

This addon creates an NVDA profile named "lambda" which is associated with the "lambda.exe" application. The profile automatically sets all braille options: the custom braille table, the focus tethering and flat mode settings.

If a previous profile with the same name is present in your system, the addon will not override it and you have to manually adjust your configuration profile. 

To stave off this situation, if you have specific settings you'd like to preserve, you can use the "Revert LAMBDA Profile Wizard". The shortcut to start this tool is NVDA+alt+r.

An easy option is also to delete old versions of the "lambda" profile after the installation of the addon. To do so, open the NVDA menu, select the "Configuration profiles" menu Item and press ENTER.

In the Configuration profiles dialog, you'll be able to locate and delete the "lambda" profile. The profile will be re-created the next time the Lambda application is started.

Deleting the "lambda" profile should be an easy solution also when the addon runs into any problem. For instance, if the braille table is not properly set, instead of manually configuring the profile, you can simply delete it. The addon will create a new one the next time you'll load the Lambda editor.

Each time the Lambda editor is started, this addon checks if a profile with the name "lambda" exists. If it doesn't, it automatically generates a profile with the following form:

```
filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Where :

* path-to-the-addon-brailleTable-dir : is the absolute path of the addon directory + "\brailleTables"
* tableName : depends on the active NVDA language. Currently only the italian and Spanish braille tables, "lambda-ita.utb" and "lambda-esp.utb" respectively, is present.


## Addon Keyboard Shortcuts:

* **NVDA+Shift+f**: Toggle braille flat mode on or off;
* **NVDA+alt+r**: Open the "Revert LAMBDA Profile Wizard".

## Known issues:

Due to a bug present in LAMBDA, the add-on provides an extra-logic that reports white spaces. This logic may fail in the following situations:
* When words like "space", "spazio" "Espacio" etc. are inserted into the text, they may be reported by NVDA as the local NVDA language translation. 
* Blank lines are not reported by the LAMBDA speech engine. The user will hear the translation of the word "space" instead. This could be both a blank line or a line containing only the word "space".

## Usefull tips

This is a set of tips that will help you on using the addon in a more eficient way.
* Character-by-character reporting: Normally, when working with maths you would like NVDA to report things you're writing character by character. To do this, there are a couple of simple steps: ensure to have the foc on the LAMBDA's window or one of its variants (the six dots representation, for example); press NVDA+2 (number two) or navigate to NVDA menu>Preferences>Keyboard settings and check the box to Speak typed characters; go to LAMBDA>Options>Voice paramethers and ensure the checkbox "echo" is ON, otherwhise NVDA won't receive anything from the speech engine while you are typing. And done, NVDA will speak written characters, but don't worry, only in LAMBDA or its special windows, the settings for the rest of applications will be left as they were.

## Addon mailing list:

To report bugs, suggestions or if you want to contribute you can subscribe the Addon Google Group (in English).
You can subscribe writing to lambda-nvda+subscribe@[plural of google group] dot com .

# Authors and Contributors:

* Author: Alberto Zanella <lapostadi[myfirstname]@gmail.com>
* Iván Novegil
* Noelia Ruiz Martínez
* Salva Doménech Miguel
* Alessandro Albano
* Christian Leo
* Simone Dal Maso
