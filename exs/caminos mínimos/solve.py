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
                temp = dist + graph.get_edge_data(n, node).get("weight")
                if temp <= dist_max:
                    dfs(node, temp)
        visited.remove(n)
        current_path.pop()
        return
    current_path.append(u)
    visited.add(u)
    for node in graph.successors(u):
        if node not in visited:
            dist = graph.get_edge_data(u, node)["weight"]
            dfs(node, dist)
        visited.discard(node)
        current_path.pop()
    return solutions_list