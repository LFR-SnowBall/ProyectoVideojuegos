'''Se debe almacenar la fecha, número de horas a contratar, consola rentada, nombre del cliente, el juego
que rento, estatus de la renta (activa o terminada).
o Para realizar la renta se debe mostrar la lista de consolas y solicitar al usuario ingrese la consola a rentar.
Al elegir la consola se muestra la lista de juegos disponibles para esa consola y se elige solo un juego.
o Se cuenta con un mecanismo para mostrar las rentas activas, indicando datos del cliente, nombre de la
consola, juego y duración de la renta.
o Se cuenta con un mecanismo para mostrar las rentas inactivas, indicando datos del cliente, nombre de la
consola, juego y duración de la renta.'''
#El archivo de renta es Dulceria
import Videojuego as v
class Rentas:
    def __init__(self,consola1,juego1):
      self.clave=int(input("Clave de la renta: "))
      self.fecha="31/10/19"
      self.horas=int(input("Horas de la renta: "))
      self.consola=(consola1)
      self.cliente=input("Nombre del cliente: ")
      self.juego=(juego1)
      self.status="Activo"

    def reporte(self):
        return "Fecha: "+ str(self.fecha) + ". Cliente: " +str(self.cliente) + ". Horas : " +str(self.horas)  + ". Juego: " + str(self.juego) 
    
    def cambiar_Status(self):#imprimir la cuentas activas
        self.status="inactivo"

    def activo(self):
        if self.status=="Activo":
            return "Clave: "+ str(self.clave) + ". Cliente: " +str(self.cliente) 
        else:
            return ""
            
    def inactivo(self):
        if self.status=="Inactivo":
            return "Clave: "+ str(self.clave) + ". Cliente: " +str(self.cliente) 
        else:
         return ""
    