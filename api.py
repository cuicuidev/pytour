from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

from core.graph import Graph
from core.algorithms.tour import Tour
from core.coordinates import Coordinates

class CoordinatesModel(BaseModel):
    latitude: float
    longitude: float

class DogCharacteristics(BaseModel):
    weight: float
    height: float
    breed: str

class AlgorithmEnum(str, Enum):
    TOUR = "TOUR"

class PathResponse(BaseModel):
    path: list[CoordinatesModel]

class Request(BaseModel):
    source: CoordinatesModel
    target: CoordinatesModel

    time_seconds: int
    dog_characteristics: DogCharacteristics

    algorithm: AlgorithmEnum

ALGORITHMS = {
    "TOUR": Tour
}

app = FastAPI()

@app.post("/get_path")
async def get_path(request: Request) -> PathResponse:
    radius = get_radius(request.dog_characteristics, request.time_seconds)
    source = Coordinates(request.source.latitude, request.source.longitude)
    target = Coordinates(request.target.latitude, request.target.longitude)
    
    G = Graph.from_api(coordinates=source, radius=radius)

    algorithm = ALGORITHMS[request.algorithm]
    algorithm = algorithm(max_distance=radius)
    path = algorithm.run(G, source, target)

    return PathResponse(path=[CoordinatesModel(latitude=point.coordinates.lat, longitude=point.coordinates.lng) for point in path.nodes])

def get_radius(dog_characteristics: DogCharacteristics, time_seconds: int):
    return 1000
