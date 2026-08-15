def without(nest: list, to_remove:list):
    """
    Funktionen tar en nästlad lista och returnerar motsvarande 
    lista utan de element som finns i to_remove. 
    """
    cleaned_list = []
    for item in nest:
        if isinstance(item, list):
            cleaned_list.append(without(item, to_remove))
        elif item not in to_remove:
            cleaned_list.append(item)

    return cleaned_list

if __name__ == "__main__":
    assert without([[1], [[2]], [[[3]]], [[[[4]]]]], [1,3]) == [[], [[2]], [[[]]], [[[[4]]]]], "Test 1 misslyckades"
    assert without([[[[[[[[[[10]]]]]]]]]], [10]) == [[[[[[[[[[]]]]]]]]]], "Test 2 misslyckades"
    assert without([[[[[[[[[[10]]]]]]]]]], [5]) == [[[[[[[[[[10]]]]]]]]]], "Test 3 misslyckades"
    assert without([[(1,2)], [["b"]], [[[None]]], [[[[42.5]]]]], [1,None]) == [[(1,2)], [["b"]], [[[]]], [[[[42.5]]]]], "Test 4 misslyckades"
    print("✓ Alla givna tester godkända!")
    
    # Test med negativa tal
    test1 = [[1], [[-2]], [[[-3]]], [[[[4]]]]]
    to_remove1 = [1,3]
    result1 = without(test1, [1,-3])
    expected1 = [[], [[-2]], [[[]]], [[[[4]]]]]
    assert result1 == expected1, f"Negativt tal test: förväntat {expected1}, fick {result1}"
    print(f"✓ Negativa tal: {test1} -> {result1}")

    # Test med tomma listor
    test2 = [[], [[]], [[[]]], [[[[]]]]]
    to_remove2 = [1,3]
    result2 = without(test2, [1,3])
    expected2 = [[], [[]], [[[]]], [[[[]]]]]
    assert result2 == expected2, f"Tomma listor test: förväntat {expected2}, fick {result2}"
    print(f"✓ Tomma listor: {test2} -> {result2}")
 