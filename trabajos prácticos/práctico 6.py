# ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# ejercicio 2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# ejercicio 3
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
frutas = list(precios_frutas.keys())
print(frutas)

# ejercicio 4
contactos = {}
for _ in range(5):
    nombre = input("Nombre: ")
    numero = input("Teléfono: ")
    contactos[nombre] = numero

buscar = input("Buscar contacto: ")
if buscar in contactos:
    print(contactos[buscar])
else:
    print("No existe")

# ejercicio 5
frase = input("Ingresa una frase: ").lower().split()
unicas = set(frase)
frecuencia = {}
for palabra in frase:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Palabras únicas:", unicas)
print("Frecuencia:", frecuencia)

# ejercicio 6
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: {promedio:.2f}")

# ejercicio 7
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {102, 104, 106, 107}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Al menos uno:", al_menos_uno)

# ejercicio 8
stock = {}
while True:
    producto = input("Producto (o 'salir'): ")
    if producto == 'salir':
        break
    if producto in stock:
        opcion = input("1. Consultar  2. Agregar stock: ")
        if opcion == '1':
            print(stock[producto])
        else:
            cantidad = int(input("Unidades a sumar: "))
            stock[producto] += cantidad
    else:
        cantidad = int(input("Stock inicial: "))
        stock[producto] = cantidad

# ejercicio 9
agenda = {}
while True:
    dia = input("Día (o 'salir'): ")
    if dia == 'salir':
        break
    hora = input("Hora: ")
    evento = input("Evento: ")
    agenda[(dia, hora)] = evento

consulta_dia = input("Consultar día: ")
consulta_hora = input("Consultar hora: ")
clave = (consulta_dia, consulta_hora)
if clave in agenda:
    print(agenda[clave])
else:
    print("No hay evento")

# ejercicio 10
original = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Perú': 'Lima'}
invertido = {capital: pais for pais, capital in original.items()}
print(invertido)