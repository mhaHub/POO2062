from flask import Blueprint,render_template,request,redirect,url_for,flash
from models.albumModels import *

albumsBP = Blueprint('albums',__name__)

#Ruta de inicio
@albumsBP.route('/')
def home():
    try:
        albums =  getAll()
        return render_template('formulario.html', errores={}, albums = albums)
    
    except Exception as e:
        print('Error al consultar todo: ' + str(e))
        return render_template('formulario.html', errores={}, albums = [])

@albumsBP.route('/consulta')
def consulta():
    return render_template('consulta.html')

#Ruta de detalles
@albumsBP.route('/detalle/<int:id>')
def detalle(id):
    try:
        album = getById(id)
        return render_template('consulta.html', album=album)
    except Exception as e:
        flash('Error al consultar el álbum: ' + str(e))
        return redirect(url_for('albums.home'))
    
#Ruta para Guardar
@albumsBP.route('/guardarAlbum', methods=['POST'])
def guardar():
    errores = {}

    titulo = request.form.get('txtTitulo', '').strip()
    artista = request.form.get('txtArtista', '').strip()
    anio = request.form.get('txtAnio', '').strip()

    if not titulo:
        errores['txtTitulo'] = 'Nombre del álbum obligatorio'
    if not artista:
        errores['txtArtista'] = 'Artista obligatorio'
    if not anio:
        errores['txtAnio'] = 'Año obligatorio'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2100:
        errores['txtAnio'] = 'Ingresa un año válido'

    if errores:
        return render_template('formulario.html', errores=errores, albums=getAll())

    try:
        insertAlbum(titulo, artista, anio)
        flash('Álbum guardado en la BD')
        return redirect(url_for('albums.home'))
    except Exception as e:
        flash('Error al guardar: ' + str(e))
        return redirect(url_for('albums.home'))
    
#Ruta para editar (abre el form)
@albumsBP.route('/editAlbum/<int:id>')
def editar(id):
    try:
        album = getById(id)
        
        if album:
            album_dicc = {'id': album[0], 'album' : album[1], 'artista' : album[2], 'anio' : album[3]}
            return render_template('formUpdate.html', album=album_dicc)
        else:
            flash('Album no encontrado.', 'warning')
            return redirect(url_for('albums.home'))
    except Exception as e:
        flash('Error al consultar para editar: ' + str(e))
        return redirect(url_for('albums.home'))
        
#Ruta para actualizar album
@albumsBP.route('/ActualizarAlbum/<int:id>', methods=['POST'])
def actualizar(id):
    errores = {}

    titulo = request.form.get('txtTitulo', '').strip()
    artista = request.form.get('txtArtista', '').strip()
    anio = request.form.get('txtAnio', '').strip()

    if not titulo:  
        errores['txtTitulo'] = 'Nombre del álbum obligatorio'
    if not artista:
        errores['txtArtista'] = 'Artista obligatorio'
    if not anio:
        errores['txtAnio'] = 'Año obligatorio'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2100:
        errores['txtAnio'] = 'Ingresa un año válido'

    if errores:
        return render_template('formUpdate.html', errores=errores, album={'id': id, 'album': titulo, 'artista': artista, 'anio': anio})

    try:
        updateAlbum(id, titulo, artista, anio)
        flash('Álbum actualizado correctamente')
        return redirect(url_for('albums.home'))
    except Exception as e:
        flash('Error al actualizar: ' + str(e))
        return redirect(url_for('albums.home'))

#Ruta confirmar delete
@albumsBP.route('/confirmaDel/<int:id>')
def confirmar_eliminar(id):
    try:
        album = getById(id)
        return render_template('confirmDel.html', album=album)
    except Exception as e:
        flash('Error al consultar para eliminar: ' + str(e))
        return redirect(url_for('albums.home'))
#Ruta ejecutar delete
@albumsBP.route('/EliminarAlbum/<int:id>')
def eliminar(id):
    try:
        softDeleteAlbum(id)
        flash('Álbum eliminado (soft delete)')
        return redirect(url_for('albums.home'))
    except Exception as e:
        flash('Error al eliminar: ' + str(e))
        return redirect(url_for('albums.home'))

