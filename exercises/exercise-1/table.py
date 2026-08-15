#🧩 Övning 102 – Multiplication table
def table():
    print("This program prints out a multiplication table.")
    n = int(input("Enter a number: "))
    for i in range(10):
        print(f"{i} * {n} = {i * n}")


table()

print("="*50)

def get_numbers():
    x, y = map(int, input("Enter two numbers separated by space: ").split())
    return x, y

def plus(x, y):
    return x + y

# Get numbers from user
x, y = get_numbers()

# Call plus() with those numbers
print(plus(x, y))
