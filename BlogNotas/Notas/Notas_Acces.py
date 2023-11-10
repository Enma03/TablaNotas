import pyodbc

def obtener_notas():
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/ASUS/Documents/GitHub/buenas practicas/EXAMEN FINAL/BlogNotas/notesdb.accdb;')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notas')
    notas = cursor.fetchall()
    conn.close()
    return notas