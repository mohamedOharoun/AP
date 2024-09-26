from sys          import maxsize as infinite
from simple_queue import *
def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {}                 # Diccionario con la distancia desde 
                                  # firstNode al resto de los nodos.
    for node in graph.nodes():
        distance[node] = infinite

    # solve it here!
    # ...
    Q = Queue()
    Q.enqueue(first_node)
    distance[first_node] = 0
    
    while not Q.isEmpty():
        node = Q.dequeue()
        for n in graph.neighbors(node):
            if distance[n] == infinite:
                distance[n] = distance[node] + 1
                Q.enqueue(n)
    return distance