"""
Ciclo:
Los ciclos son una herramienta que nos permite repetir una instruccion de codigo hasta que una condicion se cumpla o se deje de cumplir. Sintaxis:

while True: --> Mientras la condición, el código se ejecuta
    print('Mensaje de ejecución')
"""
#declaración del ciclo
counter = 0
while counter < 10:
    print(counter)
    counter += 1 #'counter' controla la ejecuación del ciclo

#forzar a romper la iteración con break
print("break")
counter = 0
while counter < 20:
    counter += 1
    #el ciclo se interrumpira cuando 'counter' llegue a 15
    if counter == 15:
        break 
    print(counter)

#saltarse una iteración con continue
print("continue")
counter = 0
while counter < 20:
    counter += 1
    #se obviaran las iteraciones en donde 'counter' < 15   
    if counter < 15:
        continue
    print(counter)
