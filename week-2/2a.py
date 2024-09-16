import time
numbers = {
    'one': 10,
    'two': 20,
    'three': 30,
    'four': 40,
    'five': 50,
    'six': 60,
    'seven': 70,
    'eight': 80,
    'nine': 90,
    'eno': 1,
    'owt': 2,
    'eerht': 3,
    'ruof': 4,
    'evif': 5,
    'xis': 6,
    'neves': 7,
    'thgie': 8,
    'enin': 9
}

def solve(input_list):
    # Resuelve aqui este ejercicio
    # ...
    result = 0
    for string in input_list:
        result += search_number(string) + search_number(string[::-1])
    return result

def search_number(string):
    i = 0
    for s1 in string:
        if s1 not in "otfsen":
            i += 1
            continue
        temp = s1
        for s2 in string[i+1:i+5]:
            temp += s2
            if temp in numbers.keys():
                return numbers[temp]
        i += 1
strings = [
    "oneabctwo",
    "pqrthreestueightvwx",
    "aonebtwocthreedfourefivef",
    "trebsevenuchet"
]
start = time.time()
sol = solve(strings)
end = time.time()
print(sol, end - start)