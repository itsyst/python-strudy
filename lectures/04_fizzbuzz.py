"""
Lecture: FizzBuzz
"""

def fizz_buzz(n: int):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n


if __name__ == "__main__":
    for i in range(1, 16):
        print(i, "→", fizz_buzz(i))
