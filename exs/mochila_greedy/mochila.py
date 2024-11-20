def solve(items, capacity):
    taken = []
    value = 0
    items = [(i, x) for i, x in enumerate(items)]
    items.sort(key = lambda x : x[1][0] / x[1][1], reverse=True)
    acc_weight = 0
    print(items)
    for i in items:
        if acc_weight + i[1][1] <= capacity:
            taken.append(i[0]+1)
            value += i[1][0]
            acc_weight += i[1][1]
        if acc_weight == capacity:
            break
    return taken, value

first_line   = input().split()
items_count  = int(first_line[0])
capacity     = int(first_line[1])

items = []

for j in range(items_count):
   parts  = input().split()
   value  = int(parts[0])
   weight = int(parts[1])
   items.append( (value, weight) )

taken, value = solve(items, capacity)

if taken:
   print(f'{sorted(taken)}:{value}')
else:
   print('No solution')