directions = {
    "N": {"L": "W", "R": "E"},
    "S": {"L": "E", "R": "W"},
    "E": {"L": "N", "R": "S"},
    "W": {"L": "S", "R": "N"}
}
signs = {
    "N": 1,
    "S": -1,
    "E": 1,
    "W": -1
}
def solve(input_list):
    # Resuelve aqui este ejercicio
    # ...
    final_coordinates = [0,0]
    # Primer paso será siempre en horizontal.
    direction = "N"
    coordinate_index = 0
    # El resto de pasos estarán condicionados tanto en eje como en sentido según los pasos anteriores.
    for instruction in input_list:
        direction = directions[direction][instruction[0]]
        sign, mov_length = signs[direction], int(instruction[1:])
        final_coordinates[coordinate_index % 2] += sign * mov_length
        coordinate_index += 1
    return sum([abs(x) for x in final_coordinates])

first_line = input().split()
num_lines  = int(first_line[0])

input_list = []
for j in range(num_lines):
    input_list.append(input())

solution = solve(input_list)
print(solution)

