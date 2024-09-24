import networkx as nx

def build_graph():
    """ 
    Read data from the standard input and build the corresponding
    nondirected graph without weights. Nodes numbering starts with
    number 1 (that is, nodes are 1,2,3,...)
    """
    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])
    g = nx.Graph()

    # Paso 1: Crear el grafo no-dirigido con sus vértices
    for v in range(num_nodes):
        g.add_node(v+1)
    
    # Paso 2: Añadirle las aristas
    for e in range(num_edges):
        temp = input().split()
        g.add_edge(int(temp[0]), int(temp[1]))
        
    return g