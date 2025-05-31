def fibonacci(n):

    a, b = 0, 1
    next = b
    count = 1
    while count <= n:
        print(next, end=" ")
        count += 1
        a, b = b, next
        next = a + b
    print()


if __name__ == '__main__':
    fibonacci(10)