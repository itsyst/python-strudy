def is_prime(n):
    """Kontrollerar om ett tal är primtal"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def fibonacci_primes(n):
    """
    Returnerar de första n primtalen i Fibonacci-sekvensen
    n = antal primtal att hitta
    """
    primes = []
    a, b = 0, 1
    
    while len(primes) < n:
        a, b = b, a + b
        if is_prime(b):
            primes.append(b)
    
    return primes


if __name__ == "__main__":
    primes1 = fibonacci_primes(10)
    primes2 = fibonacci_primes(5)
    print(f"{primes1}\n{primes2}")

# >>> fibonacci_primes(10)
# [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437]

# >>> fibonacci_primes(5)
# [2, 3, 5, 13, 89]
