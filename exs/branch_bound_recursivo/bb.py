from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    def __init__(self, index, taken, value, room):
        self.index = index
        self.taken = taken
        self.value = value
        self.room = room
        return

    def estimate(self, items):
        return self.value + sum([item.value for item in items[self.index:]])

def solve_branch_and_bound_DFS(capacity, items, record_visiting_order = False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: best_value, taken, visiting_order
    """

    visiting_order = []

    root_node  = Node(index = 0, taken = [], value = 0, room = capacity)
    best       = root_node
    best_value = 0
    
    def recursive_BB(current):
        nonlocal best_value, best
        if record_visiting_order:
            visiting_order.append(current.index) 
        if current.estimate(items) < best_value or current.room < 0:
            return
        if current.value > best_value:
            best_value = current.value
            best = current
        if current.index < len(items):
            recursive_BB(Node(current.index+1, current.taken + [current.index+1], current.value + items[current.index].value, current.room - items[current.index].weight))
            recursive_BB(Node(current.index+1, current.taken, current.value, current.room))
    recursive_BB(root_node)
    return best_value, best.taken, visiting_order

first_line = input().split()
item_count = int(first_line[0])
capacity = int(first_line[1])
    
items = []
for i in range(1, item_count+1):
    line = input()
    parts = line.split()
    items.append(Item(i, int(parts[0]), int(parts[1])))

value, taken, visiting_order = solve_branch_and_bound_DFS(capacity, items, True)

print(visiting_order)
print(value)
print(taken)