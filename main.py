from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/otros')
def otros():
    return render_template('otros.html')

@app.route('/mangas')
def mangas():
    return render_template('mangas.html')

app.run(host="localhost", port=4000, debug=True)