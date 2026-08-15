def combinations(seq):
    if not seq:
        return ()

    if len(seq) == 1:
        #print(seq[0])
        #print("ye: ", [x for x in range(1, seq[0]+1)])
        this = [x for x in range(1, seq[0] + 1)]
        #print('this: ', this)
        return this

    without_first = combinations(seq[1:])
    rest = without_first
    print('rest: ', rest)
    
    with_first = [y for y in range(1, seq[0] + 1)]
    print('with_first: ', with_first)
    print('without_first: ', without_first)
    return set(tuple([x] + [y]) for x in with_first for y in without_first)
    #return with_first.union(without_first)
