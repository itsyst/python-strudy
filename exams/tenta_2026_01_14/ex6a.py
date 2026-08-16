import sys

file_system = {
    "home": {
        "user": {
        "resume.txt": 100,
        "picture.jpg": 2000
        },
        "todo.txt": 50
    },
    "boot.ini": 10
}


def total_size(fs: dict):
    total = 0
    for k, v in fs.items():
        if isinstance(v, dict):
            total += total_size(v) 
        else:
            total += v
    
    return total


def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    # (100 + 2000 + 50 + 10)
    assert total_size(file_system) == 2160

    assert total_size({" a ": 10, " b ": 20}) == 30

    # ( En tom mapp har storlek 0)
    assert total_size({}) == 0
    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")
    new_file = file_system.copy()
    new_file["info"] = 120
    assert total_size(new_file) == 2280
    # nested dict
    assert total_size({"1":{"2":{"3":{"4":{"5":{"6":{"7":{"info": -2}}}}}}}}) == -2

    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print(total_size(file_system))                    # 2160
    print(total_size({" a ": 10, " b ": 20}))         #   30
    print(total_size({}))                             #    0
    print(total_size(new_file))                       # 2280
    print(total_size({"1":{"2":{"3":{"4":{"5":{"6":{"7":{"info": -2}}}}}}}})) #   -2

    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
