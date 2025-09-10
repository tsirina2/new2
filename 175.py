original_array = [300, 32, 9, 11, 12, 14, 7, 12, 218]
result = []
while len(original_array) > 0:
    result.append([])
    original_array.remove(original_array[0])
    def find(original_array):
        max_val = original_array[0]
        for item in original_array:
            if item > max_val:
                max_val = item
                
        return max_val
    print(find(result))
