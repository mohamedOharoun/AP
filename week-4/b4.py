import networkx as nx
from simple_stack import Stack
from a4 import build_digraph_with_weights

def dfs_topological_sort(graph: nx.DiGraph):
    """
    Compute one topological sort of the given graph.
    """
    
    # La solucion que retorna esta función es un diccionario de Python.
    #   * La clave del diccionario es el número del nodo
    #   * El valor es el orden topologico asignado a ese nodo
    # 
    # Por ejemplo, si tenemos el siguiente grafo dirigido con 3 vertices:
    #                    3 ---> 2 ---> 1
    # ... el orden topologico es:
    #                El vértice 3 va en la primera posición
    #                El vértice 2 en la segunda posición
    #                El vértice 1 en la tercera posición
    # Con lo que debemos devolver un diccionario con este contenido:
    #     {1: 3, 2: 2, 3: 1}
    N = graph.number_of_nodes()
    all = Stack()
    
    visibleNodes = set()  # En este ejercicio utilizamos un set
                          # para recordar los nodos visibles
    order = {}
    # solve it here! ------------------------------------------------
    def dfs_iterative(u):
        nonlocal N
        #  1. Añade código aqui
        #  ...
        s = Stack()
        s.push(u)

        while not s.isEmpty():
            node = s.pop()
            for n in graph.successors(node):
                if n not in visibleNodes:
                    s.push(n)
                    visibleNodes.add(n)
            print(node)
            all.push(node)
        return

    #  2. Añade código también aqui
    #  ...
    for n in graph.nodes:
        if n not in visibleNodes:
            visibleNodes.add(n)
            dfs_iterative(n)
    return order

graph    = build_digraph_with_weights()
assert nx.is_directed_acyclic_graph(graph)   # Our input graphs must be ok

solution = dfs_topological_sort(graph)
d_swap = {v: k for k, v in solution.items()}

print(dict(sorted(d_swap.items())))