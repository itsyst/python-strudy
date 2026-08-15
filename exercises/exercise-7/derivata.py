def differentiate(expr, var):
    """Returns the symbolic derivative of expr with respect to var."""
    
    # Variable
    if expr == var:
        return 1

    # Constant (numbers or other symbols)
    elif isinstance(expr, (int, float)) or isinstance(expr, str):
        return 0

    # Addition
    elif expr[1] == '+':
        return [differentiate(expr[0], var), '+', differentiate(expr[2], var)]
    
    # Multiplication (product rule)
    elif expr[1] == '*':
        return [[expr[0], '*', differentiate(expr[2], var)],
                '+',
                [differentiate(expr[0], var), '*', expr[2]]]

    # Exponent: x^n
    elif expr[1] == '^':
        base, _, power = expr
        
        # Only handling x^n where base == var and n is a number
        if base == var and isinstance(power, (int, float)):
            # n * x^(n-1)
            return [power, '*', [var, '^', power - 1]]
        else:
            raise Exception("Only power rule for x^n supported")

    else:
        raise Exception("Invalid expression")
 
def to_string(expr):
    # atomic
    if isinstance(expr, (int, float, str)):
        return str(expr)

    op = expr[1]

    # binary operators
    left = to_string(expr[0])
    right = to_string(expr[2])

    # add parentheses only when needed
    if op == '+':
        return f"{left} + {right}"
    elif op == '*':
        return f"{left}*{right}"
    elif op == '^':
        return f"{left}^{right}"
    else:
        raise Exception("Unknown operator")

def show(expr):
    # Helper to pretty-print results
    print(f"{expr}  ->  {differentiate(expr, 'x')}")
    print(f"{to_string(expr)}  ->  {to_string(differentiate(expr, 'x'))}")
    print()


# d/dx (x + x)
show(["x", "+", "x"])     # förväntat: [1, '+', 1]

# d/dx (x + 5)
show(["x", "+", 5])       # förväntat: [1, '+', 0]

# d/dx (x * x)
show(["x", "*", "x"])
# förväntat: [[x, '*', 1], '+', [1, '*', x]]

# d/dx (x * 5)
show(["x", "*", 5])
# förväntat: [[x, '*', 0], '+', [1, '*', 5]]

# d/dx ( (x * x) + x )
show([[ "x", "*", "x"], "+", "x"])

# d/dx ( (x + 2) * (x + 3) )
show([[ "x", "+", 2], "*", ["x", "+", 3]])

# x^2
show(["x", "^", 2])
# förväntat: [2, '*', ["x", "^", 1]]

# x^5
show(["x", "^", 5])
# förväntat: [5, '*', ["x", "^", 4]]

# x^(1/2)
show(["x", "^", 0.5])
# förväntat: [0.5, '*', ["x", "^", -0.5]]

# x^(-3)
show(["x", "^", -3])
# förväntat: [-3, '*', ["x", "^", -4]]

# nested: (x^3 + x)
show([["x", "^", 3], "+", "x"])
# förväntat: [[3, '*', ["x", "^", 2]], '+', 1]
 
try:
    differentiate(["x", "-", "x"], "x")
except Exception as e:
    print("Caught error:", e)
# exponent där bas ≠ x (ska ge fel)
try:
    show(["y", "^", 2])
except Exception as e:
    print("Caught error:", e)

# ✔ Förklaring
    # Testerna täcker:
    # Derivat av variabel
    # Derivat av konstant
    # Derivat av annan variabel
    # Addition
    # Produktregel
    # Nästlade uttryck
    # Felhantering

# def differentiate(expr, var):
#     if is_constant(expr):
#         return make_constant(0)

#     elif is_variable(expr):
#         if same_variable(expr, var):
#             return make_constant(1)
#         else:
#             return make_constant(0)

#     elif is_sum(expr):
#         return make_sum(differentiate(arg1(expr), var),
#                         differentiate(arg2(expr), var))

#     elif is_product(expr):
#         return make_sum(
#             make_product(arg1(expr), differentiate(arg2(expr), var)),
#             make_product(differentiate(arg1(expr), var), arg2(expr))
#         )
#     else:
#         raise Exception("Invalid expression!")
