"""
CRUD en diccionarios:
    - Create
    - Read
    - Update
    - Delete

Operaciones a ejecutar con los elementos de lista
"""

#declaración de diccionario
#Create
person = {
    'name': 'Mike',
    'last_name': 'Wazowski',
    'langs': ['door', 'gate'],
    'age': 28
}
print(person)

#update - sobreescritura
person['name'] = 'Luke'

#update - valores númericos
person['age'] = 50

#add - agregar llave-valor no existente
person['code'] = 1
print(person)

#add - agregar valor a una llave
person['langs'].append('cave')
print(person)

#delete - eliminar elemento completo (clave-valor)
del person['code']
print(person)

#delete - eliminar elemento con pop(llave)
person.pop('age')
print(person)

#verificar items(elementos clave-valor)
print(person.items())

#verificar solo llaves del diccionario
print(person.keys())

#Verificar solo alores del diccionario
print(person.values())