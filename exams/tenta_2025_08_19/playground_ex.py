import math

def find_least_close(seq1: list[int], seq2: list[int]):
    if len(seq1) == 0 or len(seq2) == 0:
        return []

    sorted_seq2 = sorted(seq2)
    result = []

    for x in seq1:
        diff_left = abs(x - sorted_seq2[0])
        diff_right = abs(x - sorted_seq2[-1])

        if diff_left > diff_right:
            result.append(sorted_seq2[0])
        else:
            result.append(sorted_seq2[-1])

    return result


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
        # while n % prime == 0:
        #     factors.append(prime)
        #     n = n // prime
        if n % prime == 0:
            return [prime] + prime_factors(n // prime)
 
    return factors


def is_attractive(n: int):
    return is_prime(len(prime_factors(n))) == True


def expand(men: list[str] , msg: list):
    pass


def  expand_concat(mem: list[str], msg: list):
    pass

def add_nested(seq1: list, seq2: list):
    pass

def pred_comp(p, t, f):
    pass

# safe_div = pred_comp():

def create_trie():
    pass

 
def add_word(trie, word:str):
   pass


def word_in_trie(trie, word:str):
    pass
 
def find_all_matches(trie, prefix: str):
    pass
