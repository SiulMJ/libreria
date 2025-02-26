from flask import Flask, render_template, request
from conexion import con

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('usuario/index.html')

@app.route('/catalogo')
def catalogo():
    return render_template('usuario/catalogo.html')

@app.route('/otros')
def otros():
    return render_template('usuario/otros.html')

@app.route('/login')
def login():
    return render_template('usuario/login.html')

@app.route('/registro')
def registro():
    return render_template('usuario/registro.html')

@app.route('/registroad', methods=['POST', 'GET'])
def registroad():
    if request.method == 'post':
        name = request.form('name')
        pass1 = request.form('pass1')
        pass2 = request.form('pass2')

    return render_template('admin/registroad.html')

@app.route('/mangas')
def mangas():
    return render_template('usuario/mangas.html')

@app.route('/libro')
def libros():
    return render_template('usuario/libro.html')

app.run(host="localhost", port=4000, debug=True)