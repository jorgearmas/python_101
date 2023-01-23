"""
CRUD en lists:
    - Create
    - Read
    - Update
    - Delete

Operaciones a ejecutar con los elementos de lista
"""

#create por medio de declaración y asignación
numbers = [1, 2, 3, 4, 5]
print(numbers)

#Agregar elementos a una lista
#append(), 'append()' agrega elementos a partir de la ultima posición de la lista
numbers.append(70)
print(numbers)
#insert(), 'insert()' agregara elementos a posición especificada
numbers.insert(0, 'hola')
print(numbers)

#Fusion de listas
print(numbers) #lista 1
tasks = ['todo 1', 'todo 2', 'todo 3']
print(tasks) #lista 2
new_list = numbers + tasks
print(new_list) #nueva lista

#Eliminar elementos de una lista
#remove(), 'remove()' eliminara el elemento según su contenido
new_list.remove('todo 1')
print(f"'new_list' sin valor 'todo 1' {new_list}")
#pop(), 'pop()' eliminara el ultimo elemento de la lista
new_list.pop()
print(new_list)
#pop(x), 'pop(x)' eliminara el elemento según su posición
new_list.pop(0)
print(new_list)

#Verificar posición de elemento con index()
index = new_list.index("todo 2")
print(index)

#reverse(), 'reverse()' invertira el orden de la lista
new_list.reverse()
print(new_list)

#Ordenar elementos de una lista con sort(), sort() solo aplica para listas con valores des mismo tipo
#sort(), 'sort()' ordenar la lista de mayor a menor
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

#sort(), 'sort()' ordenar la lista alfabeticamente
strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)