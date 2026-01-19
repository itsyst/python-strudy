import math


def is_prime(n: int) -> bool:
    """
    Determine whether a given integer is a prime number.

    A number is considered prime if it is greater than or equal to 2 and has
    no positive divisors other than 1 and itself. This function checks for any
    divisor in the range [2, sqrt(n)] and returns False immediately if one is found.

    Parameters
    ----------
    n : int
        The integer to test.

    Returns
    -------
    bool
        True if `n` is prime, False otherwise.

    Notes
    -----
    - Returns False for all integers < 2.
    - Uses trial division up to √n for efficiency.
    """
        
    if n < 2:
        return False

    return not any([n % i == 0 for i in range(2, int(math.sqrt(n)) + 1)])


def prime_factors(n: int) -> list:
    """
    Compute the prime factorization of an integer.

    Returns a list of prime factors of `n`, including multiplicity.
    For example, 20 → [2, 2, 5]. Factors are returned in non-decreasing order.

    Parameters
    ----------
    n : int
        The integer to factorize. Expected to be >= 2.

    Returns
    -------
    list[int]
        A list containing the prime factors of `n`.

    Notes
    -----
    - Uses repeated division starting from the smallest divisor (2 upward).
    - Behavior for n < 2 is not mathematically defined; currently returns [].
    """   
    factors = []
    divisor = 2
    number = n

    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return factors


def is_attractive(n: int) -> bool:
    """
    Determine whether a number is an attractive number.

    A number is considered attractive if the count of its prime factors
    (with multiplicity) is itself a prime number.

    Examples
    --------
    20 → prime factors = [2, 2, 5] → count = 3 → 3 is prime → True
    12 → prime factors = [2, 2, 3] → count = 3 → True
    10 → [2, 5] → count = 2 → True
    8  → [2, 2, 2] → count = 3 → True
    9  → [3, 3] → count = 2 → True

    Parameters
    ----------
    n : int
        The integer to test.

    Returns
    -------
    bool
        True if `n` is attractive, False otherwise.

    Notes
    -----
    - Relies on `prime_factors` to determine factor multiplicity.
    - Returns False for n < 2 (since factor count will not be prime).
    """
    return is_prime(len(prime_factors(n)))


def test_is_prime() -> None:
    is_prime_cases = [
        (1, False),
        (2, True),
        (10, False),
        (11, True),
        (10_000_000_019, True),
        (-1, False),
        (int(1e10 + 18), False),
    ]

    print("=" * 25, "is_prime", "="*25)
    for i, testcase in enumerate(is_prime_cases):
        result = is_prime(testcase[0])
        assert result == testcase[1], f"is_prime({testcase[0]}) expected {testcase[1]}, got {result}"
        print(f"Test{i + 1}: is_prime({testcase[0]}) -> {result}")
    print()


def test_prime_factors() -> None:

    prime_factors_cases = [
        (2, [2]),
        (10, [2, 5]),
        (20, [2, 2, 5]),
        (55, [5, 11]),
        (-1, []),
    ]

    print("=" * 25, "prime_factors", "="*25)
    for i, testcase in enumerate(prime_factors_cases):
        result = prime_factors(testcase[0])
        assert result == testcase[1], f"prime_factors({testcase[0]}) expected {testcase[1]}, got {result}"
        print(f"Test{i + 1}: prime_factors({testcase[0]}) -> {result}")
    print()


def test_is_attractive() -> None:
    test_is_attractive_cases = [
        (16, False),
        (20, True),
        (21, True),
        (22, True),
        (23, False),
        (24, False),
        (55, True),
    ]

    print("=" * 25, "is_attractive", "="*25)
    for i, testcase in enumerate(test_is_attractive_cases):
        result = is_attractive(testcase[0])
        assert result == testcase[1], f"is_attractive({testcase[0]}) expected {testcase[1]}, got {result}"
        print(f"Test{i + 1}: is_attractive({testcase[0]}) -> {result}")
    print()


if __name__ == "__main__":
    test_is_prime()
    test_prime_factors()
    test_is_attractive()
