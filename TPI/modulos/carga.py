#modulos/carga.py
import csv
from typing import List, Dict

def cargar_paises(archivo: str) -> List[Dict]:
    paises = []
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    pais = {
                        'nombre': fila['nombre'].strip(),
                        'poblacion': int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente'].strip()
                    }
                    if pais['poblacion'] < 0 or pais['superficie'] < 0:
                        print(f"Advertencia: datos negativos en {pais['nombre']}")
                        continue
                    paises.append(pais)
                except (ValueError, KeyError) as e:
                    print(f"Error en fila: {e}")
        print(f"Se cargaron {len(paises)} países correctamente.")
    except FileNotFoundError:
        print(f"Error: archivo '{archivo}' no encontrado.")
    except Exception as e:
        print(f"Error al leer CSV: {e}")
    return paises