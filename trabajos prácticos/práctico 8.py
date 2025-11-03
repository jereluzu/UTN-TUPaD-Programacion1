# ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Ingresa un número: "))
for i in range(1, n + 1):
    print(f"{i}! = {factorial(i)}")

# ejercicio 2
def fibonacci(pos):
    if pos <= 1:
        return pos
    return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("Ingresa una posición: "))
print("Serie de Fibonacci:")
for i in range(n):
    print(fibonacci(i), end=" ")
print()

# ejercicio 3
def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

base = float(input("Base: "))
exp = int(input("Exponente: "))
print(f"{base}^{exp} = {potencia(base, exp)}")

# ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

n = int(input("Ingresa un número decimal: "))
print(f"Binario: {decimal_a_binario(n)}")

# ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingresa una palabra: ").lower().replace(" ", "")
print(es_palindromo(texto))

# ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

n = int(input("Ingresa un número: "))
print(suma_digitos(n))

# ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

n = int(input("Bloques en la base: "))
print(f"Total de bloques: {contar_bloques(n)}")

# ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    return contar_digito(numero // 10, digito)

numero = int(input("Número: "))
digito = int(input("Dígito a contar: "))
print(contar_digito(numero, digito))