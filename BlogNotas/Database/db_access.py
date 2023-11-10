import pyodbc

def agregar_estudiante(nombre):
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/ASUS/Documents/GitHub/buenas practicas/EXAMEN FINAL/BlogNotas/notesdb.accdb;')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO notas (alumnos) VALUES ('{nombre}')")
    conn.commit()
    conn.close()

def eliminar_estudiante(nombre):
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/ASUS/Documents/GitHub/buenas practicas/EXAMEN FINAL/BlogNotas/notesdb.accdb;')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM notas WHERE alumnos='{nombre}'")
    conn.commit()
    conn.close()

def editar_nota(alumno, materia, nueva_nota):
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/ASUS/Documents/GitHub/buenas practicas/EXAMEN FINAL/BlogNotas/notesdb.accdb;')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE notas SET {materia}={nueva_nota} WHERE alumnos='{alumno}'")
    conn.commit()
    conn.close()