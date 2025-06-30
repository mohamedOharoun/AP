import minigraph as nx
def solve(graph, node):

    prim = nx.Graph()
    visited_nodes = set()
    visited_edges = set()

    edges_pool = set([(e[0], e[1], e[2]["weight"]) for e in graph.edges(node, data=True)])

    edges_list = list()
    while len(graph.nodes()) != len(prim.nodes()):
        edge = min(
                edges_pool - visited_edges,
                key=lambda e : e[2]
            )
        visited_edges.add((edge[0], edge[1], edge[2]))
        if edge[0] in visited_nodes and edge[1] not in visited_nodes:
            visited_nodes.add(edge[0])
            visited_nodes.add(edge[1])
            for x in [(e[0], e[1], e[2]["weight"]) for e in graph.edges(edge[0], data=True)]:
                edges_pool.add(x)
            for x in [(e[0], e[1], e[2]["weight"]) for e in graph.edges(edge[1], data=True)]:
                edges_pool.add(x)
            prim.add_edge(edge[0], edge[1], weight=edge[2])
            edges_list.append(edge)
    return edges_list

if __name__ == "__main__":
    num_lines = int(input())
    graph = nx.Graph()
    meh = list()
    for l in range(num_lines):
        n1, n2, w = input().split()
        meh.append(n1)
        graph.add_edge(n1, n2, weight=int(w))
    
    sol = solve(graph, meh[0])

    total_weight = 0

    for e in sol:
        total_weight += e[2]
    
    print(total_weight)