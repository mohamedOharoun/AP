# Resolver el problema de la mochila con la restricción de no coger dos elementos consecutivos

def mochila_no_consecutiva(values, weights, capacity):
    n = len(values)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # No tomar el ítem i
            curr_pos = table[i-1][w]
            
            # Tomar el ítem i (saltando i-1)
            around_pos = 0
            if weights[i-1] <= w:
                if i >= 2:
                    around_pos = table[i-2][w - weights[i-1]] + values[i-1]
                else:
                    around_pos = values[i-1]

            table[i][w] = max(curr_pos, around_pos)

    # Recuperar los ítems elegidos
    elegidos = []
    i, w = n, capacity
    while i > 0:
        if table[i][w] != table[i-1][w]:
            elegidos.append(i)
            w -= weights[i-1]
            i -= 2  # saltar el consecutivo
        else:
            i -= 1

    elegidos.reverse()
    return table[n][capacity], elegidos

values = [3, 10, 3, 1, 2]
weights = [1, 1, 1, 1, 1]
capacity = 5

beneficio, items = mochila_no_consecutiva(values, weights, capacity)
print(beneficio, items)
