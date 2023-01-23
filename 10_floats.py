"""
Floats
"""
#Presición décimal
x = 3.3
y = 1.1 + 2.2

#Por presicón décimal la consola muestra que 'x' y 'y' son distintos
print(f"x -> {x}")
print(f"y -> {y}")

#Comparación decimal con str format
#Reducción de decimales en y. Se da formato a 'y' almacenandolo en una variable srt. El parámetro '2g' retorna el número de cifras significativas depues del decimal. 
y_str = format(y, ".2g")
print(y_str==str(x))

#Comparación decimal de forma matemática
#tolerance es el valor de toleracia a ser comparado
tolerance = 0.00001
#El valor absoluto del residuo de 'x' y 'y' es menor al valor de tolerancia
print(abs(x-y)<tolerance)