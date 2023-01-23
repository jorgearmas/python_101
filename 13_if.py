"""
Condicional If:
La condicional If determina el flujo de ejecución del programa. If siempre es validado con una condición booleana
"""
#if
#Si la condicion es verdadera entonces se ejetara el bloque de código, de lo contrario no lo hara
pet = input("Cual es tu mascota favorita? ")
if pet == "perro":
    print("Que perro tan bonito!")

if pet == "gato":
    print("Que gato tan tierno!")

#if - else
#Si la condición es falsa entonces se ejecutara una otro bloque de código como salida alterna
stock = int(input("Digita el stock -> "))
if stock >= 100 and stock <= 1000:
    print(f"El stock: {stock} es suficiente")
else:
    print(f"El stock: {stock} no es suficiente")

#if - elif
#elif permite brindar multiples salidas de ejecución si la condición inicial es falsa
pet = input("Cual es tu mascota favorita? ")
if pet == "perro":
    print("Que perrito tan bonito!")
elif pet == "gato":
    print("Que gatito tan bonito!")
elif pet == "tortuga":
    print("Que tortuga tan bonita!")
else:
    print("Tu mascota no esta listada, pero estoy seguro de que es muy bonita!")
