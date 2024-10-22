from b5 import My_Iterator
import networkx as nx

def solve(graph: nx.DiGraph, path):
    for i, x in enumerate(path[::-1]):
        for node in graph.predecessors(x):
            if node not in path[:(len(path) -i -1)]:
                return False
    return True


num = int(input())

graph = nx.DiGraph()
for i in range(num):
    temp = input().split()
    graph.add_edge(int(temp[0]), int(temp[1]))
solutions = []
obj = My_Iterator(graph.number_of_nodes(), graph.number_of_nodes())
for c in obj.next():
    if len(c) != len(set(c)):
        continue
    if solve(graph, c):
        solutions.append(c.copy())
print(solutions)