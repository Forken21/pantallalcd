#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import requests


tiempo = requests.get('https://wttr.in/San_Fernando,Spain?format="%l:+%c+%t+%m+Viento+%w"\n')

def menu():
    os.system('clear')
    print("")
    print('El tiempo que hace hoy es...'+tiempo.text)
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
    print("\t6 - Reiniciar")
    print("\t0 - Salir")
    print("")

while True:
    menu()
    opcionMenu = input("    Inserte el numero de la opcion: ")

    if opcionMenu == 1 :
        print("")
        #os.system('sudo git clone https://github.com/Forken21/pantallalcd/blob/main/menuLCD')
        print("...Bajando archivos necesarios")
        os.system('sudo python menuLCD.py')
    
    elif opcionMenu == 0 :
        break

    else:
        input("No has elegido ninguna opcion")