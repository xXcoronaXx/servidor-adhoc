#!/bin/bash
#
# Configura los setting por defecto
#
# Written by Antonio Acevedo Bañez <acevedo.corona@gmail.com>
# git clone https://github.com/xXcoronaXx/servidor-adhoc.git
echo '** Configurando setting por defecto... **'
sudo cp script/setting_servicio_def.py setting.py
sudo cp script/setting_interfaz_def.py interfaz/setting.py
echo '** Listo para funcionar en Raspberry pi suponiendo que la ip del interfaz eth0 es 192.168.1.115 ! **'