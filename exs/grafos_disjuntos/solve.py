import networkx as nx

def solve(graph: nx.Graph):
    solutions = []
    current_path = []
    visited = set()

    def dfs(node):
        for x in graph.neighbors(node):
            if x not in visited:
                visited.add(x)
                current_path.append(x)
                dfs(x)
        # Una vez se procesen todos los nodos de un grafo se retorna
        return

    for x in graph.nodes():
        if x not in visited:
            visited.add(x)
            current_path.append(x)
            dfs(x) # Se empiezan a procesar todo el grafo asociado al nodo.
            solutions.append(current_path.copy())
            current_path.clear() # Se elimina todos los nodos procesados y se comienza con otro nodo.
    return solutions

first_line = int(input())
graph = nx.Graph()
for x in range(first_line):
    temp = input().split()
    if len(temp) == 1:
        graph.add_node(int(temp[0]))
    else:
        graph.add_edge(int(temp[0]), int(temp[1]))
for x in graph.nodes():
    print(x, end=", ")
print()
print(solve(graph))