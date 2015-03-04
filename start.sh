#!/bin/bash
#
# Arranca el servivio en Raspberry pi
#
# Written by Antonio Acevedo Bañez <acevedo.corona@gmail.com>
# git clone https://github.com/xXcoronaXx/servidor-adhoc.git
echo '** Arrancando Bluetooth **'
cd ..
cd ecodroidlink/
sudo ./edl_main &
sleep 4
echo '** Arrancando servidor de nombrado... **'
export PYRO_HMAC_KEY='the_same_string_for_server_and_client'
python -m Pyro4.naming --host 192.168.1.115 &
sleep 2
cd ..
cd servidor-adhoc/
echo '** Arrancando servicio REST ** '
sudo python service.py &
sleep 4
echo '** Configurando Iptables... **'
sudo sysctl net.ipv4.ip_forward=1
sudo iptables -t nat -A PREROUTING -d 192.168.1.115 -p tcp --dport 80 -j DNAT --to-destination 192.168.0.1:80
sudo iptables -t nat -A POSTROUTING -j MASQUERADE
echo '** Servicio up! **'