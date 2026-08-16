import sys

def split_by_first(seq: list[str]) -> dict[str, list]:
    result = {}
    for item in seq:
        first_char = item[0]
        if first_char not in result.keys():
            result[first_char] = [item]
        else:
            result[first_char] += [item]
        
 
    return result



def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    assert split_by_first(['apa', 'bepa', 'arg']) == {'a': ['apa', 'arg'], 'b': ['bepa']}
    assert split_by_first(['01', '13', '02', '14', '01']) == {'0': ['01', '02', '01'], '1': ['13', '14']}
    assert split_by_first(['Bakom', 'brödbutiken', 'bodde', 'Baskerbosses', 'båda', 'bröder', 'bröderna', 'Basker']) == {'B': ['Bakom', 'Baskerbosses', 'Basker'],
    'b': ['brödbutiken', 'bodde', 'båda', 'bröder', 'bröderna']}
    assert split_by_first(['abc']) == {'a': ['abc']}

    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")


    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print("Kör utskriftstester...")
    print(split_by_first(['apa', 'bepa', 'arg']))
    print(split_by_first(['bepa', 'apa', 'arg']))
    print(split_by_first(['01', '13', '02', '14', '01']))
     
    
    print("Har kört alla tester")

if __name__ == '__main__':
    check_python_version()
    run_tests()