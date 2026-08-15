#%%

#Uppgift 2 #skit dålig lösning

def pairwise_add_r(seq1, seq2):
    if not seq1 and not seq2:
        return []
    if seq1 and not seq2:
        return [seq1[0]] + pairwise_add_r(seq1[1:], [])
    if not seq1 and seq2:
        return [seq2[0]] + pairwise_add_r([], seq2[1:])
    return [seq1[0] + seq2[0]] + pairwise_add_r(seq1[1:], seq2[1:])

def pairwise_add_i(seq1: list, seq2: list) -> list:
    newlist = []
    lngth1 = len(seq1)
    lngth2 = len(seq2)
    ind = seq1
    if lngth1 > lngth2 or lngth1 == lngth2:
        ind = seq2
    lngth_ind = len(ind)
    for i in range(lngth_ind):
        newlist.append(seq1[i] + seq2[i])
    start = 0
    more = False
    if lngth_ind > lngth1:
        start = seq2
        more = True
    elif lngth_ind > lngth2:
        start = seq1
        more = True
    if more:
        for i in range(len(start), lngth_ind):
            newlist.append(start[i])
    return newlist

###Uppgift 1
def score_i(pins: list) -> int:
    """Given a list of bowling throws, function returns the calculated score"""
    result = 0
    mult = 0
    prev = 0
    for throw in enumerate(pins):
        add = throw[1]
        if throw[1] == 10:
            mult += 2
        elif prev + add == 10:
            mult += 1
        if mult > 0:
            add += add + 10
            mult -= 1
        result += add
        prev = throw[1]
    return result


if __name__ == '__main__':
    #print(pairwise_add_i([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
    #print(pairwise_add_i([2, 4, 6], [1, 3]))
    #print(score_i([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    #print(score_i([6, 2, 8, 2, 10, 9, 0, 6, 4, 8, 1, 9, 1, 10, 10, 8, 2, 7]))
    print(score_i([1, 3, 3, 6, 2, 5, 9, 0, 0, 5, 0, 0, 4, 5, 5, 3, 1, 8, 7, 2]))
    pass
#%%
