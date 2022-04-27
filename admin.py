from bottle import static_file,route,run,jinja2_view,TEMPLATE_PATH,TEMPLATES,request
from settings import STATIC_FILES,BD
from sql import Sql

TEMPLATE_PATH.append(TEMPLATES)

def modifica_fecha(lista_tuplas):
    salida = []
    tmp_tupla = ()
    pass

@route('/static/<filename:path>')
def server_static(filename):
    archivo = static_file(filename, root=STATIC_FILES)
    return archivo

@route('/')
@jinja2_view('admin_index.html')
def home():
    basedatos = Sql(BD)
    resp = basedatos.select('select p.id,p.fecha,p.autor,p.titulo,p.cuerpo from posts p')
    return {'posts':resp}

@route('/editar')
@route('/editar/<id:int>')
@jinja2_view('admin_formu.html')
def mi_form(id=None):
    basedatos = Sql(BD)
    if id:
        resp = basedatos.select(f'select p.id,p.fecha,p.autor,p.titulo,p.cuerpo from posts p where p.id={id}')
    return {'posts':resp}

@route('/guardar',method='POST')
def guardar():
    id = request.POST.id
    fecha = request.POST.fecha
    autor = request.POST.autor
    titulo = request.POST.titulo
    cuerpo = request.POST.cuerpo
    pass

run(host='localhost', port=8002,debug=True,reloader=True)
