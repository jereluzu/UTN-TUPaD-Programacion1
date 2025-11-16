#modulos/filtros.py
from typing import List, Dict

def por_continente(paises: List[Dict], continente: str) -> List[Dict]:
    return [p for p in paises if p['continente'].lower() == continente.strip().lower()]

def por_poblacion(paises: List[Dict], min_pob: int, max_pob: int) -> List[Dict]:
    return [p for p in paises if min_pob <= p['poblacion'] <= max_pob]

def por_superficie(paises: List[Dict], min_sup: int, max_sup: int) -> List[Dict]:
    return [p for p in paises if min_sup <= p['superficie'] <= max_sup]