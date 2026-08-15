def sums(seq: list[int]):
    result = []
    cumulative_sum = 0

    if not isinstance(seq, list):
        raise ValueError("Must be a list")
    if len(seq) == 0:
        return []

    for item in seq:
        cumulative_sum += item
        result.append(cumulative_sum)

    return result


def sums_rec(seq: list[int]):
    if len(seq) == 0:
        return []
    if len(seq) == 1:
        return [seq[0]]

    # recursive call on all but the last element
    prev = sums(seq[:-1])      # <-- only recursive call

    # cumulative sum for the last element
    last_value = prev[-1] + seq[-1]

    return prev + [last_value]



def check_python_version():
    # färdig kod som kollar att du kör rätt version av Python
    import sys
    assert sys.version_info >= (3, 8), "Python 3.8 or newer required"

def run_tests():
    # Givna tester
    print("="*25, "given tests", "="*25)
    result1 = sums([1, 2, 3, 4, 5])
    test1 = [1, 3, 6, 10, 15]
    assert result1 == test1, f"Random numbers: expected: {test1}, result: {result1}"
    print(f"Random numbers: {test1} → {result1}")

    test2 = sums([])
    result2 = []
    assert test2 == result2, f"Empty list: expected: {test2}, result: {result2}"
    print(f"Empty list: {test2} -> {result2}")

    test3 = sums_rec([-1, -2, -3])
    result3 = [-1, -3, -6]
    assert test3 == result3, f"Negative numbers: expected: {test3}, result {result3}"
    print(f"Negative numbers: {test3} → {result3}")
    print("All given tests passed!")
    print()

    print("="*25, "property-based checks", "="*25)
    # property-based checks
    seq = [10, -5, 7, -2, 1000, -999]
    result = sums(seq)
    assert len(result) == len(seq), "length invariant violated"
    print(f"Length invariant violation: {"len(result)"} → {"len(seq)"}")
    assert result[-1] == sum(seq), "last element must equal sum(seq)"
    print(f"Last element must equal sum(seq): {"result[-1]"} → {"sum(seq)"}")


    for i in range(1, len(seq)):
        assert result[i] - result[i - 1] == seq[i], \
            "difference between cumulative sums must equal input element"
    print(f"Difference between cumulative sums must equal input element: {"result[i] - result[i - 1]"} → {"seq[i]"}")

    data = [1, 2, 3]
    _ = sums(data)
    assert data == [1, 2, 3], "function must not modify input list"
    print(f"Function must not modify input list: {data} → {_}")

    seq = [3, 1, 4]
    result = sums(seq)
    assert len(result) == len(seq), "output length must match input length"
    print(f"Output length must match input length: {"len(result)"}-> {"len(seq)"}")
    print("Har kört alla tester")
    
if __name__ == "__main__":
    check_python_version()
    run_tests()