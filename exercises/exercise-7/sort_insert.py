def insertion_sort_copy(seq):
    """ Sorts a list using insertion sort. """
    res = []
    for e in seq:
        i = 0
        while i < len(res) and res[i] < e:
            i += 1
        res.insert(i, e)
    return res

def insertion_sort_inplace(seq):
    """ Sorts a list using insertion sort. """
    for i in range(1, len(seq)):
        item = seq[i]
        hole = i
        while hole > 0 and seq[hole-1] > item:
            seq[hole] = seq[hole-1]
            hole -= 1
        seq[hole] = item
    return seq

numbers = [1,2,3,8, -3,-1,0,0,99 ]
sorted = insertion_sort_copy(numbers)
print(sorted)
