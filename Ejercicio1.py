class Libro():


    #Creamos el constructor
    def __init__(self, nombre,autor,editorial,precioBase, genero, nPaginas):
        self.nombre = nombre
        self.autor= autor
        self.editorial= editorial
        self.precioBase= precioBase
        self.genero= genero
        self.nPaginas= nPaginas



libro =  Libro("El Palomo","Carlos Rodriguez","Edelvives","180","Aventuras","330")
print(libro.nombre,libro.autor, libro.editorial,libro.precioBase,libro.genero,libro.nPaginas)