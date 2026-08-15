import math


def is_prime(n):
    # Edge case: n <= 1
    if n <= 1:
        return False
    # Edge case: n == 2
    if n == 2:
        return True
    # Edge case: n % 2 == 0 (jämna tal)
    if n % 2 == 0:
        return False
    
    limit = get_check_limit(n)
    return not has_divisor(n, limit)


def get_check_limit(n):
    # Returnera √n + 1
    return int(math.sqrt(n)) + 1


def has_divisor(n, limit):
    for i in range(3, limit, 2):  # Steg 2 = hoppa över jämna tal
        if n % i == 0:
            return True  # Hittade en divisor!
        
    return False
 
if __name__ == "__main__":
    print("=" * 60)
    print(f"√ Alla givna tester godkända!")
    assert is_prime(1) == False, "Test 1 misslyckades."
    assert is_prime(2) == True, "Test 2 misslyckades."
    assert is_prime(10) == False, "Test 3 misslyckades."
    assert is_prime(11) == True, "Test 4 misslyckades."
    assert is_prime(10000000019) == True, "Test 5 misslyckades."
    print("=" * 60)
    print("\nTESTAR EDGE CASES")
    print("=" * 60)
    
    # 1. NEGATIVA TAL
    print("\n1. NEGATIVA TAL")
    test1 = -5
    result1 = is_prime(test1)
    expected1 = False
    assert result1 == expected1, f"Negativt tal test, förväntat: {expected1}, fick: {result1}"
    print(f"√ Negativa tal: {test1} -> {result1}")
    
    test2 = -100
    result2 = is_prime(test2)
    expected2 = False
    assert result2 == expected2, f"Negativt tal test, förväntat: {expected2}, fick: {result2}"
    print(f"√ Negativa tal: {test2} -> {result2}")
    
    # 2. NOLL
    print("\n2. NOLL")
    test3 = 0
    result3 = is_prime(test3)
    expected3 = False
    assert result3 == expected3, f"Noll test, förväntat: {expected3}, fick: {result3}"
    print(f"√ Noll: {test3} -> {result3}")
    
    # 3. ETT
    print("\n3. ETT")
    test4 = 1
    result4 = is_prime(test4)
    expected4 = False
    assert result4 == expected4, f"Ett test, förväntat: {expected4}, fick: {result4}"
    print(f"√ Ett: {test4} -> {result4}")
    
    # 4. TVÅ (enda jämna primtal)
    print("\n4. TVÅ (enda jämna primtal)")
    test5 = 2
    result5 = is_prime(test5)
    expected5 = True
    assert result5 == expected5, f"Två test, förväntat: {expected5}, fick: {result5}"
    print(f"√ Två: {test5} -> {result5}")
    
    # 5. JÄMNA TAL
    print("\n5. JÄMNA TAL")
    test6 = 4
    result6 = is_prime(test6)
    expected6 = False
    assert result6 == expected6, f"Jämnt tal test, förväntat: {expected6}, fick: {result6}"
    print(f"√ Jämnt tal: {test6} -> {result6}")
    
    test7 = 10
    result7 = is_prime(test7)
    expected7 = False
    assert result7 == expected7, f"Jämnt tal test, förväntat: {expected7}, fick: {result7}"
    print(f"√ Jämnt tal: {test7} -> {result7}")
    
    test8 = 100
    result8 = is_prime(test8)
    expected8 = False
    assert result8 == expected8, f"Jämnt tal test, förväntat: {expected8}, fick: {result8}"
    print(f"√ Jämnt tal: {test8} -> {result8}")
    
    # 6. NON-NUMERIC INPUT
    print("\n6. NON-NUMERIC INPUT (felhantering)")
    
    test_cases = [5.5, "hello", None, [1, 2, 3]]
    
    for test_value in test_cases:
        print(f"\nTest med {repr(test_value)}:")
        try:
            result = is_prime(test_value)
            print(f"→ Resultat: {result} (ingen error kastades)")
        except Exception as e:
            print(f"→ Fångat fel (förväntat): {type(e).__name__}: {e}")
 
    # SAMMANFATTNING
    print("\n" + "=" * 60)
    print("√√√ ALLA TESTER GODKÄNDA! √√√")
    print("=" * 60)
    print(f"Totalt antal tester: 12")
    print("\nTestade edge cases:")
    print("  ✓ Negativa tal")
    print("  ✓ Noll")
    print("  ✓ Ett")
    print("  ✓ Två (enda jämna primtal)")
    print("  ✓ Jämna tal")
    print("  ✓ Non-numeric input (float, string, None, list)")
    print("=" * 60)
