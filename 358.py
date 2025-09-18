def find(array):
   max_val = array[0]
   for item in array:
      if item>max_val:
         max_val = item
   return max_val


original_array = [300,32,9,11,12,14,7,12]
result =[]
max_elmenent = find(original_array)
original_array.remove(max_elmenent)
result.append(max_elmenent)
print(result)

