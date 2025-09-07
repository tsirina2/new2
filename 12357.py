from nt import remove

original_array = [300,32, 9, 11, 12, 14, 7, 12, 218]
result = []
def find(max_value):
    max_value = original_array[element]
    for element in original_array:
        if element > max_value:
            max_value = element
            result[element-1] = max_value
            remove(element)
    while len(original_array) > 0:
        append(result[element])

    return find(max_value)
    print(result)
