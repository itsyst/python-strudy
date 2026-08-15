import sys


def is_domino_chain(dominos: list):
    if len(dominos) <= 1:
        return True
    for i in range(len(dominos) - 1):
        left_domino = dominos[i]
        right_domino = dominos[i+1]
        if left_domino[1] != right_domino[0]:
            return False
    return True


def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    # Här matchar man 4 med 4, och 3 med 3
    assert is_domino_chain([(1, 4), (4, 3), (3, 6)]) == True

    # Här matchar inte 4 med 5
    assert is_domino_chain([(1, 4), (5, 3)]) == False

    # En tom kedja räknas som giltig
    assert is_domino_chain([]) == True

    # En ensam bricka är alltid en giltig kedja
    assert is_domino_chain([(1, 2)]) == True

    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")
    print("Resultat 1:", is_domino_chain([(1, 4), (4, 4), (4, 5)]))

    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print("Kör utskriftstester...")
    print("Resultat 1:", is_domino_chain([(1, 4), (4, 3), (3, 6)]))
    print("Resultat 2:", is_domino_chain([(1, 4), (5, 3)]))
    print("Resultat 3:", is_domino_chain([]))
    print("Resultat 4:", is_domino_chain([(1, 2)]))

    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
