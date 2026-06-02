
#error
#try y el except



""" try:  #intenta ejecutar esto
    lista = [1,2,3,4,5,6,7,8]
    print(lista[20])
except IndexError: # si el bloque anterior de try tiene errores  esto captura el error especifico lo muestra en pantalla cli y continua con la ejecucion
     print(f"indice fuera de rango")


try:
    a = int(input("ingresa un numero:"))
    b = int(input("ingrese un numero:")) 
    resultado = a/b
    print(resultado)
except SyntaxError:
    print("error de sistaxis en python")
except ValueError:
    print("solo numeros plz")
except ZeroDivisionError:
    print("no se puede  dividir por 0 plz")
 """




#try y el except

#raise, else finally

# regla: que la edad sea superior o igual a 0



""" try: # el try  ejecutara el bloque 
    edad = int(input("ingresa tu edad:"))
    if edad < 0:
        raise ValueError("raise: error de edad menor a 0")#el raise  forza el error si la validacion salio mal 
    
except Exception as e: #la clase exception captura todos los errores del bloque
    print(f"exception: error capturado desde el bloque try : {e}")

else: # el else se ejecuta si todo salio bien y no hay errores
    print("else : todo salio bien felicidades!!!!!!")

finally:
    print("finally: proceso terminado y completado con o sin fallas con manejo de errores!!!")

 """
import re

try:
    nombre = input("ingrese su nombre")
    nota = float(input("ingrese su nota"))

    if re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ]+$', nombre):
        print("esto es un nombre valido")
    else:
        raise re.error("error de regex")

    #validar nota
    if nota < 1 or nota > 7:
        raise ValueError("la nota debe ser entre 1 y 7")
    
    #open, abrir el archivo en modo append
    archivo = open("notas.txt", "a")


except Exception as e:
    print(f"errores capturados desde el bloque try : {e}")

else:
    #esto se va a ejecutar si todo salio bien 
    archivo.write(f"{nombre},{nota}")
    print("datos guardados en el archivo correctamente")

finally:
    try:
        archivo.close()
        print("archivo cerrado!!")
    except NameError:
        print("no se puede cerrar un archivo que no existe")






        












    











