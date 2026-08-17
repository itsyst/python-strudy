import sys

def is_mountain_flags(seq: list[int]) -> bool:
    if len(seq) < 3:
        return False

    has_increased = False
    has_decreased = False

    for i in range(len(seq) - 1):
        a = seq[i]
        b = seq[i + 1]

        if a == b:
            return False

        if a < b:
            if has_decreased:
                return False
            has_increased = True
        else:
            has_decreased = True

    return has_increased and has_decreased


def is_mountain_top(seq: list[int]) -> bool:
    if len(seq) < 3:
        return False

    top = max(seq)
    top_index = seq.index(top)

    if top_index == 0 or top_index == len(seq) - 1:
        return False

    for i in range(top_index):
        if seq[i] >= seq[i + 1]:
            return False

    for i in range(top_index, len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            return False

    return True


def test_mountain(method):
    assert method([1, 3, 5, 4, 2]) is True
    assert method([0, 10, 5, 2]) is True
    assert method([1, 2, 2, 3, 1]) is False
    assert method([1, 2, 3]) is False
    assert method([3, 2, 1]) is False
    assert method([1, 3, 2, 4, 1]) is False
    assert method([]) is False
    assert method([5]) is False

    # Egna extra tester
    assert method([1, 2, 1]) is True
    assert method([2, 1, 2]) is False
    assert method([1, 3, 3, 2]) is False
    assert method([1, 4, 3, 2, 1]) is True


def check_python_version():
    print(
        f"Python {sys.version_info.major}."
        f"{sys.version_info.minor}."
        f"{sys.version_info.micro}"
    )


def run_tests():
    print("Testar is_mountain_flags...")
    test_mountain(is_mountain_flags)
    print("is_mountain_flags klarade alla tester.")

    print("*" * 40)

    print("Testar is_mountain_top...")
    test_mountain(is_mountain_top)
    print("is_mountain_top klarade alla tester.")

    print("*" * 40)
    print("Har kört alla tester.")


if __name__ == '__main__':
    check_python_version()
    run_tests()