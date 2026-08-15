def contains_prefixes(list1, list2):
    """
    Kontrollerar om varje sträng i list1 är ett prefix till någon sträng i list2.
    """
    for prefix in list1:
        found = False
        for string in list2:
            if string.startswith(prefix):
                found = True
                break
        if not found:
            return False
    return True
    
#""" Kortare version:"""
# def contain_prefixes(list1, list2):
#     return all(any(s.startswith(prefix) for s in list2) for prefix in list1)


if __name__ == "__main__":
    print("="*50)
    print("Experimentering: Prefix")
    print("="*50)
    word1 = contains_prefixes(["hej"], ["hejsan", "asdfasdf"])
    word2 = contains_prefixes(["hej", "sdf"], ["hejsan", "asdfasdf"])
    word3 = contains_prefixes(["hej", "sdf"], ["hejsan", "asdfasdf"])
    word4 = contains_prefixes(["h", "as"], ["hejsan", "asdfasdf"])

    tests = [word1, word2, word3, word4]
    for i in range(4):
        print(f"prefix-{ i+ 1}: {tests[i]}")