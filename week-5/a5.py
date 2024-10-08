def next_number(digits, base):
    """
    :param digits: list containing all the digits of a number 
                   in the given base
    :param base: numeric base of the number
    :return: list representing the next value of the number

     Example: digits = [0, 1, 0, 1]   number 5
                base = 2

              returns [0, 1, 1, 0]    number 6
    """

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

# Main
first_line = input().split()
num_values = int(first_line[0])
base       = int(first_line[1])

for j in range(num_values):
    data = input()

    # Convertimos la string en la lista que contiene
    # el número de entrada.
    digits = []
    for digit in data:
        digits.append(int(digit))

    # Mostramos la lista con el número de entrada y
    # la lista con el siguiente número.
    print(digits, '- ', end="")
    print(next_number(digits, base))