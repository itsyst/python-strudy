# ExempellÃ¶sningar till datortenta i TDDD73 2016-01-12 eftermiddag

### Uppgift 1
def rotn(string, n):
    """
    Rotate each character in string n steps,
    i.e. return the rot-n version of the string string.
    """
    ans = ""
    for c in string:
        ans += chr((ord(c)-ord('a')+n)%26+ord('a'))
    return ans

def encode(string):
    """
    If the length of string is even,
    then encode the string string using rot-n where n is the length
    of the string divided by 2 and rot-13 otherwise.
    """
    if len(string)%2==0:
        return rotn(string, n/2)
    else:
        return rotn(string, 13)

def decode(string):
    """ Decode a string encoded with encode. """
    if len(string)%2==0:
        return rotn(string, -n/2)
    else:
        return rotn(string, -13)


### Uppgift 2
def rle_i(seq):
    """ Generate the run length encoding of seq iteratively. """
    rle = []
    current_character = seq[0]
    count = 1
    for character in seq[1:]:
        if character == current_character:
            count += 1
        else:
            rle += [current_character, count]
            current_character = character
            count = 1
    return rle + [current_character, count]

def rle_r(seq, count=1):
    """ Generate the run length encoding of seq recursively. """
    if not seq:
        return []
    elif len(seq) == 1:
        return [seq[0], count]
    elif seq[0] == seq[1]:
        return rle_r(seq[1:], count+1)
    else:
        return [seq[0], count] + rle_r(seq[1:], 1)


### Uppgift 3a
def mymap(fnm, seq):
    """
    Apply the function fnm on every element in seq,
    if the element is a sequence apply fnm to every element
    of that sequence as well.
    """
    # Notering 2022-01-02, av nuvarande examinator (som inte skapade denna
    # tenta eller lösningsförslagen):
    # 
    # Detta lösningsförslag använder len() och isinstance, som enligt
    # https://docs.python.org/3/library/functions.html är inbyggda funktioner,
    # Meningen med kravet att "inte använda inbyggda funktioner" var troligen
    # inte att undvika dessa, utan att man inte fick använda inbyggda
    # funktioner som själva gjorde en stor del av jobbet, t.ex. den inbyggda
    # map().  Vi strävar mot att vara tydligare med den här typen av
    # begränsningar.
    #
    if len(seq) == 0:
        return []
    else:
        return [fnm(seq[0])] + mymap(fnm, seq[1:])

### Uppgift 3b
def myreduce(fnr, seq):
    """
    Reduce a sequence to a value by applying fnr to pairs of elements
    until only a single value remains.
    """
    # Notering 2022-01-02:  Se notering för 3a.
    if len(seq) == 1:
        return seq[0]
    elif len(seq) == 2:
        return fnr(seq[0], seq[1])
    else:
        return fnr(seq[0], myreduce(fnr, seq[1:]))

### Uppgift 3c
def odd_cubes(n):
    """
    Return the product of the cubes of all odd numbers less than or equal to n.
    """
    return myreduce(lambda x, y: x*y,
                    mymap(lambda x: x*x*x if x%2==1 else 1, range(n+1)))


### Uppgift 4
def edit_distance(s1, s2):
    """
    Return the edit distance between s1 and s2,
    i.e. the number of edits required to change one s1 to s2.
    """
    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))
    else:
        if s1[0] == s2[0]:
            return edit_distance(s1[1:], s2[1:])
        else:
            return 1 + min(edit_distance(s1[1:], s2),
                           edit_distance(s1, s2[1:]),
                           edit_distance(s1[1:], s2[1:]))


### Uppgift 5
def get_next_token(string):
    """ Get the next token in the string string. """
    # Find the first non white space character
    start = 0
    while string[start] == " ":
        start += 1

    # Find the first white space or start of next token
    end = start
    while end < len(string) and string[end] not in " (),":
        end += 1
    if end == start:
        end += 1

    return string[start:end], string[end:]


def tokenize(string):
    """ Tokenize a string. """
    tokens = []
    while string:
        token, string = get_next_token(string)
        tokens += [token]
    return tokens


def parse(string):
    """ Parse string according to given grammar. """
    return parse_fopl(tokenize(string))


def parse_fopl(inp):
    """ Parse a FOPL into a parse tree. """
    if len(inp) == 0:
        return ""
    elif inp[0] == "forall" or inp[0] == "exists":
        return [inp[0], inp[1], parse_fopl(inp[2:])]
    else:
        pred, new_inp = parse_predicate(inp)
        res = [pred]
        while len(new_inp) > 0 and new_inp[0] in ["and", "or", "->"]:
            res += [new_inp[0]]
            pred, new_inp = parse_predicate(new_inp[1:])
            res += [[pred]]
        return res


def parse_predicate(inp):
    """ Parse a predicate, return the parse tree and the rest of input. """
    if inp[0] == "not":
        pred, new_inp = parse_predicate(inp[1:])
        return [inp[0], pred], new_inp
    else:
        terms, new_inp = parse_terms(inp[2:]) # Skip (
        return [inp[0]]+terms, new_inp[1:]    # Skip )


def parse_terms(inp):
    """ Parse a term sequence, return the parse tree and the rest of input. """
    print("parse_terms", inp)
    term, new_inp = parse_term(inp)
    res = [term]
    while new_inp[0] == ",":
        term, new_inp = parse_term(new_inp[1:]) # Skip ,
        res += [term]
    return res, new_inp


def parse_term(inp):
    """ Parse a term, return the parse tree and the rest of input. """
    if inp[1] == "(":
        terms, new_inp = parse_terms(inp[2:]) # Skip (
        return [inp[0]] + terms, new_inp[1:]  # Skip )
    else:
        return inp[0], inp[1:]


### Uppgift 6
def mymap(fnm, seq):
    """
    Apply the function fnm on every element in seq,
    if the element is a sequence apply fnm to every element
    of that sequence as well.
    """
    # Notering 2022-01-02:  Se notering för 3a.
    if len(seq) == 0:
        return []
    elif isinstance(seq[0],list):
        return [mymap(fnm, seq[0])] + mymap(fnm, seq[1:])
    else:
        return [fnm(seq[0])] + mymap(fnm, seq[1:])


def myreduce(fnr, seq):
    """
    Reduce a sequence to a value by applying fnr to pairs of elements
    until only a single value remains. It handles list of lists.
    """
    # Notering 2022-01-02:  Se notering för 3a.
    if len(seq) == 1:
        if isinstance(seq[0], list):
            return myreduce(fnr, seq[0])
        else:
            return seq[0]
    elif isinstance(seq[0], list):
        return fnr(myreduce(fnr, seq[0]), myreduce(fnr, seq[1:]))
    else:
        return fnr(seq[0], myreduce(fnr, seq[1:]))

def mapreduce(fnm, fnr, seq):
    """
    Apply fnm to every element in seq and then reduce the elements
    to a single value using fnr.
    """
    return myreduce(fnr, mymap(fnm, seq))
