from abc import ABC, abstractmethod

from ..graph import Graph
from ..node import Node
from ..coordinates import Coordinates

class PathfindingAlgorithm(ABC):
    """
    An abstract base class for pathfinding algorithms.
    """
    
    @abstractmethod
    def run(self, graph: Graph, start: Coordinates, end: Coordinates) -> list:
        """
        Finds a path between two nodes in a graph.

        :param graph: The graph to search.
        :param start: The starting coordinates.
        :param end: The ending coordinates.
        :return: A list of nodes representing the path between the start and end nodes.
        """

        start_node = graph.node_at(start)
        end_node = graph.node_at(end)

        if start_node is None or end_node is None:
            return []
       
        return self._run(graph, start_node, end_node)

    @abstractmethod
    def _run(self, graph: Graph, start: Node, end: Node) -> list:
        """
        Finds a path between two nodes in a graph.

        :param graph: The graph to search.
        :param start: The starting node.
        :param end: The ending node.
        :return: A list of nodes representing the path between the start and end nodes.
        """

        pass
