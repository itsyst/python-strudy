import math
import sys

# Global reusable rules
IS_EVEN = lambda x: x % 2 == 0
IS_POSITIVE = lambda x: x > 0
RULES = [IS_EVEN, IS_POSITIVE]

NUMBERS = [-2, 2, 3, 4, 5]
 
def make_validator(rules: list):
   def validator(value):
       for rule in rules:
           if not rule(value):
               return False
       return True
   return validator

def filter_valid(seq: list, validator_func) -> list:
    return [num for num in seq if validator_func(num)] 
 
def test_method(method, name: str):
    if name == "make_validator":
        assert method(RULES)(4) is True
        assert method(RULES)(3) is False
        assert method(RULES)(-2) is False
        assert method(RULES)(-3) is False

        always_ok = method([])
        assert always_ok("anything") == True

    elif name == "filter_valid":
        assert method(NUMBERS, make_validator(RULES)) == [2, 4]
        assert method([], make_validator(RULES)) == []
        assert method([1, 2, 6, 8, -10], make_validator(RULES)) == [2, 6, 8]

def check_python_version():
    print(
        f"Python {sys.version_info.major}."
        f"{sys.version_info.minor}."
        f"{sys.version_info.micro}"
    )


def run_tests():
    print("Testar make_validator...")
    test_method(make_validator, "make_validator")
    print("make_validator klarade alla tester.")

    print("*" * 40)

    print("Testar filter_valid...")
    test_method(filter_valid, "filter_valid")
    print("filter_valid klarade alla tester.")

    print("*" * 40)
    print(make_validator(RULES)(4))
    print(make_validator(RULES)(-2))
    print(make_validator([])("anything"))
    print(filter_valid(NUMBERS, make_validator(RULES)))
    print(filter_valid([0, -1, max(2,3), 26, math.sqrt(4)], make_validator(RULES)))
    print("Har kört alla tester.")
 
if __name__ == '__main__':
    check_python_version()
    run_tests()
