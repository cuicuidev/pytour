from typing import Optional

class Node:

    def __init__(self, value: float, tag: str) -> None:
        self.id: int = 0
        self.value = value
        self.tag = tag
        self.x = 0
        self.y = 0
        self.g = float("inf")


class Edge:
    
    def __init__(self, weight: float, source: Node, target: Node) -> None:
        self.id: int = 0
        self.weight = weight
        self.source = source
        self.target = target

class Constraints:
    max: float

class Path:

    def __init__(self, edges: list[Edge]):
        self.edges=edges
        
        assert self.continuous(), "Path is not valid. Unable to traverse from the starting node to the ending node."

    def continuous(self):
        i = 0
        q = [self.edges[0]]
        while q:
            edge = q.pop(0)
            i += 1
            if len(self.edges) < i:
                q.append(self.edges[i])
                current_target = edge.target
                next_source = q[0].source
                if current_target != next_source:
                    return False
        return True

    def append_edge(self, edge: Edge) -> None:
        self.edges.append(edge)
        assert self.continuous(), "Cannot append edge to the path because it would stop being continuous"

class Graph:
    
    def __init__(self, nodes: list[Node], edges: list[Edge]) -> None:  
        self.nodes = nodes
        self.edges = edges

        self._initialize_ids()

    def _initialize_ids(self) -> None:
        for i, node in enumerate(self.nodes):
            node.id = i
        for i, edge in enumerate(self.edges):
            edge.id = i

    def _get_node_by_id(self, id: int) -> Node:
        return self.nodes[id]

    def _heuristic(self, node_id: int, destination_id: int, weight_constraints: Constraints) -> float:
        node = self._get_node_by_id(node_id)
        destination = self._get_node_by_id(destination_id)
        max_weight = weight_constraints.max
        distance = abs(node.x - destination.x) + abs(node.y + destination.y)
        heuristic = distance + (max_weight - node.g) * node.value
        return heuristic

    def tour(self, start_id: int, destination_id: int, weight_constraints: Constraints) -> Path:
        max_weight = weight_constraints.max
        






