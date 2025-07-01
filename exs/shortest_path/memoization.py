import minigraph as nx

def solve(graph, from_node, to_node):
    memo = {}
    
    def dfs(current_node, visited, current_path, current_dist):
        
        if current_node == from_node:
            return current_dist, current_path + [current_node]
        
        if current_node in memo:
            memo_dist, memo_path = memo[current_node]
            
            if current_dist >= memo_dist:
                return memo_dist, memo_path
        
        min_dist = float('inf')
        min_path = []
        
        for n in graph.predecessors(current_node):
            if n not in visited:
                temp = get_weight(current_node, n, graph)
                dist, path = dfs(n, visited | {n}, current_path + [current_node], current_dist + temp)
                
                if dist < min_dist:
                    min_dist = dist
                    min_path = path
        
        if current_node not in memo or min_dist < memo[current_node][0]:
            memo[current_node] = (min_dist, min_path)
            
        return min_dist, min_path
    
    distance, path = dfs(to_node, set(), [], 0)
    return distance, path[::-1]

def get_weight(node, predecessor, graph):
    for u, v, data in graph.in_edges(node, data=True):
        if u == predecessor:
            return data["weight"]

first_line = input().split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])
from_node  = int(first_line[2])
to_node    = int(first_line[3])

graph = nx.DiGraph()
for node_id in range(1,num_nodes+1):
    graph.add_node(node_id)

for j in range(1, num_edges+1):
   parts = input().split()
   u = int(parts[0])
   v = int(parts[1])
   w = int(parts[2])
   graph.add_edge(u, v, weight=w)

min_d, taken = solve(graph, from_node, to_node)
print(min_d)
print(taken)