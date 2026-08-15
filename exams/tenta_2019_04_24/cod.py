#%%

#Uppgift 1

def sum_nth(seq):
    """1"""
    if not seq:
        return 0
    

#Uppgift 2

def merge_x_i(s1: list, s2: list) -> list:
    """!"""
    if not s1 or not s2:
        return s1 or s2

    result = []
    i, j, = 0, 0
    lngth1, lngth2 = len(s1), len(s2)
    while len(result) < lngth1 + lngth2:
        if s1[i] < s2[j]:
            result.append(s1[i])
            i += 1
        else:
            result.append(s2[j])
            j += 1
        if i == lngth1 or j == lngth2:
            result += s1[i:] or s2[j:]
            break
    return result


if __name__ == '__main__':
    print(merge_x_i([1, 2, 8, 22], [3, 5, 21]))
#%%
