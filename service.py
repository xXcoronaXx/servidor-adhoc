# coding=utf8
from webservice import *
from admin import *
from seting import *

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

	daemon = Pyro4.Daemon(host=DIRECCION_PYRO)
	#daemon = Pyro4.Daemon(host="192.168.0.18", port=5150);
	uri = daemon.register(configura)
	ns = Pyro4.locateNS()
	print uri
	ns.register(OBJETO_PYRO, uri)

	#arrancamos el hilo del servicio web
	configura.run()

	print 'Pyro4 ready !'
	daemon.requestLoop() 
	#fin del servicio Pyro4


if __name__=="__main__":
	main()