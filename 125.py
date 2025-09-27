def find(array):
    max_val = array[0]
    for item in array:
        if item > max_val:
            max_val = item
    return max_val

original_array = [300, 32, 9, 11, 12, 14, 7, 12, 218]
result = []
while len(original_array) > 0:
    result.sort(reverse=True)
    result.append(original_array.pop())

print(result)
