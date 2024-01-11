from abc import ABC, abstractmethod
from typing import Iterable, Type

from .properties import Properties

class Node(ABC):

    def __init__(self, id: int, properties: Properties) -> None:
        self.id = id
        self.properties = properties
