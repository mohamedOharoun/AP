import minigraph as nx

def solve(string):

    def get_freqs(string):
        freqs = dict()
        for char in string:
            freqs[char] = freqs.get(char, 0) + 1
        return freqs
    
    def build_ordered_dict(freqs, other=None):
        if other != None:
            freqs.update(other)
        return dict(sorted(freqs.items(), key=lambda char : char[1], reverse=True))
    
    def huffman_code(graph: nx.DiGraph, freqs, root):
        sol = dict()
        def dfs(node, prefix):
            i = 0
            for n in sorted(graph.neighbors(node), key=lambda k : k[1]):
                dfs(n, f"{prefix}{i}")
                i += 1
            if node[0] in freqs.keys():
                sol[node[0]] = prefix
        dfs(root, "")
        return sol

    def build_graph(freqs):
        heap = dict(freqs)
        graph = nx.DiGraph()
        root_node = None
        while len(freqs) != 0:
            node1 = heap.popitem()
            node2 = heap.popitem()
            freqs.pop(node1[0], None)
            freqs.pop(node2[0], None)

            sum = node1[1] + node2[1]
            label = f"{node1[0]}{node2[0]}"
            new_node = (label, sum)

            graph.add_node(new_node)
            graph.add_edge(new_node, (f"{node1[0]}", node1[1]))
            graph.add_edge(new_node, (f"{node2[0]}", node2[1]))

            heap = build_ordered_dict(heap, {label : sum})

            root_node = new_node
        return graph, root_node
    
    freqs = build_ordered_dict(get_freqs(string))
    graph, root_node = build_graph(dict(freqs))
    huffman = huffman_code(graph, freqs, root_node)
    sol = sum([freqs[k] * len(huffman[k]) for k in freqs.keys()])
    return sol

if __name__ == "__main__":
    string = input()
    print(f"Total bits = {solve(string)}")