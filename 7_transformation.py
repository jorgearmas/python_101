"""
Transformaciones de datos:
Una transformación se da cuando transformamos el valor de una variable a otro tipo de dato
"""
#transformación dinámica de datos
var = "Luke"
print(var)
print(type(var))

var = 12
print(var)
print(type(var))

var = True
print(var)
print(type(var))

#transformación Entero (int) a String (str)
age = 12
print(age)
print(type(age))

age = str(age) #variable age guarda la transformación srt de la variable age
print(age)
print(type(age))

#transformación String (str) a Entero (int)
random_num = "20"
print(random_num)
print(type(random_num))

random_num = int(random_num) #variable random_num guarda la transformación int de la variable random_num age
print(random_num)
print(type(random_num))

#transformación desde el input
age = int(input("Escribe tu edad: "))
print(age)
print(type(age))