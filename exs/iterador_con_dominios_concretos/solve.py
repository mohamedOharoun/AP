class My_Iterator:
    
    def __init__(self, num_digits, digit_values):
        self.digit_values = digit_values
        self.num_digits = num_digits
    
    def next(self):
        current_path = []
        def dfs(level):
            if level == self.num_digits:
                yield current_path.copy()
                return 
            for x in self.digit_values[level]:
                current_path.append(x)
                yield from dfs(level + 1)
                current_path.pop()
        yield from dfs(0)

first_line = input().split()
num_digits = int(first_line[0])
digit_values = []
for j in range(num_digits):
    line = input().split() # domain values of each digit
    int_values = []
    for value in line:
        int_values.append(int(value))
    digit_values.append(int_values)
obj = My_Iterator(num_digits, digit_values)
for c in obj.next():
    print(c)
