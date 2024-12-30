import networkx as nx

def solve(graph: nx.Graph):
    """
    Calcula los componentes conectados. Retorna una lista
    de listas donde cada sublista contiene los componentes
    conectados.
    """
    solutions = []
    visited = set()
    
    def bfs(node):
        queue = list()
        queue.append(node)
        visited.add(node)
        current_path = []
        current_path.append(node)
        while len(queue) != 0:
            x = queue.pop(0)
            for n in graph.neighbors(x):
                if n not in visited:
                    current_path.append(n)
                    visited.add(n)
                    queue.append(n)
        return current_path.copy()

    for x in graph.nodes():
        if x not in visited:
            solutions.append(bfs(x))
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