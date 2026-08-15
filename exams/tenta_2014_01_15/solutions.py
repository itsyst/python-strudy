# encoding: iso-8859-1

# -----------------------------------------------------------------------------
#  Datortentamen i kursen TDDD73 Funktionell och imperativ programmering i Python
#  2014-01-15
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#  Uppgift 1
# -----------------------------------------------------------------------------

def ascending(str):
    result = str[0]
    for char in str[1:]:
        if char.upper() > result[-1].upper():
            result += char
    return result

def decode(str):
    words = str.split(' ')
    result = ""
    for word in words:
        result += ascending(word)
    return result

# -----------------------------------------------------------------------------
#  Uppgift 2
# -----------------------------------------------------------------------------

def remove_empty_r(series):
    if not series:
        return []
    elif not series[0]:
        return remove_empty_r(series[1:])
    else:
        return [series[0]] + remove_empty_r(series[1:])
        
def remove_empty_i(series):
    result = []
    for s in series:
        if s:
            result += [s]
    return result

# -----------------------------------------------------------------------------
#  Uppgift 3
# -----------------------------------------------------------------------------

def with_series(series, fn_check, fn_series):
    if not series:
        return []
    elif fn_check(series[0]):
        return [fn_series(series[0])] + with_series(series[1:], fn_check, fn_series)
    else:
        return with_series(series[1:], fn_check, fn_series)
        
def averages(series, threshold):
    return with_series(series, 
                      (lambda s: s and all([x >= threshold for x in s])),
                      (lambda s: sum(s)/len(s)))

# -----------------------------------------------------------------------------
#  Uppgift 4
# -----------------------------------------------------------------------------

def max_level(seq):
    if not seq:
        return 0
    elif not isinstance(seq[0], list):
        return max(1, max_level(seq[1:]))
    else:
        return max(1+max_level(seq[0]), max_level(seq[1:]))
        
def levels(x, seq):
    def levels_help(x, seq, lvl):
        if not seq:
            return []
        elif seq[0] == x:
            return [lvl] + levels_help(x, seq[1:], lvl)
        elif isinstance(seq[0], list):
            return levels_help(x, seq[0], lvl+1) + levels_help(x, seq[1:], lvl)
        else:
            return levels_help(x, seq[1:], lvl)
    return levels_help(x, seq, 1)
    
# -----------------------------------------------------------------------------
#  Uppgift 5
# -----------------------------------------------------------------------------

def listify(expr):
    if not isinstance(expr, list):
        return [expr]
    else:
        return expr
        
def postfix(expr):
    if not isinstance(expr, list):
        return expr
    else:
        return listify(postfix(expr[0])) + listify(postfix(expr[2])) + [expr[1]]
        
# -----------------------------------------------------------------------------
#  Uppgift 6
# -----------------------------------------------------------------------------

from match_s import *

# Recognizer for new expression type

def is_number(obj):
    "object -> truth value"
    return isinstance(obj, list) and len(obj) == 2 and obj[0] == '='

# New version of dictionary extending

def extend_dictionary(pattern, expr, dict):
    name = variable_name(pattern)
    if name in dict:
        if same_expression(dict[name], expr):
            return dict
        else:
            return 'fail'
    else:
        dict[name] = expr
        return dict

# New version of matcher

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
    elif is_number(pattern):
        if isinstance(expr, int):
            return extend_dictionary(pattern, expr, dict)
        else:
            return 'fail'
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

def matcher(pattern, expr):
    return match(pattern, expr, {})
