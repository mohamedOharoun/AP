import time
import re

numbers_regex = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
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
        # result += search_number(string)*10 + search_number(string[::-1])
        result += search_regex(string)
    return result

def search_number(string):
    for i, s1 in enumerate(string):
        if s1.isdigit():
            return int(s1)
        if s1 not in "otfsen":
            continue
        for s2 in string[i+1:i+5]:
            s1 += s2
            if s1 in numbers.keys() or s1.isdigit():
                return numbers[s1]

def toNumber(string):
    if string.isdigit():
        return string
    return numbers_regex[string]

def search_regex(string):
    regex = r"\d|one|t(?:wo|hree)|f(?:our|ive)|s(?:ix|even)|eight|nine"
    var = re.findall(regex,string)
    return int(toNumber(var[0]) + toNumber(var[-1]))

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

s = "3three2"
search_regex(s)