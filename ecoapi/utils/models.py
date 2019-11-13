from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Optional

class Stats(BaseModel):
    estado: str
    disponibles: int
    libres: int
    anclajes: int

class Estacion(BaseModel):
    nombre: str
    codigo: int
    ubicacion: str
    inauguracion: datetime
    actualizacion: datetime
    estado: Stats
    geometria: Dict[str, str]