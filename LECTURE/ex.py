j = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        j += 1
print(f"We have {j} even numbers")


for i, number in enumerate(range(1, 10)):
    if number % 2 != 0:
        print(f"{i}: {number}")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number

    return total


print("total:", multiply(2, 3, 4))


def save_user(**user):
    print(user.get('username'))
    print(user.keys())
    print(user.items())
    print(user.pop('id'))
    print(user.popitem())
    del user['username']
    print()

    user['username'] = "Doe"
    user['age'] = 23
    print(user)


save_user(id=1, username="joe", age=33)
