#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from wsme import *
from wsme.types import *

import time
from datetime import date

from Models import *
from peewee import *

from setting import *

class Item(object):
	id = int
	disponible = bool
	precio = float
	nombre = unicode
	descripcion = unicode
	imagen = bytes #imagen
	modificado = date 

	def showImage(self):
		fh = open("imageToSave.jpg", "wb")
		fh.write(self.imagen.decode('base64'))
		fh.close()

	def setImage(self, f):
		with open(f, "rb") as imageFile:
			img = base64.b64encode(imageFile.read())
		return img

	def __init__(self, id = None , disponible = False,precio = None, nombre = None, descripcion = None, imagen = None, modificado = None ):
		if id:
			self.id = id
		if disponible:
			self.disponible = disponible
		if precio:
			self.precio = precio
		if nombre:
			self.nombre = nombre
		if descripcion:
			self.descripcion = descripcion
		if imagen:
			self.imagen = imagen
		if modificado:
			self.modificado = modificado

class Menu(Base):
	id = int
	precio = float
	disponible = bool
	nombre = unicode
	descripcion = unicode
	fecha_ini = date
	fecha_fin = date
	imagen = bytes
	primeros = [Item]
	segundos = [Item]
	postres = [Item]
	modificado = date 

	def setImage(self, f):
		with open(f, "rb") as imageFile:
			img = base64.b64encode(imageFile.read())
		return img
	
	def __init__(self, id=None, disponible = False, precio = 0 ,nombre= None,descripcion = None,  primeros = None, segundos = None, postres = None,fecha_ini = None, fecha_fin = None, imagen = None, modificado = None ):
		if id:
			self.id = id
		if precio:
			self.precio = precio
		if disponible:
			self.disponible = disponible
		if nombre:
			self.nombre = nombre
		if descripcion:
			self.descripcion = descripcion
		if primeros:
			self.primeros = list(primeros)
		if segundos:
			self.segundos = list(segundos)
		if postres:
			self.postres = list(postres)
		if fecha_ini:
			self.fecha_ini = fecha_ini
		if fecha_fin:
			self.fecha_fin = fecha_fin
		if imagen:
			self.imagen = imagen
		if modificado:
			self.modificado = modificado	




class Oferta(Base):
	id = int
	disponible = bool
	precio = float
	descripcion = unicode
	items = [Item]
	fecha_ini = date
	fecha_fin = date
	#codigo =  unicode
	imagen = bytes
	modificado = date 

	def setImage(self, f):
		with open(f, "rb") as imageFile:
			img = base64.b64encode(imageFile.read())
		return img

	def __init__(self, id = None, disponible = False, precio = None,nombre = None ,descripcion = None, items = None, fecha_ini = None, fecha_fin = None, imagen = None, modificado = None ):
		if id:
			self.id = id
		if precio:
			self.precio = precio
		if descripcion:
			self.descripcion = descripcion
		if disponible:
			self.disponible = disponible
		if fecha_ini:
			self.fecha_ini = fecha_ini
		if fecha_fin:
			self.fecha_fin = fecha_fin
		if descripcion:
			self.descripcion = descripcion
		if items:
			self.items = list(items)
		if imagen:
			self.imagen = imagen
		if modificado:
			self.modificado = modificado

class ControladorWS(WSRoot):

	#devuelve un menu
	@expose(Menu)
	def getMenu(self):
		print "Menu WS"
		try:
			menu = Menu_db.select()[0]
			p = [] #primeros
			s = [] #segundos
			d = [] #postres
			for y in Item_db.select().where( Item_db.primeros==menu ):
				p.append( Item( y.id, y.disponible, float(y.precio), y.nombre, y.descripcion, y.imagen, y.modified ) )
			for v in Item_db.select().where(Item_db.segundos==menu):
				s.append( Item( v.id, v.disponible, float(v.precio), v.nombre, v.descripcion, v.imagen, v.modified ) )
			for z in Item_db.select().where(Item_db.postres==menu):
				d.append( Item( z.id, z.disponible, float(z.precio), z.nombre, z.descripcion, z.imagen, z.modified ) )
			menu = Menu( menu.id, menu.disponible, float(menu.precio), menu.nombre, menu.descripcion,  p, s, d, menu.fecha_ini, menu.fecha_fin, menu.imagen, menu.modified)
			return menu
		except Exception, e:
			return Menu()

	#devuelve un array de menus
	@expose([Menu])
	def getMenus(self):
		print "Menus WS"
		try:
			menus = [] #arrays de menus
			m = Menu_db.select()
			for x in m:
				print x.nombre
				p = [] #primeros
				s = [] #segundos
				d = [] #postres
				for y in Item_db.select().where( Item_db.primeros==x ):
					p.append( Item( y.id, y.disponible, float(y.precio), y.nombre, y.descripcion, y.imagen, y.modified ) )
				for v in Item_db.select().where( Item_db.segundos==x ):
					s.append( Item( v.id, v.disponible, float(v.precio), v.nombre, v.descripcion, v.imagen, v.modified ) )
				for z in Item_db.select().where( Item_db.postres==x ):
					d.append( Item( z.id, z.disponible, float(z.precio), z.nombre, z.descripcion, z.imagen, z.modified ) )
				menus.append( Menu( x.id, x.disponible, float(x.precio), x.nombre, x.descripcion, p, s, d, x.fecha_ini, x.fecha_fin, x.imagen, x.modified ) )
			return menus
		except Exception, e:
			return []

	#devuelve un item
	@expose([Item])
	def getItems(self):
		print 'Items WS'
		try:
			items = []
			for x in Item_db.select():
				items.append( Item( x.id, x.disponible, float(x.precio), x.nombre, x.descripcion, x.imagen, x.modified ) )
			return items
		except Exception, e:
			return []
		
		
	@expose()
	def showImg(self):
		primeros.showImage()

	#devuelve una oferta
	@expose(Oferta)
	def getOferta(self):
		print "Oferta WS"
		try:
			oferta = Oferta_db.select()[0]
			i = [] # items de la oferta
			for y in Item_db.select().where( Item_db.ofertas==oferta ):
				i.append( Item( y.id, y.disponible, float(y.precio), y.nombre, y.descripcion, y.imagen, y.modified ) )
			return Oferta( oferta.id, oferta.disponible, float(oferta.precio), oferta.nombre, oferta.descripcion, i, oferta.fecha_ini, oferta.fecha_fin, oferta.imagen, oferta.modified )
		except Exception, e:
			return Oferta()

	#devuelve un array de ofertas
	@expose([Oferta])
	def getOfertas(self):
		print "Ofertas WS"
		ofertas = []
		try:
			o = Oferta_db.select()
			i = [] # items de la oferta
			for x in o:
				for y in Item_db.select().where( Item_db.ofertas==x ):
					i.append( Item( y.id, y.disponible, float(y.precio), y.nombre, y.descripcion, y.imagen, y.modified ) )
				ofertas.append( Oferta( x.id, x.disponible, float(x.precio), x.nombre, x.descripcion, i, x.fecha_ini, x.fecha_fin, x.imagen, x.modified ) )
			return ofertas
		except Exception, e:
			return []