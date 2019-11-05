'''Administra las listas de consolas y juegos y rentas registradas.
o Para fines de administración del negocio, cuenta con las funciones necesarias para generar los siguientes
reportes:
§ Ganancias por consola (cada renta tiene una consola la cual tiene costo por hora).
§ Ganancias totales.
o Para cerrar una renta, se deberá mostrar en pantalla la lista de rentas activas y el usuario seleccionará la
renta a cerrar.
o Ofrece un menú con las siguientes funciones:
§ Registrar Consola
§ Buscar Consola
§ Ver consolas
§ Registrar Juego
§ Buscar Juego
§ Rentar
§ Terminar renta
§ Ver rentas activas
§ Ver rentas inactivas
§ Generar reporte:
• Ganancias por consola.
• Ganancias totales'''
import Contratos as j
import Renta as r
class Principal:

    def __init__(self):
        self.obj_contrato=j.Contratos()

    def menu(self):
        self.obj_contrato=j.Contratos()
        print("\n-------------------| Bienvenido |------------------")
        self.ciclo=True
        #i1=True
        #i2=True
        i3=True
        i4=True
        i5=True
        while (self.ciclo==True):
            i3=True
            i4=True
            print("\n1) Registrar consola")
            print("2) Buscar consola")
            print("3) Ver consolas")
            print("4) Registrar juego")
            print("5) Buscar juego")
            print("6) Ver juegos")
            print("7) Rentar")
            print("8) Terminar renta")#status inactivo
            print("9) Ver rentas activas")
            print("10) Ver rentas inactivas")
            print("11) Generar reporte")
            print("12) Salir\n")
            self.opcion=int(input("*Ingresa una opcion: "))
            if(self.opcion==1):
                print("Registar Consola")
                self.obj_contrato.registrar_consola()
                print("________________________________")
               
            elif(self.opcion==2):
                print("Buscar Consola")
                self.busqueda=input("Nombre de la consola: ")
                for i in range(0, len(self.obj_contrato.funciones)):
                    self.resultado=self.obj_contrato.funciones[i].consultar(self.busqueda)
                    if(self.resultado!=None):
                        print("\n"+self.resultado)
                print("________________________________")

            elif(self.opcion==3):
                print("Ver Consolas")
                for i in range(0, len(self.obj_contrato.funciones)):
                    self.resultado=self.obj_contrato.funciones[i].consulta()
                    if(self.resultado!=None):
                        print("\n"+self.resultado)
                print("________________________________")

            elif(self.opcion==4):
                print("Registar Juego\n\nConsolas: ")
                for i in range(0,len(self.obj_contrato.funciones)):
                    self.resultado=self.obj_contrato.funciones[i].Consolas()
                    if(self.resultado!=None):
                        print(self.resultado)
                self.Console=input("Nombre de la Consola: ")
                for i in range(0,len(self.obj_contrato.funciones)):
                    self.resultado=self.obj_contrato.funciones[i].RegistrarJuegoConsola(self.Console)
                    if(self.resultado!=None):
                        self.obj_contrato.registrar_juegos(self.resultado)

                print("_____________________________")


                #self.obj_contrato.registrar_juegos()
            elif(self.opcion==5):
                print("Buscar Juego")
                self.busqueda=input("Nombre del juego: ")
                for i in range(0, len(self.obj_contrato.funciones)):
                    self.resultado=self.obj_contrato.juegos[i].buscar_juego(self.busqueda)
                    if(self.resultado!=None):
                        for i in range(0, len(self.obj_contrato.funciones)):
                            self.resultado2=self.obj_contrato.funciones[i].consultar(self.resultado)
                        if(self.resultado2!=None):
                            print(self.resultado2)
                print("________________________________")
            
            elif(self.opcion==6):
                print("Juegos")
                for i in range(0,len(self.obj_contrato.juegos)):
                    self.resultado=self.obj_contrato.juegos[i].Juegos()
                    if(self.resultado!=None):
                        for i in range(0, len(self.obj_contrato.funciones)):
                            self.resultado2=self.obj_contrato.funciones[i].consultar(self.resultado)
                        if(self.resultado2!=None):
                            print("Consola: "+self.resultado2)


            elif(self.opcion==7):
                print("Rentar")
                for i in range(0,len(self.obj_contrato.funciones)):
                    self.resultado=self.obj_contrato.funciones[i].Consolas()
                    if(self.resultado!=None):
                        print(self.resultado)
                self.Consola=input("Ingresa la consola a rentar: ")
                for i in range(0,len(self.obj_contrato.funciones)):
                    self.resultado=self.obj_contrato.funciones[i].RegistrarJuegoConsola(self.Consola)
                if(self.resultado!=None):
                    for i in range(0, len(self.obj_contrato.funciones)):
                        self.resultado2=self.obj_contrato.juegos[i].buscar_juegoConsola(self.resultado)
                        print(self.resultado2)
                    if(self.resultado2!=None):
                        self.Juego=input("Ingresa el juego que se rentara: ")
                self.obj_contrato.registrar_renta(self.Consola,self.Juego)


                print("________________________________")
            elif(self.opcion==8):
                print("Terminar Renta")
                self.Consola=input("Consola con la que terminara actividad: ")
                self.Juego=input("Juego con el que terminara la actividad: ")
                for i in range(0,len(self.obj_contrato.rentas)):
                    self.resultado=self.obj_contrato.rentas[i].cambiar_Status(self.Consola,self.Juego)
                    if(self.resultado==True):
                        self.obj_contrato.rentas[i]="0"
                        print("Cambio realizado")
                    else: print("Consola o juego no encontrados activos")


                print("________________________________")
            elif(self.opcion==9):
                print("Rentas Activas")
                for i in range(0,len(self.obj_contrato.rentas)):
                    self.resultado=self.obj_contrato.rentas[i].activo()
                    if(self.resultado!=None):
                        print(str(self.resultado))
                print("________________________________")
               
            elif(self.opcion==10):
                print("Rentas Inactivas")
                for i in range(0,len(self.obj_contrato.rentas)):
                    self.resultado=self.obj_contrato.rentas[i].activo()
                    if(self.resultado!=None):
                        print(self.resultado)
                print("________________________________")
            elif(self.opcion==11):
                #errores
                print("Generar reporte")
                while i5==True:
                    print("\n1) Ganancias por consola")
                    print("2) Imprimir inventario")
                    print("3) Buscar Producto")
                    self.op=int(input("Ingresa una opcion: "))
                    if self.op==1:
                        self.resultadoX=0
                        print("Ganancias por consola")
                        self.busqueda=input("Nombre de la consola: ")
                        for i in range(0, len(self.obj_contrato.funciones)):
                            self.resultado=self.obj_contrato.funciones[i].consultarganancia(self.busqueda)
                            if(self.resultado!=None):
                                for i in range(0,len(self.obj_contrato.rentas)):
                                    self.resultadoX+=self.obj_contrato.rentas[i].consola(self.busqueda)
                        if(self.resultado2!=None):
                            self.total=self.resultadoX*self.resultado
                            print(str(self.total))
                        print("________________________________")
                    
                    elif self.op==2:
                        print("Ganancias Totales")

                        print("________________________________")
                    else:
                        i4=False

            else:
                self.ciclo=False
                print("-----------------------------------| Adiós |-------------------------------")

p=Principal()
p.menu()