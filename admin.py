#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import Pyro4
import threading

import bottle

import time
from datetime import date

import base64
import serpent

from Models import *
from peewee import *

from setting import *
from webservice import *

class ControladorPyro(object):
	"""docstring for ControladorPyro"""
	# crea item
	def createItem(self,disponible, precio, nombre,descripcion, imagen, primeros_id, segundos_id, postres_id, ofertas_id):
		try:
			print 'Crear Item'
			if nombre == '':
				raise Exception("No se puede crear un item sin nombre")
			try:
				# si el item existe no se crea
				i = Item_db.select().where(Item_db.nombre==nombre).get()
				return False
			except Exception, e:
				# si no existe se captura la excepcion y se crea
				nuevoItem = Item_db(disponible=disponible, precio=precio, nombre=nombre,descripcion=descripcion, imagen=imagen, primeros=primeros_id, segundos=segundos_id, postres=postres_id, ofertas=ofertas_id)
				nuevoItem.save()
				return True
		except Exception, e:
			return False

	# update item
	def updateItem(self, nomAnt, disponible, precio, nombre, descripcion, imagen):
		try:
			print 'Update Item'
			items = Item_db.update(disponible=disponible,precio=precio,descripcion=descripcion, imagen=imagen,nombre=nombre).where(Item_db.nombre==nomAnt)
			items.execute()
			return True
		except Exception, e:
			return False

	# crea menu
	def createMenu(self,disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen):
		try:
			print 'Crear menu'
			if nombre == '':
				raise Exception("No se puede crear un menu sin nombre")
			fecha_ini = fecha_ini.split('/')
			fecha_fin = fecha_fin.split('/')
			nuevoMenu = Menu_db(disponible=disponible, precio=precio, nombre=nombre,descripcion=descripcion,fecha_ini=date(int(fecha_ini[0]),int(fecha_ini[1]),int(fecha_ini[2])),fecha_fin=date(int(fecha_fin[0]),int(fecha_fin[1]),int(fecha_fin[2])) ,imagen=imagen)	
			nuevoMenu.save()
			return True
		except Exception, e:
			return False

	# update menu
	def updateMenu(self, disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen):
		try:
			print 'Update menu'
			menu = Menu_db.select().where(Menu_db.nombre==nombre).get()
			menu.disponible = disponible
			menu.precio = precio
			menu.descripcion = descripcion
			fecha_ini = fecha_ini.split('/')
			fecha_fin = fecha_fin.split('/')
			menu.fecha_ini = date(int(fecha_ini[0]),int(fecha_ini[1]),int(fecha_ini[2]))
			menu.fecha_fin = date(int(fecha_fin[0]),int(fecha_fin[1]),int(fecha_fin[2]))
			menu.imagen = imagen
			menu.save()
			return True
		except Exception, e:
			return False

	# crea oferta
	def createOferta(self, disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen):
		try:
			print 'Crear oferta'
			if nombre == '':
				raise Exception("No se puede crear una oferta sin nombre")
			fecha_ini = fecha_ini.split('/')
			fecha_fin = fecha_fin.split('/')
			nuevaOferta = Oferta_db(disponible=disponible, precio=precio, nombre=nombre,descripcion=descripcion,fecha_ini=date(int(fecha_ini[0]),int(fecha_ini[1]),int(fecha_ini[2])),fecha_fin=date(int(fecha_fin[0]),int(fecha_fin[1]),int(fecha_fin[2])) ,imagen=imagen)	
			nuevaOferta.save()
			return True
		except Exception, e:
			return False

	# update oferta
	def updateOferta(self, disponible, precio, nombre, descripcion, fecha_ini, fecha_fin, imagen):
		try:
			print 'Update oferta'
			oferta = Oferta_db.get(Oferta_db.nombre==nombre)
			oferta.disponible = disponible
			oferta.precio = precio
			oferta.descripcion = descripcion
			fecha_ini = fecha_ini.split('/')
			fecha_fin = fecha_fin.split('/')
			oferta.fecha_ini = date(int(fecha_ini[0]),int(fecha_ini[1]),int(fecha_ini[2]))
			oferta.fecha_fin = date(int(fecha_fin[0]),int(fecha_fin[1]),int(fecha_fin[2]))
			oferta.imagen = imagen
			oferta.save()
			return True
		except Exception, e:
			return False

	#añade item a los primeros del menu duplicandolo
	def addItemMenuP(self, item, menu):
		try:
			print 'añadiendo primero'
			i = Item_db.select().where(Item_db.id==item).get()
			m = Menu_db.select().where(Menu_db.nombre==menu).get()
			print i.nombre+' '+m.nombre
			nuevoItemA = Item_db(disponible=i.disponible, precio=i.precio, nombre=i.nombre,descripcion=i.descripcion, imagen=i.imagen, primeros=m.id, segundos=0, postres=0, ofertas=0)
			nuevoItemA.save()
			return True
		except Exception, e:
			return False

	#añade item a los segundos del menu duplicandolo
	def addItemMenuS(self, item, menu):
		try:
			print 'añadiendo segundo'
			i = Item_db.select().where(Item_db.id==item).get()
			m = Menu_db.select().where(Menu_db.nombre==menu).get()
			print i.nombre+' '+m.nombre
			nuevoItemA = Item_db(disponible=i.disponible, precio=i.precio, nombre=i.nombre,descripcion=i.descripcion, imagen=i.imagen, primeros=0, segundos=m.id, postres=0, ofertas=0)
			nuevoItemA.save()
			return True
		except Exception, e:
			return False

	#añade item a los postres del menu duplicandolo
	def addItemMenuD(self, item, menu):
		try:
			print 'añadiendo postre'
			i = Item_db.select().where(Item_db.id==item).get()
			m = Menu_db.select().where(Menu_db.nombre==menu).get()
			print i.nombre+' '+m.nombre
			nuevoItemA = Item_db(disponible=i.disponible, precio=i.precio, nombre=i.nombre,descripcion=i.descripcion, imagen=i.imagen, primeros=0, segundos=0, postres=m.id, ofertas=0)
			nuevoItemA.save()
			return True
		except Exception, e:
			return False

	#añade item a una oferta duplicandolo
	def addItemOferta(self, item, oferta):
		try:
			print 'añadiendo item a oferta'
			i = Item_db.select().where(Item_db.id==item).get()
			m = Oferta_db.select().where(Oferta_db.nombre==oferta).get()
			print i.nombre+' '+m.nombre
			nuevoItemA = Item_db(disponible=i.disponible, precio=i.precio, nombre=i.nombre,descripcion=i.descripcion, imagen=i.imagen, primeros=0, segundos=0, postres=0, ofertas=m.id)
			nuevoItemA.save()
			return True
		except Exception, e:
			return False

	# borra primero de un menu
	def delItemMenuP(self, item, menu):
		try:
			print 'borrando primero'
			m = Menu_db.select().where(Menu_db.nombre==menu).get()
			i = Item_db.select().where(Item_db.nombre==item, Item_db.primeros==m.id).get()
			i.delete_instance()
			return True
		except Exception, e:
			return False

	# borra segundo de un menu
	def delItemMenuS(self, item, menu):
		try:
			print 'borrando segundo'
			m = Menu_db.select().where(Menu_db.nombre==menu).get()
			i = Item_db.select().where(Item_db.nombre==item, Item_db.segundos==m.id).get()
			i.delete_instance()
			return True
		except Exception, e:
			return False

	# borra postre de un menu
	def delItemMenuD(self, item, menu):
		try:
			print 'borrando postre'
			m = Menu_db.select().where(Menu_db.nombre==m).get()
			i = Item_db.select().where(Item_db.nombre==item, Item_db.postres==m.id).get()
			i.delete_instance()
			return True
		except Exception, e:
			return False

	# borra item de una oferta
	def delItemOferta(self, item, oferta):
		try:
			print 'borrando item oferta'
			i = Item_db.select().where(Item_db.nombre==item, Item_db.ofertas==oferta).get()
			i.delete_instance()
			return True
		except Exception, e:
			return False

	# devuelve el primer item
	def getItem(self):
		b = Item_db.select()
		return serpent.dumps(b[0],indent=False)

	#borra el item
	def delItem(self, idItem):
		try:
			print 'Borrando Item pyro'
			b = Item_db.select().where(Item_db.id==idItem).get()
			b.delete_instance()
			return True
		except Exception, e:
			return False

	#devuelve todos los item
	def getItems(self):
		try:
			print 'Item pyro'
			i = []
			# busca todos lo items que no estan asignados a ningun meno o oferta
			for x in Item_db.select().where( Item_db.segundos == 0, Item_db.primeros == 0 ,Item_db.postres == 0 ,Item_db.ofertas == 0 ):
			 	i.append(x)
			return serpent.dumps(i,indent=False)
		except Exception, e:
			return False

	#devuelve un menu
	def getMenu(self, menu):
		try:
			print "Menu pyro"
			x = Menu_db.select().where(Menu_db.nombre==menu).get()
			p = [] #primeros
			s = [] #segundos
			d = [] #postres
			m = {}
			m['nombre'] = x.nombre
			m['disponible'] = x.disponible
			m['precio'] = float(x.precio)
			m['descripcion'] = x.descripcion
			m['fecha_ini'] = x.fecha_ini
			m['fecha_fin'] = x.fecha_fin
			m['imagen'] = x.imagen
			for y in Item_db.select().where(Item_db.primeros==x):
				p.append(y)
			for y in Item_db.select().where(Item_db.segundos==x):
				s.append(y)
			for y in Item_db.select().where(Item_db.postres==x):
				d.append(y)
			m['primeros'] = p
			m['segundos'] = s
			m['postres'] = d
			return serpent.dumps(m,indent=False)
		except Exception, e:
			return False

	#borra el menu
	def delMenu(self, menu):
		try:
			print "Borrando Menu pyro"
			m = Menu_db.select().where(Menu_db.nombre==menu).get()
			for i in Item_db.select().where(Item_db.primeros==m.id):
				i.delete_instance()
			for i in Item_db.select().where(Item_db.segundos==m.id):
				i.delete_instance()
			for i in Item_db.select().where(Item_db.postres==m.id):
				i.delete_instance()
			m.delete_instance()
			return True
		except Exception, e:
			return False

	#devuelve un array de menus
	def getMenus(self, fecha):
		try:
			print "Menus pyro"
			fecha = str(fecha).split('-')
			fecha = date(int(fecha[0]),int(fecha[1]),int(fecha[2]))
			menus = []
			for x in Menu_db.select().where( Menu_db.fecha_ini <= fecha  ).where( Menu_db.fecha_fin >= fecha ):
				p = [] #primeros
				s = [] #segundos
				d = [] #postres
				m = {}
				m['nombre'] = x.nombre
				m['disponible'] = x.disponible
				m['precio'] = float(x.precio)
				m['descripcion'] = x.descripcion
				m['fecha_ini'] = x.fecha_ini
				m['fecha_fin'] = x.fecha_fin
				m['imagen'] = x.imagen
				for y in Item_db.select().where(Item_db.primeros==x):
					p.append(y)
				for y in Item_db.select().where(Item_db.segundos==x):
					s.append(y)
				for y in Item_db.select().where(Item_db.postres==x):
					d.append(y)
				m['primeros'] = p
				m['segundos'] = s
				m['postres'] = d
				# agregamos el menu
				menus.append(m)
			return serpent.dumps(menus,indent=False)
		except Exception, e:
			return False
		
	#devuelve una oferta
	def getOferta(self, oferta):
		try:
			print "Oferta pyro"
			x = Oferta_db.select().where(Oferta_db.nombre==oferta).get()
			i = [] #items
			m = {}
			m['nombre'] = x.nombre
			m['disponible'] = x.disponible
			m['precio'] = float(x.precio)
			m['descripcion'] = x.descripcion
			m['fecha_ini'] = x.fecha_ini
			m['fecha_fin'] = x.fecha_fin
			m['imagen'] = x.imagen
			for y in Item_db.select().where(Item_db.ofertas==x):
				i.append(y)
			m['items'] = i
			return serpent.dumps(m,indent=False)
		except Exception, e:
			return False

	# borra la oferta
	def delOferta(self, oferta):
		try:
			print "Borrando Oferta pyro"
			o = Oferta_db.select().where(Oferta_db.nombre==oferta).get()
			for i in Item_db.select().where(Item_db.ofertas==o.id):
				i.delete_instance()
			o.delete_instance()
			return True
		except Exception, e:
			return False

	#devuelve un array de ofertas
	def getOfertas(self, fecha):
		try:
			print "Ofertas pyro"
			fecha = str(fecha).split('-')
			fecha = date(int(fecha[0]),int(fecha[1]),int(fecha[2]))
			ofertas = []
			for x in Oferta_db.select().where( Oferta_db.fecha_ini <= fecha  ).where( Oferta_db.fecha_fin >= fecha ):
				i = [] #items
				m = {}
				m['nombre'] = x.nombre
				m['disponible'] = x.disponible
				m['precio'] = float(x.precio)
				m['descripcion'] = x.descripcion
				m['fecha_ini'] = x.fecha_ini
				m['fecha_fin'] = x.fecha_fin
				m['imagen'] = x.imagen
				for y in Item_db.select().where(Item_db.ofertas==x):
					i.append(y)
				m['items'] = i
				# agregamos la oferta
				ofertas.append(m)
			return serpent.dumps(ofertas,indent=False)
		except Exception, e:
			return False

	#simple ping
	def online(self):
		return True

	def run(self):
		def servicio_Rest():
			# creamos el servicio  
			servicio = ControladorWS(webpath = WEBPATH)

			servicio.addprotocol(PROTOCOL)

			bottle.mount(WEBPATH, servicio.wsgiapp())

			logging.basicConfig(level=logging.DEBUG)

			database2 = SqliteDatabase(DATABASE, threadlocals=True)

			# Arrancamos el servcio web para la aplicacion
			bottle.run(host=DIRECCION_WS, port=PUERTO_WS)
			# fin de arranque del servicio REST
		# manejo de hilos en pyro4
		thread = threading.Thread(target=servicio_Rest)
		thread.setDaemon(True)
		thread.start()