#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# clase proveedora de contenidos a la interfaz

import Pyro4

import time
from datetime import date
#from Models import *


import base64
import serpent

KEY='the_same_string_for_server_and_client'

class ServicioPyro(object):
	"""docstring for ServicioPyro"""
	#variables
	Menus = []
	Ofertas = []
	Items = []
	Online = False
	servicio = 0
	#fin de variables 
	def __init__(self):
		super(ServicioPyro, self).__init__()
		print 'Conectando ...'
		Pyro4.config.HMAC_KEY=KEY
		self.servicio = Pyro4.Proxy('PYRONAME:servidor1.configura')
		self.Online = self.servicio.online()
		print 'Conectado al servicio !'
		self.Menus = serpent.loads(self.servicio.getMenus())
		self.Ofertas = serpent.loads(self.servicio.getOfertas())
		self.Items = serpent.loads(self.servicio.getItems())
	
	def updateMenus(self):
		self.Menus = serpent.loads(self.servicio.getMenus())

	def updateOfertas(self):
		self.Ofertas = serpent.loads(self.servicio.getOfertas())

	def updateItems(self):
		self.Items = serpent.loads(self.servicio.getItems())

	def isOnline(self):
		try:
			self.Online = self.servicio.online()
		except Exception, e:
			self.Online = False
		return self.Online
	def createItem(self,disponible, precio, nombre,descripcion, imagen, primeros_id, segundos_id, postres_id, ofertas_id):
		return self.servicio.createItem(disponible, precio, nombre,descripcion, imagen, primeros_id, segundos_id, postres_id, ofertas_id)