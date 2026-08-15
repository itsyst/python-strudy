# ----- Constants -----
def is_constant(obj):
    return isinstance(obj, (int, float))

def make_constant(n):
    return n


# ----- Variables -----
def is_variable(obj):
    return isinstance(obj, str)

def same_variable(v1, v2):
    return v1 == v2


# ----- Sum -----
def is_sum(obj):
    return isinstance(obj, list) and len(obj) == 3 and obj[1] == '+'

def make_sum(e1, e2):
    return [e1, '+', e2]


# ----- Product -----
def is_product(obj):
    return isinstance(obj, list) and len(obj) == 3 and obj[1] == '*'

def make_product(e1, e2):
    return [e1, '*', e2]


# ----- Expression accessors -----
def arg1(expr):
    return expr[0]

def arg2(expr):
    return expr[2]
