from partition import *

# Programa aqui el algoritmo de Quick Sort. Utiliza este VPL para programar
# una versión eligiendo privote fijo y otra con pivote aleatorio.

def quick_sort(data):
    def quicksort(items, left, right):
        if left < right:
            index = partition(items, left, right)
            quicksort(items, left, index-1)
            quicksort(items, index+1, right)
        return
    quicksort(data, 0, len(data) -1)
    return