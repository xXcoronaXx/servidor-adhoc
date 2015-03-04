#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Configuracion Pyro4
DATABASE = 'ws.db'
OBJETO_PYRO = 'servidor1.configura'
DIRECCION_PYRO = '192.168.1.115'				# en nuestro caso la direccion del objeto y del servidor de nombrado será el mismo ya que estan en la misma maquina
DIRECCION_PYRO_LOCAL = '192.168.1.115'
KEY = 'the_same_string_for_server_and_client'


# Configuracion WS
WEBPATH = '/ws'
PROTOCOL = 'restjson'
DIRECCION_WS = '192.168.0.1'
PUERTO_WS = 80