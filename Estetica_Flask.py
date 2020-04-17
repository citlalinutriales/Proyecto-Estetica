from flask import Flask
from flask import render_template, request, redirect, url_for

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Urb@no1125',
                             db='Estetica',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


app = Flask(__name__, template_folder="templates")
    
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/Inventario',)
def inventario():
    return render_template('inventario_form.html')

@app.route('/Ventas',)
def ventas():
    return render_template('ventas.html')

@app.route('/Citas',)
def citas():
    return render_template('citas.html')

@app.route('/Clientes', methods=['GET','POST'])
def clientes():

    if request.method == "GET":
       return render_template('clientes.html')

    else:
        Nombre_Cliente = request.form['Nombre_Cliente']
        Apellido_Cliente = request.form['Apellido_Cliente']
        Telefono_Cliente = request.form['Telefono_Cliente']
        Cumpleaños_Cliente = request.form['Cumpleaños_Cliente']

        try:
            with connection.cursor() as cursor:
                # Agregar un nuevo Usuario
                cursor.execute("INSERT INTO Clientes2 (Nombre_Cliente, Apellido_Cliente, Telefono_Cliente, Cumpleanos_Cliente) VALUES (%s,%s,%s,%s)",(Nombre_Cliente, Apellido_Cliente, Telefono_Cliente, Cumpleaños_Cliente))

            # Conexion a la BD para Registro
            connection.commit()
        finally:
            print("Se Guardo")

        return render_template("index.html")        


if __name__ == '__main__':
    app.run(debug = True, port=8000)

