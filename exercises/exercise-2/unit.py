import numbers

# ----------------------------------------------------
# Övning 201: unit() and ten()
# ----------------------------------------------------
def unit(n):
    """Return the ones digit (ental) of n."""
    return n % 10

def ten(n):
    """Return the tens digit (tiotal) of n."""
    return (n // 10) % 10

def hundred(n):
    """Return the hundreds digit (hundratal) of n."""
    return (n // 100) % 10

def thousand(n):
    """Return the thousands digit (tusental) of n."""
    return (n // 1000) % 10


# ----------------------------------------------------
# Övning 202: swap_unit_ten()
# ----------------------------------------------------

def swap_unit_ten(n):
    """Swap the ones and tens digits of an integer n."""
    u = unit(n)
    t = ten(n)
    rest = n // 100
    return rest * 100 + u * 10 + t

# ----------------------------------------------------
# Övning 203: power()
# ----------------------------------------------------

def power(x, y):
    """Return x raised to the power of y (iteratively)."""
    result = 1
    for _ in range(y):
        result *= x
    return result

# ----------------------------------------------------
# Övning 204: sum_first()
# ----------------------------------------------------

def sum_first(n):
    """Return the sum of the first n integers."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# ----------------------------------------------------
# Övning 205: sum_numbers()
# ----------------------------------------------------

def is_number(x):
    """Return True if x is a number."""
    return isinstance(x, numbers.Number)

def sum_numbers(lst):
    """Sum only numeric elements in the list lst."""
    total = 0
    for item in lst:
        if is_number(item):
            total += item
    return total

# ----------------------------------------------------
# Övning 206: find_letter()
# ----------------------------------------------------

def find_letter(letter, word_list):
    """Return True if letter is in word_list."""
    for ch in word_list:
        if ch == letter:
            return True
    return False

# ----------------------------------------------------
# Övning 207: remove_vowels()
# ----------------------------------------------------

def remove_vowels(letters):
    """Return a new list with vowels removed."""
    vowels = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
    result = []
    for ch in letters:
        if not find_letter(ch, vowels):
            result.append(ch)
    return result

# ----------------------------------------------------
# Example tests
# ----------------------------------------------------

if __name__ == "__main__":
    print("unit(1234) =", unit(1234))
    print("ten(1234) =", ten(1234))
    print("hundred(1234) =", hundred(1234))
    print("thousand(1234) =", thousand(1234))
    print("swap_unit_ten(123) =", swap_unit_ten(123))
    print("power(2,3) =", power(2, 3))
    print("sum_first(6) =", sum_first(6))
    print("sum_numbers(['a',1,'b',2,3]) =", sum_numbers(['a',1,'b',2,3]))
    print("find_letter('u', ['h','u','s']) =", find_letter('u', ['h','u','s']))
    print("remove_vowels(['b','i','r','g','i','t','t','a']) =",
          remove_vowels(['b','i','r','g','i','t','t','a']))
