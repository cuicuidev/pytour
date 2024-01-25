from .core import PathfindingAlgorithm

from ..graph import Graph
from ..node import Node
from ..path import Path

class Tour(PathfindingAlgorithm):
    """
    A pathfinding algorithm that returns the highest value path between two nodes no longer than a given distance.
    """

    def __init__(self, max_distance: int) -> None:
        """
        :param max_distance: The maximum distance a path can be.
        """
        self.max_distance = max_distance

    def _run(self, graph: Graph, start: Node, end: Node) -> Path:
        """
        :param graph: The graph to search.
        :param start: The starting node.
        :param end: The ending node.
        :return: The path between the two nodes.
        """
        return self._tour(graph, start, end, self.max_distance)

    def _tour(self, graph: Graph, start: Node, end: Node, max_distance: float) -> Path:
        """
        :param graph: The graph to search.
        :param start: The starting node.
        :param end: The ending node.
        :param max_distance: The maximum distance a path can be.
        :return: The path between the two nodes.
        """

        # BFS Implementation for testing purposes

        queue = [[start, Path([start])]]
        visited = set()

        while queue:
            current_node, current_path = queue.pop(0)
            visited.add(current_node)

            if current_node == end:
                return current_path

            for neighbor in graph.get_adjacent_nodes(current_node):
                if neighbor not in visited:
                    queue.append([neighbor, Path(current_path.nodes + [neighbor])])

        return Path([start])
