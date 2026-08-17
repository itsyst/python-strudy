import importlib

EXERCISES = [
    ("playground_ex", "invert_dict"),
    ("playground_ex", "is_mountain"),
    ("playground_ex", "enumerate_nested"),
    ("playground_ex", "make_validator"),
    ("playground_ex", "crosses_own_path"),
    ("playground_ex", "new_listset"),
]


def test_ex1(module) -> None:
    assert module.invert_dict({"a": 1, "b": 1, "c": 2}) == {
        1: ["a", "b"], 2: ["c"]}
    assert module.invert_dict({"x": "hello", "y": "world"}) == {
        "hello": ["x"], "world": ["y"]}
    assert module.invert_dict({}) == {}


def test_ex2(module) -> None:
    assert module.is_mountain([1, 3, 5, 4, 2]) is True
    assert module.is_mountain([0, 10, 5, 2]) is True
    assert module.is_mountain([1, 2, 2, 3, 1]) is False
    assert module.is_mountain([1, 2, 3]) is False
    assert module.is_mountain([3, 2, 1]) is False
    assert module.is_mountain([1, 3, 2, 4, 1]) is False
    assert module.is_mountain([]) is False
    assert module.is_mountain([5]) is False


def test_ex3(module) -> None:
    assert module.enumerate_nested([10, [20, 30]]) == {
        (0,): 10,
        (1, 0): 20,
        (1, 1): 30,
    }
    assert module.enumerate_nested([[['a']], 'b']) == {
        (0, 0, 0): 'a', (1,): 'b'}
    assert module.enumerate_nested([[], 42]) == {(1,): 42}
    assert module.enumerate_nested([]) == {}


def test_ex4(module) -> None:
    def is_even(x): return x % 2 == 0
    def is_positive(x): return x > 0
    valid_num = module.make_validator([is_even, is_positive])

    assert valid_num(4) is True
    assert valid_num(3) is False
    assert valid_num(-2) is False
    assert valid_num(-3) is False
    assert module.make_validator([])("anything") is True
    assert module.filter_valid([-2, 2, 3, 4, 5], valid_num) == [2, 4]
    assert module.filter_valid([], valid_num) == []
    assert module.filter_valid([1, 2, 6, 8, -10], valid_num) == [2, 6, 8]


def test_ex5(module) -> None:
    assert module.crosses_own_path("NESW") is True
    assert module.crosses_own_path("NNN") is False
    assert module.crosses_own_path("NESEN") is False
    assert module.crosses_own_path("EW") is True
    assert module.crosses_own_path("") is False


def test_ex6(module) -> None:
    ls1 = module.new_listset()
    assert isinstance(ls1, module.ListSet)

    module.listset_add(ls1, 10)
    module.listset_add(ls1, 20)
    module.listset_add(ls1, 10)

    assert module.listset_contains(ls1, 10) is True
    assert module.listset_contains(ls1, 99) is False
    assert len(ls1.elements) == 2

    ls2 = module.new_listset()
    module.listset_add(ls2, 20)
    module.listset_add(ls2, 30)
    ls_union = module.listset_union(ls1, ls2)

    assert module.listset_contains(ls_union, 10) is True
    assert module.listset_contains(ls_union, 20) is True
    assert module.listset_contains(ls_union, 30) is True
    assert len(ls_union.elements) == 3


TESTS = {
    "invert_dict": test_ex1,
    "is_mountain": test_ex2,
    "enumerate_nested": test_ex3,
    "make_validator": test_ex4,
    "crosses_own_path": test_ex5,
    "new_listset": test_ex6,
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
