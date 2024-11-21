import networkx as nx


     

def dsat_coloring(graph: nx.Graph, order_nodes):
    def get_degree(node):
        return len(list(graph.neighbors(node)))
    
    def get_saturation_degree(node):
        # Count unique colors of neighbors
        if nodes_colors[node] is not None:
            return 0
        neighbor_colors = set()
        for neighbor in graph.neighbors(node):
            if nodes_colors[neighbor] is not None:
                neighbor_colors.add(nodes_colors[neighbor])
        return len(neighbor_colors)
    
    def select_next_node(graph):
        # Select node with highest saturation degree, 
        # breaking ties by highest degree
        uncolored_nodes = [n for n in graph.nodes() if nodes_colors[n] is None]
        return max(uncolored_nodes, 
                   key=lambda node: (get_saturation_degree(node), get_degree(node), -node))
    
    def get_smallest_available_color(node):
        # Find smallest color not used by neighbors
        used_colors = set()
        for neighbor in graph.neighbors(node):
            if nodes_colors[neighbor] is not None:
                used_colors.add(nodes_colors[neighbor])
        
        # Find the smallest unused color
        color = 0
        while color in used_colors:
            color += 1
        return color

    # Initialize color assignment
    nodes_colors = {node: None for node in order_nodes}
    
    # Color the first node with the first color
    first_node = max(order_nodes, key=get_degree)
    nodes_colors[first_node] = 0
    
    # Color remaining nodes
    while None in nodes_colors.values():
        # Select next node to color
        current_node = select_next_node(graph)
        
        # Assign smallest available color
        nodes_colors[current_node] = get_smallest_available_color(current_node)
    
    return [nodes_colors[node] for node in order_nodes]



def create_wheel_graph():
    """Crea un wheel graph, centrado en 'g'

    Returns:
        tuple: Un grafo de NetworkX y la lista de nodos.
    """
    G = nx.Graph()
    nodos = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    G.add_nodes_from(nodos)
    aristas = [('a', 'g'), ('b', 'g'), ('c', 'g'), ('d', 'g'), ('e', 'g'), ('f', 'g'),
               ('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'a')]
    G.add_edges_from(aristas)
    return G, nodos

first_line = input().split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])
    
graph = nx.Graph()
graph.add_nodes_from(range(1,num_nodes+1))


for j in range(1, num_edges+1):
        parts = input().split()

        u = int(parts[0])
        v = int(parts[1])

        graph.add_edge(u, v)


order_nodes = graph.nodes()
colores_nodos = dsat_coloring(graph, order_nodes)
    
print(colores_nodos)