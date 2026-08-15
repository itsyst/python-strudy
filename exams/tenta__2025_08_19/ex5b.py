import sys
import math
from ex5a import pred_comp
 
safe_div = pred_comp(lambda div: div[1] !=0,  lambda div : div[0] / div[1], lambda div: 0)

def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    assert safe_div((10, 5)) == 2
    assert safe_div((10, 4)) == 2.5
    assert safe_div((10, 0)) == 0
    assert math.isclose(safe_div((2.5, 6.5)), 0.38, abs_tol=0.01)
    assert round(safe_div((2.5, 5.5)), 2 ) == 0.45
    assert abs(safe_div((2.5, 6.5)) - 0.38) < 0.01
    
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
    print(safe_div((10, 5)))
    print(safe_div((10, 4)))
    print(safe_div((10, 0)))
    print(safe_div((2.5, 6.5)))
    print(safe_div((2.5, 5.5)))
   
    print("Har kört alla tester")

if __name__ == '__main__':
    check_python_version()
    run_tests()
