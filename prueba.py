#!/usr/bin/python
# -*- coding: utf-8 -*-


import os

def menu():
    os.system('clear')
    print("Selecciona una opcion")
    print("\t1 - primera opcion")
    print("\t2 - segunda opcion")
    print("\t3 - tercera opcion")
    print("\t9 - salir")
    
while True:
    menu()
    opcionMenu = input
    if opcionMenu=="1":
        print("opcion 1")
        input("Has elegido opcion 1... \n pulsa una tecla para continuar")
    
    elif opcionMenu=="2":
        print("opcion 2")
        input("Has elegido opcion 2... \n pulsa una tecla para continuar")
        
    elif opcionMenu=="3":
        print("opcion 3")
        input("Has elegido opcion 3... \n pulsa una tecla para continuar")
    
    elif opcionMenu=="9":
        break
    
    else:
        print("")
        input("No has pulsado ninguna opcion correcta")
