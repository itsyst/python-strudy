from operator import contains
import sys

def find_least_close(seq1:list[int], seq2: list[int]):
    if len(seq1) == 0 or len(seq2) == 0:
        return []
    sorted_seq2 = sorted(seq2)
    result =  []
    for x in seq1:
        diff_left = abs(x - sorted_seq2[0])
        diff_right = abs(x - sorted_seq2[-1])
 
        if diff_left > diff_right:
            result.append(sorted_seq2[0])
        else:
            result.append(sorted_seq2[-1])

    return result
 

def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    # Det tal i seq2 som är längst bort från 11 är 5
    assert find_least_close([11], [5, 8, 12, 15]) == [5]

    # Seq1 är tom, så svaret blir också tomt
    assert find_least_close([], [1]) == []
    assert find_least_close([10], [5, 8, 12, 15]) == [15]
    # Seq1 innehåller två tal, och båda är längst bort från -1000
    assert find_least_close([12, 10], [-1000, 5, 8, 12, 15]) == [-1000, -1000]

    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")
    assert find_least_close([2,3,4], [1]) == [1,1,1]
    assert find_least_close([4,10,6], [1,2,3]) == [1,1,1]
    
    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print("Kör utskriftstester...")
    print(find_least_close([11], [5, 8, 12, 15]))            # [5]
    print(find_least_close([], [1]))                         # []
    print(find_least_close([10], [5, 8, 12, 15]))            # [15]
    print(find_least_close([12, 10], [-1000, 5, 8, 12, 15])) # [-1000, -1000]

    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
