from abc import ABC, abstractmethod

from .properties import Properties

class Edge(ABC):

    def __init__(self, id: int, properties: Properties) -> None:
        self.id = id
        self.properties = properties
