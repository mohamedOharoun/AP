
import networkx as nx


def dsat_coloring(graph, order_nodes):
    # Inicializar colores y colores vecinos
    colors = {node: None for node in order_nodes}
    neighbor_colors = {node: set() for node in order_nodes}

    # Colorear primer nodo (máximo grado) con color 0
    first_node = max(order_nodes, key=lambda x: (graph.degree[x], -ord(str(x)[0])))
    colors[first_node] = 0

    for neighbor in graph.neighbors(first_node):
        neighbor_colors[neighbor].add(0)

    # Colorear nodos restantes
    while None in colors.values():
        # Seleccionar nodo con mayor saturación, grado y orden lexicográfico
        uncolored = [n for n in order_nodes if colors[n] is None]
        selected = max(uncolored, key=lambda x: (len(neighbor_colors[x]), graph.degree[x], -ord(str(x)[0])))

        # Asignar menor color disponible
        used_colors = neighbor_colors[selected]
        color = 0
        while color in used_colors:
            color += 1
        colors[selected] = color

        # Actualizar colores vecinos
        for neighbor in graph.neighbors(selected):
            neighbor_colors[neighbor].add(color)

    return [colors[node] for node in order_nodes]

input_data = """7 12
1 2
2 3
3 4
4 5
5 6
6 1
7 1
7 2
7 3
7 4
7 5
7 6
"""

# Convertir input en lista de líneas
lines = input_data.strip().split("\n")

# Primera línea: número de nodos y aristas
first_line = lines[0].split()
num_nodes = int(first_line[0])
num_edges = int(first_line[1])

# Crear grafo
graph = nx.Graph()
graph.add_nodes_from(range(1, num_nodes + 1))

# Leer aristas
for j in range(1, num_edges + 1):
    parts = lines[j].split()
    u = int(parts[0])
    v = int(parts[1])
    graph.add_edge(u, v)

# Orden de los nodos
order_nodes = list(graph.nodes())

# Llamar a tu función DSATUR
colores_nodos = dsat_coloring(graph, order_nodes)

# Imprimir resultado
print(colores_nodos)