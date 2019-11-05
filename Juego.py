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
            print(str(self.clave) +")" +". Juego: " + str(self.juego) + " " + ". Consola: ")
            return self.consola
        elif(str(self.clave)==nombre):
            return self.juego
        else:
            return "No existe el juego"  

    def buscar_juegoConsola(self,consolas):
        if(self.consola==consolas):
            return self.juego
        else:
            return "No existe el juego en esa consola"    

    def JuegoRenta(self,nombre):
        if(self.juego==nombre):
            return self.clave
        else:
            return "No existe el juego" 

    def Juegos(self):
        print("Juego: "+str(self.juego))
        return self.consola