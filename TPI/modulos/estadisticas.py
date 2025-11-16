#modulos/estadisticas.py
from typing import List, Dict

def calcular(paises: List[Dict]) -> Dict:
    if not paises:
        return {}
    pob = [p['poblacion'] for p in paises]
    sup = [p['superficie'] for p in paises]
    return {
        'mayor_poblacion': max(paises, key=lambda x: x['poblacion']),
        'menor_poblacion': min(paises, key=lambda x: x['poblacion']),
        'promedio_poblacion': sum(pob) // len(pob),
        'promedio_superficie': sum(sup) // len(sup),
        'por_continente': contar_continentes(paises)
    }

def contar_continentes(paises: List[Dict]) -> Dict:
    conteo = {}
    for p in paises:
        cont = p['continente']
        conteo[cont] = conteo.get(cont, 0) + 1
    return conteo