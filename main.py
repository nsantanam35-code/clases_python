#clase persona tiene que ser en mayusculas y con la palabra reservada class 

class Telefono:
    pass


class Persona:   # j  , j,    34
    def __init__(self,nombre,edad,rut):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut

    def saludar(self):
        print(f"hola mi nombre es : {self.nombre} y tengo {self.edad}")

    def cumplir_anios(self):
        self.edad += 1

    def verificar_rut(self):
        if self.rut == 0:
            pass
     
#instancia
juanito = Persona("juanito", 34, 1111111111)
carlos = Persona("carlos", 32,2222222222)

print(juanito.cumplir_anios())
print(juanito.verificar_rut())
print(juanito.saludar())









        



      



    


