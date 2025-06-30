# Aunque podríamos utilizar las listas de Python, este ejercicio lo resolvemos
# utilizando numpy para recordar el uso de numpy.

import numpy as np;
from solve import *
import random

first_line = input().split()
numValues  = int(first_line[0])
items      = np.zeros((numValues), dtype = int)

for j in range(1, numValues+1):
    parts      = input().split()
    items[j-1] = int(parts[0])

random.seed(0)

quick_sort(items)
print(items)