servidor-adhoc
==============

Servidor REST para redes wifi ad hoc y bluetooth.

Esta habilitada la seguridad HMAC de Pyro4, por lo tanto hay que asegurarse de que el servidor de nombrado utiliza la misma clave HMAC que el servidor y el cliente. Ejecutar el siguiente comando para que este disponible la clave HMAC para el servidor de nombrado.

	```export PYRO_HMAC_KEY='the_same_string_for_server_and_client'```

En seting.py, estan las constantes de configuración del servicio REST.

Instalación de requerimientos
=============================
Es posible que algunos requerimientos tengas que instalarlos de manera manual según tu sistema operativo.

	```pip install -r requiriments.txt```

Arrancar servidor y cliente
===========================
Para arrancar el servidor de nombrado.

	```python -m Pyro4.naming```

Para arrancar el servidor REST.

	```python service.py```

Para arrancar el cliente para la gestion del servicio (modo texto).

	```python clientePyro.py```