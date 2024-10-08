
import networkx as nx
def solve(input_list, voltage):
    solutions_list = []

    # Programa tu código aquí
    # ...
    graph = nx.DiGraph()
    for s in input_list:
        temp = s.split()
        graph.add_edge(int(temp[0]), int(temp[1]))
    max_level = -1
    def dfs(sol, level):
        nonlocal max_level
        if max_level != -1 and level > max_level:
            return
        if sol[-1][1] == voltage:
            max_level = level
            solutions_list.append(sol.copy())
            return
        for x in graph.successors(sol[-1][1]):
            sol.append((sol[-1][1],x))
            dfs(sol, level+1)
            sol.pop()
    for x in graph.successors(0):
        sol = [(0,x)]
        dfs(sol, 1)
    temp = list()
    for x in solutions_list:
        if len(x) == max_level:
            temp.append(x)
    solutions_list = temp
    return solutions_list

first_line = input().split()
num_lines  = int(first_line[0])
voltage    = int(first_line[1])

input_list = []
for j in range(num_lines):
    input_list.append(input())

try:
    solutions_list = solve(input_list, voltage)
    # VPL output

    for sublist in solutions_list:
        print(sublist)

    print(len(solutions_list), "solutions")

except:
    print ("wrong code; exception raised")