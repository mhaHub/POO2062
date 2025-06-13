
from flask import Flask

app = Flask(__name__)

#Ruta simple
@app.route('/')
def home():
    return 'Hola Mundo FLASK'

#Ruta con parametros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola, '+nombre+'!!!'

#Ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8 !!!', 404

#Ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'Soy el mismo recurso del servidor'

#Ruta POST
@app.route('/formulario', methods = ['POST'])
def formulario():
    return 'Soy un formulario'



if __name__ == '__main__':
    app.run(port=3000, debug=True)