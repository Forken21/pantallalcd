#!/usr/bin/python
# -*- coding: utf-8 .*-

import os
import time

def menu():
    os.system('clear')
    #https://github.com/chubin/wttr.in
    os.system('curl wttr.in/San_Fernando,España?format="%l:+%c+%t+%m+Viento+%w\n"')
    #print(\n,output)