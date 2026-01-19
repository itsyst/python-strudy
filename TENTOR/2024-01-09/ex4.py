def split_at(seq, pred):
    result = []
    temp = []
    for item in seq:
        if pred(item):
            result.append(list(temp))
            temp.clear()
        else:
            temp.append(item)
    result.append(temp)
    return result


def add_for_each(seq: list, func):
    total = 0
    [(total := total + func(item)) for item in seq]

    return total


def run_split_at_tests():
    print("=" * 25, "split_at", "="*25)
    result = split_at([1, 2, 3, 4, 2, 5], lambda x: x == 2)
    expected = [[1], [3, 4], [5]]
    assert result == expected, f"Split at value 2: expected: {result}, get: {expected}"
    print(f"Test1: Split at value 2: {[1, 2, 3, 4, 2, 5]}-> {expected}")

    result = split_at([2, 3, 4, 2, 5], lambda x: x == 2)
    expected = [[], [3, 4], [5]]
    assert result == expected, f"Split at value 2 as first element: expected: {result}, get: {expected}"
    print(
        f"Test2: Split at value 2 as first element: {[2, 3, 4, 2, 5]}-> {expected}")

    result = split_at([1, 2, 3, 4, 2], lambda x: x == 2)
    expected = [[1], [3, 4], []]
    assert result == expected, f"Split at value 2 as last element: expected: {result}, get: {expected}"
    print(
        f"Test3: Split at value 2 as last element: {[1, 2, 3, 4, 2]}-> {expected}")

    result = split_at([1, 2, 2, 3, 4, 2, 5], lambda x: x == 2)
    expected = [[1], [], [3, 4], [5]]
    assert result == expected, f"Split at successive 2: expected: {result}, get: {expected}"
    print(
        f"Test4: Split at successive 2: {[1, 2, 2, 3, 4, 2, 5]}-> {expected}")

    result = split_at("abcdeba", lambda x: x == "b")
    expected = [["a"], ["c", "d", "e"], ["a"]]
    assert result == expected, f"Split at a char b: expected: {result}, get: {expected}"
    print(f"Test5: Split at a char b: {"abcdeba"}-> {expected}")

    result = split_at([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    expected = [[1], [3], [5]]
    assert result == expected, f"Return odd numbers only: {result}, get: {expected}"
    print(f"Test6: Return odd numbers only: {[1, 2, 3, 4, 5]}-> {expected}")
    print()


def run_add_for_each_tests():
    print("=" * 25, "add_for_each", "="*25)
    result = add_for_each([1, 2, 3, 4], lambda x: x**2)
    expected = 30
    assert result == expected, f"Return odd numbers only: {result}, get: {expected}"
    print(f"Test7: factor every number by 2: {[1, 2, 3, 4]}-> {expected}")

    result = add_for_each([], lambda x: x**2)
    expected = 0
    assert result == expected, f"Return odd numbers only: {result}, get: {expected}"
    print(f"Test8: factor every number by 2: {[]}-> {expected}")

    result = add_for_each([[1, 2, 3], [1], [1, 2, 3, 4]], lambda x: len(x))
    expected = 8
    assert result == expected, f"Return odd numbers only: {result}, get: {expected}"
    print(
        f"Test9: factor every number by 2: {[[1, 2, 3], [1], [1, 2, 3, 4]]}-> {expected}")
    print()


if __name__ == "__main__":
    # run_split_at_tests()
    run_add_for_each_tests()
