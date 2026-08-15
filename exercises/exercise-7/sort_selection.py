def selection_sort_copy(seq):
    """ Sorts a list using selection sort. """
    res = []
    while seq:
        e = min(seq)
        res.append(e)
        seq.remove(e)
    return res


numbers1 = [1,4,-4,9,2,4,5,6,9]
sorted1 = selection_sort_copy(numbers1)
print(sorted1)

def selection_sort_inplace(seq):
    """ Sorts a list using selection sort. """
    n = len(seq)
    for bottom in range(n-1):
        minpos = bottom
        for i in range(bottom+1, n):
            if seq[i] < seq[minpos]:
                minpos = i
        seq[bottom], seq[minpos] = seq[minpos], seq[bottom]
    return seq

numbers2 = [1,4,-4,9,2,4,5,6,9]
sorted2 = selection_sort_inplace(numbers2)
print(sorted2)
