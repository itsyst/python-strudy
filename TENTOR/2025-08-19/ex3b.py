import sys
from ex3a import expand


def  expand_concat(mem: list[str], msg: list):
    expanded = expand(mem, msg)
  
    buffer = ''
    result = []
    for elem in expanded:
        if isinstance(elem, str):
            buffer = buffer + elem
        else:                        
            if buffer != '':
                result.append(buffer)
                buffer = ''
            result.append(elem)       
    if buffer != '':
        result.append(buffer)
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
    print(expand_concat(mem, [2, 6, 1, 3]))                       # ['lyckaäratttenta']
    print(expand_concat(mem, [2, 0, 6, 0, 1, 0, 3]))              # ['lycka är att tenta']
    print(expand_concat(mem, [2, 0, 6, [7, 0, 'att', []], 3, 0])) # ['lycka är', ['kanske att', []], 'tenta ']
    print(expand_concat(mem, [[[3, 3, [], [], 3]]]))              #[[['tentatenta', [], [], 'tenta']]]
    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
