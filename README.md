# pyTrash
Pequeño script en python que implementa una papelera en linux
Funcionamiento 
============
Al usar el script se crea un directorio que sirve de papelera y se mueve el archivo dentro de este directorio y se agrega una base de datos la ruta y una fecha de caducidad. 
Dependencias
==========
* sqlalchemy

Recomendación
===========
Agregar a cron o anacron trashd.py que su función es que llegada la fecha de debe borrar los archivos caducos
