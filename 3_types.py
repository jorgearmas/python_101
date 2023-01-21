"""
Tipos de datos:
Dependiendo de las necesidades del flujo de ejecuacion de nuestro programa, vamos a necesitar distintos tipos de datos. Los principales tipos de datos primitivos son: string, integer y boolean

- String:
    Son una secuencia ordenada de elementos (caracteres) que pertenecen a un lenguaje formal (como el idioma Español). Los datos string contienen caracteres, asimismo pueden contener sub-strings (Fracciones de la cadena de caracteres)

- Int:
    Tipo de dato definido por un numero entero

- Boolean:
    Tipo de dato definido por un valor de verdad. Los datos boolean unicamente pueden contener un valor verdadero (True) o falso (False)

 Por defecto los valores ingresados en un input son recibidos como String.

 Python al ser un lenguaje no tipado no necesita que se declare un tipo de dato para cada variable. Las variables pueden tomar distintos tipos de datos en la ejecucion si es necesario.
"""

#String
my_name = "Santiago"
print(my_name)

#Int (Integer)
my_age = 20
print(my_age)

#boolean
is_a_student = True
print(is_a_student)

#demostracion input
my_age = input("Cual es tu edad? ")
print(my_age)
print(type(my_age)) #la funcion type imprime el tipo de dato de la variable
