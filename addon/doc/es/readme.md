# Complemento de Lambda para NVDA

lambda-nvda ha sido escrito por alberto Zanella.

Puede encontrar más información sobre este complemento en: https://github.com/albzan/lambda-nvda.


Este proyecto es un módulo de aplicación para el software Lambda. Ha sido inspirado por el trabajo de Peter Lecky en la Comenius University.
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis, acceso lineal a las matemáticas mediante pantallas braille y síntesis de audio) es un programa que ayuda a las personas ciegas a leer y escribir matemáticas usando una pantalla braile y/o un sintetizador de audio.
LAMBDA es el resultado de un proyecto EU. Para más información acerca de LAMBDA por favor visite [http://www.lambdaproject.org/](http://www.lambdaproject.org/).  
La versión actual de este complemento tiene tablas braille solo para los idiomas italiano y español pero su interfaz está disponible tanto en el idioma italiano como en español, inglés y gallego ahora mismo.
Si es usted un usuario no italiano de LAMBDA y le gustaría contribuír con traducciones en su idioma, siéntase libre de contactar al autor (consulte más abajo) o bifurcar este proyecto.

**Nota:** Este complemento ha sido desarrollado por Alberto Zanella como una actividad voluntaria. Ni el autor ni los contribuyentes están relacionados con la venta o el desarrollo del programa LAMBDA. si quisiera obtener más información sobre LAMBDA, reportar problemas u obtener soporte, por favor contacte con su distribuidor local (en España, ONCE-CIDAT). Si está encontrando dificultades usando o instalando este complemento, por favor contacte con el autor o use el enlace "Issues" (errores) disponible en la página del proyecto en Github.

## Demostración en audio

Si desea oír este complemento en acción le recomendamos escuchar la audiodemostración realizada por Salva Doménech para la lista "LAMBDA with NVDA", en el siguiente enlace: [https://drive.google.com/file/d/0B8k1H5BNRE0BY2JQNjRlVWFtV2s/view?usp=sharing] Esta demostración cubre la instalación del complemento, la escritura y verbalización de las acciones más frecuentes en LAMBDA y la explicación del soporte Braille, aún en desarrollo para el idioma español.

## Características del complemento

### Soporte para habla:

* Se informa de los menús y diálogos correctamente;
* Soporte para habla natural de las fórmulas matemáticas usando el motor interno de LAMBDA (p.ej. "raíz compuesta 3 de raíz compuesta 3 x más 24, fin de raíz, menos 3 igual 0");
* Lectura por carácter, palabra, línea y Verbalizar Todo implementada.
* Habla cuando un bloque de texto está seleccionado o es extendido  (usando CTRL+B y SHIFT+CTRL+B);
* Habla al moverse por el texto con comandos de Windows y con comandos específicos de Lambda;
* Tanto el modo de habla corto como el extendido están soportados (puede establecerlo usando el menú Herramientas de LAMBDA);
* Ventanas de diálogos especiales como la del modo estructura, la calculadora, y la de matriz son ahora correctamente reportadas y NVDA lee correctamente al mover el cursor por ellas o al introducir texto;
* El eco de escritura utiliza el procesador de texto de Lambda, de forma que se informará correctamente símbolos y marcadores serán.

### Soporte para Braille:

*El complemento instala (dentro del directorio de perfil de usuario) y activa un perfil de NVDA con una tabla braille. Esta tabla puede diferir en distintos idiomas. La tabla ha sido construida desde la presente en elos scripts de Jaws para LAMBDA (archivo jbt). entonces los símbolos y marcadores son representados mediante los mismos patrones de puntos;
* El complemento crea un perfil de configuración y establece la configuración de braille estándar. De forma que la salida a la tabla braille personalizada solo está establecida cuando LAMBDA está activo;
* Los diálogos y menús son correctamente braillificados;
* El contenido del editor es correctamente adaptado para braille y el usuario puede moverse usando las teclas de desplazamiento braille y de ruta del cursor;
* empezando desde la versión del complemento 1.1.0 existen dos formas en las cuales el contenido es representado: "Modo plano" and "Modo no plano". Cuando el "Modo plano" está activado, NVDA usará el Modelo de Mostrado para obtener el contenido desde Lambda y para determinar la posición del cursor braille. Esto es especialmente beneficioso cuando el usuario necesita moverse por la pantalla, incluso por los espacios en blanco del editor. Cuando el "Modo plano" está establecido a "Desactivado", la representación del texto en la pantalla braille es más estable, ya que NVDA usa Windows API para obtenerla. De modo que, cuando el usuario se mueve entre espacios en blanco el cursor en la pantalla braille no seguirá al cursor real hasta que un espacio no en blanco sea insertado por el usuario. 

El "Modo plano" está activo por defecto. Puede alternar el "Modo plano" entre activado y desactivado pulsando NVDA+SHIFT+F.

Se recomienda vivamente deshabilitar el "Modo plano" cuando se use DPI personalizado en Windows (opción de Tamaño personalizado), eespecialmente cuando se tiene una configuración de pantalla de más de 96 DPI (más largo que 100%).
* La estructura de los cuadros de diálogo es más sencilla, eliminando información repetida;
* La selección es marcada correctamente usando los puntos 7 y 8, y correctamente refrescada al presionar comandos estándar de Windows (SHIFT+FLECHAS) o comandos específicos de Lambda (CTRL+B, CTRL+SHIFT+B).

## Antes de empezar a usar este complemento.
Este complemento crea un perfil de NVDA nombrado como "lambda" que está asociado con la aplicación lambda.exe. Este perfil está configurado con todas las opciones en lo que a las opcioens braille, a la tabla braille personalizada, a la localización del foco y a las opciones del modo plano se refiere.


Si un perfil previamente existente con el mismo nombre está presente en su sistema, no será sobreescrito y deberá ajustar manualmente el perfil de configuración.

Para salir de esta situación, si tiene configuraciones espcíficas que le gustaría preservar, puede usar el "Asistente de Reversión del perfil LAMBDA". La tecla rápida para abrir esta herramienta es NVDA+alt+r (cuando se está dentro de LAMBDA).

Una opción fácil es también borrar viejas versiones del perfil "lambda" después de la instalación del complemento. Para hacer esto, abra el menú de NVDA, seleccione el elemento de menú "Perfiles de configuración" y pulse ENTER.

En el diálogo de Perfiles de configuración, podrá localizar y borrar el perfil "lambda". El perfil será creado nuevamente la próxima vez que se inicie Lambda.

Eliminar el perfil "lambda" debería de ser una solución fácil también cuando encuentre algún fallo que "aparezca" en algún punto mientras se use el complemento. Por ejemplo, si la tabla braille no está correctamente establecida, en lugar de configurar manualmente el perfil puede simplemente borrarlo. El complemento creará uno nuevo la próxima vez que abra el editor Lambda.

Cada vez que el editor Lambda es arrancado, el complemento verifica si existe un perfil con el nombre "lambda". Si no existe crea automáticamente un perfil con la siguiente forma:

```
Nombre del fichero: userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

 ```

Where :
* path-to-the-addon-brailleTable-dir : Es la ruta absoluta del directorio del complemento + "\brailleTables"
* tableName : Depende del idioma seleccionado. Actualmente las tablas braille italiana y española, "lambda-ita.utb" y "lambda-esp.utb" respectivamente, está presente.

## Teclas Rápidas del Complemento

* **NVDA+Shift+f**: Alterna el modo plano de braille entre activado y desactivado;
* **NVDA+alt+r**: Abre el "Asistente de Reversión del Perfil LAMBDA".



