import json

class Transaccion:
    
    def __init__(self, monto,descripcion):
        self.__monto = monto
        self.descripcion = descripcion
    
    def get_monto(self):
        return self.__monto      
    
    def set_monto(self,monto):
        if monto > 0:
           self.__monto = monto
        else:
           print("monto ingresado es 0 o menor de 0")

    def tipo(self):
        return "Transaccion"
        
    def mostrar(self):
        return f"{self.descripcion} - {self.get_monto()} - {self.tipo()} "
    
    def __str__(self):
        return f"{self.descripcion} - {self.get_monto()} - {self.tipo()} "
        
    
#pago1 = Transaccion(100, "pago banco")
#print(pago1)
#print(pago1.mostrar())

class Ingreso(Transaccion):
    #polimorfismo del metodo tipo de la clase transaccion 
    def __init__(self, monto, descripcion):
        super().__init__(monto, descripcion)
    def tipo(self):
        return "Ingreso"
        
        
class Egreso(Transaccion):
    #polimorfismo del metodo tipo de la clase transaccion 
    def tipo(self):
        return "Egreso"

class GestorFinanzas:
    def __init__(self):
        self.transacciones = [] #lista vacia
        

    def agregar(self,transaccion):
        if not isinstance(transaccion, Transaccion):
            raise TypeError("Debe ser una transaccion valida")
        self.transacciones.append(transaccion)
        print(f"transaccion agregada de tipo {type(transaccion)}")

    def mostrar_todo(self):
        return [t.mostrar() for t in self.transacciones]
        

    def calcular_balance(self):
        balance = 0
        for transaccion in self.transacciones:
            if not isinstance(transaccion, Ingreso):
                balance += transaccion.get_monto()
                print(balance)
            else:
                balance -= transaccion.get_monto()
                print(balance)
        return balance
            
    def guardar_en_archivo(self, archivo="archivo.txt" ):
        data = [{
            "tipo":transaccion.tipo(),
            "monto":transaccion.get_monto(),
            "descripcion":transaccion.descripcion
        } 
        for transaccion in self.transacciones
        ]

        with open(archivo,"w") as w:
            pass


    def importar_del_archivo(self):
        pass
    
    

#instanciando  objetos de tipo transaccion    
ingreso1 = Ingreso(1000,"ingreso")
ingreso2 = Ingreso(10000,"ingreso")
ingreso3 = Ingreso(1030,"ingreso")
ingreso4 = Ingreso(10029,"ingreso")
egreso1 = Egreso(10044, "dasdda")
egreso2 = Egreso(1002, "dasdda")
egreso3 = Egreso(100200, "dasdda")




#instancia de tipo gestor
gestor = GestorFinanzas()



#agregando a la lista de la clase gestor 
gestor.agregar(egreso1)
gestor.agregar(ingreso1)
gestor.agregar(egreso2)
gestor.agregar(ingreso2)
gestor.agregar(egreso3)
gestor.agregar(ingreso3)
gestor.agregar(ingreso4)
gestor.calcular_balance()
print(gestor.mostrar_todo())



