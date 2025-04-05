from random import choice, randint

list1 = [randint(1, 101) for _ in range(11)]

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = choice(lst)

    less = [x for x in lst if x < pivot]
    eq = [x for x in lst if x == pivot]
    more = [x for x in lst if x > pivot]
    
    return quick_sort(less) + eq + quick_sort(more)

print(f"Unsorted List: {list1}")
sorted_list = quick_sort(list1)
print(f"Sorted List: {sorted_list}")