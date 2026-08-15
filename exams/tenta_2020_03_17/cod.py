#%%
"""Uppgift 2"""
def by_sensor_r1(seq: list) -> dict:
    def inner(lst, key, seq1, done):
        #print("f")
        if not seq1:
            if len(lst) > 0:
                return lst
            return {}
        curr = seq1[0]
        if curr[0] in done:
            return inner([], seq1[1][0], seq1[1:], done)
        else:
            if key == curr[0]:
                if len(lst) > 0:
                    return inner(lst + [curr[1]], key, seq1[1:], done) #| inner([], seq1[1][0], seq1[1:])
                else:
                    first = {key: inner(lst + [curr[1]], key, seq1[1:], done)}
                    print('first: ', first)
                    #print(seq1[1])
                    if seq1[1:]:
                        return first | inner([], seq1[1][0], seq1[1:], done.union({key}))
                    else:
                        return first
            if len(lst) > 0:
                return inner(lst, key, seq1[1:], done)
        return inner([], seq1[0][0], seq1[1:], done) #| inner([], seq1[1][0], seq1[1:], done)
    return inner([], seq[0][0], seq, set())

def by_sensor_r(seq: list) -> dict:
    def inner(dct, seq1):
        if not seq1:
            return dct
        curr = seq1[0]
        if curr[0] in dct:
            return inner(dct | {curr[0]: dct[curr[0]] + [curr[1]]}, seq1[1:]) #| inner(dct, seq1[1:])
        else:
            return inner(dct | {curr[0]: [curr[1]]}, seq1[1:])
    return inner({}, seq)


if __name__ == '__main__':
    #print(by_sensor_r([('a', -1), ('a', 1)]))
    print(by_sensor_r([('a', 2), ('b', 0), ('a', 6), ('c', 0), ('b', 1)]))
#%%
