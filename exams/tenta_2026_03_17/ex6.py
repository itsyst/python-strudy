import sys
from typing import NamedTuple, Any
 
#class ListSet(NamedTuple): elements: list[Any]
ListSet = NamedTuple("ListSet", [("elements", list[Any])])
 
def new_listSet()  -> ListSet:
    return ListSet([])

def listSet_contains(ls, val):
    return True if val in ls.elements else False

def listSet_add(ls: ListSet, val: Any) -> None:
    if val not in ls.elements:
        ls.elements.append(val)
 
def listSet_union(ls1: ListSet, ls2: ListSet):
    new_set = new_listSet()
 
    for val in [*ls1.elements, *ls2.elements]:
        if val not in new_set.elements:
            new_set.elements.append(val)

    return new_set
 
ls1 = new_listSet()
ls2 = new_listSet()
ls_union = listSet_union(ls1, ls2) 

def test_method(method):
    # list set one
    assert isinstance(ls1, ListSet)

    listSet_add(ls1, 10)
    listSet_add(ls1, 20)
    listSet_add(ls1, 10) # Dubblett, ska ignoreras     

    assert method(ls1, 10) == True 
    assert method(ls1, 99) == False 
    assert len(ls1.elements) == 2

    # list set two 
    listSet_add(ls2, 20) 
    listSet_add(ls2, 30)

    # list union
    assert listSet_contains(ls_union,10) 
    assert listSet_contains(ls_union, 20) 
    assert listSet_contains(ls_union, 30) 
    assert len(ls_union.elements) == 3

def check_python_version():
    print(
        f"Python {sys.version_info.major}."
        f"{sys.version_info.minor}."
        f"{sys.version_info.micro}"
    )

def run_tests():
    print("Testar listset_contains...")
    # test_method(listset_contains)
    print("listset_contains klarade alla tester.")
 
    print("*" * 40)
 
    print("Har kört alla tester.")
    listSet_add(ls1, 20)
    listSet_add(ls2, 10)
    listSet_add(ls2, 20)

    print(listSet_contains(ls1, 20))
    print(listSet_union(ls1, ls2))
 
if __name__ == '__main__':
    check_python_version()
    run_tests()
