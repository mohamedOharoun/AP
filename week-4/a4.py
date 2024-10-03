import networkx as nx

def build_digraph_with_weights():
    """ 
    Read data from the standard input and build the corresponding
    directed graph with weights. Nodes numbering starts with number
    1 (that is, nodes are 1,2,3,...)
    """

    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])
    graph = nx.DiGraph()
    # Paso 1: Crear grafo direcional con num_nodes
    for n in range(num_nodes):
        graph.add_node(n+1)
    # Paso 2: Añadir los vértices del grafo
    for e in range(num_edges):
        temp = input().split()
        graph.add_edge(int(temp[0]), int(temp[1]), weight=int(temp[2]))

    return graph

