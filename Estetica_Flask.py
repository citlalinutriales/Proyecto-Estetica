from flask import Flask
from flask import render_template, request, redirect, url_for

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

if __name__ == '__main__':
    app.run(debug = True, port=8000)

