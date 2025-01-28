def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
                k += 1
            while i < len(left):
                array[k] = left[i]
                i +=1
                k +=1
                while j < len(right):
                    array[k] = right[j]
                    j +=1
                    k +=1

array= [12,11,13,5,6,8]
merge_sort(array)
print("Sorted array: ",array)





























