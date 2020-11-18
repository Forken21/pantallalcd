import os
import time
import requests

menu = "Introduzca opcion: "
tiempo = requests.get('https://wttr.in/San_Fernando,Spain?format="%l:+%c+%t+%m+Viento+%w"\n')

def principal():
    os.system('clear')
    print("")
    print("")
    print("El tiempo que hace ahora...:"+tiempo.text)
    print("")
    print("--------------------------------")
    print("         MENU PRINCIPAL         ")
    print("--------------------------------")
    print("")
    print("     Selecciona una opcion:")
    print("\t1 - Menu LCD")
    print("\t2 - Menu Disco Duro")
    print("\t3 - Menu Plex")
    print("\t4 - Menu Tautulli")
    print("\t5 - Menu Transmission")
    print("\t6 - Actualizar Sistema")
    print("\t7 - Reiniciar")
    print("\t0 - Salir")
    print("")
   
    set_menu = int(input(menu))
    if set_menu == 1:
        menulcd()
    elif set_menu ==2:
        menudiscoduro()
    elif set_menu == 3:
        menuplex()
    elif set_menu == 4:
        menutautulli()
    elif set_menu == 5:
        menutransmission()
    elif set_menu == 6:
        actualizacion()
    elif set_menu == 7:
        reinicio()
    elif set_menu == 0:
        return
    else:
        print("no has elegido ninguna opcion")
        principal()
   
def menulcd():
    os.system('clear')
    print
    print("")
    print("--------------------------------")
    print("         MENU INSTALACION       ")
    print("--------------------------------")
    print("")
    print("     Selecciona una opcion:")
    print("\t1 - Actualizar sistema")
    print("\t2 - Instalacion AUTOMATICA LCD (Se Reiniciará)")
    print("\t3 - Instalador LCD (Sin reinicio)")
    print("\t4 - Instalador Driver LCD (Sin reinicio)")
    print("\t5 - Cambiar de LCD a HDMI")
    print("\t6 - Cambiar de HDMI a LCD")
    print("\t7 - Instalar TouchUI (Automatico)")
    print("\t8 - Reinstalar TouchUI <<<EN CONSTRUCCION>>>")
    print("\t9 - Instalar OctoDash")
    print("\t10 - Actualizar OctoDash")
    print("\t11 - Reiniciar")
    print("\t0 - Salir")
    print("")

    set_menu = int(input(menu))
    if set_menu == 1:
        print("")
        print("ACTUALIAZACION DEL SISTEMA")
        os.system('sudo apt-get update -y')
        time.sleep(3)
        os.system('sudo apt-get upgrade -y')
        time.sleep(3)
        print("")
        print("...actualizacion completada...")
        print("Pulsa ENTER para continuar...")
        input()
        time.sleep(5)
        menulcd()

    elif set_menu ==2:
        print("")   
        print("INSTALACION AUTOMATICA LCD")
        print(" ---> Se Reiniciará <---  ")
        print("" "")
        os.system('cd ~')
        time.sleep(3)
        print("Bajando archivos...")
        os.system('wget http://kedei.net/IMG/v6_1/LCD_show_v6_1_3.tar.gz')
        time.sleep(3)
        print("...Descomprimiendo archivos...")
        os.system('tar xzvf LCD_show_v6_1_3.tar.gz')
        time.sleep(3)
        print("...abriendo carpeta...")
        os.system('cd LCD_show_v6_1_3')
        time.sleep(3)
        print("...ejecutando LCD_show_v6_1_3")
        os.system('./LCD35_v')
        time.sleep(5)
        print("Empezamos con el Driver")
        print("...bajando driver...")
        os.system('cd ~')
        os.system('wget https://sourceforge.net/projects/wavetech/files/lcd.tar.gz')
        time.sleep(3)
        print("...descomprimiendo...")
        os.system('tar -xf lcd.tar.gz')
        time.sleep(3)
        print("")
        print("+--------------------------------------+")
        print("|          INSTALANDO LOS DRIVER       |")
        print("+--------------------------------------+")
        print("")
        time.sleep(5)
        print("...actualizando Kernel...")
        os.system('sudo cp ./lcd_files/kernel.img /boot/kernel.img')
        os.system('sudo cp ./lcd_files/kernel7.img /boot/')
        os.system('sudo cp ./lcd_files/*.dtb /boot/')
        os.system('sudo cp ./lcd_files/overlays/*.dtb* /boot/overlays/')
        time.sleep(3)
        print("...subiendo modulos kernel...")
        os.system('sudo cp -rf ./lcd_files/lib/* /lib/')
        os.system('sudo rm /boot/bcm2710-rpi-3-b-plus.dtb')
        time.sleep(3)
        print("...desabilitando actualizacion del kernel...")
        os.system('sudo apt-mark hold raspberrypi-kernel')
        print("--> INSTALACION COMPLETADA <--")
        time.sleep(3)
        print("...REINICIANDO...")
        time.sleep(5)
        os.system('sudo reboot')
        menulcd()
    
    elif set_menu == 3:
        print("")
        print("   INSTALACION LCD    ")
        print("---> Sin reinicio <---")
        print("")
        time.sleep(3)
        print("Bajando archivos...")
        os.system('cd~')
        os.system('wget http://kedei.net/IMG/v6_1/LCD_show_v6_1_3.tar.gz')
        time.sleep(3)
        print("...Descomprimiendo archivos...")
        os.system('tar xzvf LCD_show_v6_1_3.tar.gz')
        time.sleep(3)
        print("...abriendo carpeta...")
        os.system('cd LCD_show_v6_1_3')
        time.sleep(3)
        print("...ejecutando LCD_show_v6_1_3")
        os.system('LCD_show_v6_1_3/./LCD35_v')
        time.sleep(3)
        print("--> INSTALACION COMPLETADA <---")
        print("Se debe reiniciar para que los cambios tengan efectos.")
        print("Pulsa ENTER para continuar...")
        input()
        menulcd()

    elif set_menu == 4:
        print("")
        print("   INSTALACION DRIVE    ")
        print("---> Sin reinicio <---  ")
        print("")
        time.sleep(3)
        print("...actualizando Kernel...")
        os.system('sudo cp ./lcd_files/kernel.img /boot/kernel.img')
        os.system('sudo cp ./lcd_files/kernel7.img /boot/')
        os.system('sudo cp ./lcd_files/*.dtb /boot/')
        os.system('sudo cp ./lcd_files/overlays/*.dtb* /boot/overlays/')
        time.sleep(3)
        print("...subiendo modulos kernel...")
        os.system('sudo cp -rf ./lcd_files/lib/* /lib/')
        os.system('sudo rm /boot/bcm2710-rpi-3-b-plus.dtb')
        time.sleep(3)
        print("...desabilitando actualizacion del kernel...")
        os.system('sudo apt-mark hold raspberrypi-kernel')
        time.sleep(3)
        print("--> INSTALACION COMPLETADA <--")
        print("PARA QUE LOS CAMBIOS TENGAN EFECTOS, SE DEBE REINICIAR")
        input()
        menulcd()

    elif set_menu == 5:
        print("")
        print(" DE LCD A HDMI")
        print("Se debe reiniciar para que los cambios surtan efectos")
        print("")
        time.sleep(3)
        print("...abriendo carpeta...")
        os.system('cd ~')
        os.system('cd LCD_show_v6_1_3')
        time.sleep(3)
        print("...ejecutando LCD_show_v6_1_3")
        os.system('./LCD_dhmi')
        time.sleep(3)
        print("--> INSTALACION COMPLETADA <--")
        print("Pulsa ENTER para continuar...")
        input()
        menulcd()

    elif set_menu == 6:
        print("")
        print(" DE HDMI A LCD")
        print("Se debe reiniciar para que los cambios surtan efectos.")
        print("")
        time.sleep(3)
        print("...abriendo carpeta LCD_show_v6_1_3...")
        os.system('cd ~')
        os.system('cd LCD_show_v6_1_3')
        time.sleep(3)
        os.system('./LCD35_v')
        print("--> INSTALACION COMPLETADA <--")
        print("Pulsa ENTER para continuar...")
        input()
        menulcd()

    elif set_menu == 7:
        print("")
        print(" INSTALACION DEL TOUCHUI ")
        print("Se debe continuar para que los cambios surtan efectos...")
        os.system('cd ~')
        os.system('git clone https://github.com/BillyBlaze/OctoPrint-TouchUI-autostart.git ~/TouchUI-autostart/')
        os.system('sudo ~/TouchUI-autostart/helpers/install')
        print("--> INSTALACION COMPLETADA <--")
        print("Pulsa ENTER para continuar...")
        input()
        menulcd()

    elif set_menu == 8:
        print("")
        print(" EN PROCESO DE CONSTRUCCION ")
        #print("--> INSTALACION COMPLETADA <--")
        print("Pulsa ENTER para continuar...")
        input()
        menulcd()

    elif set_menu == 9:
        print("")
        print(" INSTALACION DE OCTODASH")
        print("Se debe continuar para que los cambios surtan efectos.")
        print("")
        os.system('cd ~')
        os.system('bash <(wget -qO- https://github.com/UnchartedBull/OctoDash/raw/master/scripts/install.sh)')
        time.sleep(3)
        print("--> INSTALACION COMPLETADA <--")
        print("Pulsa ENTER para continuar...")
        input()
        menulcd()

    elif set_menu == 10:
        print("")
        print(" ACTUALIAZACION DE OCTODASH")
        print("Se debe continuar para que los cambios surtan efectos.")
        print("")
        os.system('cd ~')
        os.system('wget -qO- https://github.com/UnchartedBull/OctoDash/raw/master/scripts/update.sh | bash')
        time.sleep(3)
        print("--> INSTALACION COMPLETADA <--")
        print("Pulsa ENTER para continuar...")
        input()
        menulcd()

    elif set_menu == 11:
        print("REINICIANDO")
        time.sleep(5)
        os.system('sudo reboot')

    elif set_menu == 0:
        return
    
    else:
        print("No has elegido ninguna opcion")
        principal()
        
def menudiscoduro():
    os.system('clear')
    print
    print("")
    print("--------------------------------")
    print("        MENU DISCO DURO         ")
    print("--------------------------------")
    print("")
    print("     Selecciona una opcion:")
    print("\t1 - Formatear Disco Duro")
    print("\t2 - Montando Disco Duro")
    print("\t3 - Atras")
    print("\t0 - Salir")
    print("")

    set_menu = int(input(menu))
    if set_menu == 1:
        print("")
        print("FORMATEAR DISCO DURO A EXT4")
        print("...Se llamará: >> unidadusb <<")
        os.system('sudo mkfs.ext4 /dev/sda1 -L unidadusb')
        time.sleep(3)
        print("...montando Disco Duro...")
        os.system('cd /mnt')
        os.system('sudo mkdir unidadusb')
        os.system('sudo mount /dev/sda1 /mnt/unidadusb')
        print("...FORMATEO TERMINADO")
        print("Pulsa ENTER para continuar...")
        input()
        time.sleep(5)
        menudiscoduro()

    elif set_menu ==2:
        print("")
        print("MONTANDO DISCO DURO")
        print("...montando Disco Duro...")
        os.system('cd /mnt')
        os.system('sudo mkdir unidadusb')
        os.system('sudo mount /dev/sda1 /mnt/unidadusb')
        print("...MONTADO TERMINADO")
        print("Pulsa ENTER para continuar...")
        input()
        time.sleep(5)
        menudiscoduro()

    elif set_menu == 3:
        principal()
    
    elif set_menu == 0:
        return

    else:
        print("no has elegido ninguna opcion")
        principal()

def menuplex():
    os.system('clear')
    print
    print("")
    print("--------------------------------")
    print("           MENU PLEX            ")
    print("--------------------------------")
    print("")
    print("     Selecciona una opcion:")
    print("\t1 - Instalar Plex")
    print("\t2 - Atras")
    print("\t0 - Salir")
    print("")

    if set_menu == 1:
        print("")
        print ("INSTALACION PLEX")
        time.sleep(2)
        print("...Añadimos el repositorio...")
        os.system('echo deb https://downloads.plex.tv/repo/deb public main | sudo tee /etc/apt/sources.list.d/plexmediaserver.list')
        time.sleep(1)
        print("...Añadiendo firmas del repositorio")
        os.system('curl https://downloads.plex.tv/plex-keys/PlexSign.key | sudo apt-key add')
        time.sleep(3)
        print("...Actualizando...")
        os.system('sudo apt-get update -y')
        time.sleep(2)
        os.system('sudo apt-get dist-upgrade')
        time.sleep(2)
        print("...Instalando Plex...")
        os.system('sudo apt-get install plexmediaserver -n') #-n puesto provisional
        time.sleep(2)
        print("INSTALACION COMPLETADA")
        print("Pulsa ENTER para continuar...")
        input()
        time.sleep(5)
        menuplex()

    elif set_menu == 2:
        principal()
    
    elif set_menu == 0:
        return

    else:
        print("no has elegido ninguna opcion")
        principal() 
       
principal()