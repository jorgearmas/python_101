"""
Tuplas: 
Las tuplas son estructuras de datos inmutables que contienen una secuencia ordenada de elementos
"""

#declaración de lista
numbers = (1, 2, 3, 4, 5)
strings = ("Santi", "Dani", "Andy", "Luke", "Andy")
print(numbers)
print(type(numbers))
print(strings)
print(type(strings))

#acceder a valor de tupla por medio del indice
print(f"Valor en numbers[0]: {numbers[0]}")
print(f"Valor en numbers[-1] (valor final): {numbers[-1]}")

#verificar posición de un elemento
print(f"Posición de elemento 'Dani': {strings.index('Dani')}")

#contar concurrencia de un elemento en una tupla
print(f"Concurrencia de elemento 'Andy': {strings.count('Andy')}")

#convertir tupla a lista
my_lst = list(strings)
print(f"Tupla 'strings' coinvertida a lista: {my_lst}")

#convertir lista a tupla
my_tupl = tuple(my_lst)
print(f"Lista 'my_lst' convertida a tupla: {my_tupl}")