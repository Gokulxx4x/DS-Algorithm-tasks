def remove_duplicates(arr):
    if not arr:
        return 0
    
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1

# Test Input
input_array = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5]
new_length = remove_duplicates(input_array)
print(f"New Length: {new_length}")
print(f"Array after removing duplicates: {input_array[:new_length]}")
