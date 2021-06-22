# Complemento do NVDA para LAMBDA #

* Autor: Alberto Zanella e o equipo de lambda-nvda.
* Descargar [versión estable][1]
* Descargar [versión en desenvolvemento][2]

Este proxecto é un módulo de aplicación para a aplicación Lambda. foi inspirado polo traballo de Peter Lecky na Comenius University.
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis, acceso lineal ás matemáticas mediante pantallas braille e síntesis de fala) é un programa que axuda ás persoas cegas a eer e escribir matemáticas utilizando unha pantalla braile e/ou un sintetizador de audio.
LAMBDA é o resultado dun proxecto EU. Para máis información acerca de LAMBDA por favor visite [https://www.lambdaproject.org/](https://www.lambdaproject.org/).  
A versión actual deste complemento ten táboas braille só para as linguas
italiana e española pero a súa interface está dispoñible na maioría de
idiomas oficiais do NVDA, debido a que o complemento é traducido pola
comunidade de tradutores do NVDA.
Se é vostede un usuario non italiano de LAMBDA e gostaríalle contribuír con
traducións na súa lingua, síntase libre de contactar ao autor (consulte
embaixo) ou subscribirse á lista de correo do proxecto.

**Nota:** Este complemento foi desenvolvido por Alberto Zanella como unha actividade voluntaria. Nin o autor nin os contribuíntes están relacionados coa venda ou co desenvolvemento do programa LAMBDA. Se quixese obter máis información sobre LAMBDA, reportar problemas ou obter soporte, por favor contacte co seu distribuidor local (en España, ONCE-CIDAT). Se está atopando dificultades usando ou instalando este complemento, por favor contacte co autor ou utilice a liga "Issues" (erros) dispoñible na páxina do proxecto en Github.

### [Repositorio Oficial en GitHub](https://github.com/lambda-nvda/lambdaNvda/)

## Características do complemento:

### Soporte para fala:

* Infórmase dos menús e diálogos correctamente;
* Soporte para fala natural das fórmulas matemáticas utilizando o motor
  interno de LAMBDA (p.ex. "raíz composta 3 de raíz composta 3 x máis 24,
  fin da raíz, menos 3 igual 0");
* lectura por carácter, palabra, liña e Verbalizar Todo implementada;
* Fala cando un bloque de texto está seleccionado ou é estendido
  (utilizando CTRL+B e SHIFT+CTRL+B);
* Fala ao moverse polo texto con comandos de Windows e con comandos
  específicos do Lambda;
* Tanto o modo de fala curto coma o estendido están soportados (pode
  establecelo utilizando o menú Ferramentas de LAMBDA);
* Xanelas de diálogos especiais como a do modo estrutura, a calculadora, e a
  de matriz son agora correctamente reportadas e NVDA le correctamente ao
  mover o cursor por elas ou ao introducir texto;
* O eco de escritura utiliza o procesador de texto de Lambda, de xeito que
  se informará correctamente de símbolos e marcadores.

### Soporte para Braille:

* O complemento instala (dentro do directorio de perfil de usuario) e activa
  un perfil de NVDA cunha táboa braille. Esta táboa pode diferir entre
  distintas linguas. A táboa foi construída dende a presente nos scripts de
  Jaws para LAMBDA (arquivo jbt). Entón os símbolos e marcadores son
  representados mediante os mesmos patróns de puntos;
* O complemento crea un perfil de configuración e establece a configuración
  de braille estándar. De xeito que a saída á táboa braille personalizada só
  está establecida cando LAMBDA está activo;
* Os diálogos e menús son correctamente braillificados;
* O contido do editor é correctamente adaptado para braille e o usuario pode
  moverse usando as teclas de desprazamento braille e de ruta do cursor;
* Comezando na versión do complemento 1.1.0 existen dúas formas nas cales o
  contido é representado: "Modo plano" e "Modo non plano". Cando o "Modo
  plano" está activado, NVDA utilizará o Modelo de Mostrado para obter o
  contido dende Lambda e para determinar a posición do cursor braille. Isto
  é especialmente beneficioso cando o usuario necesita moverse pola
  pantalla, incluso polos espazos en branco do editor. Cando o "Modo plano"
  está estabelecido a "Desactivado", a representación do texto na pantalla
  braille é máis estable, xa que NVDA utiliza Windows API para obtela. De
  xeito que, cando o usuario se move entre espazos en branco o cursor na
  pantalla braille non seguirá ao cursor real ata que un espazo non en
  branco sexa inxerido polo usuario.

O "Modo plano" está activo por defecto. Pode alternar o "Modo plano" entre
activado e desactivado premendo NVDA+SHIFT+F.

Recoméndase encarecidamente deshabilitar o "Modo plano" cando se utilice DPI
personalizado en Windows (opción de Tamano personalizado), e especialmente
cando se ten unha configuración de pantalla de máis de 96 DPI (máis longo
que 100%).

* A estrutura dos cadros de diálogo é máis sinxela, eliminando información
  repetida;
* A selección é marcada correctamente utilizando os puntos 7 e 8, e
  correctamente refrescada ao premer comandos estándar de Windows
  (SHIFT+FRECHAS) ou comandos específicos de Lambda (CTRL+B, CTRL+SHIFT+B).

## Antes de empezar a usar este complemento.

Este complemento crea un perfil de NVDA nomeado como "lambda" que está
asociado coa aplicación lambda.exe. Este perfil está configurado con todas
as opcións no que ás opcións braille, á táboa braille personalizada, á
localización do foco e ás opcións do modo plano se refire.

Se un perfil previamente existente co mesmo nome está presente no seu
sistema, non será sobrescrito e deberá axustar manualmente o perfil de
configuración.

Para saír desta situación, se ten configuracións espcíficas que lle gostaría
preservar, pode utilizar o "Asistente de Reversión do perfil LAMBDA". O
atallo para abrir esta ferramenta é NVDA+alt+r (cando se está dentro de
LAMBDA).

Unha opción fácil é tamén borrar vellas versións do perfil "lambda" despois
da instalación do complemento. Para facer isto, abra o menú de NVDA,
seleccione o elemento de menú "Configuración de perfís" e prema ENTER.

No diálogo de Configuración de perfís, poderá localizar e borrar o perfil
"lambda". O perfil será criado novamente a vindeira vez que se inicie
Lambda.

Eliminar o perfil "lambda" debería de ser unha solución fácil tamén cando
atope algún fallo que "apareza" nalgún punto mentres se utilice o
complemento. Por exemplo, se a táboa braille non está correctamente
estabelecida, no lugar de configurar manualmente o perfil pode simplemente
borralo. O complemento criará un novo a vindeira vez que abra o editor
Lambda.

Cada vez que o editor Lambda é arrincado, o complemento verifica se existe
un perfil co nome "lambda". Se non existe crea automaticamente un perfil coa
seguinte forma:

```
nome de arquivo : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName
```

Onde :

* path-to-the-addon-brailleTable-dir : É a ruta absoluta do directorio do
  complemento + "\brailleTables"
* tableName : Depende do idioma seleccionado. Actualmente as táboas braille
  italiana e española, "lambda-ita.utb" e "lambda-esp.utb" respectivamente,
  están presentes.

## Atallos de Teclado do Complemento:

* **NVDA+Shift+f**: Alterna o modo plano do braille entre activado e
  desactivado;
* **NVDA+alt+r**: Abre o "Asistente de Reversión do Perfil LAMBDA";
* **NVDA+d**: duplicar liñas (úseo en lugar de ctrl+d).

## Erros coñecidos:

Debido a un erro presente no LAMBDA, o complemento proporciona unha lóxica
adicional que informa dos espazos en branco. Esta lóxica pode fallar nas
seguintes situacións:

* Cando palabras coma "space", "spazio", "espacio", etc. son inxeridas no
  texto, éstas poden ser reportadas polo NVDA no idioma do usuario.
* As liñas en blanco non son reportadas polo motor da fala de LAMBDA. O
  usuario oirá a tradución da palabra "espazo" no seu lugar. Isto podería
  ser tanto unha liña en branco coma unha liña contendo soamente a palabra
  "espazo".

## Consellos útiles

Este é un conxunto de consellos que lle axudará a utilizar o complemento dun
xeito máis eficiente.

* Lectura caracter por caracter: normalmente, cando está escribindo
  matemáticas gústalle que NVDA diga aquilo que está escribindo caracter por
  caracter. Para facer isto, hai uns cantos simples pasos: asegúrese de ter
  focalizada a xanela de LAMBDA ou unha das súas variantes (a representación
  en seis puntos, por exemplo); prema NVDA+2 (número dous) ou navegue a menú
  NVDA>Preferencias>Opcións de teclado e marque a casilla para reportar
  caracteres ao escribir; diríxase a LAMBDA>Herramientas>Parámetros de voz
  (Ferramentas>Parámetros de voz) e asegúrese de que a casilla "Eco" está
  marcada, doutro xeito NVDA non recibirá nada do motor da voz mentres
  vostede escribe. E feito, NVDA lerá os caracteres escritos, pero non se
  preocupe, só en LAMBDA, os axustes doutras aplicacións serán deixados como
  estaban.

## Rolda de correo do complemento:

Para reportar erros, suxestións ou se simplemente quere contribuír pode
subscribirse ao Grupo do complemento (en inglés). Pode subscribirse a través
da seguinte páxina web: <https://groups.io/g/lambda-nvda>.

## Rexistro de trocos

Embaixo atópase unha lista de cambios entre as diferentes versións do
complemento. A carón do número de versión, entre parénteses, atópase o
estado de desenvolvemento. A versión actualmente en desenvolvemento non se
inclúe xa que podería haber cambios ata que ésta sexa marcada coma estable
ou descartada coma candidata.

### Versión 1.3.0 (estable)

* Soporte para a última versión do NVDA (Soporte para Python 3)
* Resolto un problema ao premer o comando duplicar liña NVDA+d nunha liña en
  branco que causaba que se pegase o contido do portapapeis. Agora cando
  premas NVDA+d estando nunha liña en branco, aparece unha nova liña en
  branco como se agarda.

### Versión 1.2.2 (estable)

* Mellorada a compatibilidade con WX Python versión 4 (introducido con NVDA
  2018.3). Xa non se mostra a advertencia relativa a wx.newId() no rexistro
  de depuración.
* Implementado guiHelper para mellorar a aparencia dos diálogos.
* Novas linguas. Traducións actualizadas.

### Versión 1.2.1a (estable)

Esta actualización foi concebida coma unha versión con soporte durante largo
tempo. Isto quere dicir que ata, alomenos, xuño do 2018, non está previsto
que se libere unha versión tan estable coma ésta. Facemos isto para
proporcionar aos estudantes máxima estabilidade e para minimizar os trocos
durante o curso académico.

* Novas linguas. Traducións actualizadas.

### Versión 1.2.1 (estable)

* Engadida compatibilidade coa maneira que NVDA 2017.3 utiliza para
  administrar o braille. Compatibilidade con versións antigas mantida.
* arranxadas varias incidencias en relación co braille.

### Versión 1.2.0 (desenvolvemento)

Esta versión non foi publicada coma estable porque a 1.2.1 incluía arranxos
importantes.

* Novas linguas. Traducións actualizadas.

### Versión 1.1.8 (estable)

* Primeira versión estable.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=lambda

[2]: https://addons.nvda-project.org/files/get.php?file=lambda-dev
