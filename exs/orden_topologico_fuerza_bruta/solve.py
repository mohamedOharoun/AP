from b5 import My_Iterator
import networkx as nx

def solve(graph: nx.DiGraph, path):
    # Por definición, en el orden topológico un nodo no aparece hasta que 
    # todos sus predecesores han sido procesados.
    for i, x in enumerate(path[::-1]):
        for node in graph.predecessors(x):
            # Se comprueba que el predecesor ha parecido antes que el nodo.
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
    # Se comprueba que no haya nodos repetidos, por 2 razones:
    # 1. Debido a que el array tendrá capacidad para solo el número de nodos, una repetición implicaría la ausencia de un nodo.
    # 2. En un orden topológico, no se pueden repetir nodos.
    if len(c) != len(set(c)):
        continue
    if solve(graph, c):
        solutions.append(c.copy())
print(solutions)