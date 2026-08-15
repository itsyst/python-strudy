
# encoding: iso-8859-1

# ----- Main matching functions -----

def matcher(pattern, expr):
    return match(pattern, expr, {})

def match(pattern, expr, dict):
    "pattern x expression x values -> values"
    if empty_pattern(pattern):
        if empty_expr(expr):
            return dict
        else:
            return 'fail'
    elif dict == 'fail':
        return 'fail'
    elif is_arbitrary(pattern):
        return extend_dictionary(pattern, expr, dict)
    elif is_element(pattern):
        if is_element(expr) and same_expression(expr, pattern):
            return dict
        else:
            return 'fail'
    elif is_element(expr):
        return 'fail'
    else:
        return match(rest_pattern(pattern), rest_expr(expr), \
                     match(first_pattern(pattern), first_expr(expr), dict))
        
def extend_dictionary(pattern, expr, dict):
    dict[variable_name(pattern)] = expr
    return dict

# ----- Primitive functions -----

# Element
    
def is_element(obj):
    "object -> truth value"
    return isinstance(obj, str) or isinstance(obj, int)
    
# Arbitrary

def is_arbitrary(obj):
    "object -> truth value"
    return isinstance(obj, list) and len(obj) == 2 and obj[0] == '?'
    
def variable_name(pattern):
    "pattern -> variable"
    return pattern[1]

# Expression

def same_expression(e1, e2):
    "expression x expression -> truth value"
    return e1 == e2
    
def first_expr(expr):
    "expression -> expression"
    return expr[0]
    
def rest_expr(expr):
    "expression -> expression"
    return expr[1:]
    
def empty_expr(expr):
    "expression -> truth value"
    return not expr

# Pattern
    
def first_pattern(pattern):
    "pattern -> pattern"
    return pattern[0]
    
def rest_pattern(pattern):
    "pattern -> pattern"
    return pattern[1:]

def empty_pattern(pattern):
    "pattern -> truth value"
    return not pattern
