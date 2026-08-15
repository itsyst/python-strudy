#%%
#def test2(str):
#    if len(str) == 1 and str[0] in valid_chars:
#        return True
#    elif str[0] in valid_chars and str[-1] in valid_chars and str[0] == str:
#        str.pop(0)
#        str.pop(-1)
#        return test2(str)
#    else:
#        return False


def is_two(foo):
    if foo == foo[::-1]:
        for letter in foo:
            if letter != "a" and letter != "b":
                return False
            return True
        return False

def is_two(s):
    return s == s[::-1] and all(let == "a" or let == "b" for let in s)

#Uppgift: Prefix
#def contains_prefixes(seq1, seq2):
#    if len(seq1) == 0:
#        return True
#    #elif len(seq1) == 1:
#    #print(f"seq1[0] = {seq1[0]}, seq2[0][0:len(seq1)] = {seq2[0][0:len(seq1[0])]}")
#    if seq1[0] == seq2[0][0:len(seq1[0])]:
#        return contains_prefixes(seq1[1:], seq2)
#    elif seq1[0] == seq2[]
#        return contains_prefixes(seq1, seq2[1:])
#    
        

##annanns::
#def contains_prefix(prefs, strs):
#    if len(prefs) > len(strs):
#        raise ValueError
#    if len(prefs) == 0:
#        return True
#    if prefs[0] == strs[0][0:len(prefs[0])]:
#        return contains_prefix(prefs[1:], strs[0])


#>>> contains_prefixes(["hej"], ["hejsan", "asdfasdf"])
#True
#>>> contains_prefixes(["hej", "sdf"], ["hejsan", "asdfasdf"])
#False

#Uppgift: Primtal i Fibbonacci-sekvensen
#mitt:
##
#annans:
#def fib_prime(num):
#    a1 = 0
#    a2 = 1
#    temp = None
#    fib = []
#    while len(fib) <= num:
#        is_prime = True
#        temp = a1+a2
#        a1 = a2
#        a2 = temp
#        if (a2 < 1):
#            for i in range(2, int(a2**0.5) + 1):
#                if a2 % i == 0:
#                    is_prime = False
#                    break
#            if is_prime == True:
#                return True
#    return primes
    
                



if __name__ == "__main__":
    #print(contains_prefixes(["hej"], ["hejsan", "asdfasdf"]))
    print(contains_prefixes(["hej", "sdf"], ["hejsan", "asdfasdf"]))

#%%