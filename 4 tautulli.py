print("")
print("INSTALACION TRANSMISSION")
time.sleep(3)
print("...Bajando archivos necesario e instalando...")
os.system('sudo apt-get install transmission-daemon')
print("Configuramos Transmission")
os.system('sudo service transmission-daemon stop')
os.system('cd /etc')
os.system('cd transmission-daemon')
print("  VAMOS A CONFIGURAR EL ARCHIVO SETTING.JSON ")
print(" Este proceso se tiene que hacer manual, asi que se explica todo con el mayor detalle posible")
time.sleep(1)
print(" Se cambiaran algunas lineas:   ")
time.sleep(1)
print("...Emepezamos...")
time.sleep(1)
print(" 1.-Indicar la carpeta que esta puesta en RED para las descargas de archivos. Para esto vamos a cambiar la siguiente linea:  ")
time.sleep(1)
print('	- "download-dir": "/mnt/usb/descargas" (¡¡¡OJO!!! CON LOS SIGNOS DE PUNTUACION!!) ')
time.sleep(3)
print(" 2.- Buscamos otra linea y cambiamos:  ")
time.sleep(1)
print('     - "incomplete-dir-enabled": false," y lo cambiamos por ""incomplete-dir-enabled": false, ')
time.sleep(3)
print(" 3.- Lo siguiente sería ponerle contraseña, para acceder a Transmission.")
time.sleep(1)
print("     Buscamos la siguiente linea y le añadimos la contraseña")
time.sleep(1)
print('     - "rpc-password":   y la cambiamos de la siguiente forma "rpc-password": "MiContraseña", ')
time.sleep(3)
print(" 4.- Un poco mas abajo nos pregunta por el nombre de usuario, nos sugiere uno... lo cambiamos a nuestro gusto")
time.sleep(1)
print('     "rpc-username": "ironman", ')
time.sleep(3)
print(" 5.- Ahora vamos a modificar el puerto, sería conveniente modificar el mismo puerto en el router, para tenerlo abierto")
time.sleep(1)
print('     - "peer-port": 51413,  y modificamos el puerto al que mas nos interese.')
time.sleep(3)
print(" 6.- Ahora debemos editar una línea más. Transmission por defecto bloquea todas las conexiones de cualquier ordenador que quiera conectarse con su interfaz, salvo que estén en una «lista blanca». A nosotros nos interesa poder acceder desde diferentes IP’s, así que vamos a anular esta configuración. Para ello vamos a buscar esta línea")
print('     - "rpc-whitelist-enabled": true, Y la vamos a cambiar por esta otra: "rpc-whitelist-enabled": false, ')
time.sleep(3)
print("")
time.sleep(1)
print("Habríamos terminado ya la instalacion de Transmission, solo nos toca guardar el archivo modificado y encender Transmmision")
time.sleep(1)
print("Vamos a modificar el archivo")
time.sleep(1)
print(" Espero que hayan apuntado todo, sino... te toca leer este tocho otra vez")
time.sleep(1)
print("Pulsa ENTER para continuar...")
input()
print("")
time.sleep(1)
print("...Abrimos el archivo para modificarlo...")
os.system('sudo nano settings.json')
print("YA LO HEMOS MODIFICADO!!")
time.sleep(1)
print("Ahora vamos a encender Transmission")
os.system('sudo service transmission-daemon start')
print("")
time.sleep(1)
print("LISTO!!!, ya puedes utilizarlo entrando en el navegador en:")
time.sleep(1)
print("La direccion es: ","http://", ip,":9091")
time.sleep(5)
print("...Pusla ENTER para volver al Menu...")
input()
principal()