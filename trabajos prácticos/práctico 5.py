#punto 1
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#punto 2
lista = ["manzana", "banana", "naranja", "uva", "pera"]
print(lista[-2])  

#punto 3
lista_vacia = []
lista_vacia.append("perro")
lista_vacia.append("gato")
lista_vacia.append("conejo")
print(lista_vacia)

#punto 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#punto 5
#El programa trabaja con una lista llamada numeros la cual contiene 5 valores enteros: 8, 15, 3, 22 y 7. Ocurre lo siguiente:
# -Se usa la función max(numeros) que sirve para encontrar el número más grande dentro de la lista, la cual en este caso sería el 22.
# -Después, se usa remove() el cual elimina el valor máximo, es decir el 22, de la lista.
# -Por último, se usa print(numeros) para mostrar la lista actualizada sin el número 22

#punto 6
num = list(range(10, 31, 5))
print(num[:2])

#punto 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fiat"
autos[2] = "renault"
print(autos)

#punto 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#punto 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#punto 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)