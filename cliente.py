from bottle import static_file,route,run,jinja2_view,TEMPLATE_PATH,redirect,request
from settings import STATIC_FILES,BD, TEMPLATES
from sql import Sql
from clase_post import Posts
from datetime import datetime


TEMPLATE_PATH.append(TEMPLATES)

def modifica_fecha(lista_tuplas):
    salida = []
    tmp_tupla = ()
    for t in lista_tuplas:
        cadena_fecha = ''
        partes = t[1].split('-')
        cadena_fecha = partes[2] + ' de ' + partes[1] + ' de ' + partes[0]
        tmp_tupla = (t[0], cadena_fecha, t[2],t[3],t[4])
        salida.append(tmp_tupla)
    return salida

@route('/static/<filename:path>')
def server_static(filename):
    archivo = static_file(filename, root=STATIC_FILES)
    return archivo

@route('/')
@jinja2_view('index.html')
def home():
    basedatos = Sql(BD)
    posts = basedatos.select('select * from posts')
    posts = modifica_fecha(posts)
    return {'posts':posts}

@route('/post/<id:int>')
@jinja2_view('post.html')
def ver_post(id):
    basedatos = Sql(BD)
    posts = basedatos.select(f'select * from posts where id={id}')
    etiquetas = posts[0][5].split(',')
    categorias = posts[0][6].split(',')
    return {'post':posts[0], 'Etiquetas': etiquetas, 'Categorias': categorias}


# PARTE DE ADMINISTRACIÓN

@route('/admin/')
@jinja2_view('admin_index.html')
def home():
    bdatos = Sql(BD)
    posts = bdatos.select('SELECT  p.id, p.fecha, p.autor ,p.titulo, p.cuerpo,p.etiquetas,p.categorias from posts p')
    posts = modifica_fecha(posts)
    return {'posts' : posts}

@route('/admin/editar')
@route('/admin/editar/<id:int>')
@jinja2_view('admin_formu.html')
def mi_form(id=None):
    bdatos = Sql(BD)
    posts = None
    # etiquetas = bdatos.select('select id, nombre from T_etiquetas;')
    # categorias = bdatos.select('select id, nombre from T_categorias;')
    if id:
        posts = bdatos.select(f'SELECT  p.id, p.fecha, p.autor ,p.titulo, p.cuerpo,p.etiquetas,p.categorias from posts p where id = {id}')
    
    #posts = modifica_fecha(posts)
    if posts:
        # return {'post' : posts[0],
        #         'etiquetas':etiquetas,
        #         'categorias':categorias,
                
        # }
        return {'post' : posts[0]}
    else:
        return {'post': ''}


@route('/admin/guardar', method='POST')
def guardar():
    if request.POST.id:
        id = request.POST.id
    else:
        id = None

    fecha = request.POST.fecha
    autor = request.POST.autor
    titulo = request.POST.titulo
    cuerpo = request.POST.cuerpo
    etiquetas = request.POST.etiquetas
    categorias = request.POST.categorias

    p = Posts(id,fecha, autor, titulo, cuerpo, etiquetas, categorias)

    bdatos = Sql(BD)
    if request.POST.id:
        posts = bdatos.update(p)
    else:
        posts = bdatos.insert(p)

    redirect('/admin/')

@route('/admin/borrar')
@route('/admin/borrar/<_id:int>')
def borrar(_id):
    p = Posts(id=_id)
    bdatos = Sql(BD)
    bdatos.delete(p)

    redirect('/admin/')
    

@route('/admin/post')
@route('/admin/post/<id:int>')
@jinja2_view('admin_formu.html')
def ver_post(id=None):
    if id:
        bdatos = Sql(BD)
        posts = bdatos.select(f'select * from posts where id={id}')
        return {'post' : posts[0]}
    else:
        return {'post':None}


run(host='localhost', port=8000,debug=True,reloader=True)
