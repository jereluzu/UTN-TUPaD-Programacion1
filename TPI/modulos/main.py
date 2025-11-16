#main
from modulos.carga import cargar_paises
from modulos.busqueda import buscar_pais
from modulos.filtros import por_continente, por_poblacion, por_superficie
from modulos.ordenamiento import ordenar
from modulos.estadisticas import calcular
from modulos.utils import mostrar_lista

def menu():
    print("Cargando datos...")
    paises = cargar_paises('paises.csv')
    if not paises:
        print("No se pudieron cargar los datos. Fin del programa.")
        return

    while True:
        print("\n" + "="*55)
        print("     GESTIÓN DE PAÍSES - MENÚ PRINCIPAL")
        print("="*55)
        print("1. Buscar país por nombre")
        print("2. Filtrar por continente")
        print("3. Filtrar por rango de población")
        print("4. Filtrar por rango de superficie")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Mostrar todos los países")
        print("8. Salir")
        print("-"*55)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del país (parcial): ")
            resultados = buscar_pais(paises, nombre)
            mostrar_lista(resultados, f"Búsqueda: '{nombre}'")

        elif opcion == "2":
            cont = input("Continente: ")
            resultados = por_continente(paises, cont)
            mostrar_lista(resultados, f"Continente: {cont}")

        elif opcion == "3":
            try:
                min_p = int(input("Población mínima: "))
                max_p = int(input("Población máxima: "))
                if min_p > max_p:
                    print("Error: el mínimo no puede ser mayor que el máximo.")
                    continue
                resultados = por_poblacion(paises, min_p, max_p)
                mostrar_lista(resultados, f"Población: {min_p:,} - {max_p:,}")
            except ValueError:
                print("Error: ingrese números enteros.")

        elif opcion == "4":
            try:
                min_s = int(input("Superficie mínima (km²): "))
                max_s = int(input("Superficie máxima (km²): "))
                if min_s > max_s:
                    print("Error: el mínimo no puede ser mayor que el máximo.")
                    continue
                resultados = por_superficie(paises, min_s, max_s)
                mostrar_lista(resultados, f"Superficie: {min_s:,} - {max_s:,} km²")
            except ValueError:
                print("Error: ingrese números enteros.")

        elif opcion == "5":
            print("\nOrdenar por:")
            print("1. Nombre (A-Z)")
            print("2. Nombre (Z-A)")
            print("3. Población (mayor a menor)")
            print("4. Población (menor a mayor)")
            print("5. Superficie (mayor a menor)")
            print("6. Superficie (menor a mayor)")
            sub = input("Opción: ")
            clave, asc = "", True
            if sub == "1": clave, asc = "nombre", True
            elif sub == "2": clave, asc = "nombre", False
            elif sub == "3": clave, asc = "poblacion", False
            elif sub == "4": clave, asc = "poblacion", True
            elif sub == "5": clave, asc = "superficie", False
            elif sub == "6": clave, asc = "superficie", True
            else:
                print("Opción inválida.")
                continue
            ordenados = ordenar(paises.copy(), clave, asc)
            mostrar_lista(ordenados, f"Ordenado por {clave} {'asc' if asc else 'desc'}")

        elif opcion == "6":
            stats = calcular(paises)
            print("\n" + "="*50)
            print("           ESTADÍSTICAS")
            print("="*50)
            print(f"País con mayor población: {stats['mayor_poblacion']['nombre']} ({stats['mayor_poblacion']['poblacion']:,})")
            print(f"País con menor población: {stats['menor_poblacion']['nombre']} ({stats['menor_poblacion']['poblacion']:,})")
            print(f"Promedio de población: {stats['promedio_poblacion']:,} habitantes")
            print(f"Promedio de superficie: {stats['promedio_superficie']:,} km²")
            print("Países por continente:")
            for cont, cant in stats['por_continente'].items():
                print(f"  • {cont}: {cant}")
            print("-"*50)

        elif opcion == "7":
            mostrar_lista(paises, "Todos los países")

        elif opcion == "8":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()