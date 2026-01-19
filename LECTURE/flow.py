age = 10

message = "Eligible" if age >= 18 else "Not Eligible"


high_income = True
good_credit = True
student = True


if not student:
    print("Eligible")
else:
    print("Not Eligible")


if "Apple" > "apple":
    print("True")

[print("Attempt", number, number * ".") for number in range(1, 10, 2)]


for x in range(5):
    print(x)

print(type(range(5)))

 
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break