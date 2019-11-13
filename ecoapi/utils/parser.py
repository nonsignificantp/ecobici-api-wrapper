from .models import Stats, Estacion
from dateutil.parser import parse
from typing import List, Dict
import re

def clean_name(name: str) -> str:
    """Removes id from station's name"""
    pattern = r'\-\s+(.+)$'
    return re.search(pattern, name).group(1)

def get_stats(contenido: List[Dict]) -> Stats:
    """Get station's stats from JSON response"""
    estado = contenido[2]['valor']
    disponibles = contenido[4]['valor']
    libres = contenido[5]['valor']
    anclajes = contenido[6]['valor']
    return Stats(**{
        'estado': estado,
        'disponibles': disponibles,
        'libres': libres,
        'anclajes': anclajes,
        })

def parse_to_response(response: Dict) -> Estacion:
    """Construct Estation response from raw JSON response"""
    return Estacion(**{
        'nombre': clean_name(response['contenido'][0]['valor']),
        'codigo': response['contenido'][1]['valor'],
        'ubicacion': response['contenido'][3]['valor'],
        'inauguracion': parse(response['fechaAlta'], dayfirst=True),
        'actualizacion': parse(response['fechaUltimaModificacion'], dayfirst=True),
        'estado': get_stats(response['contenido']),
        'geometria': response['ubicacion'],
    })