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


def print_notes(notes):
    """
    Skriver ut toner som ett förenklat notsystem.
    Förväntar att notes bara innehåller bokstäverna i "cdefgah".
    """
    # Definiera ordningen på toner från lägst till högst
    note_order = ['c', 'd', 'e', 'f', 'g', 'a', 'h']
    
    # Skapa en dictionary för att snabbt hitta index för varje ton
    note_to_index = {note: i for i, note in enumerate(note_order)}
    
    # Skapa en lista med 7 tomma strängar (en för varje rad)
    # Rad 0 (index 0) är för 'h' (högst), rad 6 är för 'c' (lägst)
    rows = ["" for _ in range(7)]
    
    # Fyll i raderna för varje ton i sekvensen
    for note in notes:
        current_note_index = note_to_index[note]
        
        # Gå igenom alla rad-positioner
        for row_idx in range(7):
            # Om den här raden motsvarar den aktuella tonen
            if row_idx == (6 - current_note_index):  # Vänd ordningen så 'h' blir överst
                rows[row_idx] += note
            else:
                rows[row_idx] += '.'
    
    # Skriv ut resultatet
    for row in rows:
        print(row)
 
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

    print()
    notes_only = "cccedddfcdefgah"
    print_notes(notes_only)
    # Förväntat utskrift:
    # ..............h
    # .............a.
    # ............g..
    # .......f...f...
    # ...e......e....
    # ....ddd..d.....
    # ccc.....c......
    print()

if __name__ == "__main__":
    run_tests()
 
