from core.graph import Graph
# from core.algorithms import Tour

def main():
    G = Graph.from_osm("test.osm")
    print(G)

    # pathfinding_algorithm = Tour()
    # path = G.get_optimal_path(pathfinding_algorithm, 0, 0)
    # print(path)

if __name__ == "__main__":
    main()
