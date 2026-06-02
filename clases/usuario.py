

class Usuario:
    def __init__(self,username, email,password, activo):
        self.username = username
        self.email = email
        self.password = password
        self.activo = activo
    def datos_del_user(self):
        print(f"nombre:{self.username} email: {self.email} activo: {self.activo}")
    def login(self, passw):
        if self.password !=  passw:
            print("password incorrecta")
        else:
            print("password correcta")
    def desactivar(self):
        self.activo = False


usuario1 =  Usuario("juanito" , "correo@correo.cl" , "1234" , True)

usuario1.datos_del_user()
usuario1.login("1234")




        