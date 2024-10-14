import networkx as nx
from sys import maxsize as infinite

def solve(graph: nx.DiGraph, u, v):
    solutions_list = []
    current_path = []
    dist_max = infinite
    visited = set()

    def dfs(n, dist):
        nonlocal dist_max
        visited.add(n)
        current_path.append(n)
        if current_path[-1] == v:
            if dist < dist_max:
                solutions_list.clear()
            dist_max = dist
            solutions_list.append(current_path.copy())
            return
        for node in graph.successors(n):
            if node not in visited:
                temp = dist + graph[n][node]["weight"]
                if temp <= dist_max:
                    dfs(node, temp)
                    current_path.pop()
                    visited.discard(node)
        return

    dfs(u,0)
    return solutions_list