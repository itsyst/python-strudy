def sums(seq: list[int]) -> list[int]:
    """
    Tar en lista av heltal och returnerar en lika lång lista där det n:te 
    talet är summan av de n första talen i seq.
    """
    if not seq:
        return []

    cumulative_sums = []
    result = 0
    for element in seq:
        result += element
        cumulative_sums.append(result)

    return cumulative_sums


def sums_rec(seq: list) -> list:
    if len(seq) == 0:
        return []
    if len(seq) == 1:
        return [seq[0]]

    prev = sums_rec(seq[:-1])

    return prev + [prev[-1] + seq[-1]]


if __name__ == "__main__":
    # Givna tester
    assert sums_rec([1, 2, 3, 4, 5]) == [
        1, 3, 6, 10, 15], "Test 1 misslyckades"
    assert sums_rec([]) == [], "Test 2 misslyckades"
    print("✓ Alla givna tester godkända!")

    # Egna tester
    print("\n--- Ytterligare tester ---")

    # Test med negativa tal
    test1 = [-1, 3, 5, 6, -8]
    result1 = sums_rec(test1)
    expected1 = [-1, 2, 7, 13, 5]
    assert result1 == expected1, f"Negativt tal test: förväntat {expected1}, fick {result1}"
    print(f"✓ Negativa tal: {test1} -> {result1}")

    # Test med endast negativa tal
    test2 = [-1, -2, -3]
    result2 = sums_rec(test2)
    expected2 = [-1, -3, -6]
    assert result2 == expected2, f"Endast negativa tal test: förväntat {expected2}, fick {result2}"
    print(f"✓ Endast negativa: {test2} → {result2}")

    # Test med nollor
    test3 = [0, 0, 0]
    result3 = sums_rec(test3)
    expected3 = [0, 0, 0]
    assert result3 == expected3, f"Nollor test: förväntat {expected3}, fick {result3}"
    print(f"✓ Nollor: {test3} → {result3}")

    # Test med ett element
    test4 = [42]
    result4 = sums_rec(test4)
    expected4 = [42]
    assert result4 == expected4, f"Ett element test: förväntat {expected4}, fick {result4}"
    print(f"✓ Ett element: {test4} → {result4}")

    # Test med stora tal
    test5 = [100, 200, 300, 400, 500]
    result5 = sums_rec(test5)
    expected5 = [100, 300, 600, 1000, 1500]
    assert result5 == expected5, f"Stora tal test: förväntat {expected5}, fick {result5}"
    print(f"✓ Stora tal: {test5} → {result5}")

    # Test med blandade positiva och negativa tal
    test6 = [10, -5, 3, -8, 15, -2]
    result6 = sums_rec(test6)
    expected6 = [10, 5, 8, 0, 15, 13]
    assert result6 == expected6, f"Blandat test: förväntat {expected6}, fick {result6}"
    print(f"✓ Blandade tal: {test6} → {result6}")

    # Verifiera att indata inte modifieras
    original = [1, 2, 3, 4, 5]
    original_copy = original.copy()
    _ = sums_rec(original)
    assert original == original_copy, "VARNING: Funktionen modifierade indata!"
    print(f"✓ Indata oförändrad: {original}")

    print("\n✓ Alla tester godkända! Funktionen fungerar korrekt.")
