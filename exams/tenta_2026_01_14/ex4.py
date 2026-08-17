from operator import contains
import sys

def add_sparse_list(v1: dict, v2: dict):
    result = {}
    key_list = []
    for k, v in v1.items():
        if k not in key_list:
           key_list.append(k)
        result[k] = v

    for k, v in v2.items():
        if k not in key_list:
            key_list.append(k)
            result[k] = v
        else:
            result[k] += v

    return result


def add_sparse_dict(v1: dict, v2: dict):
    result = dict(v1)
    for k2, v2 in v2.items():
        if k2 not in result.keys():
            result[k2] = v2
        else:
            result[k2] += v2

    return result

 
def test_add_spare(method):
    # Index 1: v1 har 10 , v2 har 5. Summa : 15.
    # Index 2: v1 saknar indexet (0) , v2 har 3. Summa : 3.
    # Index 5: v1 har 2 , v2 saknar indexet (0) . Summa : 2.
    v1 = {1: 10, 5: 2}
    v2 = {1: 5, 2: 3}
    assert method(v1, v2) == {1: 15, 2: 3, 5: 2}
    # Man kan addera till en tom dictionary .
    assert method({}, {0: 100}) == {0: 100}
    # Det ä r till å tet att ha nollor explicit lagrade i resultatet , eller att " ta bort " dem .
    # {1: 0} ä r lika korrekt som en tom dictionary , dict () .
    assert method({1: 10}, {1: -10}) in ({1: 0}, dict())

    # Egna extra tester
    # Addera två tom dictionary
    assert method({}, {}) == {}
     # Addera två identic dictionary
    assert method({1:2}, {1:2}) == {1:4}
     # Large integers
    big = 2**60
    assert method({1:big}, {1:big}) == {1: big + big}

     # None numeric values
    big = 2**60
    assert method({1:"a"}, {1:"b"}) == {1: "ab"}
    print(method({1:"a"}, {1:"b"}))
       
def check_python_version():
    print(
        f"Python {sys.version_info.major}."
        f"{sys.version_info.minor}."
        f"{sys.version_info.micro}"
    )


def run_tests():
    print("Testar add_sparse_list...")
    test_add_spare(add_sparse_list)
    print("add_sparse_list klarade alla tester.")

    print("*" * 40)

    print("Testar add_sparse_dict...")
    test_add_spare(add_sparse_dict)
    print("add_sparse_dict klarade alla tester.")

    print("*" * 40)
    print("Har kört alla tester.")


if __name__ == '__main__':
    check_python_version()
    run_tests()
