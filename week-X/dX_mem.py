from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_memoization(items, capacity):
    taken = []
    mem={}

    def t(n,w):
        # Primera fase: Calculamos la recurrencia guardando en
        # el diccionario la solución optima de cada subproblema.
        #   Aviso: Para resolver este ejercicio no es valido
        #          utilizar el soporte de @functools
        # ...
        if (n,w) in mem:
            return mem[(n,w)]
        if n < 0:
            mem[(n, w)] = 0
            return 0
        if items[n].weight > w:
            mem[(n, w)] = t(n-1, w)
            return mem[(n, w)]
        mem[(n, w)] = max(t(n-1, w), t(n-1, w-items[n].weight) + items[n].value)
        return mem[(n, w)]

    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de los items elegidos.
        # ...
        i = n
        k = capacity
        while i >= 0 and k > 0:
            if mem[(i, k)] != mem[(i-1, k)]:
                taken.insert(0, i+1)
                k -= items[i].weight
            i -= 1
        return taken

    n = len(items) - 1

    max_benefit = t(n,capacity)
    fill_taken()

    return max_benefit, taken


first_line = input().split() 	# N, Capacity
N          = int(first_line[0])
capacity   = int(first_line[1])

items = []
for i in range(1, N+1):
    parts = input().split()
    items.append(Item(i, int(parts[0]), int(parts[1])))

# Comenzamos programando la recurrencia mediante tabulation
# value1, taken1 = solve_tabulation(items, capacity)
# print(value1, taken1)

# Cuando termines tabulation, comenta el código anterior
# para desactivarlo (la llamada a solve_tabulation y los
# dos print) y descomenta las siguientes lineas para que
# programes la recurrencia mediante memoization.
 
value2, taken2 = solve_memoization(items, capacity)
print(value2, taken2)

# Cuando termines los dos ejercicios puedes activar estas
# lineas para comprobar que los dos dan exactamente los
# mismos resultados.

# assert value1 == value2
# assert taken1 == taken2
