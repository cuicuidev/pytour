from .coordinates import Coordinates

class Node:

    def __init__(self, id: int, coordinates: Coordinates) -> None:
        self.id = id
        self.coordinates = coordinates

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: "Node") -> bool:
        return self.id == other.id


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

        return cls(id, coordinates)
