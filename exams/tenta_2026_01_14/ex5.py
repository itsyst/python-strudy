from operator import contains
import sys


def validate_brackets(s: str) -> bool:
    opens_par = []

    for char in s:
        if char == '(' or char == '[':
            opens_par.append(char)

        if char == ')':
            if  len(opens_par) == 0:
                return False
            elif opens_par[-1] == '(':
                opens_par.pop()
            elif opens_par[-1] != '(' or len(opens_par) == 0: 
                return False
 
        if char == ']':
            if  len(opens_par) == 0:
                return False
            elif opens_par[-1] == '[':
                opens_par.pop()
            elif opens_par[-1] != '[':
                return False
      
    return len(opens_par) == 0


def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    assert validate_brackets("a(b)c") == True

    # Här öppnas '(' först, sedan '['. Då måste ']' komma före ')')
    assert validate_brackets("a(b[c])") == True

    # ( Felaktig n ä stling : ’[ ’ ö ppnades sist men ’) ’ f ö rs ö kte st ä nga f ö rst )
    assert validate_brackets(" ([) ] ") == False

    # ( Oavslutad parentes )
    assert validate_brackets(" ( ") == False

    # ( F ö rs ö k att st ä nga utan att ha ö ppnat )
    assert validate_brackets(" ] ") == False

    # ( Inga parenteser alls r ä knas som balanserat )
    assert validate_brackets(" Hej ") == True

    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")
    print(" [((((('Hej')))))]] expected False", "got False")
    assert validate_brackets(" [((((('Hej')))))]] ") == False
    print(" (('Hej' + (Lui) + [])) expected True", "got True")
    assert validate_brackets(" (('Hej' + (Lui) + [])) ") == True

    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print(validate_brackets("a(b)c"))      # True
    print(validate_brackets(" ([) ] "))    # False
    print(validate_brackets(" ( "))        # False
    print(validate_brackets("a(b[c])"))    # True
    print(validate_brackets(" ] "))        # False
    print(validate_brackets(" Hej "))      # True

    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
