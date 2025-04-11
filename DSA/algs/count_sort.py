def counting_sort(lst):
    """function which implements counting sort

    Args:
        lst: list which will be sorted

    Returns:
        out_lst: sorted output list
    """
    if len(lst) <= 1:
        return lst
    
    peek = max(lst)
    count_lst = [0] * (peek + 1)

    for index in lst:
        count_lst[index] += 1
    
    out_lst = []
    for index in range(len(count_lst)):
        out_lst.extend([index] * count_lst[index])
    
    return out_lst

 
   # if list is empty or has one element, return itself 
    
    # find the largest element
    # and create the counting list

    
    # fill the counting list with frequency of each number

    
    # create the sorted output list   


## This input required for testing
# If you want to test you code you can enter data in the following format:
# 1 2 3 4 5
list1 = [int(x) for x in input("Unsorted List: ").split()]

sorted_list = counting_sort(list1)
print(f"Sorted List: {sorted_list}")
