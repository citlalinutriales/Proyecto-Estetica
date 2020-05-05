from flask import Flask
from flask import render_template, request, redirect, url_for

import pymysql.cursors



app = Flask(__name__, template_folder="templates")
    
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/Inventario', methods=['GET','POST'])
def inventario():

    if request.method == "GET":
       return render_template('inventario_form.html')

    else:
        Marca_Producto = request.form['Marca_Producto']
        Modelo_Producto = request.form['Modelo_Producto']
        Costo_Producto = request.form['Costo_Producto']

        finally:
            print("Se Guardo")
        return render_template("index.html")     

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

        return render_template("index.html")        


if __name__ == '__main__':
    app.run(debug = True, port=8000)

