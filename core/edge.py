class Edge:

    def __init__(self, id: int, source: int, target: int) -> None:
        self.id = id
        self.source = source
        self.target = target

    def __str__(self) -> str:
        return f"Edge {self.id}: {self.source} -> {self.target}"
