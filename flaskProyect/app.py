
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
        
#Rura de detalle
@app.route('/detalle/<int:id>')
def detalle(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_album WHERE id = %s', (id,))
        consultaId = cursor.fetchone()
        return render_template('consulta.html', album = consultaId)
    
    except Exception as e:
        print('Error al consultar por id: ' + e)
        return redirect(url_for('home'))
    finally:
        cursor.close()

@app.route('/editar/<int:id>')
def editar(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_album WHERE id = %s', (id,))
    album = cursor.fetchone()
    cursor.close()
    
    if album is None:
        flash('Álbum no encontrado')
        return redirect(url_for('home'))
    
    return render_template('formUpdate.html', album=album)

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    album = request.form['TxtTitulo']
    artista = request.form['TxtArtista']    
    anio = request.form['TxtAnio']
    
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE tb_album
        SET album = %s, artista = %s, anio = %s
        WHERE id = %s
    """, (album, artista, anio, id))
    mysql.connection.commit()
    cursor.close()
    
    flash('Album Actualizado en la BD')
    
    errores = {}
    if not album:
        errores['TxtTitulo'] = 'El título del álbum es obligatorio'
    if not artista:
        errores['TxtArtista'] = 'El artista es obligatorio'
    if not anio:
        errores['TxtAnio'] = 'El año es obligatorio'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2030:
        errores['TxtAnio'] = 'Ingresa un año válido (entre 1800 y 2030)'

    # Si hay errores, volver al formulario con los mensajes
    if errores:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_album WHERE id = %s', (id,))
        album = cursor.fetchone()
        cursor.close()
        return render_template('formUpdate.html', album=album, errores=errores)

    # Si no hay errores, actualizar en la BD
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE tb_album
            SET album = %s, artista = %s, anio = %s
            WHERE id = %s
        """, (album, artista, anio, id))
        mysql.connection.commit()
        flash('Álbum actualizado correctamente', 'success')
    except Exception as e:
        mysql.connection.rollback()
        flash(f'Error al actualizar: {str(e)}', 'danger')
    finally:
        cursor.close()
    return redirect(url_for('home'))
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