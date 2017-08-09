# Module complémentaire Lambda pour NVDA #

* Auteur : Alberto Zanella et l'équipe de lambda-nvda.
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Ce projet est un module complémentaire pour le logiciel LAMBDA. Il s'inspire du travail de Peter Lecky de l'Université Comenius. 
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) est un logiciel qui aide les personnes aveugles à lire et écrire les mathématiques en utilisant un afficheur braille et/ou un synthétiseur vocal.
LAMBDA est le résultat d'un EU-Project. Pour plus d'informations sur LAMBDA veuillez visiter [http://www.lambdaproject.org/](http://www.lambdaproject.org/).  
Cette version du module contient des tables braille pour l'Italien et
l'Espagnol Et son interface est disponible dans la plupart des langues
officielles de NVDA, car il est traduit par les traducteurs de la
communauté. Si vous n'êtes pas un utilisateur Italien de LAMBDA et que vous
voulez contribuer au portage des tables braille dans votre langue, n'hésitez
pas à contacter l'auteur (voir ci-dessous) ou inscrivez-vous à la liste de
discussion du projet.

**Veuillez noter :** Ce module a été développé par Alberto Zanella en tant qu'activité bénévole. Ni l'auteur ni les contributeurs ne sont impliqués dans la vente ou le développement du logiciel Lambda. Si vous voulez plus d'informations sur Lambda, ou avez besoin de support pour l'utiliser, veuillez contacter votre distributeur local. Si vous rencontrez des difficultés d'utilisation ou d'installation de ce module, veuillez contacter l'auteur ou utiliser le lien "Issues" sur la page Github du projet.

### [Dépôt officiel sur Github](https://github.com/lambda-nvda/lambdaNvda/)

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
* **NVDA+alt+r** : Ouvre l'"assistant de restauration profil de Lambda".
* **NVDA+d**: Dupliquer les lignes (utilisez ceci au lieu de contrôle+d).

## Problèmes connus :

En raison d'un bogue affectant LAMBDA, ce module complémentaire fournit une
logique supplémentaire qui rapporte des espaces blancs. Cette logique peut
échouer dans les situations suivantes :

* Quand des mots tels que "space", "spazio" "Espacio" etc. sont insérés dans
  le texte, Ils peuvent être signalés par NVDA dans la langue de NVDA.
* Les lignes vides ne sont pas annoncées par la synthèse vocale de LAMBDA. À
  la place, l'utilisateur entendra la traduction du mot "space". Cela peut
  être soit une ligne vierge, soit une ligne contenant uniquement le mot
  "space".

## Conseils utiles

Ceci est un ensemble de conseils qui vous aideront à utiliser le module
complémentaire plus efficacement.

* Annonce caractère par caractère : Normalement, lorsque vous travaillez sur
  des maths, vous souhaitez que NVDA sonorise ce que vous écrivez caractère
  par caractère. Pour ce faire, il existe quelques étapes faciles :
  Assurez-vous que le focus est sur la fenêtre de LAMBDA ou sur une de ces
  variantes. (La représentation par les six points, par exemple) ; appuyez
  sur NVDA+2 (chiffre 2) ou naviguez jusqu'au menu NVDA > Préférences >
  Paramètres du clavier. Cochez la case Écho clavier par caractère ; allez
  vers LAMBDA > Options > Paramètres vocaux puis veillez à ce que la case
  "écho" est cochée, sinon NVDA ne recevra rien de la synthèse vocale
  lorsque vous écrirez. Ceci fait, Une fois que cela est fait, NVDA dira les
  caractères écrits, mais ne vous inquiétez pas, ce sera seulement dans
  LAMBDA ou ses fenêtres spéciales, les paramètres du reste des applications
  resteront tels quels.

## Liste de discussion du module :

Pour signaler des bogues, faire des suggestions ou contribuer vous pouvez
souscrire au groupe traitant de ce module (en Anglais).  Vous pouvez
souscrire en écrivant à lambda-nvda+subscribe@[plural of google group] dot
com.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=lambda

[2]: https://addons.nvda-project.org/files/get.php?file=lambda-dev
