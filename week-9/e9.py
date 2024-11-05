import networkx as nx
import time
def solve(input_list, voltage, N):
    # Resuelve aqui este ejercicio
    num_solutions = 0
    mem = {}

    graph = nx.DiGraph()
    nodes = set()
    for s in input_list:
        temp = s.split()
        node1 = int(temp[0])
        node2 = int(temp[1])
        graph.add_edge(node1, node2)
        nodes.add(node1)
        nodes.add(node2)

    def dfs(sol):
        num_solutions = 0
        if sol in mem:
            return mem[sol]
        if sol == voltage:
            return 1
        
        for i in range(N+1):
            if (sol + i) not in nodes:
                continue
            for x in graph.successors(sol + i):
                    num_solutions += dfs(x)
        mem[sol] = num_solutions
        return num_solutions

    for x in graph.successors(0):
        num_solutions +=  dfs(x)
    return num_solutions

first_line = input().split()
num_lines  = int(first_line[0])
voltage    = int(first_line[1])
N          = int(first_line[2])

input_list = []
for j in range(num_lines):
    charger_data = input()

    # Para simplificar el ejercicio, no hay ningún cargador duplicado
    assert charger_data not in input_list

    input_list.append(charger_data)

num_solutions = solve(input_list, voltage, N)
start = time.time()
print(num_solutions, "solutions")
end = time.time()
print(end - start)
