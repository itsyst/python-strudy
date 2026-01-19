import unittest

def sums(seq: list):
    if seq == []:
        return []

    result =  []
    accum = 0
    for item in seq:
        accum += item 
        result.append(accum)
    
    return result

def sums_rec(seq: list):
    if not seq:
        return []

    if len(seq) == 1:
        return [seq[0]]

    prev = sums(seq[1:])
    shifted = [seq[0] + x for x in prev]
    print(shifted )
    print([seq[0]] + shifted)
    return [seq[0]] + shifted

# sums([1,2,3,4,5,6])   prev = [2,3,4,5,6]
# sums([2,3,4,5,6])   prev = [3,4,5,6]
# sums([3,4,5,6])   prev = [4,5,6]
# sums([4,5,6])   prev = [5,6]
# sums([5,6])   prev = [6]
# [5]  shifted [5+6] => [5,11]
# prev = [5, 11]  shifted [4+5, 4+11] = [9, 15] => [4, 9,15]
# prev [4, 9,15]  shifted  [3+4,3+9,3+15] = [7,12,18] => [3,7, 12,18]
# prev [3,7, 12,18]  shifted [2+3, 2+7, 2+12,2+18] =[5,9, 14,20] => [2,5,9, 14,20]
# prev [2,5,9,14,20] shifted  [1+2,1+5,1+9, 1+14,1+20] = [3,6,10, 15,21] => [1,3,6,10, 15,21]


def check_python_version():
    # färdig kod som kollar att du kör rätt version av Python
    import sys
    assert sys.version_info >= (3, 8), "Python 3.8 or newer required"


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester ...")

    assert sums([]) == [], "empty list should return empty list"
    assert sums([1, 2, 3, 4, 5, 6]) == [1, 3, 6, 10, 15, 21], \
        "basic cumulative sum failed"
    assert sums([-1, -2, -4]) == [-1, -3, -7], \
        "negative numbers should accumulate correctly"

    # Här lägger du dina egna tester.
    print("Kör egna tester ...")

    assert sums([5]) == [5], "single element list should return same value"
    assert sums([0, 1, 2]) == [0, 1, 3], "zero handling is incorrect"

    data = [1, 2, 3]
    _ = sums(data)
    assert data == [1, 2, 3], "function must not modify input list"

    seq = [3, 1, 4]
    result = sums(seq)
    assert len(result) == len(seq), \
        "output length must match input length"

    # Här kan du lägga tester där du inte vet korrekta svar
    print("Kör utskriftstester ...")

    seq = [10, -5, 7, -2, 1000, -999]
    result = sums(seq)

    # property-based checks
    assert len(result) == len(seq), "length invariant violated"
    assert result[-1] == sum(seq), "last element must equal sum(seq)"

    for i in range(1, len(seq)):
        assert result[i] - result[i - 1] == seq[i], \
            "difference between cumulative sums must equal input element"

    print("Resultat:", result)
    print("Resultat 1:", sums([10, -5, 7, -2]))

    print("Har kört alla tester")


if __name__ == "__main__":
    check_python_version()
    run_tests()