def without(nest, to_remove) -> list:
    result = []
    for element in nest:
        if isinstance(element, list):
            result.append(without(element, to_remove))
        elif element not in to_remove:
            result.append(element)
    return result


def without_head_tail(nest, to_remove):
    if not nest:
        return []

    head, *tail = nest

    if isinstance(head, list):
        new_head = without_head_tail(head, to_remove)
    elif head in to_remove:
        new_head = None
    else:
        new_head = head

    new_tail = without_head_tail(tail, to_remove)

    if new_head is None:
        return new_tail
    else:
        return [new_head] + new_tail


def run_tests():
    print(without([[1], [[2]], [[[3]]], [[[[4]]]]], [1, 3]))
    assert without([[1], [[2]], [[[3]]], [[[[4]]]]], [1, 3]) == [
        [], [[2]], [[[]]], [[[[4]]]]]
    assert without([[[[[[[[[[10]]]]]]]]]], [10]) == [[[[[[[[[[]]]]]]]]]]
    assert without([[[[[[[[[[10]]]]]]]]]], [5]) == [[[[[[[[[[10]]]]]]]]]]
    assert without([[(1, 2)], [["b"]], [[[None]]], [[[[42.5]]]]], [1, None]) == [
        [(1, 2)], [["b"]], [[[]]], [[[[42.5]]]]]
    assert without([[[[[]]]]], []) == [[[[[]]]]]
    assert without([[[]], [[], [[]]]], []) == [[[]], [[], [[]]]]


if __name__ == "__main__":
    run_tests()
