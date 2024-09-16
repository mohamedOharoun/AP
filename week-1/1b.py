def solve(input_list):
    # Resuelve aqui este ejercicio
    # ...
    result = 0
    
    for item in input_list:
        #result += find_number(item, True)*10 + find_number(item)
        temp = [s for s in item if s.isdigit()]
        result += int(temp[0] + temp[-1])
    return result

def find_number(string, is_decena=False):
    string = string if is_decena else reversed(string)
    for s in string:
        if s.isdigit():
            return int(s)