#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

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