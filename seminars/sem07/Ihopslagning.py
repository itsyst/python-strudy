def merge_sorted_lists(list1, list2):
    """
    Slår ihop två sorterade listor till en sorterad lista.
    Om listorna inte är sorterade, sorteras de först.
    """
    # Sortera listorna först
    list1 = sorted(list1)
    list2 = sorted(list2)
    
    result = []
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Lägg till återstående element från list1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    
    # Lägg till återstående element från list2
    while j < len(list2):
        result.append(list2[j])
        j += 1
    
    return result


if __name__ == "__main__":
    merge1 = merge_sorted_lists([10, 3, 5], [2, 4, 6])
    merge2 = merge_sorted_lists([1, 11, 3], [4, 5, 6])
    merge3 = merge_sorted_lists([8, 7, 9], [2, 3, 4])
    print(f"{merge1}\n{merge2}\n{merge3}")
 
# [2, 3, 4, 5, 6, 10]
# [1, 3, 4, 5, 6, 11]
# [2, 3, 4, 7, 8, 9]
