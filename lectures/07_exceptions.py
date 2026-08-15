"""
Lecture: Exceptions (try / except)
"""

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(f"\033[91m{ex}\033[0m")
else:
    print("No exception was thrown. Result:", xfactor)

print("\nColor demo:")
print("\033[91mRed text\033[0m")
print("\033[92mGreen text\033[0m")
print("\033[93mYellow text\033[0m")
print("\033[94mBlue text\033[0m")
