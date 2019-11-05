'''Clase Consola:
o Implementa un método constructor encargado de registrar los datos de una nueva consola (clave,
nombre, número de consolas disponibles, costo de renta por hora, …, etc).
o Se cuenta con un mecanismo de búsqueda de consolas nombre, el cual es recibidos como parámetros. Se
retorna como salida la información completa de la consola.
o Cuando una consola es rentada, será necesario validar la existencia y se decrementar la existencia en uno.
o Para funciones de inventario, se cuenta con un mecanismo que retorna la clave, nombre y existencia de
la consola.'''
class Consola:
    def __init__(self):
      self.clave=int(input("ingresa la clave de la consola: "))
      self.consola=input("ingresa el nombre de la consola: ")
      self.consolas_disponibles=input("Consolas disponibles: ")
      self.precio=int(input("ingresa el costo de renta por hora: "))
    
    def consultar(self,nombre):
        if(self.consola==nombre):
            return "Clave: "+ str(self.clave) + ". Consola: " + str(self.consola) + " " + ". Costo por hora: " + str(self.precio)
        elif(str(self.clave)==nombre):
            return self.consola
        else:
            return "No existe la consola"
    def consultarganancia(self,nombre):
        if(self.consola==nombre):
            return self.precio
        else:
            return "No existe la consola"
    def ConsolaRenta(self,nombre):
        if(self.consola==nombre):
            return self.clave
        else:
            return "No existe la consola"
    def RegistrarJuegoConsola(self,nombre):
        if(self.consola==nombre):
            return str(self.clave)
        else: return None
    def consulta(self):
            return "Clave: "+ str(self.clave) + ". Consola: " +str(self.consola) +" Disponibles:"+str(self.consolas_disponibles)+" Precio de renta:"+ str(self.precio)
    def Consolas(self):
        return str(self.consola)   

    def contratar(self,clv,cantidad):
        if(self.clave==clv):
            if self.consolas_disponibles-(cantidad)>=0:
               self.total=self.total+(cantidad*self.precio)
               self.consolas_disponibles=self.consolas_disponibles-cantidad
               print("Productos restantes: "+str(self.consolas_disponibles))
               print("Ganancias: "+str(self.total))
            else:
                print("No hay suficientes Consolas")
    
    def inventario(self):
            return self.consola