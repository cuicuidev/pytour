from test_graph import G

def main():
    print("NODES\n")
    for node in G.nodes:
        print(node.tag)

    print("\n")
    print("EDGES\n")
    for edge in G.edges:
        print(f"{edge.weight}m {edge.source.tag} - {edge.target.tag}")

if __name__ == "__main__":
    main()
