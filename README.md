servidor-adhoc
==============

Servidor REST para redes wifi ad hoc y bluetooth.

Esta habilitada la seguridad HMAC de Pyro4, por lo tanto hay que asegurarse de que el servidor de nombrado utiliza la misma clave HMAC que el servidor y el cliente. Ejecutar el siguiente comando para que este disponible la clave HMAC para el servidor de nombrado.

	export PYRO_HMAC_KEY='the_same_string_for_server_and_client'

En seting.py, estan las constantes de configuración del servicio REST.

Instalación de requerimientos
=============================
Es posible que algunos requerimientos tengas que instalarlos de manera manual según tu sistema operativo.

	pip install -r requeriments.txt

Para instalar la libreria gráfica la descargamos e instalamos de:

	http://www.wxpython.org/download.php

Arrancar servidor y cliente
===========================
Para arrancar el servidor de nombrado.

	python -m Pyro4.naming (--host localhost)

Para arrancar el servidor REST.

	python service.py

Para arrancar el cliente para la gestion del servicio (modo texto).

	python clientePyro.py

Para ver si esta corriendo el navegador las direcciones del servicio REST son del tipo:

	http://localhost:8080/ws/getMenus.json
	http://localhost:8080/ws/getMenu.json
	http://localhost:8080/ws/getItems.json
	...

Si no tienes ningun menu creado obviamente te devolvera una lista vacia.
