from .utils.responses import isNotStation
from .utils.query import search_by_id
from .utils.parser import parse_to_response
from fastapi import FastAPI

app = FastAPI()

@app.get("/estacion/{estacion}")
def read_root(estacion: int):
    response = search_by_id(estacion)
    if not response:
        return isNotStation(estacion)
    return parse_to_response(response)