# Tabla de Notas

    Este es un proyecto de Tabla de notas desarrollado con Flask y una base de datos Microsoft Access.

## Requisitos

    - Python 3.x
    - Flask
    - pyodbc

## Configuración del Entorno

1. Instala las dependencias:

   pip install Flask pyodbc

2. Configura la conexión a la base de datos:

    Asegúrate de tener una base de datos de Microsoft Access (notesdb.accdb) y ajusta la ruta en Database/db_access.py.

    Ejecutar la Aplicación

    python App.py

3. Visita http://127.0.0.1:5000/ en tu navegador.

## Características

    - Visualización de notas y alumnos.
    - Agregar, eliminar y editar estudiantes.
    - Editar notas por nombre de estudiante.

## Estructura del Proyecto
    BlogNotas
    |
    ├── Database
    │   └── db_access.py
    │   
    ├── Estudiantes
    │   ├── Estudiantes.Acess.py      
    |
    ├── Notas
    │   ├── Notas.Acess.py 
    |
    ├── templates
    │     └── index.html
    |
    ├── App.py
    ├── notesdb.accdb
    └── README.md


Asegúrate de personalizar la información del proyecto, como la estructura de directorios y las características específicas de tu aplicación.

