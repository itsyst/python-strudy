"""
Lecture: Factorial
Exact computation + Stirling approximation
"""

import math


def factorial(n: int) -> int:
    """Exact factorial using math.prod."""
    if n < 0:
        raise ValueError("n must be >= 0")
    return math.prod(range(1, n + 1)) if n > 0 else 1


def stirling_approx(n: int) -> float:
    """Stirling approximation of n!."""
    if n <= 1:
        return 1.0
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n


def stirling_log10(n: int) -> float:
    """Approximate log10(n!) to avoid overflow."""
    if n <= 1:
        return 0.0
    return n * math.log10(n / math.e) + 0.5 * math.log10(2 * math.pi * n)


def demo():
    print("=" * 50)
    print("FACTORIAL DEMO")
    print("=" * 50)

    cases = [0, 1, 5, 10, 20]
    for n in cases:
        exact = factorial(n)
        approx = stirling_approx(n)
        err = abs(approx - exact) / exact if exact else 0
        print(f"n={n:2d}  exact={exact:<22}  approx={approx:.5e}  rel_err={err:.4%}")

    print("\nLarge n (digits only):")
    n = 1_000_000
    digits = int(stirling_log10(n)) + 1
    print(f"{n}! has approximately {digits} digits")


if __name__ == "__main__":
    demo()
