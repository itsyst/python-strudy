import sys

def invert_dict(d: dict) -> dict:
    inverted = {}
    for key, value in d.items():
        if value not in inverted.keys():
            inverted[value] = []
        inverted[value] += [key]
            
    return inverted



def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    assert invert_dict({'a': 1, 'b': 1, 'c': 2}) == {1: ['a', 'b'], 2: ['c']}
    assert invert_dict({'x': 'hello', 'y': 'world'}) == {'hello': ['x'], 'world': ['y']}
    assert invert_dict({}) == {}
    assert invert_dict({'p': 5, 'q': 5, 'r': 5}) == {5: ['p', 'q', 'r']}

    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")
    

    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print(invert_dict({'a': 1, 'b': 1, 'c': 2}))
     

    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
