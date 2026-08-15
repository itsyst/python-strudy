"""
Lecture: Functions (*args, **kwargs)
"""

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def save_user(**user):
    print("Username:", user.get("username"))
    print("Keys:", user.keys())
    print("Items:", list(user.items()))
    if "id" in user:
        print("Pop id:", user.pop("id"))
    user["username"] = "Doe"
    user["age"] = 23
    print("Updated:", user)


if __name__ == "__main__":
    print("total:", multiply(2, 3, 4))
    print()
    save_user(id=1, username="joe", age=33)

    # Even numbers example
    j = 0
    for number in range(1, 10):
        if number % 2 == 0:
            print(number)
            j += 1
    print(f"We have {j} even numbers")
