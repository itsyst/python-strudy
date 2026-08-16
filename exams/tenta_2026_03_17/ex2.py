from operator import indexOf
import sys

def is_mountain(seq: list[int]) -> bool :
    max_num = 0
  
    if len(seq) < 3:
        return False

    # for i in range(len(seq)):
    #     if seq[i] < seq[i+1] or seq[i] > seq[i+1]:
    #         return False

    for element in seq:
        if element > max_num:
            max_num = element
     
    for i in range(seq.index(max_num), seq.index(seq[-1])):
        print(seq[i])
        for j in range(0, seq.index(max_num)):
            print(seq[j])
            if seq[j] < max_num and max_num > seq[i]:
                return True
                
        
    return False



def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    assert is_mountain([1, 3, 5, 4, 2]) == True
    # assert is_mountain([0, 10, 5, 2]) == True
    # assert is_mountain([1, 2, 2, 3, 1]) == False # Ej strängt växande (2 följt av 2)
    # assert is_mountain([1, 2, 3]) == False # Saknar avtagande del
    # assert is_mountain([3, 2, 1]) == False # Saknar växande del
    # assert is_mountain([1, 3, 2, 4, 1]) == False # Mer än en topp
    # assert is_mountain([]) == False
    # assert is_mountain([5]) == False

    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")
    

    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    # print(is_mountain([1, 3, 5, 4, 2]))
     

    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
