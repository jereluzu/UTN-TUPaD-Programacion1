#modulos/ordenamiento.py
from typing import List, Dict

def ordenar(paises: List[Dict], clave: str, ascendente: bool = True) -> List[Dict]:
    reverse = not ascendente
    if clave == 'nombre':
        return sorted(paises, key=lambda x: x['nombre'].lower(), reverse=reverse)
    elif clave in ['poblacion', 'superficie']:
        return sorted(paises, key=lambda x: x[clave], reverse=reverse)
    return paises