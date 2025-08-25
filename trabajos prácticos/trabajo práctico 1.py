#punto 1
print("Hola Mundo!")
#punto 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")
#punto 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")
#punto 4
radio = float(input("Ingrese el radio del círculo que quiere calcular: "))
area = 3.14 * radio ** 2
perímetro = 2 * 3.14 * radio
print(f"El área es: {area}")
print(f"El perímetro es: {perímetro}")
#punto 5
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"Los {segundos} segundos equivalen a {horas}")
#punto 6
num = int(input("Ingrese un número: "))
print(f"{num} x 1 = {num * 1}")
print(f"{num} x 2 = {num * 2}")
print(f"{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}")
print(f"{num} x 5 = {num * 5}")
print(f"{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}")
print(f"{num} x 8 = {num * 8}")
print(f"{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}")
#punto 7
num1 = int(input("Ingrese un número que no sea 0: "))
num2 = int(input("Ahora otro número que tampoco sea 0: "))
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multi}")
print(f"División: {div}")
#punto 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura) ** 2
print(f"su índicie de masa corporal es: {imc}")
#punto 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit}°F")
#punto 10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2} y {num3} es de: {promedio}")