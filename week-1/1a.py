def order_crossover(parent1, parent2, lower_bound, upper_bound):
    size = len(parent1)
    child1 = [0]*size
    child1[lower_bound:upper_bound] = parent1[lower_bound:upper_bound]
    child_index = par2_index = upper_bound
    total = len(parent1[lower_bound:upper_bound])
    while total < size:
        temp = parent2[par2_index % size]
        if temp not in child1:
            child1[child_index % size] = temp
            child_index += 1
            total += 1
        par2_index += 1
    return child1