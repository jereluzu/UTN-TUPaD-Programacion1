#punto 1
for numero in range(101):
    print(numero)

#punto 2
num = int(input("ingrese un número: "))
if num == 0:
    digitos = 1
else: 
    digitos = 0
    temp = num
    while temp > 0:
        temp = temp // 10
        digitos += 1
print(f"El número tiene {digitos} dígitos.")

#punto 3
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
if valor1 > valor2:
    valor1, valor2 = valor2, valor1  
suma = 0
for num in range(valor1 + 1, valor2):
    suma += num
print(f"La suma entre {valor1} y {valor2} (excluyéndolos) es: {suma}")

#punto 4 
suma = 0
while True:
    num = int(input("Ingrese un número (0 para detener): "))
    if num == 0:
        break
    suma += num
print(f"La suma total es: {suma}")

#punto 5
import random
num_secreto = random.randint(0, 9)
intentos = 0
while True:
    adivinanza = int(input("Adivine un número entre 0 y 9: "))
    intentos += 1
    if adivinanza == num_secreto:
        break
print(f"Adivinaste! y en tan solo {intentos} intentos.")

#punto 6
for num in range(100, -1, -1):
    if num % 2 == 0:
        print(num)

#punto 7
num = int(input("Ingrese un número entero positivo: "))
if num < 0:
    print("No se puede, debe ser un número positivo.")
else:
    suma = 0
    for i in range(num + 1):
        suma += i
    print(f"La suma de 0 a {num} es: {suma}")

#punto 8
cantidad = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i + 1} (o 0 para terminar antes): "))
    if num == 0:
        break  
    if num > 0:
        positivos += 1
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    elif num < 0:
        negativos += 1
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

#punto 9
cantidad = 100
suma = 0
contador = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i + 1} (o 0 para terminar antes): "))
    if num == 0:
        break
    suma += num
    contador += 1
if contador > 0:
    media = suma / contador
    print(f"La media de los {contador} números ingresados es: {media}")
else:
    print("No se ingresaron números válidos para calcular la media.")

#punto 10
num = int(input("Ingrese un número entero: "))
if num < 0:
    print("Error: El número debe ser positivo.")
else:
    invertido = 0
    temp = num
    while temp > 0:
        digito = temp % 10
        invertido = invertido * 10 + digito
        temp = temp // 10
    print(f"El número invertido de {num} es: {invertido}")