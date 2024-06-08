def factorial(n):
    # Base case: if n is 0 or 1
    if n == 0 or n == 1:
        return 1
    # Recursive step: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Test Input
n = 10
result = factorial(n)
print(f"Factorial of {n}: {result}")
