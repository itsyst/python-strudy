import sys

def pred_comp(p, t, f):
    # if lambda x: p(x):
    #     return lambda x:t(x)
    # else:
    #     return lambda x: f(x)
    return lambda x:t(x) if p(x) else f(x)
    

def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    assert pred_comp(lambda x: x > 0, lambda x: x, lambda x: -x)(-4) == 4
    add_world = pred_comp(lambda x: x == "", lambda x: x, lambda x: x + "World")
    assert add_world("Hello") == "HelloWorld"
    assert add_world("") == ""
    
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
    print(pred_comp(lambda x: x > 0, lambda x: x, lambda x: -x)(-4))
    print(add_world("Hello"))
    print(add_world(""))
   
    print("Har kört alla tester")

if __name__ == '__main__':
    check_python_version()
    run_tests()
