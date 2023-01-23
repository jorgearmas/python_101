"""
Indexación:
En una cadena de caracteres cada caracter tiene una posición dentro de la cadena 

Las cadenas de caracteres no se pueden modificar desde el index.

Slicing:
Extracción de substring a partir de una cadena
"""
#demostración del index
text = "Ella sabe Python"
print(f"Valor de posición [0]: {text[0]}")
print(f"Valor de posición [1]: {text[1]}")

#verificar valor de posición final
size = len(text)
print(f"Ultima posición de 'text': {text[size-1]}")

#demostración de slicing
print(f"Substring de 0 a 5: {text[0:5]}")
print(f"Substring de 10 a 16: {text[10:16]}")
print(f"Substring de inic a 10: {text[:10]}")
print(f"Substring de 5 a final: {text[0:5]}")
print(f"Substring completo de inicio a final: {text[:]}")

#saltos, indican el paso con el que se recorrera el string
#2 saltos - de posición 10 a 16
print(f"I: 10 - F:16 - Saltos: 2 / {text[::2]}")
#recorrido en reversa usando saltos
print(f"I - F - Saltos: -1 / {text[::-1]}")




