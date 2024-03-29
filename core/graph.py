import warnings

from .node import Node
from .edge import Edge
from .coordinates import Coordinates

from typing import Generator, Iterable, Any, Optional

class Graph:

    def __init__(self, nodes: Iterable[Node], edges: Iterable[Edge]) -> None:
        self.nodes = nodes
        self.edges = edges
        
    def __str__(self):
        nodes_repr = '\n'.join([str(node) for node in self.nodes])
        edges_repr = '\n'.join([str(edge) for edge in self.edges])
        return f"Nodes:\n{nodes_repr}\n\nEdges:\n{edges_repr}"

    def node_at(self, coordinates: Coordinates) -> Optional[Node]:
        for node in self.nodes:
            if node.coordinates == coordinates:
                return node

    def nearest_node(self, coordinates: Coordinates) -> Node:
        nearest_node = None
        nearest_distance = float("inf")
        for node in self.nodes:
            distance = node.coordinates.get_distance(coordinates)
            if distance < nearest_distance:
                nearest_node = node
                nearest_distance = distance
        return nearest_node

    @classmethod
    def from_api(cls, coordinates: Coordinates, radius: float) -> "Graph":
        warnings.warn("This method is not implemented yet, returning test graph from osm file")
        return cls.from_osm("test.osm")

    @classmethod
    def from_osm(cls, file: str) -> "Graph":
        elements = cls._flow_from_osm(file)
        nodes = []
        edges = []
        edge_id = 0
        for element in elements:
            strip_element = element.strip()
            if strip_element.startswith("<node"):
                node = Node.from_xml(element)
                nodes.append(node)
            if strip_element.startswith("<way"):
                way_nodes = []
                for line in element.splitlines():
                    if line.strip().startswith("<nd"):
                        node_id = int(line.split('"')[1])
                        way_nodes.append(node_id)

                # Create edges
                for i in range(len(way_nodes) -1):
                    edge = Edge(edge_id, way_nodes[i], way_nodes[i+1])
                    edges.append(edge)
                    edge_id += 1

        graph = cls(nodes, edges)
        return graph

    @staticmethod
    def _flow_from_osm(file: str) -> Generator[str, Any, Any]:
        with open(file, "r") as f:
            reading_node = False
            node = []

            reading_way = False
            way = []
            for line in f:
                strip_line = line.strip()
                if strip_line.startswith("<node"):
                    if reading_node:
                        node.append(line)
                        node = ''.join(node)
                        yield node
                        node = []

                    reading_node = True
                if strip_line.startswith("</node"):
                    reading_node = False
                    node.append(line)
                    node = ''.join(node)
                    yield node
                    node = []

                if reading_node:
                    node.append(line)


                if strip_line.startswith("<way"):
                    reading_way = True
                if strip_line.startswith("</way"):
                    reading_way = False
                    way.append(line)
                    way = ''.join(way)
                    yield way
                    way = []

                if reading_way:
                    way.append(line)


    def get_node(self, node_id: int) -> Optional[Node]:
        for node in self.nodes:
            if node.id == node_id:
                return node

    def get_adjacent_nodes(self, node: Node) -> Generator[Node | None, Any, Any]:
        for edge in self.edges:
            if edge.source == node.id:
                yield self.get_node(edge.target)
            if edge.target == node.id:
                yield self.get_node(edge.source)
