# 🧠 Guía Completa: Programación Orientada a Objetos en Python

## 🎯 Objetivo
Esta guía está diseñada para enseñar Programación Orientada a Objetos (POO) en Python desde cero, partiendo de conocimientos básicos del lenguaje.

---

# 📚 1. ¿Qué es la POO?

La Programación Orientada a Objetos es un paradigma que organiza el código en "objetos" que contienen datos (atributos) y comportamientos (métodos).

👉 Objetivo: modelar problemas reales de forma más natural.

---

# 🧱 2. Conceptos Base

## Clase
Plantilla para crear objetos.

## Objeto
Instancia de una clase.

## Atributos
Variables dentro de una clase.

## Métodos
Funciones dentro de una clase.

---

# 🏗️ 3. Ejemplo Base

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

persona1 = Persona("Juan", 25)
persona1.saludar()
```

---

# 🧬 4. Herencia

Permite crear nuevas clases a partir de otras.

```python
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
```

📌 Beneficio: reutilización de código

---

# 🔁 5. Polimorfismo

Mismo método, diferente comportamiento.

```python
class Perro:
    def sonido(self):
        print("Ladra")

class Gato:
    def sonido(self):
        print("Maulla")

animales = [Perro(), Gato()]

for animal in animales:
    animal.sonido()
```

---

# 🔒 6. Encapsulación

Controlar el acceso a los datos.

```python
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, monto):
        self.__saldo += monto

    def obtener_saldo(self):
        return self.__saldo
```

---

# 🔧 7. Mutadores (Getters y Setters)

Permiten modificar atributos de forma controlada.

```python
class Usuario:
    def __init__(self, edad):
        self.__edad = edad

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad

    def get_edad(self):
        return self.__edad
```

---

# ⚠️ 8. Manejo de Errores (try/except)

```python
try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("Error: Debe ingresar un número válido")
```

---

# 📦 9. Manejo de Archivos

## Leer archivo
```python
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
```

## Escribir archivo
```python
with open("datos.txt", "w") as archivo:
    archivo.write("Hola mundo")
```

---

# 🧩 10. Sobrecarga de Métodos

Python no soporta sobrecarga tradicional, pero se simula:

```python
class Calculadora:
    def sumar(self, a, b, c=0):
        return a + b + c
```

---

# 🧮 11. Métodos Especiales (Dunder)

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
```

---

# 🗺️ 12. Diagrama de Clases

Representación visual:

```
Persona
-----------------
- nombre
- edad
-----------------
+ saludar()

Empleado (hereda de Persona)
-----------------
- sueldo
-----------------
```

---

# 🧠 13. Buenas Prácticas

- Usar nombres claros
- Evitar clases gigantes
- Separar responsabilidades
- Usar encapsulación

---

# 🚀 14. Mini Proyecto Integrador

Sistema de Finanzas:

- Clase Transaccion
- Clase Ingreso
- Clase Gasto
- Clase Gestor

Incluye:
- Herencia
- Polimorfismo
- Archivos
- try/except

---

# 📅 15. Plan de Enseñanza

Día 1: Clases y objetos
Día 2: Herencia
Día 3: Polimorfismo
Día 4: Encapsulación
Día 5: Archivos + Proyecto

---

# 🎯 Conclusión

La POO permite construir sistemas escalables, organizados y reutilizables.

👉 El objetivo no es memorizar, sino entender cómo modelar problemas reales.
