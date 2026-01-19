def find_notes_1(text: str) -> str:
    notes = set("cdefgah")  # {'c','d','e','f','g','a','h'} # set for faster membership test
   
    if not text:
        return ""
    
    matches = [char for char in text.lower() if char in notes]
    return ''.join(matches)

def find_notes_2(text: str) ->str:
    notes = set("cdefgah")
    result = ""
    for char in text:
        if char in notes:
            result += char
    return result

# The optimal implementation
def find_notes_3(text: str) -> str:
    notes = set("cdefgah")  # {'c','d','e','f','g','a','h'} # set for faster membership test
   
    if not text:
        return ""

    return ''.join(char for char in text.lower() if char in notes)

def run_tests():
    expected1 = ""
    result1 = find_notes_1("")
    assert expected1 == result1, f"Vacuous: expected: {expected1}, result: {result1}"
    print(f"Test1: find_notes({expected1}) -> {result1}")

    expected1 = "aae"
    result1 = find_notes_2("Bananer")
    assert expected1 == result1, f"Canonical: expected: {expected1}, result: {result1}"
    print(f"Test2: find_notes({expected1}) -> {result1}")

    expected2 = "adgh"
    result2 = find_notes_3("Andningshål")
    assert expected2 == result2, f"Canonical: expected: {expected2}, result: {result2}"
    print(f"Test3: find_notes({expected2}) -> {result2}")

    expected2 = "aeadeaaf"
    result2 = find_notes_3("Nu ska vi testa denna lilla funktion")
    assert expected2 == result2, f"Sentence: expected: {expected2}, result: {result2}"
    print(f"Test3: find_notes({expected2}) -> {result2}")

if __name__ == "__main__":
    run_tests()
