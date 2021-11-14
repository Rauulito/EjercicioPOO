#Ponemos los atributos para que no salte error al declarar la clase
class Animal():
    def __init__(self, nombre):
            self.nombre= nombre
class Mamifero(Animal):
    def __init__(self, edad):
            self.edad= edad
class Oviparo(Animal):
    def __init__(self, edad):
            self.edad= edad
class Pollo(Oviparo):
    def __init__(self, hijos):
            self.hijos=hijos
class Gato(Mamifero):
    def __init__(self, vidas):
            self.vidas= vidas
class Ornitorrincno(Mamifero, Oviparo):
    def __init__(self, hermanos):
            self.hermanos= hermanos

