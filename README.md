Herramientas Web - API
====================

## Requerimientos

* Python 3.5+
* Pip 3
* MySQL

## Setup Inicial

1. Crear Ambiente Virtual con Python `virtualenv`

2. Clonar el Proyecto  

3. Activar el Ambiente Virtual\
Linux:
`$ source env/bin/activate`\
Windows: `C:/path_to_the_folder/ > env/Project_name/Scripts/activate.bat`

4. Instalar las Librerías Requeridas\
`$ pip3 install -r requirements.txt`

5. Configurar Conexión a Base de Datos (MySQL)  
`./herramientasweb_api/my.cnf`

6. Crear la Base de Datos y Aplicar las Migraciones  
`$ python3 manage.py makemigrations herramientasweb_api`\
`$ python3 manage.py migrate`

7. Dentro del Path del Proyecto Correr el Servidor\
 `python3 manage.py runserver`

Fork del Proyecto: https://github.com/Luis-Yael/herramientasweb_api
