'''Implementa un método constructor encargado de registrar los datos de un nuevo juego (clave, nombre,
tipo de consola, …, etc).
o Se cuenta con un mecanismo de búsqueda de juegos por nombre, el cual es recibidos como parámetros.
Se retorna como salida la información completa del juego'''

class Juego:

    def __init__(self,consola1):
        self.clave=int(input("ingresa la clave del juego: "))
        self.juego=input("ingresa el nombre del juego: ")
        self.consola=consola1
  
    def buscar_juego(self,nombre):
        if(self.juego==nombre):
            return  self.clave +")" +". Juego: " + self.juego + " " + ". Consola: " + self.consola
        else:
            return "No existe el juego"    