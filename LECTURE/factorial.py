import math
 

def factorial(n: int) -> int:
    """
    Compute factorial using a generator expression.
    Returns n! as an integer.
    """
    # Generator produces numbers 1 through n lazily
    gen_numbers = (i for i in range(1, n + 1))

    # Consume generator to compute factorial
    return math.prod(gen_numbers)


def stirling_factorial_approx(n):
    """
    Approximate n! using Stirling's formula.
    Returns an approximate value as a float.
    """
    if n == 0 or n == 1:
        return 1
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n


def stirling_factorial_approx_log(n):
    """
    Approximate factorial in log10 scale to avoid overflow.
    Returns log10(n!) instead of n! itself.
    """
    if n == 0 or n == 1:
        return 0  # log10(1) = 0
    return n * math.log10(n / math.e) + 0.5 * math.log10(2 * math.pi * n)


def test_factorial_functions():
    print("="*25, "Testing factorial functions", "="*25)

    # -------------------------
    # Test factorial (exact)
    # -------------------------
    test_cases = [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800),
        (20, 2432902008176640000)
    ]

    print("Testing factorial (exact)...")
    for n, expected in test_cases:
        result = factorial(n)
        assert result == expected, f"factorial({n}) expected {expected}, got {result}"
        print(f"factorial({n}) = {result} ✅")

    # -------------------------
    # Test Stirling approximation
    # -------------------------
    print("\nTesting stirling_factorial_approx (approximate)...")
    for n, _ in test_cases:
        approx = stirling_factorial_approx(n)
        exact = factorial(n)
        relative_error = abs(approx - exact) / exact
        print(
            f"stirling_factorial_approx({n}) ≈ {approx:.5e}, exact = {exact}, relative error = {relative_error:.5%}")
        # 5% tolerance
        assert relative_error < 0.05, f"Approximation too far for n={n}"

    # -------------------------
    # Test stirling_factorial_approx_log
    # -------------------------
    print("\nTesting stirling_factorial_approx_log (approximate number of digits)...")
    for n, _ in test_cases:
        digits_approx = stirling_factorial_approx_log(n)
        digits_exact = len(str(factorial(n)))
        print(
            f"stirling_factorial_approx_log({n}) = {digits_approx}, actual digits = {digits_exact}")
        assert abs(
            digits_approx - digits_exact) <= 1, f"Digit estimate off by more than 1 for n={n}"

    # -------------------------
    # Creative large n test
    # -------------------------
    n_large = 10_000_000
    log10_fact = stirling_factorial_approx_log(n_large)  # log10(n!)
    approx_digits = int(log10_fact) + 1

    # Optional: estimate mantissa for scientific notation
    exponent = int(log10_fact)
    mantissa = 10 ** (log10_fact - exponent)
    print(f"{n_large}! ≈ {mantissa:.3f}e{exponent} (~{approx_digits} digits)")

    print("\nAll tests passed!")


if __name__ == "__main__":
    test_factorial_functions()
