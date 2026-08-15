def split_at(seq, pred):
    """
    Funktionen returnerar en uppdelad sekvensen vid pred positioner
    """
    temp_lista = []
    splitted_list = []
    
    for element in seq:
        if not pred(element):
            temp_lista.append(element)
        else:
            splitted_list.append(list(temp_lista))
            temp_lista = []
 
    splitted_list.append(list(temp_lista))
    
    return splitted_list
 
if __name__ == "__main__":
    assert split_at([1,2,3,4,2,5], lambda x: x==2) == [[1], [3,4], [5]], "Test 1 misslyckades"
    assert split_at([2,3,4,2,5], lambda x: x==2) == [[], [3,4], [5]], "Test 2 misslyckades"
    assert split_at([1,2,3,4,2], lambda x: x==2) == [[1], [3,4], []], "Test 3 misslyckades"
    assert split_at([1,2,2,3,4,2,5], lambda x: x==2) == [[1], [], [3,4], [5]], "Test 4 misslyckades"
    assert split_at("abcdeba", lambda x: x=="b") == [["a"], ["c", "d", "e"], ["a"]], "Test 5 misslyckades"
    assert split_at([1,2,3,4,5], lambda x: x % 2 == 0) == [[1], [3], [5]], "Test 6 misslyckades"
    print("✓ Alla givna tester godkända!")