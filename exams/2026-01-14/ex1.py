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
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    print("Kör uppgiftens tester...")
    assert is_domino_chain([(1, 4), (4, 3), (3, 6)]) == True
    assert is_domino_chain([(1, 4), (5, 3)]) == False
    assert is_domino_chain([]) == True
    assert is_domino_chain([(1, 2)]) == True

    print("*"*40)
    print("Kör egna tester...")
    print("Resultat 1:", is_domino_chain([(1, 4), (4, 4), (4, 5)]))

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
