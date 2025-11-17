# TPI - Gestión de Datos de Países  
**Programación 1 – Tecnicatura Universitaria en Programación – UTN**

---

## Descripción del programa

Aplicación en consola desarrollada en Python 3.11 que permite gestionar un dataset de países almacenado en un archivo CSV.  
Cumple con todos los requerimientos del Trabajo Práctico Integrador (TPI) de Programación 1:

- Lectura de datos desde CSV con validación de formato.
- Búsqueda parcial por nombre (insensible a mayúsculas).
- Filtros por continente, rango de población y superficie.
- Ordenamiento por nombre, población o superficie (ascendente/descendente).
- Estadísticas básicas: mayor/menor, promedios, conteo por continente.
- Código modular, claro, comentado y con una función por responsabilidad.
- Validación de entradas y manejo robusto de errores.
- Salida formateada con separadores y comas en números grandes.

---

## Objetivo del TPI

"Desarrollar una aplicación en Python que permita gestionar información sobre países, aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas. El sistema debe ser capaz de leer datos desde un archivo CSV, realizar consultas y generar indicadores clave a partir del dataset."

---

## Estructura de datos utilizada

pais = {
    'nombre': str,        # Ej: "Argentina"
    'poblacion': int,     # Ej: 45376763
    'superficie': int,    # Ej: 2780400
    'continente': str     # Ej: "América"
}

- Lista de diccionarios: paises = [pais1, pais2, ...]
- Almacenada en memoria tras la carga del CSV.
- Permite acceso rápido por clave y compatibilidad con csv.DictReader.

---

## Funcionalidades del menú

| Opción | Descripción |
|-------|-------------|
| 1 | Buscar país por nombre (coincidencia parcial, insensible a mayúsculas) |
| 2 | Filtrar por continente |
| 3 | Filtrar por rango de población |
| 4 | Filtrar por rango de superficie |
| 5 | Ordenar por nombre, población o superficie (asc/desc) |
| 6 | Estadísticas: mayor/menor, promedios, conteo por continente |
| 7 | Mostrar todos los países |
| 8 | Salir |

---

## Instrucciones de uso

1. Clonar el repositorio:
   git clone https://github.com/tu-usuario/tpi-paises-utn.git
2. Entrar a la carpeta:
   cd tpi-paises-utn
3. Ejecutar el programa:
   python main.py
4. Seguir las opciones del menú en consola

Requisitos: Python 3.x, archivo paises.csv en la raíz.

---

## Ejemplos de entradas y salidas

### 1. Búsqueda parcial
> Opción: 1
> Nombre: bra
=== Búsqueda: 'bra' (1 países) ===
Nombre: Brasil
Población: 213,993,437 habitantes
Superficie: 8,515,767 km²
Continente: América

### 2. Filtro por continente
> Opción: 2
> Continente: América
=== Continente: América (4 países) ===
Argentina | 45,376,763 | 2,780,400 km² | América
Brasil    | 213,993,437| 8,515,767 km² | América
Chile     | 19,116,201 | 756,096 km²   | América
Perú      | 32,971,854 | 1,285,216 km² | América

### 3. Filtro por población (con error)
> Opción: 3
> Mínimo: 500000000
> Máximo: 100000000
Error: el mínimo no puede ser mayor que el máximo.

### 4. Ordenamiento
> Opción: 5 → 3 (Población descendente)
1. China     | 1,444,216,107 habitantes
2. India     | 1,380,004,385 habitantes
3. Brasil    | 213,993,437 habitantes
...
10. Chile    | 19,116,201 habitantes

### 5. Estadísticas
ESTADÍSTICAS
==================================================
País con mayor población: China (1,444,216,107)
País con menor población: Chile (19,116,201)
Promedio de población: 306,842,996 habitantes
Promedio de superficie: 3,441,094 km²
Países por continente:
  • América: 4
  • Asia: 3
  • Europa: 3

---

## Estructura del proyecto

TPI/
├── main.py                      ← Menú principal y orquestación
├── paises.csv                   ← Dataset base (10 países)
├── README.md                    ← Este archivo
├── modulos/
│   ├── __init__.py              ← Paquete Python (vacío)
│   ├── carga.py                 ← Lectura y validación del CSV
│   ├── busqueda.py              ← Búsqueda parcial
│   ├── filtros.py               ← Filtros por continente, población, superficie
│   ├── ordenamiento.py          ← Ordenamiento flexible
│   ├── estadisticas.py          ← Cálculos estadísticos
│   └── utils.py                 ← Formateo y visualización
├── capturas/                    ← Evidencias de ejecución
│   ├── menu.png
│   ├── busqueda_chi.png
│   ├── filtro_america.png
│   ├── orden_poblacion.png
│   ├── estadisticas.png
│   └── error_rango.png
└── informe/
    └── informe_tpi.pdf          ← Informe teórico completo

---

## Conceptos aplicados (explicación breve)

| Concepto | Uso en el proyecto |
|--------|-------------------|
| Listas | paises = [] → almacena todos los países |
| Diccionarios | Cada país es un dict con claves |
| Funciones | 6 módulos, 10+ funciones reutilizables |
| Condicionales | if/elif/else en menús y validaciones |
| Ordenamientos | sorted() con key=lambda |
| Estadísticas | max, min, sum, comprensiones |
| Archivos CSV | csv.DictReader con validación |

---

## Validaciones implementadas

| Validación | Implementación |
|----------|----------------|
| Formato CSV | try/except en carga.py |
| Datos negativos | if poblacion < 0: continue |
| Entradas inválidas | try/except ValueError |
| Rangos inválidos | if min > max: error |
| Búsquedas sin resultado | if not resultados: "No se encontraron..." |
| Archivo no encontrado | FileNotFoundError |

---

## Capturas de pantalla (evidencias)

- menu.png → Menú principal  
- busqueda_chi.png → Búsqueda "chi" → Chile y China  
- filtro_america.png → Filtro por continente  
- orden_poblacion.png → Orden descendente por población  
- estadisticas.png → Resultados completos  
- error_rango.png → Validación de rango inválido  

---

## Participación de los integrantes

| Nombre | Rol | Contribución |
|-------|-----|--------------|
| Jeremías | Desarrollador único | 100% del proyecto: código, documentación, pruebas, video |
