import math
import sys

def is_prime(n:int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0:
            return False
    return True

def prime_dividers(n: int):
    prime_divider = []
    for i in range(2,n + 1):
        if is_prime(i):
            prime_divider.append(i)
    return prime_divider

def prime_factors(n: int):  
    factors =[]
    prime_divider = prime_dividers(n)
    for prime in prime_divider:
        if n % prime == 0:
            return [prime] + prime_factors(n // prime)
    return factors

def is_attractive(n: int):
    return is_prime(len(prime_factors(n))) == True
 
 
def check_python_version():
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def run_tests():
    print("Kör uppgiftens tester...")
    assert is_prime(1) == False            
    assert is_prime(2) == True 
    assert is_prime(10) == False
    assert is_prime(11) == True
    prim_numbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    for num in prim_numbers:
        assert is_prime(num)

    print("*"*40)
    assert sorted(prime_factors(2)) == [2]
    assert sorted(prime_factors(10)) == [2, 5]
    assert sorted(prime_factors(20)) == [2, 2, 5]
    assert sorted(prime_factors(55)) == [5, 11]
    assert is_attractive(16) == False

    print("*"*40)
    print("Kör egna tester...")
    assert is_prime(-1) == False
 
    print("*"*40)
    print("Kör utskriftstester...")
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(10))
    print(is_prime(11))
    print(prime_factors(2))
    print(prime_factors(10))
    print(prime_factors(20))
    print(is_attractive(16))
    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
