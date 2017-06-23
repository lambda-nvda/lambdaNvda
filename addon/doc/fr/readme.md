# Lambda Add-On for NVDA #

* Author: Alberto Zanella and the lambda-nvda team.
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Ce projet est un module complémentaire pour le logiciel LAMBDA. Il s'inspire du travail de Peter Lecky de l'Université Comenius. 
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) est un logiciel qui aide les personnes aveugles à lire et écrire les mathématiques en utilisant un afficheur braille et/ou un synthétiseur vocal.
LAMBDA est le résultat d'un EU-Project. Pour plus d'informations sur LAMBDA veuillez visiter [http://www.lambdaproject.org/](http://www.lambdaproject.org/).  
The current version of the addon has braille tables for Italian and Spanish
languages and its interface is available in most of the NVDA's official
languages, because it is translated by the NVDA translations community.  If
you are a non-italian user of LAMBDA and you would like to contribute with
the porting of the braille table in your language, feel free to contact the
author (see below) or subscribe the project mailing list.

**Veuillez noter :** Ce module a été développé par Alberto Zanella en tant qu'activité bénévole. Ni l'auteur ni les contributeurs ne sont impliqués dans la vente ou le développement du logiciel Lambda. Si vous voulez plus d'informations sur Lambda, ou avez besoin de support pour l'utiliser, veuillez contacter votre distributeur local. Si vous rencontrez des difficultés d'utilisation ou d'installation de ce module, veuillez contacter l'auteur ou utiliser le lien "Issues" sur la page Github du projet.

### [Official Github Repository](https://github.com/lambda-nvda/lambdaNvda/)

## Fonctions du Module :

### Support de la parole :

* Les dialogues et les menus sont correctement annoncés;
* Support naturel de la parole pour les formules mathématiques utilisant le
  moteur mathématique Lambda, ex. "compound root 3 sep compound root 3 x
  plus 24, close compound root, minus 3 equals 0";
* Support de la lecture par caractère, mot, ligne et dire tout;
* Parle quand un bloc de texte est sélectionné ou étendu (en utilisant
  CTRL+B et MAJ+CTRL+B);
* Parle lors du déplacement dans l'éditeur de texte en utilisant les
  commandes standards de Windows ou les commandes spécifiques de Lambda;
* Le mode de parole court et étendu est supporté (vous pouvez le
  sélectionner en utilisant le menu Outils de Lambda);
* Les dialogues spéciaux comme le mode de structure, la calculatrice, et la
  fenêtre de matrice sont maintenant annoncés correctement et NVDA lit
  correctement quand on déplace le curseur ou quand on ajoute du texte;
* L'écho de frappe utilise le processeur de texte de Lambda, ainsi les
  symboles et les marqueurs seront annoncés correctement.

### Support du braille :

* Le module s'installe (dans le répertoire de paramètres de l'utilisateur)
  et active une table braille spécifique. Cette table peut être différente
  selon la langue. Les tables braille ont été créées à partir de celles du
  script Jaws pour Lambda (fichier jbt). Ainsi les symboles et marqueurs
  sont représentés en utilisant les mêmes combinaisons de points;
* Le module crée un profil NVDA pour une configuration braille
  standard. Ainsi, l'affichage n'utilise la table spécifique que lorsque
  l'application Lambda est active;
* Les dialogues et les menus sont correctement affichés en braille;
* Le contenu de l'éditeur est correctement reproduit en braille et
  l'utilisateur peut se déplacer en utilisant les touches de défilement ou
  les curseur routines;
* A partir de la version 1.1.0 du module, le texte peut être présenté de
  deux façons dans l'éditeur Lambda : "Mode Plat" et "Mode non-Plat". Quand
  le "Mode Plat" est activé, NVDA utilise le modèle d'affichage pour obtenir
  l'information de l'éciteur et pour déterminer la position du curseur. Ceci
  est particulièrement quand l'utilisateur veut se déplacer dans l'écran,
  même dans les espaces blancs. Quand le "mode Plat" est désactivé, la
  présentation du texte sur l'afficheur braille est plus stable, puisque
  NVDA utilise les API de Windows pour l'obtenir. Cependant quand le curseur
  est amené dans l'espace blanc en fin de ligne de texte, l'afficheur
  braille ne suit pas le vrai curseur tant qu'un espace non blanc n'est pas
  ajouté par l'utilisateur.

Le "mode plat" est activé par défaut. Vous pouvez le désactiver ou l'activer
en pressant NVDA+MAJ+F.

Nous recommandons vivement de désactiver le Mode Plat si vous utilisez une
définition d'écran personnalisée sous Windows (option de personnalisation de
la taille), en particuliers quand votre écran est paramétré avec plus de 96
dpi (plus de 100%).

* La structure des boîtes de dialogue est plus simple, les informations
  répétées ont été supprimées;
* La sélection sera marquée correctement par les points 7 et 8, et le
  marquage est raffraîchi correctement quand on utilise les commandes
  standard de Windows (MAJ+Flèches) ou les commandes spécifiques de Lambda
  (CTRL+B, CTRL+MAJ+B).

## Avant de commencer à utiliser ce module.

Ce module crée un profil NVDA nommé "lambda" associé à
l'application"lambda.exe". Le profil règle automatiquement toutes les
options braille : La table braille spécifique, le suivi du focus et les
paramètres du mode plat.

Si un profil avec le même nom est déjà présent dans votre système, le module
ne le remplacera pas et vous devrez ajuster manuellement votre profil de
configuration.

Pour vous sortir de cette situation, si vous avez des paramètres
particuliers que vous désirez conserver, vous pouvez utiliser l'"Inverseur
Magique de Profil LAMBDA". Le raccourci pour démarrer cet outil est
NVDA+alt+r (quand LAMBDA est en avant-plan).

Une solution simple est d'effacer les anciennes versions du profil "lambda"
après l'installation du module. Pour ce faire, ouvrez le menu NVDA,
sélectionnez "Profils de configuration" et pressez entrer.

Dans le dialogue de configuration des profils, vous pourrez trouver et
effacer le profil "lambda". Le profil sera recréé au prochain démarrage de
l'application Lambda.

Effacer le profil "lambda" est aussi une solution simple quand le module
rencontre un problème. Par exemple, si la table braille est mal configurée,
au lieu de configurer manuellement le profil, vous pouvez simplement
l'effacer. Le module en créera un nouveau la prochaine fois que vous
chargerez l'éditeur Lambda.

Chaque fois qu'on lance l'éditeur Lambda, ce module vérifie si un profil
nommé "lambda" existe. Si ce n'est pas le cas, il génère automatiquement un
profil de la forme suivante :

``` nom de fichier : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Où :

* path-to-the-addon-brailleTable-dir : c'est le chemin absolu du répertoire
  du module + "\brailleTables"
* tableName : Dépend de la langue active de NVDA. Actuellement seules les
  tables braille italiennes et espagnoles, respectivement "lambda-ita.utb"
  et "lambda-esp.utb", sont présentes.

## Raccourcis clavier du module :

* **NVDA+Maj+f** : Active/désactive le mode braille plat;
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

## Liste de discussion du module :

To report bugs, suggestions or if you want to contribute you can subscribe
the Addon Group (in English).  You can subscribe from the website:
https://groups.io/g/lambda-nvda .

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=lambda

[2]: http://addons.nvda-project.org/files/get.php?file=lambda-dev
