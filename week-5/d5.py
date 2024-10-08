
def check(c):
    if len(c) != len(set(c)):
        return False
    for i, x in enumerate(c):
        for j in range(i+1, len(c)):
            if x+i == j+c[j] or x-i == c[j] - j:
                return False
    return True
def solve(num_queens):
    """
    Using backtracking compute all the solutions to place the
    given number of queens in a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """
    solutions_list = []

    def dfs(sol):
        nonlocal solutions_list
        if not check(sol):
            return
        if len(sol) == num_queens:
            solutions_list.append(sol.copy())
            return
        for x in range(num_queens):
            sol.append(x)
            dfs(sol)
            sol.pop()
    # solve it here!
    for x in range(num_queens):
        sol = [x]
        dfs(sol)
    
    return solutions_list

first_line = input().split()
num_queens = int(first_line[0])

solutions_list = solve(num_queens)

for solution in solutions_list:
    print(solution)