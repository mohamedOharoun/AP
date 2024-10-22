
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
