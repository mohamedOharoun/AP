# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_tabulation(items):
    table = [0]*len(items)
    taken = []
    n = len(items)
    
    def fill_table():
        # Primera fase: Rellenamos la lista 'table' con las
        # soluciones de todos los subproblemas (o sea, los
        # beneficios que puede conseguir el ladrón).
        # ...
        table[0] = items[0]
        table[1] = max(items[0], items[1])
        for i in range(2, n):
            table[i] = max(items[i] + table[i-2], table[i-1])
        return
        
    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. En el ejemplo de las
        # transparencias el contenido de esta lista es: [2,5]
        # (la segunda casa y la quinta casa).
        # ...
        temp = table[len(items) - 1]
        nonlocal taken
        i = len(items) - 1
        while i > -1 and temp > 0:
            if (table[i] != table[i-1] or i == 0) and table[i] <= temp:
                taken = [i+1] + taken
                temp -= items[i]
            i -= 1
        return
        
    fill_table()
    fill_taken()
    return table[n-1], taken

first_line = input().split()
item_count = int(first_line[0])

items = []
for i in range(1, item_count+1):
    parts = input().split()
    items.append(int(parts[0]))

# Comenzamos programando la recurrencia mediante tabulation
value1, taken1 = solve_tabulation(items)
print(value1)
print(taken1)

# Cuando termines tabulation, comenta el código anterior
# para desactivarlo (la llamada a solve_tabulation y los
# dos print) y descomenta las siguientes lineas para que
# programes la recurrencia mediante memoization.
# 
# value2, taken2 = solve_memoization(items)
# print(value2)
# print(taken2)

# Cuando termines los dos ejercicios puedes activar estas
# lineas para comprobar que los dos dan exactamente los
# mismos resultados.
#
# assert value1 == value2
# assert taken1 == taken2