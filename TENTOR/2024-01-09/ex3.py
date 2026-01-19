def without(nest, to_remove) -> list:
    result = []
    for element in nest:
        if isinstance(element, list):
            # Recurse into sublist
            result.append(without(element, to_remove))
        elif element not in to_remove:
            # Keep atomic elements not in to_remove
            result.append(element)
        else:
            # element is in to_remove → skip by doing nothing
            pass
    return result

def without_head_tail(nest, to_remove):
    if not nest:  # empty list
        return []

    head, *tail = nest

    # Process head
    if isinstance(head, list):
        new_head = without_head_tail(head, to_remove)
    elif head in to_remove:
        new_head = None  # skip
    else:
        new_head = head

    # Recurse on tail
    new_tail = without_head_tail(tail, to_remove)

    # Combine head and tail
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
