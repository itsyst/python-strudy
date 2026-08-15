def merge(s1: list, s2: list) -> list:
    """
    Funktionen tar två sorterade listor s1 och s2 av godtycklig längd, och
    returnerar en sorterad lista.
    """
    if s1 == []:
        return s2
    elif s2 == []:
        return s1

    sorted_list = []
    i = 0 
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] <= s2[j]:
            sorted_list.append(s1[i])
            i += 1
        else:
            sorted_list.append(s2[j])
            j += 1

    sorted_list.extend(s1[i:])
    sorted_list.extend(s2[j:])
 
    return sorted_list

if __name__ == "__main__":
    test1 = merge([], [1])
    result1 = [1]
    assert test1 == result1, f"Empty list: expected: {test1}, result: {result1}"
    print(f"Empty list: {test1} -> {result1}")
    
    test2 = merge([1], [])
    result2 = [1]
    assert test2 == result2, f"Empty list: expected: {test2}, result: {result2}"
    print(f"Empty list: {test2} -> {result2}")
 
    test3 = merge([1, 2, 5, 13], [3, 5, 21])
    result3 = [1, 2, 3, 5, 5, 13, 21]
    assert test3 == result3, f"Random numbers: expected: {test2}, result: {result2}."
    print(f"Random numbers: {test3} -> {result3}")

    test4 = merge(['a', 'c'], ['b', 'o'])
    result4 = ['a', 'b', 'c', 'o']
    assert test4 == result4, f"Lists of character: expected: {test4}, result: {result4}."
    print(f"Lists of character: {test4} -> {result4}")

    test5 = merge([], [])
    result5 = []
    assert test5 == result5, f"Empty list: expected: {test5}, result: {result5}"
    print(f"Two empty lists: {test5} -> {result5}")

    print("✓ Alla givna tester godkända!")