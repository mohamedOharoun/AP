# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_memoization(items):
    mem = {}
    taken = []

    def t(n):
        # Primera fase: Calculamos la recurrencia guardando en
        # el diccionario la solución optima de cada subproblema.
        # ...
        #   Aviso: Para resolver este ejercicio no es valido
        #          utilizar el soporte de @functools
        key = n

        if key not in mem:
            if n >= 0:
                mem[key] = max(t(n-2) + items[n], t(n-1))
            else:
                mem[key] = 0
        return mem[n]

    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. En el ejemplo de las
        # transparencias el contenido de esta lista es: [2,5]
        # (la segunda casa y la quinta casa).
        # ...
        temp = mem[n]
        nonlocal taken
        i = len(items) - 1
        while i > -1 and temp > 0:
            if (mem[i] != mem[i-1] or i == 0) and mem[i] <= temp:
                taken = [i+1] + taken
                temp -= items[i]
            i -= 1
        return

    n = len(items) - 1    
    
    max_benefit = t(n)
    fill_taken()
    
    return max_benefit, taken


first_line = input().split()
item_count = int(first_line[0])

items = []
for i in range(1, item_count+1):
    parts = input().split()
    items.append(int(parts[0]))

# Comenzamos programando la recurrencia mediante tabulation
#value1, taken1 = solve_tabulation(items)
#print(value1)
#print(taken1)

# Cuando termines tabulation, comenta el código anterior
# para desactivarlo (la llamada a solve_tabulation y los
# dos print) y descomenta las siguientes lineas para que
# programes la recurrencia mediante memoization.
# 
value2, taken2 = solve_memoization(items)
print(value2)
print(taken2)

# Cuando termines los dos ejercicios puedes activar estas
# lineas para comprobar que los dos dan exactamente los
# mismos resultados.
#
# assert value1 == value2
# assert taken1 == taken2