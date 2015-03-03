servidor-adhoc
==============

Servidor REST para redes wifi ad hoc y bluetooth.

Esta habilitada la seguridad HMAC de Pyro4, por lo tanto hay que asegurarse de que el servidor de nombrado utiliza la misma clave HMAC que el servidor y el cliente. Ejecutar el siguiente comando para que este disponible la clave HMAC para el servidor de nombrado.

	export PYRO_HMAC_KEY='the_same_string_for_server_and_client'

IMPORTANTE : todos los scripts estan configurados teniendo en cuenta que la direccion de nuestro interfaz eth0 es 192.168.1.115. Si es otra, por favor revisa los archivos configura.sh, setting.py y start.sh.

En seting.py, estan las constantes de configuración del servicio REST, en interfaz/settging.py estan las correspondientes para el cliente.

Instalación de requerimientos
=============================
Es posible que algunos requerimientos tengas que instalarlos de manera manual según tu sistema operativo.

	pip install -r requeriments.txt

Para instalar la libreria gráfica la descargamos e instalamos de:

	http://www.wxpython.org/download.php

Arrancar servidor y cliente (manual)
====================================
Para arrancar el servidor de nombrado.

	python -m Pyro4.naming (--host localhost)

Para arrancar el servidor REST.

	python service.py

Para arrancar el cliente para la gestion del servicio (modo texto, desactualizado).

	python clientePyro.py

Para cargar la interfaz grafica nos cambiamos a su directorio y ejecutamos.

	python InterfazServidor.py

En los archivos setting.py estan los parametros de configuracion de los programas.

Para ver si esta corriendo el navegador las direcciones del servicio REST son del tipo:

	http://localhost/ws/getMenus.json
	http://localhost/ws/getMenu.json
	http://localhost/ws/getItems.json
	...

Si no tienes ningun menu creado obviamente te devolvera una lista vacia.
