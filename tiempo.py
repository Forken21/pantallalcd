#!/usr/bin/python
# -*- coding: utf-8 .*-

import os
import time
import requests

tiempo = requests.get('https://wttr.in/San_Fernando,Spain?format="%l:+%c+%t+%m+Viento+%w"\n')
print('El tiempo que hace hoy es...'+tiempo.text)