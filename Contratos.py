#Es Cine
import Videojuego as vj
import Renta as r
import Juego as j
class Contratos:
    funciones=[]
    rentas=[]#dulces
    juegos=[] 
    activos=[]
    inactivoss=[]
    def registrar_consola(self):
        consola=vj.Consola()
        self.funciones.append(consola)

    '''def MostrarCuenta_Activa(self):
        activa=r.activo()
        self.activos.append(activa)

    def MostrarCuenta_Inactiva(self):
        inactivos=r.inactivo()
        self.inactivo.append(inactivos)'''
    
    
    def registrar_juegos(self,consola1):
        juego=j.Juego(consola1)
        self.juegos.append(juego)

    
    def registrar_renta(self,consola1,juego1):
        servicio=r.Rentas(consola1,juego1)
        self.rentas.append(servicio)

    def ganancias_por_consola(self):
        ganancias=dict()
        total=0
        for i in range(0,len(self.rentas)):
            rentas=self.rentas[i].producto
            ingresos=self.rentas[i].total
            if(rentas not in ganancias):
                ganancias[rentas]=ingresos
            else:
                ganancias[rentas]=ganancias[rentas]+ingresos
            total+=ingresos
        for clave in ganancias:
            print("Renta: ",clave,"Total: ",ganancias[clave])
        print("ingresos total:",total) 
    
    def obtenerGanancias(self):
        ganancias=dict()
        total=0
        for i in range(0,len(self.funciones)):
            consola=self.funciones[i].consola
            ingresos=self.funciones[i].total
            if(consola not in ganancias):
                ganancias[consola]=ingresos
            else:
                ganancias[consola]=ganancias[consola]+ingresos
            total+=ingresos
        for clave in ganancias:
            print("Consola:",clave,"Total:",ganancias[clave])
        print("Ingresos totales:",total)

    def obtenerGananciasCorto(self):
        ganancias=dict()
        total=0
        for i in range(0, len(self.funciones)):
            pelicula=self.funciones[i].pelicula
            ingresos=self.funciones[i].total
            ganancias[pelicula]=ganancias.get(pelicula,0)+ingresos
            total+=ingresos

            for clave in ganancias:
                print("pelicula:",clave,"Total: ",ganancias[clave])
            print("Ingresos Totales: ",total)