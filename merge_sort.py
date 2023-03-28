def merge_sort(numbs):
    if len(numbs) > 1:
        mid = len(numbs) // 2
        left = numbs[:mid]
        right = numbs[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbs[k] = left[i]
                i += 1
            else:
                numbs[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            numbs[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            numbs[k] = right[j]
            j += 1
            k += 1
list_1 = [1,23,4523,67,12,63,7,33,8,23,9,45]
merge_sort(list_1)
print(list_1)