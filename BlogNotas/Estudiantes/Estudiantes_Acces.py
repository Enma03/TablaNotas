import pyodbc

def obtener_alumnos():
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/ASUS/Documents/GitHub/buenas practicas/EXAMEN FINAL/BlogNotas/notesdb.accdb;')
    cursor = conn.cursor()
    cursor.execute('SELECT alumnos FROM notas')
    alumnos = cursor.fetchall()
    conn.close()
    return alumnos