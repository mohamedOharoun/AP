from collections       import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

import numpy as np

def solve_tabulation(items, capacity):
    taken = []
    table = np.zeros((len(items)+1,capacity+1), dtype=int)

    def fill_table():
        for i in range(1, len(items)+1):
            for k in range(1, capacity+1):
                withoutTaken = table[i-1][k]
                withTaken = 0
                
                if(k >= items[i-1].weight):
                    withTaken = items[i-1].value
                    remaining_capacity = k - items[i-1].weight
                    withTaken += table[i-1][remaining_capacity]
                
                table[i][k] = max(withTaken, withoutTaken)
        return table[len(items)][capacity]

    def fill_taken():
        i = len(items)
        k = capacity
        while i >= 0 and k > 0:
            if table[i][k] != table[i-1][k]:
                k -= items[i-1].weight
                taken.insert(0, i)
            i -= 1
        return

    fill_table()
    fill_taken()
    return table[len(items)][capacity], taken

first_line = input().split() 	# N, Capacity
N          = int(first_line[0])
capacity   = int(first_line[1])

items = []
for i in range(1, N+1):
    parts = input().split()
    items.append(Item(i, int(parts[0]), int(parts[1])))

# Comenzamos programando la recurrencia mediante tabulation
value1, taken1 = solve_tabulation(items, capacity)
print(value1, taken1)

# Cuando termines tabulation, comenta el código anterior
# para desactivarlo (la llamada a solve_tabulation y los
# dos print) y descomenta las siguientes lineas para que
# programes la recurrencia mediante memoization.
 
# value2, taken2 = solve_memoization(items, capacity)
# print(value2, taken2)

# Cuando termines los dos ejercicios puedes activar estas
# lineas para comprobar que los dos dan exactamente los
# mismos resultados.

# assert value1 == value2
# assert taken1 == taken2
