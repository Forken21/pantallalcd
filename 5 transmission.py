#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time


def menuprog():
    os.system('clear')
    print
    print("")
    print("--------------------------------")
    print("   MENU INSTALACION PROGRAMAS   ")
    print("--------------------------------")
    print("")
    print("     Selecciona una opcion:")
    print("\t1 - Instalar Transmission")
    print("\t2 - Instalar Octoprint")
    print("\t3 - Instalar Tautulli")
    print("\t4 - Instalar Plex")
    print("\t5 - Instalador AUTOMATICO (Plex, Octoprint, Tautulli, Transmission")
    print("\t6 - Atras")
    print("\t7 - Salir")
    print("")


while True:
    menuprog()
    opcionMenu = input("    Inserte el numero de la opcion: ")

    if opcionMenu == 1 :
        print("")
        print("INSTALACION TRANSMISSION")
        os.system('sudo apt-get update -y')
        time.sleep(3)
        os.system('sudo apt-get upgrade -y')
        time.sleep(3)
        print("")
        print("...actualizacion completada...")
        print("Pulsa ENTER para continuar...")
        input()
        time.sleep(5)