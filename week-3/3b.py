import networkx as nx
directions = {
    "N": {"L": {"sign": -1, "direction": "W"}, "R": {"sign": 1, "direction": "E"}},
    "S": {"L": {"sign": 1, "direction": "E"}, "R": {"sign": -1, "direction": "W"}},
    "E": {"L": {"sign": 1, "direction": "N"}, "R": {"sign": -1, "direction": "S"}},
    "W": {"L": {"sign": -1, "direction": "S"}, "R": {"sign": 1, "direction": "N"}}
}
def solve(input_list):
    # Resuelve aqui este ejercicio
    # ...
    is_vertical = False
    final_coordinates = [0,0]
    # Primer paso será siempre en horizontal.
    direction = "N"
    # El resto de pasos estarán condicionados tanto en eje como en sentido según los pasos anteriores.
    for instruction in input_list:
        coordinate_index = 1 if is_vertical else 0
        temp = directions[direction][instruction[0]]
        sign, direction = temp["sign"], temp["direction"]
        mov_length = int(instruction[1:])
        final_coordinates[coordinate_index] += sign * mov_length
        is_vertical = not is_vertical
    return sum([abs(x) for x in final_coordinates])

first_line = input().split()
num_lines  = int(first_line[0])

input_list = []
for j in range(num_lines):
    input_list.append(input())

solution = solve(input_list)
print(solution)

