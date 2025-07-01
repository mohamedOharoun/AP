def solve(items):
    """
    Sort the given list of items in ascending order
    """

    def merge(left, mid, right):
        A = items[left:mid]
        B = items[mid:right]
        i = j = 0
        k = left
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                items[k] = A[i]
                i += 1
            else:
                items[k] = B[j]
                j += 1
            k += 1
        
        while i < len(A):
            items[k] = A[i]
            i += 1
            k += 1
        
        while j < len(B):
            items[k] = B[j]
            j += 1
            k += 1
    
    def merge_sort(left, right):
        if left < right - 1:
            mid = (right + left) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)
            merge(left, mid, right)
    
    merge_sort (0, len(items))
    return

first_line = input().split()
numValues  = int(first_line[0])

items = []
for j in range(1, numValues+1):
    parts      = input().split()
    items.append (int(parts[0]))

solve(items)
print(items)