#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# clase proveedora de contenidos a la interfaz

import Pyro4

import time
from datetime import date
#from Models import *


import base64
import serpent

# variables globales para conectarse con el cliente
OBJETO_PYRO = 'servidor1.configura'					# nombre del objeto que buscamos
DIRECCION_PYRO = '@localhost'						# direccion del servidor de nombrado el @ es importante
PROXY_PYRO = 'PYRONAME:'+OBJETO_PYRO+DIRECCION_PYRO
KEY = 'the_same_string_for_server_and_client'

class ServicioPyro(object):
	"""docstring for ServicioPyro"""
	def __init__(self, direccion=DIRECCION_PYRO, objeto=OBJETO_PYRO, key=KEY):
		super(ServicioPyro, self).__init__()
		#variables
		self.Menus = []
		self.Ofertas = []
		self.Items = []
		self.Online = False
		self.servicio = 0
		self.dir = direccion
		self.key = key
		#fin de variables
		try:
			print 'Conectando ...'
			#Pyro4.config.HMAC_KEY=key
			#Pyro4.Daemon._pyroHmacKey = key
			#Pyro4.Proxy._pyroHmacKey = key
			self.servicio = Pyro4.Proxy(Pyro4.resolve('PYRONAME:'+objeto+direccion,hmac_key=key))
			self.Online = self.servicio.online()
			self.servicioActual = objeto
			print 'Conectado al servicio !'
			self.Menus = serpent.loads(self.servicio.getMenus())
			self.Ofertas = serpent.loads(self.servicio.getOfertas())
			self.Items = serpent.loads(self.servicio.getItems())
		except Exception, e:
			print e
			self.servicioActual = 'Desconectado'
			pass 	# para que cree el objeto vacio si no encuentra el servicio

	def reconectar(self, direccion, objeto, key):
		try:
			print 'Conectando ...'
			Pyro4.config.HMAC_KEY=key
			self.servicio = Pyro4.Proxy(Pyro4.resolve('PYRONAME:'+objeto+direccion,hmac_key=key))
			self.Online = self.servicio.online()
			self.servicioActual = objeto
			self.dir = direccion
			self.key = key
			print 'Conectado al servicio !'
			self.Menus = serpent.loads(self.servicio.getMenus())
			self.Ofertas = serpent.loads(self.servicio.getOfertas())
			self.Items = serpent.loads(self.servicio.getItems())
			return True
		except Exception, e:
			self.servicioActual = 'Desconectado'
			return False
	
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

	def delItem(self,item):
		return self.servicio.delItem(item)

	def updateItem(self, nomAnt, disponible, precio, nombre, descripcion, imagen):
		return self.servicio.updateItem(nomAnt, disponible, precio, nombre, descripcion, imagen)

	def createMenu(self,disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen):
		fecha_ini = fecha_ini.replace('-','/')
		fecha_fin = fecha_fin.replace('-','/')
		return self.servicio.createMenu(disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen)
	
	def addItemMenuP(self, items, menu):
		for item in items:
			if not self.servicio.addItemMenuP(item, menu):
				#self.servicio.delMenu(menu)
				return False
		return True

	def addItemMenuS(self, items, menu):
		for item in items:
			if not self.servicio.addItemMenuS(item, menu):
				#self.servicio.delMenu(menu)
				return False
		return True

	def addItemMenuD(self, items, menu):
		for item in items:
			if not self.servicio.addItemMenuD(item, menu):
				#self.servicio.delMenu(menu)
				return False
		return True

	def delMenu(self, menu):
		return self.servicio.delMenu(menu)

	def updateMenu(self, disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen):
		fecha_ini = fecha_ini.replace('-','/')
		fecha_fin = fecha_fin.replace('-','/')
		return self.servicio.updateMenu(disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen)

	def delItemMenuP(self, items, menu):
		for item in items:
			if not self.servicio.delItemMenuP(item, menu):
				return False
		return True

	def delItemMenuS(self, items, menu):
		for item in items:
			if not self.servicio.delItemMenuS(item, menu):
				return False
		return True

	def delItemMenuD(self, items, menu):
		for item in items:
			if not self.servicio.delItemMenuD(item, menu):
				return False
		return True

	def createOferta(self, disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen):
		fecha_ini = fecha_ini.replace('-','/')
		fecha_fin = fecha_fin.replace('-','/')
		return	self.servicio.createOferta(disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen)

	def updateOferta(self, disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen):
		fecha_ini = fecha_ini.replace('-','/')
		fecha_fin = fecha_fin.replace('-','/')
		return 	self.servicio.updateOferta(disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen)

	def delOferta(self, oferta):
		return self.servicio.delOferta(oferta)

	def delItemOferta(self, items, oferta):
		for item in items:
			if not self.servicio.delItemMenuD(item, oferta):
				return False
		return True

	def addItemOferta(self, items, oferta):
		for item in items:
			if not self.servicio.addItemOferta(item, oferta):
				return False
		return True

	def getMenu(self, menu):
		return serpent.loads(self.servicio.getMenu(menu))

	def getOferta(self, oferta):
		return serpent.loads(self.servicio.getOferta(oferta))