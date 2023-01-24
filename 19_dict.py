"""
Diccionarios:
Son estructuras de datos que nos permiten alamacenar parejas clave-valor (key - values). Los diccionarios son estructuras de datos mutables
"""

#declaracón de diccionario
my_dict = {
    'name': 'Obi-Wan',
    'last_name': 'Kenobi',
    'age': 57
}

print(my_dict)
print(type(my_dict))

#verificar el numero de elementos en un diccionario
print(f"Numero de elementos en 'my_dict': {len(my_dict)}")

#verificar el valor de la llave
print(f"Valor de llave 'name': {my_dict['name']}")
print(f"Valor de llave 'last_name': {my_dict['last_name']}")
print(f"Valor de llave 'age': {my_dict['age']}")

#verificar el valor de la llave con get()
print(f"Valor de la llave con get(): {my_dict.get('age')}")

#verificar si una llave esta en un diccionario
print(f"La llave 'last_name' esta en 'my_dict': {'last_name' in my_dict}")
