def add1(x, y):
    return x + y

def add2(x, y):
    print(x + y)

add1(5, 5)  # returns 10
add2(3, 8)  # prints 10 but returns None

a = add1(15, 3)
b = add2(9, 9)

print(a, b)
