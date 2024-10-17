
class My_Iterator:
    def __init__(self, digs, mins, maxs):
        self.digs = digs
        self.mins = mins
        self.maxs = maxs
        return

    def next(self):
        current_path = []
        def dfs(level):
            if level == self.digs:
                yield current_path
                return
            for x in range(self.mins[level], self.maxs[level] + 1):
                current_path.append(x)
                yield from dfs(level + 1)
                current_path.pop()
        yield from dfs(0)
        return


first_line = input().split()
num_digits = int(first_line[0]) # Number of digits
second_line = input().split() # min values of each digit
min_values = []
for j in range(num_digits):
    min_values.append(int(second_line[j]))
third_line = input().split() # max values of each digit
max_values = []
for j in range(num_digits):
    max_values.append(int(third_line[j]))
obj = My_Iterator(num_digits, min_values, max_values)
for c in obj.next():
    print(c)
