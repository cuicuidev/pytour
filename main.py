from core.graph import Graph
from core.algorithms import Tour
from core.coordinates import Coordinates

def main():
    G = Graph.from_osm("test.osm")

    pathfinding_algorithm = Tour(1000)
    starting_coordinates = Coordinates(36.7346160, -2.6222383)
    ending_coordinates = Coordinates(36.7295526, -2.6191530)
    path = pathfinding_algorithm.run(G, starting_coordinates, ending_coordinates)
    print(path)

if __name__ == "__main__":
    main()
