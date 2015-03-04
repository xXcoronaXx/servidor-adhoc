#!/bin/bash
#
# Configura los setting para arrancar los setting en local
#
# Written by Antonio Acevedo Bañez <acevedo.corona@gmail.com>
# git clone https://github.com/xXcoronaXx/servidor-adhoc.git
echo '** Configurando setting para ejecutar servicio e interfaz en local... **'
sudo cp script/setting_servicio_local.py setting.py
sudo cp script/setting_interfaz_local.py interfaz/setting.py
echo 'INFO: Se recomienda el arranque manual del servicio ya que es posible que el tethering no funcione en su sistema.'
echo '** Listo para funcionar en local ! **'