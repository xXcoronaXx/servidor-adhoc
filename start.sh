#!/bin/bash
#
# Configuracion de interfaces para Raspberry pi
#
# Written by Antonio Acevedo Bañez <acevedo.corona@gmail.com>
# git clone https://github.com/xXcoronaXx/servidor-adhoc.git
echo '** Arrancando Bluetooth **'
cd ..
cd ecodroidlink/
sudo ./edl_main &
echo '** Arrancando servidor de nombrado... **'
export PYRO_HMAC_KEY='the_same_string_for_server_and_client'
python -m Pyro4.naming --host 192.168.1.115 &
cd 
cd servidor-adhoc/
echo '** Arrancando servicio REST ** '
sudo python service.py &
echo '** Servicio up! **'