array = [2, 9, 11, 12, 14, 7, 12, 218]
def find():
    max = array[0]
    for element in array:
        if element > max:
            max = element
    return max
find()
print(find())



