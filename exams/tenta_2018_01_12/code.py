#%%
###Uppgift 2

def odd_i(seq: list) -> list:
    lst = []
    for num in seq:
        if num % 2 == 1:
            lst.append(num)
    return lst

def odd_r(seq: list) -> list:
    if not seq:
        return []
    if seq[0] % 2 == 1:
        return [seq[0]] + odd_r(seq[1:])
    return odd_r(seq[1:])


###Uppgift 3
def partition(seq: list) -> dict:
    dct = {}
    for ele in seq:
        key = len(ele)
        print(f"len: {key}")
        dct[key] = dct.get(key, []) + [ele]
    return dct

if __name__ == '__main__':
    #print(odd_r([1, 2, 3, 4, 5]))
    #print(odd_i([2, 4, 6]))
    #print(partition(['a', 'aa', 'b', 'ccc', 'dd']))
    print(partition(['a', ['aa', ['b'], ['ccc', 'dd']]]))
#%%
