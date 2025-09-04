original_array = [300,32, 9, 11, 12, 14, 7, 12, 218]
result = []
def find(original_array):
    max_value = original_array[0]
    for element in original_array:
        if element > max_value:
            max_value = element
        return max_value
    while len(original_array) > 0:
        max_value = find(original_array)
        result.append(max_value)
        original_array.remove(max_value)
    print(result.append(max_value))
