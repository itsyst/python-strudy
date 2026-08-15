import numbers

def power(x, n):
    """Beräknar x upphöjt till n rekursivt."""
    if n == 0:
        return 1
    return x * power(x, n - 1)


def is_number(x):
    return isinstance(x, numbers.Number)

def sum_numbers(lst):
    """Summerar alla tal i en lista (rekursivt, ignorerar icke-tal)."""
    if not lst:
        return 0
    head, *tail = lst
    if isinstance(head, list):
        return sum_numbers(head) + sum_numbers(tail)
    elif is_number(head):
        return head + sum_numbers(tail)
    else:
        return sum_numbers(tail)

def find_letter(letter, letters):
    """Returnerar True om letter finns i listan letters."""
    if not letters:
        return False
    head, *tail = letters
    if head == letter:
        return True
    return find_letter(letter, tail)

def remove_vowels(letters):
    """Returnerar en ny lista med alla vokaler borttagna."""
    if not letters:
        return []
    vowels = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
    head, *tail = letters
    rest = remove_vowels(tail)
    if head.lower() in vowels:
        return rest
    else:
        return [head] + rest

def range_product(nmin, nmax):
    """Returnerar produkten av alla heltal mellan nmin och nmax (inklusive)."""
    if nmin > nmax:
        return 1
    if nmin == nmax:
        return nmin
    return nmax * range_product(nmin, nmax - 1)

def factorial(n):
    """Returnerar n! (fakultet) rekursivt."""
    if n == 0:
        return 1
    return n * factorial(n - 1)
