#%%
def prod_sum(vals: list) -> tuple:
    if not vals:
        return (1, 0.0)
    curr = vals[0]
    rest = vals[1:]

    calc_rest = prod_sum(rest)

    if isinstance(curr, int):
        return (curr * calc_rest[0], calc_rest[1])
    else:
        return (calc_rest[0], curr[1] * calc_rest[1])

if __name__ == "__main__":
    print(prod_sum([1,1,1]))
#%%
