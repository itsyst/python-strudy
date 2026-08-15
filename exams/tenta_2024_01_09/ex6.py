def create_trie():
    """
    Skapar och returnerar en tom Trie.
    """
    return {'children': {}, 'is_end': False}


def add_word(trie, word: str):
    """
    Addera ett nytt ord (icke-tom sträng) till en Trie.
    """
    if not isinstance(word, str):
        raise ValueError("Ordet måste vara en sträng")
    
    if not word:
        raise ValueError("Ordet kan inte vara tomt")
    
    current = trie
    for char in word:
        current['children'].setdefault(char, {'children': {}, 'is_end': False})
        current = current['children'][char]
    current['is_end'] = True


def word_in_trie(trie, word: str):
    """
    Avgör om ett ord finns med i trie.
    
    Args:
        trie: Trie
        word: sträng
    
    Returns:
        True om ordet word finns i trie annars False.
    """
    if not isinstance(word, str):
        raise ValueError("Ordet måste vara en sträng")
    
    if not word:
        raise ValueError("Ordet kan inte vara tomt")
    
    current = trie
    for char in word:
        if char not in current['children']:
            return False
        current = current['children'][char]
    
    return current['is_end']


def find_all_matches(trie, prefix: str):
    """
    Deluppgift 6b: Returnerar en mängd (set) med alla ord som börjar med prefix.
    Funktionen gör ingen ändringar i trie.
    
    Args:
        trie: Trie
        prefix: sträng som prefix
    
    Returns:
        En set med alla ord som börjar med prefix
    
    Exempel:
        find_all_matches(trie, "ace") == {"ace", "aced", "aces"}
    """
    if not isinstance(prefix, str) or not prefix:
        raise ValueError("Prefix måste vara en icke-tom sträng")
    
    current = trie
    for char in prefix:
        if char not in current['children']:
            return set()  # Returnera tom set om prefix inte finns
        current = current['children'][char]
    
    # Nested rekursiv funktion för att samla ord
    def collect_words(node, current_word):
        """Inre rekursiv funktion för att samla ord"""
        result = set()  # Använd set istället för list
        
        if node['is_end']:
            result.add(current_word)  # Använd add() istället för append()
        
        for char, child_node in node['children'].items():
            result.update(collect_words(child_node, current_word + char))
        
        return result
    
    # Anropa den inre funktionen och returnera resultatet
    return collect_words(current, prefix)


if __name__ == "__main__":
    print("=" * 70)
    print("DELUPPGIFT 6a: GRUNDERNA - TESTER")
    print("=" * 70)
    
    # TESTER FRÅN UPPGIFTSBESKRIVNINGEN 6a
    print("\n📝 Ursprungliga tester från uppgiftsbeskrivningen:")
    trie = create_trie()
    for word in ["ace", "aced", "aces", "acre", "acres", "act", "acted", "acting", "acts"]:
        add_word(trie, word)
        assert word_in_trie(trie, word), f"MISSLYCKADES: {word} hittades inte efter add_word()"
    
    for word in ["ace", "aced", "aces", "acre", "acres", "act", "acted", "acting", "acts"]:
        assert word_in_trie(trie, word), f"MISSLYCKADES: {word} hittades inte i sökning"
    
    for word in "En Trie är en effektiv datastruktur".split(" "):
        assert not word_in_trie(trie, word), f"MISSLYCKADES: {word} borde inte hittas"
    
    print("✓ Alla ursprungliga tester från 6a GODKÄNDA\n")
    
    # TESTER FÖR DELUPPGIFT 6b: find_all_matches
    print("=" * 70)
    print("DELUPPGIFT 6b: FORTSÄTTNING PÅ PREFIX - TESTER")
    print("=" * 70)
    
    # TEST 6b.1: Grundläggande find_all_matches test
    print("\n📝 TEST 6b.1: Grundläggande find_all_matches")
    result = find_all_matches(trie, "ace")
    expected = {"ace", "aced", "aces"}
    assert result == expected, f"MISSLYCKADES: Förväntade {expected}, fick {result}"
    print(f"✓ find_all_matches(trie, 'ace') == {result} GODKÄND")
    
    # TEST 6b.2: Prefix "act"
    print("\n📝 TEST 6b.2: Prefix 'act'")
    result = find_all_matches(trie, "act")
    expected = {"act", "acted", "acting", "acts"}
    assert result == expected, f"MISSLYCKADES: Förväntade {expected}, fick {result}"
    print(f"✓ find_all_matches(trie, 'act') == {result} GODKÄND")
    
    # TEST 6b.3: Prefix "acre"
    print("\n📝 TEST 6b.3: Prefix 'acre'")
    result = find_all_matches(trie, "acre")
    expected = {"acre", "acres"}
    assert result == expected, f"MISSLYCKADES: Förväntade {expected}, fick {result}"
    print(f"✓ find_all_matches(trie, 'acre') == {result} GODKÄND")
    
    # TEST 6b.4: Prefix som inte finns
    print("\n📝 TEST 6b.4: Prefix som inte finns")
    result = find_all_matches(trie, "xyz")
    expected = set()
    assert result == expected, f"MISSLYCKADES: Förväntade {expected}, fick {result}"
    print(f"✓ find_all_matches(trie, 'xyz') == set() GODKÄND")
    
    # TEST 6b.5: Enstaka ord som är prefix till andra
    print("\n📝 TEST 6b.5: Prefix 'a' (många matchningar)")
    result = find_all_matches(trie, "a")
    expected = {"ace", "aced", "aces", "acre", "acres", "act", "acted", "acting", "acts"}
    assert result == expected, f"MISSLYCKADES: Förväntade {len(expected)} ord, fick {len(result)}"
    print(f"✓ find_all_matches(trie, 'a') returnerade alla {len(result)} ord GODKÄND")
    
    # TEST 6b.6: Fel-hantering - tom sträng
    print("\n📝 TEST 6b.6: Fel-hantering - tom prefix")
    try:
        find_all_matches(trie, "")
        print("✗ TEST 6b.6 MISSLYCKADES: Skulle kasta ValueError")
        exit(1)
    except ValueError as e:
        print(f"✓ ValueError kastades korrekt: '{e}'")
    
    # TEST 6b.7: Fel-hantering - felaktig typ
    print("\n📝 TEST 6b.7: Fel-hantering - felaktig typ")
    try:
        find_all_matches(trie, 123)
        print("✗ TEST 6b.7 MISSLYCKADES: Skulle kasta ValueError")
        exit(1)
    except ValueError as e:
        print(f"✓ ValueError kastades korrekt: '{e}'")
    
    # TEST 6b.8: Returnerar set (inte list)
    print("\n📝 TEST 6b.8: Returnerar set (inte list)")
    result = find_all_matches(trie, "ace")
    assert isinstance(result, set), f"MISSLYCKADES: Förväntade set, fick {type(result)}"
    print(f"✓ find_all_matches returnerar set (inte list)")
    
    # TEST 6b.9: Set jämförelse (ordningen spelar ingen roll)
    print("\n📝 TEST 6b.9: Set jämförelse (ordningen spelar ingen roll)")
    result1 = find_all_matches(trie, "ace")
    result2 = {"aced", "ace", "aces"}  # Annan ordning
    assert result1 == result2, f"MISSLYCKADES: Sets borde vara lika"
    print(f"✓ Set jämförelse fungerar oavsett ordning")
    
    # TEST 6b.10: Längre prefix som motsvarar exakt ord
    print("\n📝 TEST 6b.10: Längre prefix som motsvarar exakt ord")
    result = find_all_matches(trie, "acted")
    expected = {"acted"}
    assert result == expected, f"MISSLYCKADES: Förväntade {expected}, fick {result}"
    print(f"✓ find_all_matches(trie, 'acted') == {result} GODKÄND")
    
    # SAMMANFATTNING
    print("\n" + "=" * 70)
    print("✅ ALLA TESTER FRÅN 6a OCH 6b GODKÄNDA!")
    print("=" * 70)
    print("\n📊 Testöversikt:")
    print("  ✓ Deluppgift 6a: Grunderna (create_trie, add_word, word_in_trie)")
    print("  ✓ Deluppgift 6b: find_all_matches returnerar set")
    print("  ✓ Prefix-sökning fungerar korrekt")
    print("  ✓ Felhantering för tom och felaktig typ")
    print("  ✓ Set-jämförelse utan ordningsberoende")
    print("=" * 70)
