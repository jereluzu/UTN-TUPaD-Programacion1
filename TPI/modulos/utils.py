#modulos/utils.py
from typing import List, Dict

def mostrar_pais(pais: Dict):
    print(f"Nombre: {pais['nombre']}")
    print(f"Población: {pais['poblacion']:,} habitantes")
    print(f"Superficie: {pais['superficie']:,} km²")
    print(f"Continente: {pais['continente']}")
    print("-" * 40)

def mostrar_lista(paises: List[Dict], titulo: str = "Resultados"):
    if not paises:
        print("No se encontraron resultados.")
        return
    print(f"\n=== {titulo} ({len(paises)} países) ===")
    for p in paises:
        mostrar_pais(p)