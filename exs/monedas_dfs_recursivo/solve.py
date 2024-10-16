from sys import maxsize as infinity
def solve(coins, change):
    max_num = infinity
    curren_path = []
    current_coins = []
    solutions = []
    def dfs(coin, pos, curr_change):
        nonlocal max_num
        # Se actualiza el estado en el salto presente.
        curren_path.append(pos)
        current_coins.append(coin)
        curr_change += coin
        # Se realiza la comprobación de viabilidad.
        if curr_change > change or len(curren_path) > max_num or coin in current_coins[pos-1:]:
            return
        # Se encuentra solución.
        if curr_change == change:
            # Si encuentra una solución más óptima se descartan las anteriores y se actualiza el óptimo
            if len(curren_path) < max_num:
                max_num = len(curren_path)
                solutions.clear()
            solutions.append(curren_path.copy())
            return
        # Se avanza en la búsqueda.
        for i, x in enumerate(coins[pos:]):
            dfs(x, pos+i+1, curr_change)
            curren_path.pop()
            current_coins.pop()
    # Inicializar el camnino con cada moneda.
    for i, x in enumerate(coins):
        dfs(x, i+1, 0)
        curren_path.pop()
        current_coins.pop()
    return solutions

first_line = input().split(" ")
num_coins = int(first_line[0])
change = int(first_line[1])
coins = []
for i in range(num_coins):
    coins.append(int(input()))
print(solve(coins, change))