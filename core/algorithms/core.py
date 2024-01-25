from abc import ABC, abstractmethod

from ..graph import Graph
from ..node import Node
from ..coordinates import Coordinates
from ..path import Path

class PathfindingAlgorithm(ABC):
    """
    An abstract base class for pathfinding algorithms.
    """
    
    def run(self, graph: Graph, start: Coordinates, end: Coordinates, approximate_coordinates: bool = True) -> Path:
        """
        Finds a path between two nodes in a graph.

        :param graph: The graph to search.
        :param start: The starting coordinates.
        :param end: The ending coordinates.
        :return: A list of nodes representing the path between the start and end nodes.
        """

        if approximate_coordinates:
            start_node = graph.nearest_node(start)
            end_node = graph.nearest_node(end)
        else:
            start_node = graph.node_at(start)
            end_node = graph.node_at(end)

        if start_node is None or end_node is None:
            return  Path([])
       
        return self._run(graph, start_node, end_node)

    def _run(self, graph: Graph, start: Node, end: Node) -> Path:
        """
        Finds a path between two nodes in a graph.

        :param graph: The graph to search.
        :param start: The starting node.
        :param end: The ending node.
        :return: A list of nodes representing the path between the start and end nodes.
        """

        pass
