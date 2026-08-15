def add_for_each(seq: list, func):
    """
    Funktionen returnerar summan av resultaten
    """
    cumulative_sum = 0
    for item in seq:
        cumulative_sum += func(item)

    return cumulative_sum

if __name__ == "__main__":
    assert add_for_each([1, 2, 3, 4], lambda x: x**2) == 30 , "Test 1 misslyckades."
    assert add_for_each([], lambda x: x**2) == 0 , "Test 2 misslyckades."
    assert add_for_each([[1, 2, 3], [1], [1, 2, 3, 4]], lambda x: len(x)) == 8 , "Test 3 misslyckades."
    print("✓ Alla givna tester godkända!")