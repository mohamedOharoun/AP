def solve(coins, change):
    sol = 0
    taken = []
    coins = [(x, i) for i, x in enumerate(coins)]
    coins.sort(key=lambda x : x[0], reverse=True)
    for c in coins:
        if sol + c[0] <= change:
            sol += c[0]
            taken.append(c[1]+1)
        if sol == change:
            break
    
    return None if sol != change else taken

first_line = input().split()
num_coins  = int(first_line[0])
change     = int(first_line[1])

coins = []
for j in range(1, num_coins+1):
   parts = input().split()
   coin  = int(parts[0])
   coins.append(coin)

solution = solve(coins, change)

if solution:
   print(sorted(solution))
else:
   print('No hay solucion')