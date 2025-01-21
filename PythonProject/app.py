from flask import Flask, render_template, request

app = Flask(__name__)


# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')


# Ruta para el ejercicio 1
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


# Ruta para procesar los datos del ejercicio 1
@app.route('/resultado1', methods=['POST'])
def resultado1():
    # Obtener las notas y asistencia del formulario
    nota1 = int(request.form['nota1'])
    nota2 = int(request.form['nota2'])
    nota3 = int(request.form['nota3'])
    asistencia = int(request.form['asistencia'])

    # Calcular el promedio
    promedio = (nota1 + nota2 + nota3) / 3

    # Verificar si el estudiante aprueba
    if promedio >= 40 and asistencia >= 75:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    return f"Promedio: {promedio}<br>Estado: {estado}"


# Ruta para el ejercicio 2
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')


# Ruta para procesar los datos del ejercicio 2
@app.route('/resultado2', methods=['POST'])
def resultado2():
    # Obtener los tres nombres del formulario
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']

    # Comparar las longitudes de los nombres
    nombres = [nombre1, nombre2, nombre3]
    nombre_largo = max(nombres, key=len)

    return f"El nombre más largo es: {nombre_largo} con {len(nombre_largo)} caracteres."


# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
