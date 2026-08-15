def create_fraction(numerator, denominator):
    """Creates a fraction n/d, automatically reduced."""
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    g = gcd(abs(numerator), abs(denominator))
    numerator //= g
    denominator //= g
    if denominator < 0:
        numerator = -numerator
        denominator = -denominator
    return (numerator, denominator)

def numerator(frac):
    return frac[0]

def denominator(frac):
    return frac[1]

def print_fraction(frac):
    print(f"{numerator(frac)}/{denominator(frac)}")

def gcd(a, b):
    """Greatest common divisor"""
    while b != 0:
        a, b = b, a % b
    return a

def fraction_add(a, b):
    n = numerator(a)*denominator(b) + numerator(b)*denominator(a)
    d = denominator(a)*denominator(b)
    return create_fraction(n, d)

def fraction_minus(a, b):
    n = numerator(a)*denominator(b) - numerator(b)*denominator(a)
    d = denominator(a)*denominator(b)
    return create_fraction(n, d)

def fraction_multiply(a, b):
    n = numerator(a)*numerator(b)
    d = denominator(a)*denominator(b)
    return create_fraction(n, d)

def fraction_divide(a, b):
    if numerator(b) == 0:
        raise ZeroDivisionError("Division by zero fraction.")
    n = numerator(a)*denominator(b)
    d = denominator(a)*numerator(b)
    return create_fraction(n, d)

a = create_fraction(8, 10)
b = create_fraction(1, 5)
print_fraction(fraction_minus(a, b))
print_fraction(fraction_multiply(a, b))
print_fraction(fraction_divide(b, a))
