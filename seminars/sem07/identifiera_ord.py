# identifiera.py
# Identifierar vilket språk en sträng tillhör

from ebnf_uppgift1 import generate_S as generate_lang1
from ebnf_uppgift2 import generate_S_recursive as generate_lang2


def recognize_language_1(s):
    """
    Identifierar om en sträng tillhör språk 1.
    Språk 1 = {a, aaa, aab, ba, bb}
    """
    valid_words = {'a', 'aaa', 'aab', 'ba', 'bb'}
    return s in valid_words


def recognize_language_2(s):
    """
    Identifierar om en sträng tillhör språk 2.
    Språk 2 = alla palindromer över {a, b}
    """
    if not all(c in ['a', 'b', ''] for c in s):
        return False
    return s == s[::-1]


if __name__ == "__main__":
    print("="*70)
    print("IDENTIFIERING AV GENERERADE STRÄNGAR")
    print("="*70)
    
    # Test strängar från språk 1
    print("\n### Strängar från uppgift1.py (Språk 1):")
    print("-"*70)
    print(f"{'#':<5} {'Sträng':<15} {'Språk 1':<12} {'Språk 2':<12} {'Resultat':<20}")
    print("-"*70)
    
    for i in range(10):
        word = generate_lang1()
        is_lang1 = recognize_language_1(word)
        is_lang2 = recognize_language_2(word)
        
        display_word = f"'{word}'" if word else "''"
        lang1_mark = "✓" if is_lang1 else "✗"
        lang2_mark = "✓" if is_lang2 else "✗"
        
        if is_lang1 and is_lang2:
            result = "Båda språken"
        elif is_lang1:
            result = "Endast språk 1"
        else:
            result = "Endast språk 2"
        
        print(f"{i+1:<5} {display_word:<15} {lang1_mark:<12} {lang2_mark:<12} {result:<20}")
    
    # Test strängar från språk 2
    print("\n### Strängar från uppgift2.py (Språk 2):")
    print("-"*70)
    print(f"{'#':<5} {'Sträng':<15} {'Språk 1':<12} {'Språk 2':<12} {'Resultat':<20}")
    print("-"*70)
    
    for i in range(10):
        word = generate_lang2()
        is_lang1 = recognize_language_1(word)
        is_lang2 = recognize_language_2(word)
        
        display_word = f"'{word}'" if word else "''"
        lang1_mark = "✓" if is_lang1 else "✗"
        lang2_mark = "✓" if is_lang2 else "✗"
        
        if is_lang1 and is_lang2:
            result = "Båda språken"
        elif is_lang1:
            result = "Endast språk 1"
        else:
            result = "Endast språk 2"
        
        print(f"{i+1:<5} {display_word:<15} {lang1_mark:<12} {lang2_mark:<12} {result:<20}")
    
    print("\n" + "="*70)
    print("SAMMANFATTNING")
    print("="*70)
    print("Språk 1 = {a, aaa, aab, ba, bb}  (5 ord)")
    print("Språk 2 = Alla palindromer över {a, b}  (oändligt)")
    print("="*70)
