def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # In case k is larger than n
    
    # Step 1: Reverse the entire array
    reverse(arr, 0, n - 1)
    
    # Step 2: Reverse the first k elements
    reverse(arr, 0, k - 1)
    
    # Step 3: Reverse the remaining elements
    reverse(arr, k, n - 1)
    
    return arr

# Test Input
input_array = [3, 8, 9, 2, 5]
k = 2
rotated_array = rotate_array(input_array, k)
print(f"Rotated Array: {rotated_array}")
