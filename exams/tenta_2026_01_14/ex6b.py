from ctypes.wintypes import tagMSG
from encodings import undefined
from operator import contains
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


def find_path(fs: dict, target: str) :
    for k,v in fs.items():
        if k == target:
            return target
 
        elif isinstance(v, dict): 
            subpath = find_path(v, target)
            if subpath != None:
                return k + "/" + subpath
  
    return None 
 
def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    assert find_path(file_system, "resume.txt") == "home/user/resume.txt"
    assert find_path(file_system, "user") == "home/user"
    assert find_path(file_system, "boot.ini") == "boot.ini"
    assert find_path(file_system, "missing.txt") is None

    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")
    new_file = file_system.copy()
    new_file["home"]["info"] = 120
    assert find_path(new_file, "info") == "home/info"
    # nested dict
    assert find_path({"1": {"2": {"3": {"4": {"5": {"6": {"7": {"backup.dat": -2}}}}}}}},
                     "backup.dat") == "1/2/3/4/5/6/7/backup.dat"

    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print(find_path(file_system, "resume.txt"))
    print(find_path(file_system, "user"))
    print(find_path(file_system, "boot.ini"))
    print(find_path(file_system, "missing.txt"))
    print(find_path(new_file, "info"))
    print(find_path(
        {"x": {"y": {"z": {"v": {"w": {"t": {"u": {"backup.dat": -2}}}}}}}}, "backup.dat"))
    print(find_path({"a":{"b":{},"c":{"backup.txt":1212}}}, "info.txt"))  # None

    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
