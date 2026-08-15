def cocktail_shaker_sort(seq):
    """
    Cocktail shaker sort - sorterar en lista på plats.
    Går fram och tillbaka genom listan och byter plats på element.
    """
    n = len(seq)
    swapped = True
    
    while swapped:
        # Första loopen - framåt
        swapped = False
        for i in range(n - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        
        # Om ingen swap gjordes, är listan sorterad
        if not swapped:
            break
        
        # Andra loopen - bakåt
        swapped = False
        for i in range(n - 2, -1, -1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
    
    # Funktionen returnerar inget, modifierar listan på plats


# Test
if __name__ == "__main__":
    test_list = [5, 3, 8, 4, 2, 7, 1, 6]
    print(f"Före: {test_list}")
    cocktail_shaker_sort(test_list)
    print(f"Efter: {test_list}")
