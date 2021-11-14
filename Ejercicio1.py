class Libro():


    #Creamos el constructor
    def __init__(self, titulo,autor,editorial,precioBase, genero, nPaginas):
        self.titulo = titulo
        self.autor= autor
        self.editorial= editorial
        self.precioBase= precioBase
        self.genero= genero
        self.nPaginas= nPaginas

    #Metodos get y set
    def setTitulo(self,titulo):
        self.titulo= titulo
    def setAutor(self,autor):
        self.autor= autor
    def setEditorial(self,editorial):
        self.editorial= editorial
    def setPrecioBase(self,precioBase):
        self.precioBase= precioBase
    def setGenero(self,genero):
        self.genero= genero
    def setNPaginas(self,nPaginas):
        self.nPaginas= nPaginas
    def getTitulo(self):
        return self.titulo
    def getAutor(self):
        return self.autor
    def getEditorial(self,editorial):
        return self.editorial
    def getPrecioBase(self,precioBase):
        return self.precioBase
    def getGenero(self):
        return self.genero
    def getNPaginas(self):
        return self.nPaginas

libro =  Libro("El Palomo","Carlos Rodriguez","Edelvives","180","Aventuras","330")
print("Titulo:"+libro.titulo,"Autor:"+libro.autor, "Editorial:"+libro.editorial,"Precio base:"+libro.precioBase,"Género:"+libro.genero,"Número de páginas:"+libro.nPaginas)