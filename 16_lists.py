"""
Listas:
Las listas son estructuras de datos que alamacenan valores de distintos tipos de datos
"""
#delaración de lista
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

#lista con elementos de distinto tipo
types = [1, True, "hola"]
print(types)
print(type(types))

#indexación en listas
print(f"Valor en posicion numbers[0]: {numbers[0]}")
print(f"Valor en posicion types[0]: {types[0]}")

#las listas se peden modificar con la indexación
types[0] = 2
print(f"Modificación de types[0]: {types[0]}")

#slicing con listas
print(f"Slicing de numbers I:0 a F:3 - {numbers[0:3]}")

#operador in en lists
print(f"Esta el elemento 'False' en lista 'numbers': {False in numbers}")
print(f"Esta el elemento '2' en lista 'types': {2 in types}")