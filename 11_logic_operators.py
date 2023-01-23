"""
Operadores lógicos
"""
#And - Conjunción
print("AND")
print("True and True -> ", True and True)
print("True and False -> ", True and False)
print("False and True -> ", False and True)
print("False and False -> ", False and False)

#Aplicación And
stock = int(input("Aplicación AND / Ingrese el stock: "))
print("Aplicación -> ", stock >= 100 and stock <= 1000)

#OR - Disyunción
print("\nOR")
print("True and True -> ", True or True)
print("True and False -> ", True or False)
print("False and True -> ", False or True)
print("False and False -> ", False or False)

#Aplicación Or
rol = input("Aplicación OR / Ingrese el rol: ")
print("Aplicación -> ", rol == 'admin' or rol == 'seller')