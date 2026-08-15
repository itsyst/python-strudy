"""
Tentamen 2024-01-09 – Uppgift 2
Merge two sorted lists
"""

import sys


def merge(s1: list, s2: list) -> list:
    """Merge two sorted lists into one sorted list (iterative)."""
    merged = []
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] <= s2[j]:
            merged.append(s1[i])
            i += 1
        else:
            merged.append(s2[j])
            j += 1
    merged.extend(s1[i:])
    merged.extend(s2[j:])
    return merged


def merge_recursive(s1: list, s2: list) -> list:
    """Recursive merge."""
    if not s1:
        return s2
    if not s2:
        return s1
    if s1[0] <= s2[0]:
        return [s1[0]] + merge_recursive(s1[1:], s2)
    return [s2[0]] + merge_recursive(s1, s2[1:])


def check_python_version():
    assert sys.version_info >= (3, 8), "Python 3.8+ required"
    print(f"Python {sys.version_info.major}.{sys.version_info.minor}")


def run_tests():
    test_cases = [
        ([], [], []),
        ([], [1], [1]),
        ([1], [], [1]),
        ([1, 2, 5, 13], [3, 5, 21], [1, 2, 3, 5, 5, 13, 21]),
        ([-5, -2], [-3, -1], [-5, -3, -2, -1]),
        (["a", "c"], ["b", "o"], ["a", "b", "c", "o"]),
    ]

    for i, (a, b, expected) in enumerate(test_cases, 1):
        r1 = merge(a[:], b[:])
        r2 = merge_recursive(a[:], b[:])
        assert r1 == expected, f"Test {i} iterative failed"
        assert r2 == expected, f"Test {i} recursive failed"
        print(f"Test {i}: OK → {expected}")

    print("All tests passed ✅")


if __name__ == "__main__":
    check_python_version()
    run_tests()
