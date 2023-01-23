"""
Strings recargados
"""
#Operador in, 'in' evalua si un substring o un caracter es parte de una cadena
text = "Ella sabe programar en Python"
if("Python" in text):
    print("La palabra 'Python' si se encuentra en la cadena de texto")
else:
    print("La palabra 'Python' no se encuentra en la cadena de texto")

#Método len(), 'len()' mide el número de caracteres en una cadena
size =  len(text)
print(f"Tamaño de 'size': {len(text)}")

#Método upper(), 'upper()' transforma toda la cadena a mayusculas
print(f"Variable 'text' convertida con upper(): {text.upper()}")

#Método lower(), 'lower()' transforma toda la cadena a  minusculas
print(f"Variable 'text' convertida con lower(): {text.lower()}")

#Método count(), 'count()' cuenta el numero de ocurrencias de un caracter o substring en un string
print(f"Variable 'text' contiene la letra 'a' {text.count('a')} veces")
print(f"Variable 'text' contiene la palabra 'Python' {text.count('Python')} veces")

#Método startswith(), 'startswith()' verifica si una cadena empieza con un caracter o substring especifico
print(f"La variable 'text' empieza con la letra 'P'? {text.startswith('E')}")

#Método endswith(), 'endswith()' verifica si una cadena termina con un caracter o substring específico
print(f"La variable 'text' termina con la palabra 'Python'? {text.endswith('Python')}")

#Método swapcase(), 'swapcase()' convierte caracteres minusculas en mayusculas y caracteres mayusculas en minusculas
print(f"Variable 'text' convertida a swapcase(): {text.swapcase()}")

#Método replace(), 'replace()' reemplazara un caracter o un substring por el que se le especifique
print(f"En variable 'text' reemplazar el substring 'Python' por 'Rust': {text.replace('Python', 'Rust')}")

#Metodo capitalize(), 'capitalize()' convierte el primer caracter del string a mayúscula
text_v2 = "este es un título2"
print(f"Variable 'text_v2' convertida con 'capitalize()': {text_v2.capitalize()}")

#Métofo tittle(), 'tittle()' convierte el primer caracter de cada palabra del string en Mayuscula
print(f"Variable 'text_v2' convertida con 'title()': {text_v2.title()}")

#Método isdigit(), 'isdigit()' verifica si la variable contiene un dígito, solo si ese digito esta definico como un string (no aplica para int y float)
digit = "0"
print(f"La variable 'text_2' es un dígito? {text_v2.isdigit()}")
print(f"La variable 'digit' es un dígito? {digit.isdigit()}")