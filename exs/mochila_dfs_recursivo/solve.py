def solve(items, capacity):
    taken = []
    sol = []
    max_value = -1
    def dfs(pos, value, weight):
        nonlocal sol
        nonlocal max_value
        if weight > capacity:
           return
        if value > max_value:
           sol = taken.copy()
           max_value = value
        for i, x in enumerate(items[pos+1:]):
           taken.append(pos+i+2)
           dfs(pos+i+1, value + x[0], weight + x[1])
           taken.pop()      
    for i, x in enumerate(items):
           taken.append(i+1)
           dfs(i, x[0], x[1])
           taken.pop()
    return sol, max_value
first_line = input().split()
items_count = int(first_line[0])
capacity = int(first_line[1])
items = []
for j in range(items_count):
    parts = input().split()
    value = int(parts[0])
    weight = int(parts[1])
    items.append( (value, weight) )
taken, value = solve(items, capacity)
if taken:
 print(f'{taken}:{value}')
else:
 print('No solution')
