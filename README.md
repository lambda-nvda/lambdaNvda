<!---
This is not the source for the readme file of NVDA Addon. This is just for the Github repository. The source for the NVDA Addon build is readme-src.md. Thanks!
-->

#Lambda Add-On for NVDA#

Se sei un utente italiano [visita questa pagina](https://github.com/albzan/lambda-nvda/wiki/benvenuto)

If you are an italian user please [visit this page](https://github.com/albzan/lambda-nvda/wiki/benvenuto)

This project is an appModule for the LAMBDA Software. It has been inspired by the work of Peter Lecky at the Comenius University. 
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) is a software that helps blind people to read and write math using a braille display and/or a speech synthesizer.
LAMBDA is the result of an EU-Project. For more information about LAMBDA please visit [http://www.lambdaproject.org/](http://www.lambdaproject.org/).  
The current version of this addon has braille tables only for the Italian language but its interface is available both in Italian and Spanish right now.
If you are a non-italian user of LAMBDA and you would like to contribute with translations in your language, feel free to contact the author (see below) or fork this project.

**Please note:** This addon has been developed by Alberto Zanella as a voluntary activity. Nor the author or the contributors are involved in selling and / or developing the software Lambda. If you would like to get more information about Lambda, address issues or get support, please contact your local distributor. If you are encountering any difficulties using or installing this addon, please contact the author or use "Issues" link available on the Github project page.

##Addon Features:

###Speech support:

* Dialogs and menus are properly spoken;
* It speaks math formulas using the internal Lambda processor engine, by this way the text on the editor sounds natural (i.e. "compound root 3 sep compound root 3 x plus 24, close compound root, minus 3 equals 0");
* Reading by character, words, lines and Say All implemented;
* Speaks when a block of text is selected or extended (using CTRL+B and SHIFT+CTRL+B);
* Speaks when moving in the text editor using standard Windows commands and Lambda-specific commands too;
* Both Extended and Short speech modes are supported (you can set it using the Tools menu in Lambda);
*  Special dialog windows like structure mode, calculator, and matrix are now correctly reported and NVDA reads correctly when you move around or input the text ;
* Typing echo uses the Lambda text processor, so symbols and markers will be correctly spoken.

###Braille support:
* The addon install (inside the user profile directory) and activates a custom braille table. This table may differs in different languages. The table was made starting from the one present in the Lamba plugin for JAWS (jbt file). Then symbols and markers are represented using the same dot patterns;
* The addon creates an NVDA profile and sets the proper braille configuration. Then, the output is set to the custom braille table only when the Lambda application is active;
* Dialogs and menus are properly reported in braille;
* The content of the editor is correctly redered in braille and the user is able to move using braille scrolling keys or cursor routing keys;
* Starting from the addon version 1.1.0 there are two ways in which the text in the Lambda editor is rendered: "Flat mode" and "non-Flat Mode". When the "Flat mode" is on, NVDA will use the Display Model to retrieve the information from the editor and to determine the caret position. This is especially beneficial when the user needs to move around on the screen, even in white spaces of the editor. When the  "Flat Mode" is set to "off", text rendering on the braille display is more stable, since NVDA uses Windows API to retrieve it. By this way, though, when the user moves in white spaces the caret on the braille display will not follows the real cursor as long as a non-white space will be inserted by the user. 

The "flat mode" is active by default. You can toggle "flat mode" on or off by pressing NVDA+SHIFT+F.

We strongly recommend to disable the Flat Mode if you are using custom DPI in Windows (Custom sizing option), especially when you are enlarging the size (larger than 100%).
* Simplifies the structure of dialog boxes removing repeated information;
* The selection will be marked properly using dots 7 and 8, and properly refreshed when pressing standard Windows commands (SHIFT+ARROWS) or Lambda specific commands (CTRL+B, CTRL+SHIFT+B).

##Setup
You can get the addon by navigating to the "Releases" link in the Github repository page and activating it, then jump to the Downloads heading. Open the first link you'll locate, which is named "lambda.nvda-addon". Download it and run it using your NVDA Screen Reader. The setup will be automatically performed.

##Before starting to use this addon.
This addon creates an NVDA profile named "lambda" which is associated with the "lambda.exe" application. The profile automatically sets all braille options: the custom braille tables, the focus tethering and the flat mode settings.

If a previous existing profile with the same name is present, the addon will not override it and you have to manually put this configuration inside your profile setting file. 

To stave off this situation, after the installation of the addon we suggest to delete old versions of the "lambda" profile. To do so, open the NVDA menu, select the "Configuration profiles" menu Item and press ENTER.

In the Configuration profiles dialog, you'll be able to locate and delete the "lambda" profile. The profile will be re-created the next time you'll launch the Lambda application.

Deleting the "lambda" profile should be an easy solution also when you find any issues that "appears" at some point using the addon. For instance, if the braille table is not properly set, instead of manually configuring the profile, you can simply delete it. The addon will create a new one the next time you'll load the Lambda editor.

Each time the Lambda editor is started, this addon checks if a profile with the name "lambda" exists. If it doesn't exists it automatically generate a profile with the following form:

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
* tableName : depends on the active NVDA language. Currently only the italian braille table, "lambda-ita.utb" , is present.




#Authors and Contributors:
* Author: Alberto Zanella <lapostadi[myfirstname]@gmail.com>
* Iván Novegil
* Noelia Ruiz Martínez
* Alessandro Albano
* Christian Leo
* Simone Dal Maso



