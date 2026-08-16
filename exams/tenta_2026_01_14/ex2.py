import sys

def depth_sum(nested_list) -> int:
    return 0
    



def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    # (10*1 + 20*1)
    assert depth_sum([6, 7]) == 13

    # (Enligt exemplet ovan)
    assert depth_sum([1, [2, 3], 4]) == 15

    # (10 ligger på djup2, 20 ligger på djup 3. Alltså 10*20 + 20*3)
    assert depth_sum([[10], [[20]]]) == 80

    # (1*0 = 0)
    assert depth_sum([]) == 0

    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")
    assert depth_sum([-1, [-1, [-1, [-1]]]]) == -10
    assert depth_sum([0, [[]]]) == 0

    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print("Kör utskriftstester...")
    print(depth_sum([6, 7]))                          # 30
    print(depth_sum([1, [2, 3], 4]))                    # 15
    print(depth_sum([[10], [[20]]]))                 # 80
    print(depth_sum([]))  # 0
    print(depth_sum([-1, [-1, [-1, [-1]]]]))  # -10
    print(depth_sum([0, [[]]]))  # 0

    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
