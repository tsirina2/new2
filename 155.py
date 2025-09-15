
def find(array):
    max_val = array[0]
    for item in array:
        if item > max_val:
            max_val = item
    original_array = [300, 32, 9, 11, 12, 14, 7, 12, 218]
    result = []
    while len(original_array) > 0:
        max_element = find(original_array)
        result.append(max_element)
        original_array.remove(max_element)

print(result)








