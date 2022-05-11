class Posts():
    def __init__(self, 
                id=None, 
                fecha=None, 
                autor=None, 
                titulo=None, 
                cuerpo=None,
                etiquetas=None,
                categorias=None) -> None:
        self.id = id
        self.fecha = fecha
        self.autor = autor
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.etiquetas = etiquetas
        self.categorias = categorias
        

class T_Etiquetas():
    def __init__(self, id, nombre) -> None:
        self.id = id
        self.nombre = nombre

class T_Categorias():
    def __init__(self, id, nombre) -> None:
        self.id = id
        self.nombre = nombre