arr = [5, 2, 9, 1, 5, 6]
# print(arr)
def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # print(f"Меняем {arr[j]} с {arr[j + 1]}\n")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
                # print(f"Проходка {count}-ая: {arr}\n")
    return f"\nFinal result:\n{arr}"

print(bubble_sort(arr))

def insertion_sort(arr):
    for index in range(1, len(arr)):
        inserted = arr[index]
        last_SortedElem = index - 1
        while last_SortedElem >= 0 and arr[last_SortedElem] > inserted:
            arr[last_SortedElem+1] = arr[last_SortedElem]
            last_SortedElem -= 1
        arr[last_SortedElem+1] = inserted
    return f"\nFinal result:\n{arr}"
print(insertion_sort([5, 2, 4, 6, 1, 3]))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1

    res.extend(left[i:])
    res.extend(right[j:])

    return res

print(merge_sort([5, 2, 4, 6, 1, 3]))