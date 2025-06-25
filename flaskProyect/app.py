
from flask import Flask,jsonify,render_template,request,url_for,flash,redirect
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST'] ="localhost"
app.config['MYSQL_USER'] ="root"
app.config['MYSQL_PASSWORD'] ="12345678"
app.config['MYSQL_DB'] ="dbflask"
#app.config['MYSQL_PORT'] =3306 // usar solo en cambio de puerto
app.secret_key = 'mysecretkey'

mysql = MySQL(app)


@app.route('/')
def home():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_album')
        consultaTodo = cursor.fetchall()
        return render_template('formulario.html', errores={}, albums = consultaTodo)
    
    except Exception as e:
        print('Error al consultar todo: ' + e)
        return render_template('formulario.html', errores={}, albums = [])
    finally:
        cursor.close()
    
#ruta para probar la conección a mysql
@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ), 200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ), 200


@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

#Ruta para la Insert
@app.route('/guardarAlbum', methods = ['POST'])
def guardar():

    #lista de errores
    errores={}

    #obtener los datos a insertar
    Vtitulo= request.form.get('txtTitulo', '').strip()
    Vartista= request.form.get('txtArtista', '').strip()
    Vanio= request.form.get('txtAnio', '').strip()

    if not Vtitulo:
        errores['txtTitulo']= 'Nombre del album obligatorio'
    if not Vartista:
        errores['txtArtista']= 'Artista es obligatorio'
    if not Vanio:
        errores['txtAnio']= 'Año es obligatorio'
    elif not Vanio.isdigit() or int(Vanio)< 1800 or int(Vanio)> 2030:
        errores['txtAnio']= 'Ingresa un año valido'

    if not errores:
        #Intentamos ejecutar el INSERT
        try:
            cursor= mysql.connection.cursor()
            cursor.execute('insert into tb_album(album,artista,anio) values(%s,%s,%s)', (Vtitulo, Vartista, Vanio))
            mysql.connection.commit()
            flash('Album se guardo en BD')
            return redirect(url_for('home'))
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo fallo: '+ str(e))
            return redirect(url_for('formulario'))
        finally:
            cursor.close()
    return render_template('formulario.html', errores= errores)


if __name__ == '__main__':
    app.run(port=3000, debug=True)