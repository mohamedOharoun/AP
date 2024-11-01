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
    :return: Por ahora sólo devuelve la lista de nodos visitados
    """

    # Completa este código para realizar el recorrido DFS; tienes
    # indicados los sitios que debes completar con tres puntos
    # suspensivos ("...")

    # Utilizamos la lista 'alive' como nuestra pila de nodos vivos
    # (pendientes de visitar) para programar nuestro recorrido DFS.

    alive = []
    
    # Utilizamos la lista Visiting_Order como el registro de nodos
    # visitados (el contenido final de esta lista lo utiliza el VPL
    # para comprobar que nuestro recorrido DFS es correcto).

    visiting_order = []

    # 1) Creamos el nodo raiz (en este VPL todavía no utilizamos los
    #    parámetros taken, value, room, con lo que se inicializan con
    #    lista vacía y 0). El único valor necesario en el nodo es el
    #    indice al primer elemento de la lista (index = 0).
    # ...
    node = Node(0, [], 0, capacity)
    # Lo añadimos a la lista de nodos vivos (alive)
    # ...
    alive.append(node)
    incumbent = node
    # Mientras haya nodos en la lista de nodos vivos
    # ...
    while len(alive) != 0:  #sustituir el True por la condición que considere más adecuada
        
        # Avanzamos al siguiente nodo de nuestro recorrido DFS (hacemos un pop
        # de la lista) y lo registramos en nuestro recorrido DFS.
        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)
        if current.estimate(items) < incumbent.value or current.room < 0:
            continue
        if current.value > incumbent.value:
            incumbent = current
        # Si no hemos llegado al final del árbol
        #    1) Ramificamos (branch) por la derecha (append)
        #    2) Ramificamos (branch) por la izquierda (append)
        # ...
        if current.index < len(items):
            right_node = Node(current.index+1,
                              current.taken + [current.index+1],
                              current.value + items[current.index].value,
                              current.room - items[current.index].weight
                              )
            left_node = Node(current.index+1,
                             current.taken,
                             current.value, 
                             current.room
                             )
            alive.append(left_node)
            alive.append(right_node)
    return incumbent.value, incumbent.taken, visiting_order

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