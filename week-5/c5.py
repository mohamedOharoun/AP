
def next_number(digits, base):
    next_digits = digits.copy()

    # Añade tu código aqui
    # ...
    next_digits[len(next_digits) - 1] += 1
    for i in range(len(next_digits)-1, -1, -1):
        x = next_digits[i]
        if x % base == 0:
            next_digits[i] = 0
            if i != 0:
                next_digits[i-1] += 1
        else:
            break
    return next_digits
    
# ----------------------------------------------------------

class My_Iterator:

    def __init__(self, num_digits, base):
        # 2.1 Añade código aqui
        # ...
        self.__num = [0]*num_digits
        self.__base = base

    def next(self):
        # 2.2 Añade código aqui
        # ...
        total = self.__base ** len(self.__num)
        for i in range(total):
            yield self.__num
            self.__num = next_number(self.__num, self.__base)
        
        # Cuando no quedan valores simplemente retornamos
        return

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
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []

    # solve it here!
    iter = My_Iterator(num_queens,num_queens)
    for i in iter.next():
        if check(i):
            solutions_list.append(i)
    return solutions_list

first_line = input().split()
num_queens = int(first_line[0])

solutions_list = solve(num_queens)

for solution in solutions_list:
    print(solution)