def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = 6
print("Factorial of", num, "is", factorial(num))

# factorial(5)
# → 5 * factorial(4)
# → 5 * 4 * factorial(3)
# → ...
# → 5 * 4 * 3 * 2 * 1 = 120