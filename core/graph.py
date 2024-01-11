from .node import Node
from .edge import Edge

class Graph:

    def __init__(self, nodes: list[Node], edges: list[Edge]) -> None:
        self.nodes = nodes
        self.edges = edges
        
    def __str__(self):
        nodes_repr = '\n'.join([str(node) for node in self.nodes])
        edges_repr = '\n'.join([str(edge) for edge in self.edges])
        return f"Nodes:\n{nodes_repr}\n\nEdges:\n{edges_repr}"

    @classmethod
    def from_osm(cls, file: str) -> "Graph":
        nodes = []
        edges = []
        graph = cls(nodes, edges)
        return graph
