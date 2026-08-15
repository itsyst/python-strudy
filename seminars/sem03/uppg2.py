#%%
def minpos_maxneg(seq: list) -> tuple: #minsta positiva, största negativa
    if not seq:
        return (None, None) # None?
    curr = seq[0]
    rest = seq[1:]
    #print(seq[1:])
    #print(rest)

    calc_rest = minpos_maxneg(rest)

    cur_min = calc_rest[0]
    cur_max = calc_rest[1]

    print(f"calc_rest[0]: {calc_rest[0]}")
    print(f"calc_rest[1]: {calc_rest[1]}")


    if curr > 0:
        if cur_min is None or curr < cur_min:
            cur_min = curr
    elif curr < 0:
        if cur_max is None or curr > cur_max:
            cur_max = curr
    return (cur_min, cur_max)

if __name__ == "__main__":
    print(minpos_maxneg([2,3,1,5, -2, -9]))
#%%