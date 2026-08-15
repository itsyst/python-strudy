"""
Lecture: Control Flow (if / loops / while)
"""

age = 10
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

student = True
if not student:
    print("Eligible")
else:
    print("Not Eligible")

print("\nOdd numbers with dots:")
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

print("\nSimple for:")
for x in range(5):
    print(x)

# Uncomment to try interactive while loop:
# while True:
#     command = input("> ")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break
