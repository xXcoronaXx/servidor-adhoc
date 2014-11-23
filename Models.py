# coding=utf8
from peewee import *
import datetime

# parametro soporte multi hilo
db = SqliteDatabase('ws.db', check_same_thread=False)

class Menu_db(Model):
	nombre = CharField(unique=True, null=False)
	precio = FloatField()
	disponible = BooleanField()
	descripcion = CharField()
	fecha_ini = DateTimeField()
	fecha_fin = DateTimeField()
	imagen = CharField()
	modified = DateTimeField()

	class Meta:
		database = db
	
	def save(self, *args, **kwargs):
		self.modified = datetime.datetime.now()
		return super(Menu_db, self).save(*args, **kwargs)

class Oferta_db(Model):
	nombre = CharField(unique=True, null=False)
	precio = FloatField()
	disponible = BooleanField()
	descripcion = CharField()
	fecha_ini = DateTimeField()
	fecha_fin = DateTimeField()
	#codigo =  CharField()
	imagen = CharField()
	modified = DateTimeField()

	class Meta:
		database = db

	def save(self, *args, **kwargs):
		self.modified = datetime.datetime.now()
		return super(Oferta_db, self).save(*args, **kwargs)

class Item_db(Model):
	nombre = CharField(null=False)
	precio = FloatField()
	disponible = BooleanField()
	descripcion = CharField()
	imagen = CharField() #imagen base64
	modified = DateTimeField()
	primeros =  ForeignKeyField(Menu_db, related_name='primeros')
	segundos = ForeignKeyField(Menu_db, related_name='segundos')
	postres = ForeignKeyField(Menu_db, related_name='postres')
	ofertas = ForeignKeyField(Oferta_db, related_name='items')
	
	class Meta:
		database = db

	def save(self, *args, **kwargs):
		self.modified = datetime.datetime.now()
		return super(Item_db, self).save(*args, **kwargs)
