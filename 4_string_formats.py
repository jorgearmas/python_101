"""
Formatos (Formats):
Los formatos de string nos permiten modelar el ourput de los datos de tipo string
"""
#variables string
name = "Nicolas"
last_name = "Molina"
age = "12"

#concatenacion de strings con operador adición (+)
full_name = name+" "+last_name+" - edad: "+age #se agregan caracteres (incluyendo space) con operador adición
print(full_name)

#formatos
#formato con concatenacion
template = "Nombre: "+name+" Apellido: "+last_name+" Edad: "+age
print(template)

#formato con .format
template = "Nombre: {} Apellido: {} Edad: {}".format(name, last_name, age)
print(template)

#format con f
template = f"Nombre: {name} Apellido: {last_name} Edad: {age}"
print(template)