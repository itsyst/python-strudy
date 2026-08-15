import sys


def expand(men: list[str] , msg: list):
    result = []
    for item in msg:  
        if isinstance(item, list):
            result =  result + [expand(men, item)]
        elif type(item) is int:
            result += [men[item]]
        else:
            result += [item]
        
    return result    
 
def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    mem = [' ','att','lycka','tenta','till','på','är','kanske','tentan']
  
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
    print(expand(mem, []))
    print(expand(mem, [2, 6, 1, 3]))
    print(expand(mem, [2, 4, 'med', 8]))
    print(expand(mem, [[2, [6]], [7, ['med'], [[4], 1]], 3]))
    print(expand(mem, [2, 6, [7, 'att', []], 3]))
 
    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
