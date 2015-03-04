#!/bin/bash
#
# Set server like a service
#
# Written by Antonio Acevedo Bañez <acevedo.corona@gmail.com>
# git clone https://github.com/xXcoronaXx/servidor-adhoc.git
sudo cp script/adhoc.conf /etc/init/
echo 'You should then be able to run the script by typing sudo start adhoc, and kill it with sudo stop adhoc'