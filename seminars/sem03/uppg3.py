"""Multiple apply uppg"""
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "last_expr" #all
#%%
def multiple_apply(func, times):
    """Applies inputted function multiple times to variable"""
    def inner(val):
        for _ in range(times):
            val = func(val)
        return val
    return inner

#def multiple_apply_rec(func, times):
#    """Applies inputted function multiple times to variable
#    recursively"""
#    amount = times
#    def inner(val):
#        if amount == 0:
#            return None
#        amount = amount - 1
#        return func(val) + inner(val)

if __name__ == '__main__':
    add_three = lambda n: n + 3
    add_three_twice = multiple_apply(add_three, 2)
    #print(add_three(1))
    print(add_three_twice(5))
    #11

    yell = lambda s: s+ "!"
    yell("hej")
    YELL = multiple_apply(yell, 5)
    print(YELL("hej"))
    #"hej!!!!!"

    pow2mult = lambda n, c: c * multiple_apply(lambda n: 2**n, 1)(n)
    print(pow2mult(3, 1))
#%%
