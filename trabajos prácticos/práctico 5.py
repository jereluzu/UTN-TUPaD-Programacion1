# ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingresa tu nombre: ")
print(saludar_usuario(nombre))

# ejericicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# ejercicio 4
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresa el radio: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

# ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresa los segundos: "))
print(f"{segundos} segundos = {segundos_a_horas(segundos):.4f} horas")

# ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingresa un número: "))
tabla_multiplicar(numero)

# ejercicio 7
def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else "Error"

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
suma, resta, multi, div = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multi}")
print(f"División: {div}")

# ejercicio 8
def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
print(f"IMC: {calcular_imc(peso, altura)}")

# ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Temperatura en °C: "))
print(f"{celsius}°C = {celsius_a_fahrenheit(celsius):.2f}°F")

# ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))
print(f"Promedio: {calcular_promedio(a, b, c):.2f}")