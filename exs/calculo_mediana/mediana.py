def solve(items, median_index):
    def partition(data, left, right):
        pivot_value = data[median_index]
        data[median_index], data[right] = data[right], pivot_value
        temp_index = left
        for i in range(left, right):
            if data[i] < pivot_value:
                data[temp_index], data[i] = data[i], data[temp_index]
                temp_index += 1
        data[temp_index], data[right] = data[right], data[temp_index]
        return temp_index
    def quick_select(data, left, right, k):
        while True:
            if left == right:
                return data[left]
            
            pivot_index = partition(data, left, right)
            
            if k == pivot_index:
                return data[k]
            elif k < pivot_index:
                right = pivot_index - 1
            else:
                left = pivot_index + 1
    return quick_select(items, 0, len(items)-1, median_index)

first_line = input().split()
numValues  = int(first_line[0])

items = []
for j in range(1, numValues+1):
    parts      = input().split()
    items.append (int(parts[0]))

median_index = len(items) // 2
median_value = solve(items, median_index)

print(median_value)