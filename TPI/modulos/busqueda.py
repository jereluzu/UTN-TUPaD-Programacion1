#modulos/busqueda.py
from typing import List, Dict

def buscar_pais(paises: List[Dict], nombre: str) -> List[Dict]:
    nombre = nombre.strip().lower()
    return [p for p in paises if nombre in p['nombre'].lower()]