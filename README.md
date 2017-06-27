# Django Mobile Shop
DMS es un proyecto de ejemplo para fines puramente educativos, implementado en la charla "Django Reloaded" con el objetivo de dar a conocer las virtudes del framework web más popular dentro del mundo Python. 


## Instalación.

** Requerimeintos:**  

- Python 3.
- Virtualenv.
- Instalador de paquetes pip.

1. Descargar el archivo zip desde GitHub.
2. Descoprimir el archivo y usando la consola nos dirigimos al directorio raiz.

	$ cd django_mobile_shop

3. Se procede a virtualizar el ambiente de trabajo usando virtualenv (también se puede usar virtualenvwrapper):

	$ virtualenv

4. Activar el ambiente virtual:

	$ source bin/activate

5. Instalar las librerias usando pip y el archivo de requerimientos (requeriments.txt):

	$ pip install -r requeriments.txt

6. Entramos al directorio src y ejecutar el comando que activa el servidor de desarrollo:

	$ cd src
	$ python manage.py runserver

7. En una pestaña del navegador escrimibos la siguiente dirección:

	http://127.0.0.1:8000/

![home](https://github.com/emilioferreyra/django_mobile_shop/blob/master/docs/screenshots/dms_home.png?raw=true)


**Nota:** para tener acceso al sitio de administración:

	http://127.0.0.1:8000/admin

User: admin
Password: djangoadmin123

Lista de personas:
![persons_list](https://github.com/emilioferreyra/django_mobile_shop/blob/master/docs/screenshots/person_list.png?raw=true)


Lista de productos:
![products_list](https://github.com/emilioferreyra/django_mobile_shop/blob/master/docs/screenshots/mobile_list.png?raw=true)

Algunas imágenes más [aquí](https://github.com/emilioferreyra/django_mobile_shop/tree/master/docs/screenshots)

## Recursos

### Iniciando con Python

Curso gratis y en español en la plataforma Code Academy: [Learn Python](https://www.codecademy.com/learn/python)

### Libros de Python y Django

Libros gratis sobre Python y Django. Hay muchos en español [Pythoniza.me](https://pythoniza.me/category/libros/)

### Iniciando con Django

Tutorial oficial de Django [Django Project - Tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)


### Manejadores de contenido CMS

- [Mezzanine](http://mezzanine.jupo.org/)
- [Wagtail](https://wagtail.io/)
- [Django CMS](https://www.django-cms.org)

### Plantillas para el site admin.

- [Django Suit](http://djangosuit.com/)
- [Grappelli](http://grappelliproject.com/)
- [Django Jet](http://jet.geex-arts.com/)

### Plantillas de proyectos.

- [Caktus Django Project Template](https://github.com/caktus/django-project-template)
- [Edge](https://github.com/arocks/edge)
- [Pydanny Django Cookiecutter](https://github.com/pydanny/cookiecutter-django)

### Comercio electrónico (e-commerce).

-[Orcar](http://oscarcommerce.com/)

### Otros

- [Django Packages](https://djangopackages.org/)

