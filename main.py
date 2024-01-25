from core.graph import Graph
from core.path import Path
from core.algorithms import Tour
from core.coordinates import Coordinates

import folium

def plot_path(path: Path):
    m = folium.Map(location=[36.728469095725444, -2.634042097367474], zoom_start=15)
    folium.PolyLine([(node.coordinates.lat, node.coordinates.lng) for node in path.nodes], color='blue').add_to(m)
    m.save('map.html')

def plot_graph(G: Graph):
    m = folium.Map(location=[36.728469095725444, -2.634042097367474], zoom_start=15)
    for edge in G.edges:
        source = G.get_node(edge.source)
        target = G.get_node(edge.target)
        way = [(source.coordinates.lat, source.coordinates.lng), (target.coordinates.lat, target.coordinates.lng)]
        folium.PolyLine(way, color='green').add_to(m)
    m.save('map.html')

    
def main():
    G = Graph.from_osm("test.osm")

    pathfinding_algorithm = Tour(1000)
    starting_coordinates = Coordinates(36.728469095725444, -2.634042097367474)
    ending_coordinates = Coordinates(36.729134833627036, -2.619659505336913)
    path = pathfinding_algorithm.run(G, starting_coordinates, ending_coordinates)
    plot_path(path)
    # plot_graph(G)

if __name__ == "__main__":
    main()
