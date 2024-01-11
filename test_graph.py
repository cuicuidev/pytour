from core import Edge, Node, Graph

nodes = [
    Node(0.0, "Casa"),
    Node(0.2, "Supermercado"),
    Node(0.5, "Parque Sofía"),
    Node(0.9, "Parque Can"),
    Node(-0.6, "Plaza Mayor"),
    Node(-0.8, "Estación de Autobuses"),
    Node(0.1, "Plaza Santa Ana"),
    Node(-0.3, "Hotel Mirador"),
    Node(0.7, "Parque Andarax")
]

edges = [
    Edge(250, nodes[0], nodes[1]), # Casa - Supermercado 250m
    Edge(250, nodes[1], nodes[0]), # Supermercado - Casa 250m

    Edge(150, nodes[0], nodes[2]), # Casa - Parque Sofía 150m
    Edge(150, nodes[2], nodes[0]), # Parque Sofía - Casa 150m

    Edge(150, nodes[1], nodes[2]), # Supermercado - Parque Sofía 150m
    Edge(150, nodes[2], nodes[1]), # Parque Sofía - Supermercado 150m

    Edge(250, nodes[0], nodes[4]), # Casa - Plaza Mayor 250m
    Edge(250, nodes[4], nodes[0]), # Plaza Mayor - Casa 250m

    Edge(400, nodes[4], nodes[5]), # Plaza Mayor - Estación de Autobuses 400m
    Edge(400, nodes[5], nodes[4]), # Estación de Autobuses - Plaza Mayor 400m

    Edge(300, nodes[5], nodes[8]), # Estación de Autobuses - Parque Andarax 300m
    Edge(300, nodes[8], nodes[5]), # Parque Andarax - Estación de Autobuses 300m

    Edge(300, nodes[8], nodes[3]), # Parque Andarax - Parque Can 300m
    Edge(300, nodes[3], nodes[8]), # Parque Can - Parque Andarax 300m

    Edge(100, nodes[2], nodes[3]), # Parque Sofía - Parque Can 100m
    Edge(100, nodes[3], nodes[2]), # Parque Can - Parque Sofía 100m

    Edge(300, nodes[1], nodes[6]), # Supermercado - Plaza Santa Ana 300m
    Edge(300, nodes[6], nodes[1]), # Plaza Santa Ana - Supermercado 300m

    Edge(250, nodes[6], nodes[7]), # Plaza Santa Ana - Hotel Mirador 250m
    Edge(250, nodes[7], nodes[6]), # Hotel Mirador - Plaza Santa Ana 250m

    Edge(300, nodes[7], nodes[8]), # Hotel Mirador - Parque Andarax 300m
    Edge(300, nodes[8], nodes[7]), # Parque Andarax - Hotel Mirador 300m

    Edge(250, nodes[3], nodes[7]), # Parque Can - Hotel Mirador 250m
    Edge(250, nodes[7], nodes[3]), # Hotel Mirador - Parque Can 250m
]

G = Graph(nodes=nodes, edges=edges)
