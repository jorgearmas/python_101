"""
Ciclo for:
En el ciclo for se itera con un número de iteraciones pre-establecidas

for element in range(1, 21):
    print(element)
"""

#recorriendo listas con for
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)

#recorriendo tuplas con for
my_tuple = ('nico', 'kick', 'ben')
for element in my_tuple:
    print(element)

#recorriendo diccionario (clave-valor) con for
product = {'name': 'Camisa', 'precio': 100, 'stock': 89}
for key, value in product.items():
    print(f"{key} => {value}")

#recorriendo una lista que contiene diccionarios
print("")
people = [
  {
    'name':'nico',
    'age':34
  },
  {
    'name':'zule',
    'age':45
  },
  {
    'name':'santi',
    'age':4
  },
]

#en el primer ciclo convertimos a 'person' en un diccionario
for person in people:
    for key, val in person.items():
        print(f"key: {key} -> age: {val}")
    print("-----------")
