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
        return

    for x in graph.nodes():
        if x not in visited:
            visited.add(x)
            current_path.append(x)
            dfs(x)
            solutions.append(current_path.copy())
            current_path.clear()
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