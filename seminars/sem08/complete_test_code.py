# Komplett körbar fil med alla lösningar

def cocktail_shaker_sort(seq):
    """Cocktail shaker sort"""
    n = len(seq)
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(n - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(n - 2, -1, -1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True


def next_state(seq, pred):
    """Cellulär automat - nästa tillstånd"""
    new_seq = []
    n = len(seq)
    for i in range(n):
        left = seq[i - 1] if i > 0 else False
        center = seq[i]
        right = seq[i + 1] if i < n - 1 else False
        new_seq.append(pred(left, center, right))
    return new_seq


def print_state(seq):
    """Skriv ut cellulär automat"""
    state = ""
    for alive in seq:
        state += "x" if alive else " "
    print(state)


def predicate_factory(n):
    """Skapa predikatfunktion för regel n"""
    def predicate(a, b, c):
        index = (a << 2) | (b << 1) | c
        return bool((n >> index) & 1)
    return predicate


if __name__ == "__main__":
    # Test sortering
    print("=== COCKTAIL SHAKER SORT ===")
    test_list = [5, 3, 8, 4, 2, 7, 1, 6]
    print(f"Före: {test_list}")
    cocktail_shaker_sort(test_list)
    print(f"Efter: {test_list}\n")
    
    # Test cellulär automat
    print("=== CELLULÄR AUTOMAT - REGEL 110 ===")
    rule_110 = predicate_factory(110)
    seq = [i == 40 for i in range(80)]
    print_state(seq)
    for i in range(20):
        seq = next_state(seq, rule_110)
        print_state(seq)
