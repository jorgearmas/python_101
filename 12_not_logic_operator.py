"""
Not:
Not es un operador lógico que niega o invierte valores de verdad.
"""

#Not aplicado a AND
print("NOT - AND")
print("Not - True and True => ", not(True and True))
print("Not - True and False => ", not(True and False))
print("Not - False and True => ", not(False and True))
print("Not - False and False => ", not(False and False))

#Aplicación not - and
stock = int(input("Aplicación NOT - AND / Ingrese el stock: "))
print("Aplicación -> ", not(stock >= 100 and stock <= 1000))

#Not aplicado a OR
print("\nNOT - OR")
print("Not - True or True => ", not(True or True))
print("Not - True or False => ", not(True or False))
print("Not - False or True => ", not(False or True))
print("Not - False or False => ", not(False or False))

#Aplicación not - or
rol = input("Aplicación NOT - OR / Ingrese el rol: ")
print("Aplicación -> ", not(rol == 'admin' or rol == 'seller'))