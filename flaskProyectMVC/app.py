
from flask import Flask,jsonify
from flask_mysqldb import MySQL
import MySQLdb
from config import Config


mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    
    from controllers.albumController import albumsBP
    app.register_blueprint(albumsBP)
    
    return app






        
#Rura de detalle






#Ruta para confirmar eliminacion

#Ruta para eliminar

#ruta para probar la conección a mysql
'''@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()   
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ), 200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ), 200'''

#Ruta para la Insert


if __name__ == '__main__':
    app = create_app()
    app.run(port=3000, debug=True)