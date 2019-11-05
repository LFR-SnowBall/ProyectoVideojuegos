'''Se debe almacenar la fecha, número de horas a contratar, consola rentada, nombre del cliente, el juego
que rento, estatus de la renta (activa o terminada).
o Para realizar la renta se debe mostrar la lista de consolas y solicitar al usuario ingrese la consola a rentar.
Al elegir la consola se muestra la lista de juegos disponibles para esa consola y se elige solo un juego.
o Se cuenta con un mecanismo para mostrar las rentas activas, indicando datos del cliente, nombre de la
consola, juego y duración de la renta.
o Se cuenta con un mecanismo para mostrar las rentas inactivas, indicando datos del cliente, nombre de la
consola, juego y duración de la renta.'''
#El archivo de renta es Dulceria
from datetime import datetime
import Videojuego as v
class Rentas:
    def __init__(self,consola1,juego1):
      self.clave=int(input("Clave de la renta: "))
      self.fecha=str(datetime.now().day)+" / "+str(datetime.now().month)+" / "+str(datetime.now().year)
      self.horas=int(input("Horas de la renta: "))
      self.consola=consola1
      self.cliente=input("Nombre del cliente: ")
      self.juego=juego1
      self.status="1"

    def reporte(self):
        return "Fecha: "+ str(self.fecha) + ". Cliente: " +str(self.cliente) + ". Horas : " +str(self.horas) 
    
    def cambiar_Status(self,consola,juego):#imprimir la cuentas activas
        if(str(self.consola)==str(consola) and str(self.juego)==str(juego)):
            return True
        else: return False
    def activo(self):
        if (str(self.status)=="1"):
            print ("Clave: "+str(self.clave) + ". Cliente: " +str(self.cliente)+". Consola: "+str(self.consola)+". Juego: "+str(self.juego))
        else:
            return "No hay activos"
    def inactivo(self):
        if (str(self.status)=="0"):
            print ("Clave: "+str(self.clave) + ". Cliente: " +str(self.cliente)+". Consola: "+self.consola+". Juego: "+self.juego)
        else:
         return "No hay Inactivos"
    
    def consola(self,consola):
        if(str(self.consola)==str(consola)):
            return self.horas
        else: "Nose encuentra la consola trabajando"