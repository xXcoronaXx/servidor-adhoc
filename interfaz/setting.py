#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Configuracion Pyro4 Cliente

# variables globales para conectarse con el servidor
OBJETO_PYRO = 'servidor1.configura'					# nombre del objeto que buscamos
DIRECCION_PYRO = '@localhost'						# direccion del servidor de nombrado el @ es importante
PROXY_PYRO = 'PYRONAME:'+OBJETO_PYRO+DIRECCION_PYRO
KEY='the_same_string_for_server_and_client'