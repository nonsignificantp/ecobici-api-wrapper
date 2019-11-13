import requests
from typing import Dict

ROOT = 'https://epok.buenosaires.gob.ar/getObjectContent'

def search_by_id(estacion: int) -> Dict:
    """Fetch original Ecobici API"""
    q = {'id': f'estaciones_de_bicicletas|{estacion}'}
    response = requests.get(ROOT, params=q)
    return response.json()
    