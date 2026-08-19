import importlib

EXERCISES = [
    ("playground_ex", "find_least_close"),
    ("playground_ex", "is_prime"),
    ("playground_ex", "prime_factors"),
    ("playground_ex", "is_attractive"),
    ("playground_ex", "expand_concat"),
    ("playground_ex", "add_nested"),
    ("playground_ex", "create_trie"),
    ("playground_ex", "add_word"),
    ("playground_ex", "word_in_trie"),
    ("playground_ex", "find_all_matches")
]

def test_ex1(module) -> None:
    assert module.find_least_close([11], [5, 8, 12, 15]) == [5]
    assert module.find_least_close([], [1]) == []
    assert module.find_least_close([10], [5, 8, 12, 15]) == [15]
    assert module.find_least_close(
        [12, 10], [-1000, 5, 8, 12, 15]) == [-1000, -1000]

def test_ex2(module) -> None:
    assert module.is_prime(1) == False
    assert module.is_prime(2) == True
    assert module.is_prime(10) == False
    assert module.is_prime(11) == True
    assert module.is_prime(10_000_000_019) == True
    prim_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for num in prim_numbers:
        assert module.is_prime(num)
    assert module.is_prime(-1) == False

def test_ex3(module) -> None:
    assert sorted(module.prime_factors(2)) == [2]
    assert sorted(module.prime_factors(10)) == [2, 5]
    assert sorted(module.prime_factors(20)) == [2, 2, 5]
    assert sorted(module.prime_factors(55)) == [5, 11]

def test_ex4(module) -> None:
    assert module.is_attractive(16) == False

def test_ex5(module) -> None:
    pass

def test_ex6(module) -> None:
    pass

def test_ex7(module) -> None:
    pass

def test_ex8(module) -> None:
    pass

def test_ex9(module) -> None:
    pass

def test_ex10(module) -> None:
    pass
TESTS = {
    "find_least_close": test_ex1,
    "is_prime": test_ex2,
    "prime_factors": test_ex3,
    "is_attractive": test_ex4,
    "expand_concat": test_ex5,
    "add_nested": test_ex6,
    "create_trie": test_ex7,
    "add_word": test_ex8,
    "word_in_trie": test_ex9,
    "find_all_matches": test_ex10
}


def run_tests() -> None:
    passed = 0
    skipped = 0
    failed = 0

    for module_name, required_function in EXERCISES:
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            print(f"Hoppar över {module_name}: filen finns inte ännu.")
            skipped += 1
            continue

        if not hasattr(module, required_function):
            print(
                f"Hoppar över {required_function}: funktionen är inte klar ännu.")
            skipped += 1
            continue

        try:
            print(f"Testar {required_function}...")
            TESTS[required_function](module)
            print(f"{required_function} klarade alla tester.")
            passed += 1
        except AssertionError:
            print(f"{required_function} klarade inte testerna.")
            failed += 1
        except (AttributeError, TypeError, NameError) as error:
            print(f"{required_function} är inte färdig ännu: {error}")
            skipped += 1

        print("*" * 40)

    print(f"Godkända: {passed}")
    print(f"Överhoppade: {skipped}")
    print(f"Misslyckade: {failed}")


if __name__ == "__main__":
    run_tests()
