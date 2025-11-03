# ejercicio 1
with open("productos.txt", "w") as f:
    f.write("Lapicera,120.5,30\n")
    f.write("Cuaderno,850.0,15\n")
    f.write("Goma,75.5,50\n")

# ejercicio 2
with open("productos.txt", "r") as f:
    for linea in f:
        datos = linea.strip().split(",")
        nombre, precio, cantidad = datos
        print(f"Producto: {nombre} | Precio: ${float(precio):.1f} | Cantidad: {cantidad}")

# ejercicio 3
with open("productos.txt", "r") as f:
    for linea in f:
        datos = linea.strip().split(",")
        nombre, precio, cantidad = datos
        print(f"Producto: {nombre} | Precio: ${float(precio):.1f} | Cantidad: {cantidad}")

nombre = input("Nuevo producto - Nombre: ")
precio = input("Precio: ")
cantidad = input("Cantidad: ")

with open("productos.txt", "a") as f:
    f.write(f"{nombre},{precio},{cantidad}\n")

# ejercicio 4
productos = []
with open("productos.txt", "r") as f:
    for linea in f:
        datos = linea.strip().split(",")
        producto = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }
        productos.append(producto)

for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']:.1f} | Cantidad: {p['cantidad']}")

# ejercicio 5
productos = []
with open("productos.txt", "r") as f:
    for linea in f:
        datos = linea.strip().split(",")
        producto = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }
        productos.append(producto)

buscar = input("Buscar producto por nombre: ")
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']:.1f} | Cantidad: {p['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado.")

# ejercicio 6
productos = []
with open("productos.txt", "r") as f:
    for linea in f:
        datos = linea.strip().split(",")
        producto = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }
        productos.append(producto)

buscar = input("Buscar producto por nombre: ")
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']:.1f} | Cantidad: {p['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado.")

nombre = input("Nuevo producto - Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

with open("productos.txt", "w") as f:
    for p in productos:
        f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")