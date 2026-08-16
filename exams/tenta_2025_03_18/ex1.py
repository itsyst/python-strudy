import sys

def doors():
    open_doors = []

    for door in range(1, 101):
        toggles = 0
        for step in range(1, 101):
            if door % step == 0:
                toggles += 1

        if toggles % 2 == 1:
            open_doors.append(door)

    return open_doors
    
    
 
def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    result = doors()
    assert result == sorted(result) # Testa korrekt ordning
    assert 1 in result
    assert 2 not in result
    assert 3 not in result
    assert 4 in result
    assert 5 not in result
    assert 6 not in result
    assert 7 not in result
    assert 8 not in result
    assert 48 not in result
    assert 49 in result
    assert 50 not in result

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
    print(doors())

 
    print("Har kört alla tester")

if __name__ == '__main__':
    check_python_version()
    run_tests()
