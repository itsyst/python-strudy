import math


def is_prime(n):
    """
    Kontrollerar om ett heltal n är ett primtal.
    
    Args:
        n (int): Heltal >= 1
        
    Returns:
        bool: True om n är primtal, annars False
    """
    if not isinstance(n, int):
        raise TypeError(f"Primtal är endast definierade för heltal. Mottaget värde: {n} (typ: {type(n).__name__})")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Testa bara division upp till sqrt(n) för effektivitet
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    
    return True


def prime_factors(n):
    """
    Returnerar en lista av primfaktorer för ett tal n.
    
    Args:
        n (int): Heltal >= 2
        
    Returns:
        list: Lista med primfaktorer
    """
    if not isinstance(n, int) or n < 2:
        raise ValueError(f"Talet måste vara ett heltal >= 2. Mottaget: {n}")
    
    factors = []
    
    # Testa division med 2 först
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Testa udda tal från 3 och uppåt
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    
    # Om n > 1 är kvar, är det en primfaktor
    if n > 1:
        factors.append(n)
    
    return factors


def is_attractive(n):
    """
    Kontrollerar om ett tal är attraktivt.
    Ett tal är attraktivt om antalet primfaktorer är ett primtal.
    
    Args:
        n (int): Heltal >= 2
        
    Returns:
        bool: True om n är attraktivt, annars False
    """
    if not isinstance(n, int) or n < 2:
        raise ValueError(f"Talet måste vara ett heltal >= 2. Mottaget: {n}")
    
    factors = prime_factors(n)
    num_factors = len(factors)
    
    return is_prime(num_factors)


if __name__ == "__main__":
    print("=" * 70)
    print("STEG 1: PRIMTAL")
    print("=" * 70)
    
    # Grundläggande primtalstester
    assert is_prime(1) == False, "Test misslyckades: is_prime(1) borde returnera False"
    assert is_prime(2) == True, "Test misslyckades: is_prime(2) borde returnera True"
    assert is_prime(10) == False, "Test misslyckades: is_prime(10) borde returnera False"
    assert is_prime(11) == True, "Test misslyckades: is_prime(11) borde returnera True"
    assert is_prime(10000000019) == True, "Test misslyckades: is_prime(10000000019) borde returnera True"
    print("√ Alla primtalstester godkända!")
    
    print("\n" + "=" * 70)
    print("STEG 2: PRIMTALSFAKTORISERING")
    print("=" * 70)
    
    # Samma testfall som steg 1 (utom 1, eftersom prime_factors kräver n >= 2)
    result = sorted(prime_factors(2))
    assert result == [2], f"Test misslyckades: prime_factors(2) borde returnera [2], fick {result}"
    
    result = sorted(prime_factors(10))
    assert result == [2, 5], f"Test misslyckades: prime_factors(10) borde returnera [2, 5], fick {result}"
    
    result = sorted(prime_factors(11))
    assert result == [11], f"Test misslyckades: prime_factors(11) borde returnera [11], fick {result}"
    
    result = sorted(prime_factors(10000000019))
    assert result == [10000000019], f"Test misslyckades: prime_factors(10000000019) borde returnera [10000000019], fick {result}"
    
    # Ursprungliga tester från uppgiften
    result = sorted(prime_factors(20))
    assert result == [2, 2, 5], f"Test misslyckades: prime_factors(20) borde returnera [2, 2, 5], fick {result}"
    
    result = sorted(prime_factors(55))
    assert result == [5, 11], f"Test misslyckades: prime_factors(55) borde returnera [5, 11], fick {result}"
    
    print("√ Alla primtalsfaktoriseringstester godkända!")
    
    print("\n" + "=" * 70)
    print("STEG 3: ATTRAKTIVA TAL")
    print("=" * 70)
    
    # Samma testfall som steg 1 (utom 1, eftersom is_attractive kräver n >= 2)
    result = is_attractive(2)
    assert result == False, f"Test misslyckades: is_attractive(2) borde returnera False (1 primfaktor, 1 är inte primtal), fick {result}"
    
    result = is_attractive(10)
    assert result == True, f"Test misslyckades: is_attractive(10) borde returnera True (2 primfaktorer, 2 är primtal), fick {result}"
    
    result = is_attractive(11)
    assert result == False, f"Test misslyckades: is_attractive(11) borde returnera False (1 primfaktor, 1 är inte primtal), fick {result}"
    
    result = is_attractive(10000000019)
    assert result == False, f"Test misslyckades: is_attractive(10000000019) borde returnera False (1 primfaktor, 1 är inte primtal), fick {result}"
    
    # Ursprungliga tester från uppgiften
    result = is_attractive(16)
    assert result == False, f"Test misslyckades: is_attractive(16) borde returnera False, fick {result}"
    
    result = is_attractive(20)
    assert result == True, f"Test misslyckades: is_attractive(20) borde returnera True, fick {result}"
    
    result = is_attractive(21)
    assert result == True, f"Test misslyckades: is_attractive(21) borde returnera True, fick {result}"
    
    result = is_attractive(22)
    assert result == True, f"Test misslyckades: is_attractive(22) borde returnera True, fick {result}"
    
    result = is_attractive(23)
    assert result == False, f"Test misslyckades: is_attractive(23) borde returnera False, fick {result}"
    
    result = is_attractive(24)
    assert result == False, f"Test misslyckades: is_attractive(24) borde returnera False, fick {result}"
    
    result = is_attractive(55)
    assert result == True, f"Test misslyckades: is_attractive(55) borde returnera True, fick {result}"
    
    print("√ Alla attraktiva tal-tester godkända!")
    
    print("\n" + "=" * 70)
    print("√√√ ALLA TESTER GODKÄNDA! √√√")
    print("=" * 70)
