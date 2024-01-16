from typing import Self
from math import radians, sin, cos, sqrt, atan2

class Coordinates:

    def __init__(self, lat: float, lng: float) -> None:
        self.lat = lat
        self.lng = lng

    def __eq__(self, other):
        assert isinstance(other, Coordinates), f"Cannot compare Coordinates with {type(other)} instance."
        return self.lat == other.lat and self.lng == other.lng

    def get_distance(self, other: Self, type: str = "haversine") -> float:
        if type == "haversine":
            return self._get_haversine(other)
        elif type == "euclidian":
            return self._get_euclidian(other)
        elif type == "manhattan":
            return self._get_manhattan(other)

        raise ValueError("The type parameter must be set to one of the following: `haversine`, `euclidian` or `manhattan`")

    def _get_euclidian(self, other: Self) -> float:
        pass

    def _get_manhattan(self, other: Self) -> float:
        pass
        
    def _get_haversine(self, other: Self) -> float:
        R = 6371.0

        lat1, lng1 = radians(self.lat), radians(self.lng)
        lat2, lng2 = radians(other.lat), radians(other.lng)

        dlat = lat2 - lat1
        dlng = lng2 - lng1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlng / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c
