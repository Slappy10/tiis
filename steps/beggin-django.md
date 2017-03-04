# Pasos
* Crear una carpeta
> mkdir djangoapps
* Crear un virtualenv
> virtualenv hunter
* Inicializar el virtualenv
> source hunter/bin/activate
* Estamos ready, ahora instalamos django
> pip install django
* Creamos un proyecto 
> django-admin startproject mysite
> cd mysite
* Corremos las migraciones
> python manage.py migrate
* Ahora para el paso final iniciamos el servidor
> python manage.py runserver
* ¡Felicidades! ¡Haz creado tu primer sitio web y los haz ejecutado usando un servidor web! ¿No es genial? 
