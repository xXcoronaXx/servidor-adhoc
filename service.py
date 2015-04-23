#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from webservice import *
from admin import *
from setting import *
import json
import socket
import time

class BroadCaster(object):
	"""BroadCaster, emite MESSAGE en formato JSON a difusion al puerto 5555"""
	def __init__(self, MESSAGE):
		super(BroadCaster, self).__init__()
		self.MESSAGE = json.dumps(MESSAGE)
		self.UDP_IP = '<broadcast>' # si no indicamos dirección lo envia a difusión
		self.UDP_PORT = PUERTO_DIFUSION
		self.sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock1.bind(('',0))
		self.sock1.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		self.sock1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		self.sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock2.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		self.sock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		print "Caster creado"
		print "UDP target IP: ", self.UDP_IP
		print "UDP target port:", self.UDP_PORT
		print "message:", self.MESSAGE
	
	def run(self):
		def broadcast(self):
			while True:
				print '* * Enviando * *'
				self.sock1.sendto(self.MESSAGE, (self.UDP_IP, self.UDP_PORT))
				self.sock2.sendto(self.MESSAGE, ("192.168.0.255", self.UDP_PORT))
				time.sleep( TIEMPO_ANUNCIOS )
		# manejo de hilos
		thread = threading.Thread(target=broadcast(self))
		thread.setDaemon(True)
		thread.start()

def main():
	# Create a database instance that will manage the connection and
	# execute queries
	try:
		db.create_tables([Menu_db, Oferta_db, Item_db])
		print 'Base de datos creada...'
	except Exception, e:
		print 'La base de datos ya existe...'
	database = SqliteDatabase(DATABASE, threadlocals=True)
	# creando algunos objetos y mostrando los existentes...
	nuevoItem = Item_db(disponible=True, precio='10.5', nombre='sqlite3',descripcion='item desde la db', imagen='nmnmnmnm', primeros=0, segundos=0, postres=0, ofertas=0)
	#nuevoItem.save()
	nuevoMenu = Menu_db(disponible=True, precio='10.5', nombre='sqlite3',descripcion='item desde la db',fecha_ini=date(1960, 1, 15),fecha_fin=date(1999, 1, 15),codigo='0123456789' ,imagen='nmnmnmnm')
	#nuevoMenu.save()
	print '---Menus---'
	for x in Menu_db.select():
		print str(x.id)+' '+x.nombre+' - '+str(x.fecha_fin)
	print '---'
	print '---Ofertas---'
	for x in Oferta_db.select():
		print str(x.id)+' '+x.nombre+' - '+str(x.fecha_fin)
	print '---'
	print '---Items-1--'
	for x in Item_db.select().where( Item_db.segundos==0,Item_db.primeros==0,Item_db.postres==0,Item_db.ofertas==0 ):
		print str(x.id)+' '+x.nombre
	print '---'
	# fin base de datos

	# servicio Pyro4
	Pyro4.config.HMAC_KEY = KEY
	configura = ControladorPyro()
	#print Pyro4.config.dump()

	daemon = Pyro4.Daemon(host=DIRECCION_PYRO_LOCAL)
	#daemon = Pyro4.Daemon(host="192.168.0.18", port=5150);
	uri = daemon.register(configura)
	ns = Pyro4.locateNS(host=DIRECCION_PYRO)
	print uri
	ns.register(OBJETO_PYRO, uri)

	#arrancamos el hilo del servicio web
	configura.run()
	
	# arrancamos hilo para anuncio del servidor
	data = {'Nombre': OBJETO_PYRO, 'IP': DIRECCION_WS+':'+str(PUERTO_WS), 'IP_2':DIRECCION_BLUETOOTH ,'Mensaje': MENSAJE}
	caster = BroadCaster(data)
	caster.run()
	
	print 'Pyro4 ready !'
	daemon.requestLoop() 
	#fin del servicio Pyro4


if __name__=="__main__":
	main()