def find_missing_number(arr):
    n = len(arr) + 1  # Since one number is missing
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    missing_number = total_sum - array_sum
    return missing_number

# Test Input
input_array = [1, 3, 4, 5, 6, 7, 8, 9, 10]
missing_number = find_missing_number(input_array)
print(f"Missing Number: {missing_number}")
