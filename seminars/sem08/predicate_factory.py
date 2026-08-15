from cellular_automat import next_state

def predicate_factory(n):
    """
    Skapar en predikatfunktion för regel nummer n (0-255).
    
    Regeln kodas i binär där varje bit representerar output för en kombination:
    Position: 7 6 5 4 3 2 1 0 (binär position)
    Input:    7 6 5 4 3 2 1 0 (a,b,c som 3-bitars tal)
    
    Exempel: Regel 110 = 01101110 i binär
    """
    def predicate(a, b, c):
        # Konvertera (a,b,c) till ett tal 0-7
        index = (a << 2) | (b << 1) | c
        # eller: index = a*4 + b*2 + c
        
        # Kolla om bit nummer 'index' i n är satt
        # Extrahera bit: (n >> index) & 1
        return bool((n >> index) & 1)
    
    return predicate


# Alternativ implementation med bin():
def predicate_factory_alt(n):
    """Alternativ med bin() för tydligare logik."""
    # Konvertera n till 8-bitars binär sträng
    binary = bin(n)[2:].zfill(8)  # Ta bort '0b' prefix, fyll med nollor
    # Vänd strängen så index matchar position
    binary = binary[::-1]
    
    def predicate(a, b, c):
        index = a*4 + b*2 + c
        return binary[index] == '1'
    
    return predicate


# Test
if __name__ == "__main__":
    print("Test av predicate_factory:")
    
    # Regel 126 (01111110 i binär)
    rule_126 = predicate_factory(126)
    print("\nRegel 126:")
    seq = [i == 40 for i in range(80)]
    print(seq)
    for i in range(10):
        seq = next_state(seq, rule_126)
        print(seq)
    
    # Regel 110 (01101110 i binär)
    rule_110 = predicate_factory(110)
    print("\nRegel 110:")
    seq = [i == 40 for i in range(80)]
    print(seq)
    for i in range(10):
        seq = next_state(seq, rule_110)
        print(seq)
