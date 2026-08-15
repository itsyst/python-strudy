import sys
 
def add_nested(seq1: list, seq2: list):
    nestled_list = []
    if len(seq1) != len(seq2):
        return []
    
    for i in range(len(seq1)):
        a = seq1[i]
        b = seq2[i]

        if isinstance(a, list) and isinstance(b,list):
                nestled_list = nestled_list + [add_nested(a, b)]
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            nestled_list.append(a + b)
        elif type(a) is type(b):
            nestled_list.append(a + b)
           
    return nestled_list
 
 

def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    # assert add_nested([1, 2], [15, 4.25]) == [16, 6.25]

    
    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")
    seq1 = [1,2,3]
    seq2 = [9,8,7]
    seq3 = [[["a"], 6, [2, (3, 5)]]]
    seq4 = [[["b"], 5, [1, (1, 1, 42)]]]
    assert add_nested(seq1, seq2) == [10,10,10]
    assert add_nested(seq3, seq4) == [[["ab"], 11, [3, (3,5,1,1,42)]]]

 
    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print("Kör utskriftstester...")
    print(add_nested(seq1, seq2))
    print(add_nested(seq3, seq4))
    print(add_nested([1, 2], [15, 4.25]))
    print(add_nested(["a"], [15]))
    print("Har kört alla tester")

if __name__ == '__main__':
    check_python_version()
    run_tests()
