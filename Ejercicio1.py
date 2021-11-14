class libro():

    #Creamos el constructor
    def __init__(self, nombre,autor,editorial,precioBase, genero, nPaginas):
        self.nombre = nombre
        self.autor= autor
        self.editorial= editorial
        self.precioBase= precioBase
        self.genero= genero
        self.nPaginas= nPaginas

    #Probamos que funciona
    libro= libro("El Palomo","Carlos Rodriguez","Edelvives","180","Aventuras","330")
