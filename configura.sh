#!/bin/bash
#
# Configuracion de interfaces para Raspberry pi
#
# Written by Antonio Acevedo Bañez <acevedo.corona@gmail.com>
# git clone https://github.com/xXcoronaXx/servidor-adhoc.git
echo 'Actualizando apt-get...'
echo 'IMPORTANTE : todos los scripts estan configurados teniendo en cuenta que la direccion de nuestro interfaz eth0 es 192.168.1.115. Si es otra, por favor revisa los archivos configura.sh, setting.py y start.sh. Luego vuelve a empezar la instalacion desde el principio'
sudo apt-get update

echo 'Configurando interfaces'
sudo cp script/interfaces /etc/network/interfaces

sudo ifdown wlan0
sudo ifup wlan0
echo 'Red WiFi up!'
echo 'Instalando y configurando DHCP...'
sudo apt-get install isc-dhcp-server
sudo cp script/dhcpd.conf /etc/dhcp/dhcpd.conf
sudo cp script/isc-dhcp-server /etc/default/isc-dhcp-server

sudo service isc-dhcp-server restart
echo 'DHCP up!'
echo 'Instalando pip y las dependencias del proyecto...'
sudo apt-get install python-pip
sudo pip install -r requeriments.txt 
## NO ESTA INSTALADA LA LIBRERIA GRAFICA ##

echo 'Instalando paquetes para manejar Bluetooth'
sudo apt-get install git-core python-dbus thon-gobject bluez bridge-utils

echo 'Configurando Iptables...'
sudo sysctl net.ipv4.ip_forward=1
sudo iptables -t nat -A PREROUTING -d 192.168.1.115 -p tcp --dport 80 -j DNAT --to-destination 192.168.0.1:80
sudo iptables -t nat -A POSTROUTING -j MASQUERADE

cd ..
git clone https://github.com/ykasidit/ecodroidlink.git
cd ecodroidlink/
sudo ./edl_main &
echo 'Bluetooth up!'