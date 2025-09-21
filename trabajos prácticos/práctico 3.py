#punto 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

#punto 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#punto 3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#punto 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#punto 5
contraseña = input("Ingrese su contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#punto 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

#punto 7
frase = input("Ingrese una frase o palabra: ")
ultimo_caracter = frase[-1].lower()
if ultimo_caracter == 'a' or ultimo_caracter == 'e' or ultimo_caracter == 'i' or ultimo_caracter == 'o' or ultimo_caracter == 'u':
    print(frase + "!")
else:
    print(frase)

#punto 8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1, 2 o 3 según desee: \n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\nOpción: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

#punto 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#punto 10
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))
hemisferio = input("Ingrese el hemisferio (N para norte, S para sur): ").upper()

if hemisferio not in ["N", "S"]:
    print("Hemisferio inválido. Use 'N' para norte o 'S' para sur.")

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    print("Invierno" if hemisferio == "N" else "Verano")
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    print("Primavera" if hemisferio == "N" else "Otoño")
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    print("Verano" if hemisferio == "N" else "Invierno")
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    print("Otoño" if hemisferio == "N" else "Primavera")