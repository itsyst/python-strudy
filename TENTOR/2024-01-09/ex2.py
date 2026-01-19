from pdb import run
from re import S

def merge(s1:list, s2:list):
    merged = []
    while True:
        if s1 and s2:
            if s1[0] < s2[0]:
                merged.append(s1[0])
                s1 = s1[1:]
            else:
                merged.append(s2[0])
                s2 = s2[1:]
        elif s1:
            merged.append(s1[0])
            s1 = s1[1:]
        elif s2:
            merged.append(s2[0])
            s2 = s2[1:]
        else:
            return merged

def merge_recursive(s1: list, s2: list):
    if len(s1) == 0:
        return s2
    if len(s2) == 0:
        return s1

    if s1[0] <= s2[0]:
        return [s1[0]] + merge_recursive(s1[1:], s2)
    else:
        return [s2[0]] + merge_recursive(s1, s2[1:])

def check_python_version():
    import sys
    # Local Python version
    major, minor, micro = sys.version_info[:3]
    print("Local Python version:", major, minor, micro)

    # assert at least Python 3.8
    assert (major, minor) >= (3, 12), "Python 3.8 or newer is required"


def run_tests():
     test_cases = [
         ([], [], []),
         ([], [1], [1]),
         ([1], [], [1]),
         ([1, 2, 5, 13], [3, 5, 21], [1, 2, 3, 5, 5, 13, 21]),
         ([-5, -2], [-3, -1], [-5,-3,-2,-1]),
         (['a', 'c'], ['b', 'o'],  ['a', 'b', 'c', 'o']),
     ]

     for i, testcase in enumerate(test_cases):
         expected = testcase[2]
         result_n = merge(testcase[0], testcase[1])
         result_r = merge_recursive(testcase[0], testcase[1])
         assert(result_n == expected), f" Test { i +1 }:expected{expected}, got {result_n}"
         print(f"Test{ i + 1}: merge({testcase[0]},{testcase[1]}) -> {testcase[2]}")
         assert(result_r == expected), f" Test_rec { i +1 }:expected{expected}, got {result_r}"
         print(f"Test_rec{ i + 1}: merge({testcase[0]},{testcase[1]}) -> {testcase[2]}\n")

if __name__ == "__main__":
    check_python_version()
    run_tests()
