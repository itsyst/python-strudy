import sys


def enumerate_nested_rec(nest: list) -> dict:
    result = {}

    def visit(current_list: list, path: tuple):
        for i, item in enumerate(current_list):
            new_path = path + (i,)
            print(new_path)
            if isinstance(item, list):
                visit(item, new_path)
            else:
                result[new_path] = item

    visit(nest, ())
    return result


def enumerate_nested_while(nest: list) -> dict:
    result = {}
    todo: list[tuple[list, tuple[int, ...]]] = [(nest, ())]

    while todo:
        lst, path = todo.pop()

        for i, value in enumerate(lst):
            new_path = path + (i,)

            if isinstance(value, list):
                todo.append((value, new_path))
            else:
                result[new_path] = value

    return result


def test_enumerate_nested(method):
    assert method([10, [20, 30]]) == {(0,): 10, (1, 0): 20, (1, 1): 30}
    assert method([[["a"]], "b"]) == {(0, 0, 0): 'a', (1,): 'b'}
    assert method([[], 42]) == {(1,): 42}
    assert method([]) == {}


def check_python_version():
    print(
        f"Python {sys.version_info.major}."
        f"{sys.version_info.minor}."
        f"{sys.version_info.micro}"
    )


def run_tests():
    print("Testar enumerate_nested_rec...")
    test_enumerate_nested(enumerate_nested_rec)
    print("enumerate_nested_rec klarade alla tester.")

    print("Testar enumerate_nested_while...")
    test_enumerate_nested(enumerate_nested_while)
    print("enumerate_nested_while klarade alla tester.")

    print("*" * 40)
    print("Har kört alla tester.")
    print(enumerate_nested_rec([10, [20, 30]]))


if __name__ == '__main__':
    check_python_version()
    run_tests()
