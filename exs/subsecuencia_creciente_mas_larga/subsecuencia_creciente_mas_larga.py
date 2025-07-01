import time
def solve_memoization(items):
    memo = {}
    taken = []
    predecessors = {}
        
    def _solve(index):
        if index in memo:
            return memo[index]
        if index == 0:
            memo[index] = 1
            return memo[index]
        if index not in memo:
            memo[index] = 1
            predecessors[index] = None
        for i in range(index-1, -1, -1):
            temp = memo[index]
            if items[index] > items[i]:
                memo[index] = max(memo[index], _solve(i) + 1)
                if memo[index] != temp:
                    predecessors[index] = i
        return memo[index]
    max_length = max(_solve(i) for i in range(len(items)))
    max_length = 0
    max_index = 0
    for i in range(len(items)):
        if memo[i] > max_length:
            max_length = memo[i]
            max_index = i

    # Reconstruct the LIS by walking predecessors backward
    taken = []
    current = max_index
    while current is not None:
        taken.append(items[current])
        current = predecessors[current]

    taken.reverse()  # Reverse to get LIS in correct order

    return max_length, taken

def solve_tabulation(items):
    table = []  # Almacenará la longitud de la subsecuencia más larga para cada índice
    taken = []  # Almacenará los elementos seleccionados en la subsecuencia óptima

    def fill_table():
        n = len(items)

        # Declare the tablet (itemsay) for table and
        # initialize table values for all indexes
        nonlocal table
        table = [1] * n
        # Compute optimized table values in bottom
        # -up manner
        for i in range(1, n):
            for j in range(0, i):
                if items[i] > items[j]:
                    table[i] = max(table[i], table[j] + 1)
        # Return the maximum of all table values
        return max(table)

    def fill_taken():
        nonlocal taken
        # Find the length of longest sequence
        max_length = max(table)
        # Start from the rightmost element
        current_length = max_length
        index = len(items) - 1
        
        # Work backwards to find elements of the sequence
        while current_length > 0 and index >= 0:
            if table[index] == current_length:
                # Check if this element can be part of our sequence
                if not taken or items[index] < items[taken[0]-1]:
                    taken.insert(0, index+1)  # Insert at beginning to maintain order
                    current_length -= 1
            index -= 1
        

    fill_table()
    fill_taken()

    return max(table), taken

first_line = input().split()
item_count = int(first_line[0])

items = []
for i in range(1, item_count+1):
    parts = input().split()
    items.append(int(parts[0]))

start = time.time_ns()
value, taken = solve_tabulation(items)
end = time.time_ns() - start
print(end)
print(value)
print(taken)
start = time.time_ns()
value, taken = solve_memoization(items)
end = time.time_ns() - start
print(end)
print(value)
print(taken)
