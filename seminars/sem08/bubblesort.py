def bubble_sort(seq):
    n = len(seq)
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(1, n):
            if seq[i-1] > seq[i]:
                # Swap the elements
                seq[i-1], seq[i] = seq[i], seq[i-1]
                swapped = True


if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(my_list)
    print(my_list)  # Output: [11, 12, 22, 25, 34, 64, 90]