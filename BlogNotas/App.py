from flask import Flask, render_template, request, redirect, url_for
from Estudiantes import Estudiantes_Acces
from Notas import Notas_Acces
from Database import db_access

app = Flask(__name__)

@app.route('/')
def index():
    notas = Notas_Acces.obtener_notas()
    alumnos = Estudiantes_Acces.obtener_alumnos()
    return render_template('index.html', notas=notas, alumnos=alumnos)

@app.route('/agregar_estudiante', methods=['POST'])
def agregar_estudiante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        db_access.agregar_estudiante(nombre)
    return redirect(url_for('index'))

@app.route('/eliminar_estudiante', methods=['POST'])
def eliminar_estudiante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        db_access.eliminar_estudiante(nombre)
    return redirect(url_for('index'))

@app.route('/editar_nota', methods=['POST'])
def editar_nota():
    if request.method == 'POST':
        alumno = request.form['alumno']
        materia = request.form['materia']
        nueva_nota = request.form['nueva_nota']
        db_access.editar_nota(alumno, materia, nueva_nota)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)