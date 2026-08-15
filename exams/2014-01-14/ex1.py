"""
Tentamen 2014-01-14 – Find notes in text
"""

def find_notes(text: str) -> str:
    """Extract musical notes (c,d,e,f,g,a,h) from text (case-insensitive)."""
    notes = set("cdefgah")
    if not text:
        return ""
    return "".join(char for char in text.lower() if char in notes)


def print_notes(notes: str):
    """Print notes as a simple staff."""
    note_order = ["c", "d", "e", "f", "g", "a", "h"]
    note_to_index = {note: i for i, note in enumerate(note_order)}
    rows = ["" for _ in range(7)]

    for note in notes:
        idx = note_to_index[note]
        for row_idx in range(7):
            if row_idx == (6 - idx):
                rows[row_idx] += note
            else:
                rows[row_idx] += "."

    for row in rows:
        print(row)


def run_tests():
    assert find_notes("") == ""
    assert find_notes("Bananer") == "aae"
    assert find_notes("Andningshål") == "adgh"
    assert find_notes("Nu ska vi testa denna lilla funktion") == "aeadeaaf"

    print("All find_notes tests passed ✅")
    print()
    print("Staff for 'cccedddfcdefgah':")
    print_notes("cccedddfcdefgah")


if __name__ == "__main__":
    run_tests()
