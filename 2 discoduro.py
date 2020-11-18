#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time


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
    print("\t3 - Instalar Tautulli")
    print("\t4 - Instalar Plex")
    print("\t5 - Instalador AUTOMATICO (Plex, Octoprint, Tautulli, Transmission")
    print("\t6 - Atras")
    print("\t7 - Salir")
    print("")


    while True:
    menudiscoduro()
    opcionMenu = input("    Inserte el numero de la opcion: ")

    if opcionMenu == 1 :
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

     if opcionMenu == 2 :
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