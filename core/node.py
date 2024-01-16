from abc import ABC, abstractmethod
from typing import Iterable, Type

from .properties import Properties
from .coordinates import Coordinates

class Node:

    def __init__(self, id: int, properties: Properties, coordinates: Coordinates) -> None:
        self.id = id
        self.properties = properties
        self.coordinates = coordinates

    def __str__(self) -> str:
        return f"Node {self.id} ({self.coordinates.lat}, {self.coordinates.lng})"

    @classmethod
    def from_xml(cls, xml: str) -> "Node":
        """
        Factory method. Constructs a Node object from a xml structured string.
        """
        
        id = int(xml.split('id="')[1].split('"')[0])
        lat = float(xml.split('lat="')[1].split('"')[0])
        lng = float(xml.split('lon="')[1].split('"')[0])
        coordinates = Coordinates(lat, lng)
        properties = Properties() # TODO: Implement properties

        return cls(id, properties, coordinates)
