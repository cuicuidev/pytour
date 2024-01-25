from .node import Node

class Path:

    def __init__(self, nodes: list[Node]) -> None:
        self.nodes = nodes

    def __len__(self):

        def distance(nodes: list[Node]) -> float:
            result = 0
            queue = [nodes.pop(0)]

            while queue:
                node = queue.pop(0)
                result += node.coordinates.get_distance(nodes[0].coordinates)
                queue.append(nodes.pop(0))

            return result

        return distance(self.nodes)
    
    def __str__(self) -> str:
        return f"Path({self.nodes.__str__()})"
