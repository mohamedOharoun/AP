import minigraph as nx

def check_cycle(tree, new_edge):
    start, end = new_edge[0], new_edge[1]
    visited = set()

    def dfs(node):
        if node == end:
            return True
        visited.add(node)
        for neighbor in tree.neighbors(node):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    return dfs(start)


def solve(input_list):
    tree_edges_list = []
    graph = nx.Graph()

    for x in input_list:
        n1, n2, w = x.split()
        graph.add_edge(n1, n2, weight=int(w))

    tree = [x for x in graph.edges(data=True)]
    tree.sort(key=lambda x : x[2]["weight"])

    kruskal_tree = nx.Graph()
    while len(tree) != 0 or len(kruskal_tree.nodes()) != len(graph.nodes()):
        edge = tree.pop(0)
        if not check_cycle(kruskal_tree, edge):
            kruskal_tree.add_edge(edge[0], edge[1], weight=edge[2]["weight"])
            tree_edges_list.append([edge[0], edge[1], edge[2]["weight"]])
    # retorna una lista con las aristas del árbol de expansión mínima.
    # main.py recorrerá esta lista para calcular la suma de las aristas.
    return tree_edges_list

if __name__ == "__main__":
    first_line = input().split()
    num_lines  = int(first_line[0])

    input_list = []
    for j in range(num_lines):
        input_list.append(input())

    tree_edges_list = solve(input_list)

    # VPL output
    total_weight = 0
    for edge in tree_edges_list:
        total_weight += edge[2]

    print("total weight=", total_weight)