# def fibonacci(n):
#     if n < 3:
#         return n - 1
#     a = 0
#     b = 0

#     for i in range(n - 2):
#         c = b
#         b = a + b
#         a = c
#     return b

# print(fibonacci(10))

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

print(fibonacci(10))  # Output: 34
print(fibonacci(1))   # Output: 0