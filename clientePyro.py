#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import Pyro4

import time
from datetime import date
#from Models import *


import base64
import serpent
import os
import time

KEY='the_same_string_for_server_and_client'

def mostrarItems():
	print '-------------- LISTA DE TODOS LOS ITEMS --------------'
	c = servicio.getItems()
	c = serpent.loads(c)
	for x in c:
		print str(x['_data']['id'])+' '+x['_data']['nombre']+' '+str(x['_data']['precio'])
	print '--------------  #######################  --------------'
	print ''

def mostrarMenus():
	print '-------------- LISTA DE TODOS LOS MENUS --------------'
	c = servicio.getMenus()
	c = serpent.loads(c)
	for x in c:
		print x['nombre']+' '+x['fecha_ini']+' '+str(x['precio'])
		print '-'
		for i in x['primeros']:
			print i['_data']['nombre']+' '+str(i['_data']['precio'])
		print '-'
		for i in x['segundos']:
			print i['_data']['nombre']+' '+str(i['_data']['precio'])
		print '-'
		for i in x['postres']:
			print i['_data']['nombre']+' '+str(i['_data']['precio'])
	print '--------------  #######################  --------------'
	print ''

def mostrarOfertas():
	print '-------------- LISTA DE TODAS LAS OFERTAS --------------'
	c = servicio.getOfertas()
	c = serpent.loads(c)
	for x in c:
		print x['nombre']+' '+x['fecha_ini']+' '+str(x['precio'])
		for i in x['items']:
			print i['_data']['nombre']+' '+str(i['_data']['precio'])
	print '--------------  #######################  --------------'
	print ''

print 'Conectando ...'
Pyro4.config.HMAC_KEY=KEY
servicio = Pyro4.Proxy('PYRONAME:servidor1.configura')
#di = Pyro4.Proxy("PYRO:mb.dispatcher@192.168.0.18:5150")
print 'Conectado al servicio !'
# preparando interfaz
text = 99
# seleccionando sistema operativo
if os.name == 'posix':
	BORRAR = 'clear'
else:
	BORRAR = 'cls'

try:
	servicio.online()
	while text > 0:
		os.system(BORRAR)

		print ''
		print '------------- Controlador WS -------------'
		print '  0  : Salir'
		print '  1  : Crear Menu'
		print '  2  : Crear Oferta'
		print '  3  : Crear Item'
		print '  4  : Borrar Menu'
		print '  5  : Borrar Oferta'
		print '  6  : Borrar Item'
		print '  7  : Asignar items a Menu -> Primeros'
		print '  8  : Asignar items a Menu -> Segundos'
		print '  9  : Asignar items a Menu -> Postres'
		print '  10 : Asignar items a Oferta'
		print '  11 : Ver menus'
		print '  12 : Ver ofertas'
		print '  13 : Ver items'
		print '-------------  ############  -------------'
		print ''
		text = raw_input(" Elige un numero -> ").strip()
		try:
			text = int(text)
		except Exception, e:
			text = 99
		os.system(BORRAR)
		print ''
		if text == 0:
			text = -1
		elif text == 1:
			print '+ creando Menu'
			name=raw_input("Nombre del menu? ").strip()
			precio=raw_input("Precio del menu? ").strip()
			if servicio.createMenu(True, precio, name,'menu descripcion piro','2000/1/1','2010/1/1','imagen del menu en base64'):
				print 'Menu creado!'
			else:
				print 'ERROR: El menu no se creo!'	
			time.sleep(2)
		elif text == 2:
			print '+ creando Oferta'
			name=raw_input("Nombre de la oferta? ").strip()
			precio=raw_input("Precio de la oferta? ").strip()
			if servicio.createOferta(True, 'CoDiGo', precio, name,'menu descripcion piro','2000/1/1','2010/1/1','imagen del menu en base64'):
				print 'Oferta creada!'
			else:
				print 'ERROR: La oferta no se creo!'
			time.sleep(2)			
		elif text == 3:
			print '+ Creando Item ...'
			name=raw_input("Nombre del item? ").strip()
			precio=raw_input("Precio del item? ").strip()
			descripcion=raw_input("Descripcion? ").strip()
			if servicio.createItem(True, precio, name, descripcion, 'imagenpiro', 0, 0, 0, 0):
				print 'Item creado!'
			else:
				print 'ERROR: El item no se creo!'
			time.sleep(2)
		elif text == 4:
			mostrarMenus()
			print '- Borrar Menu '
			name=raw_input("que Menu quieres borrar? ").strip()
			if servicio.delMenu(name):
				print 'Menu Borrado'
			else:
				print 'ERROR: El menu NO se borro'
			time.sleep(2)
		elif text == 5:
			mostrarOfertas()
			print '- Borrar Oferta '
			name=raw_input("que oferta quieres borrar? ").strip()
			if servicio.delOferta(name):
				print 'Oferta Borrada'
			else:
				print 'ERROR: La oferta NO se borro'
			time.sleep(2)
		elif text == 6:
			mostrarItems()
			print '- Borrar Item '
			name=raw_input("que item quieres borrar? ").strip()
			if servicio.delItem(name):
				print 'item Borrado'
			else:
				print 'ERROR: El item NO se borro'
			time.sleep(2)
		elif text == 7:
			mostrarItems()
			print '+ item a Menu Primero'
			name=raw_input("que item quieres anadir? ").strip()
			os.system("clear")
			mostrarMenus()
			name2=raw_input("A que menu quieres anadir? ").strip()
			if servicio.addItemMenuP(name,name2):
				print 'Introducido con exito'
			else:
				print 'ERROR: introduciendo primero'
			time.sleep(2)
		elif text == 8:
			mostrarItems()
			print '+ item a Menu Segundo'
			name=raw_input("que item quieres anadir? ").strip()
			os.system("clear")
			mostrarMenus()
			name2=raw_input("A que menu quieres anadir? ").strip()
			if servicio.addItemMenuS(name,name2):
				print 'Introducido con exito'
			else:
				print 'ERROR: introduciendo segundo'
			time.sleep(2)
		elif text == 9:
			mostrarItems()
			print '+ item a Menu Postre'
			name=raw_input("que item quieres anadir? ").strip()
			os.system("clear")
			mostrarMenus()
			name2=raw_input("A que menu quieres anadir? ").strip()
			if servicio.addItemMenuD(name,name2):
				print 'Introducido con exito'
			else:
				print 'Error introduciendo postre'
			time.sleep(2)
		elif text == 10:
			mostrarItems()
			print '+ item a Oferta'
			name=raw_input("que item quieres anadir? ").strip()
			os.system("clear")
			mostrarOfertas()
			name2=raw_input("A que oferta quieres anadir? ").strip()
			if servicio.addItemOferta(name,name2):
				print 'Introducido con exito'
			else:
				print 'ERROR: introduciendo item en oferta'
			time.sleep(2)
		elif text == 11:
			mostrarMenus()
			name=raw_input("Intro para continuar ").strip()
		elif text == 12:
			mostrarOfertas()
			name=raw_input("Intro para continuar ").strip()
		elif text == 13:
			mostrarItems()
			name=raw_input("Intro para continuar ").strip()
except Exception, e:
	print 'No se encuentra el servidor'
	