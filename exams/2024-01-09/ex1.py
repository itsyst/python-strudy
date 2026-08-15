"""
Tentamen 2024-01-09 – Uppgift 1
Cumulative sums (iterative + recursive)
"""

import sys


def sums(seq: list) -> list:
    """Return cumulative sums of the sequence."""
    if not seq:
        return []
    result = []
    accum = 0
    for item in seq:
        accum += item
        result.append(accum)
    return result


def sums_rec(seq: list) -> list:
    """Recursive version of cumulative sums."""
    if not seq:
        return []
    if len(seq) == 1:
        return [seq[0]]
    prev = sums_rec(seq[1:])
    shifted = [seq[0] + x for x in prev]
    return [seq[0]] + shifted


def check_python_version():
    assert sys.version_info >= (3, 8), "Python 3.8 or newer required"


def run_tests():
    print("Running tests ...")

    assert sums([]) == []
    assert sums([1, 2, 3, 4, 5, 6]) == [1, 3, 6, 10, 15, 21]
    assert sums([-1, -2, -4]) == [-1, -3, -7]
    assert sums([5]) == [5]
    assert sums([0, 1, 2]) == [0, 1, 3]

    data = [1, 2, 3]
    _ = sums(data)
    assert data == [1, 2, 3], "function must not modify input"

    seq = [10, -5, 7, -2, 1000, -999]
    result = sums(seq)
    assert len(result) == len(seq)
    assert result[-1] == sum(seq)
    for i in range(1, len(seq)):
        assert result[i] - result[i - 1] == seq[i]

    print("All tests passed ✅")
    print("Example:", sums([10, -5, 7, -2]))


if __name__ == "__main__":
    check_python_version()
    run_tests()
