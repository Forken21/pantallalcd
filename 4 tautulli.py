sudo apt-get install transmission-daemon
Configuramos Transmission
 sudo service transmission-daemon stop
 cd /etc
cd transmission-daemon
 sudo nano settings.json


Si miramos dentro de esa carpeta (con el comando «ls») sólo nos encontraremos un archivo «Readme» y un archivo llamado «settings.json». Efectivamente, el archivo que hay que editar es ese último, así que tecleamos esto para editarlo:

sudo nano settings.json
Vamos a cambiar algunas líneas. En primer lugar nos interesa cambiar el directorio al que van a ir las descargas que hagamos. En el tutorial de aMule habíamos creado una carpeta dentro de la carpeta «home» del usuario «pi». La ruta era ésta.

/home/pi/descargas
Esa carpeta la habíamos compartido en la red para poder acceder a ella de forma sencilla, así que vamos a aprovecharla para usarla también como carpeta de descargas del Transmission. Si no habéis seguido ese tutorial, os recomiendo que al menos leáis esa parte para tener todo bien configurado.

Al lío que me estoy yendo por las ramas. Estábamos editando el archivo settings.json para decirle al Transmission que todo lo que descargue lo deje en la carpeta que tenemos compartida. En ese archivo, Buscamos una línea que pone «download-dir» y la cambiamos por la siguiente:

"download-dir": "/home/pi/descargas",
Mucho ojo con los signos de puntuación. No quitéis la coma del final ni ninguna de las comillas.

También vamos a buscar una línea que pone

"incomplete-dir-enabled": false,
Y la cambiamos por esto:

"incomplete-dir-enabled": true,
Ahora haremos algo similar a lo que hicimos en el amule. Vamos a crear un usuario y una contraseña para poder acceder a nuestro Transmission desde otro ordenador, ya sea desde una página web o desde una aplicación propia. Vamos a buscar la línea que empieza por:

"rpc-password": 
y vamos a poner la contraseña con la que queramos acceder al Transmission. Elegid siempre una contraeña segura, que no hayáis usado en otras aplicaciones y que sea lo suficientemente complicada como para ponérselo difícil a quién la quiera averiguar. Yo voy a poner «ElSoftLibreMola1000», pero por favor, vosotros usad una contraseña distinta y segura. Voy a dejar la línea tal que así:

"rpc-password": "ElSoftLibreMola1000",
Un poco más abajo nos pregunta por el nombre de usuario y nos sugiere uno. Vamos a cambiarlo por un usuario o un nick nuestro. Yo voy a poner «ironman» como ejemplo, pero os ruego que pongáis un nombre de usuario diferente (y divertido, por favor).

"rpc-username": "ironman",
Ahora vamos a asignar un puerto para realizar las descargas (algo similar a lo que hicimos con aMule). Transmission por defecto usa el 51413, pero como no nos interesa ir por el puerto estandard (por si nuestro proveedor de internet capa el tráfico en ese puerto) vamos a cambiarlo por otro, por ejemplo el 51228 (pero podéis poner un número cualquiera entre el 49152 y el 65535). Para ello tenemos que buscar la línea que pone:

"peer-port": 51413,
Y cambiarla por esta otra

"peer-port": 51228,
… pero lo dicho: poned un número cualquiera entre ese rango.

Ahora debemos editar una línea más. Transmission por defecto bloquea todas las conexiones de cualquier ordenador que quiera conectarse con su interfaz, salvo que estén en una «lista blanca». A nosotros nos interesa poder acceder desde diferentes IP’s, así que vamos a anular esta configuración. Para ello vamos a buscar esta línea

"rpc-whitelist-enabled": true,
Y la vamos a cambiar por esta otra:

"rpc-whitelist-enabled": false,
Por último vamos a hacer otros dos cambios más. Al igual que pasó con el aMule, nos interesa limitar la velocidad de subida y bajada para no saturar nuestra conexión a internet y para no saturar el procesador de la propia Raspberry. Vamos a limitarla a 1900 Kb/Seg. de bajada y a 900 Kb/Seg. de subida. Habrá a quién le parezca poca velocidad. A mi, con una línea 100/10 me va genial así. Además así dejo el ancho de banda de mi hogar libre para otros menesteres, ya que de nada sirve poner aquí un montón de velocidad, y luego, cuando vayamos a ver un vídeo en una página de streaming, que el vídeo vaya a pedales. Vamos a empezar buscando en el archivo de configuración estas dos líneas:

"speed-limit-down": 100,
"speed-limit-down-enabled": false,
Y vamos a cambiarlas por estas otras:

"speed-limit-down": 1900,
"speed-limit-down-enabled": true,
Ahora vamos a modificar la velocidad de subida. Buscamos estas líneas:

"speed-limit-up": 100,
"speed-limit-up-enabled": false,
Y vamos a cambiarlas por estas otras.

"speed-limit-up": 900,
"speed-limit-up-enabled": true,
Una vez hecho esto, podemos volver a encender el servicio del Transmission con el siguiente comando:

sudo service transmission-daemon start


Acceso por el interfaz web
Ahora ya deberíamos poder acceder a nuestro Transmission así que, desde un navegador de nuestro ordenador, vamos a acceder a la siguiente dirección (cambiad la IP por la de vuestra raspberry):

http://10.0.1.222:9091
