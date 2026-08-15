def next_state(seq, pred):
    """
    Returnerar nästa tillstånd av automaten baserat på predikatfunktionen.
    Kanter hanteras genom att anta att celler utanför listan är döda (False).
    """
    new_seq = []
    n = len(seq)
    
    for i in range(n):
        # Hantera kanter: anta att celler utanför är döda
        left = seq[i - 1] if i > 0 else False
        center = seq[i]
        right = seq[i + 1] if i < n - 1 else False
        
        # Använd predikatfunktionen för att avgöra nästa tillstånd
        new_state = pred(left, center, right)
        new_seq.append(new_state)
    
    return new_seq


# Alternativ hantering av kanter (wrap-around):
def next_state_wrap(seq, pred):
    """
    Samma som next_state men med wrap-around (cirkulär lista).
    """
    new_seq = []
    n = len(seq)
    
    for i in range(n):
        left = seq[i - 1]  # Python hanterar -1 som sista elementet
        center = seq[i]
        right = seq[(i + 1) % n]  # Wrap around
        
        new_state = pred(left, center, right)
        new_seq.append(new_state)
    
    return new_seq


# Förklaring av kanthantering:
#     Metod 1: Anta att celler utanför är döda - fungerar bra för mönster som växer från mitten
#     Metod 2: Wrap-around - behandlar listan som cirkulär, bra för periodiska mönster
#     Problem: Båda kan orsaka artefakter där mönster reflekteras eller påverkas av kanter
