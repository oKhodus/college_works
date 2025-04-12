# Replace ___ with your code

def insertion_sort(lst, interval):
    for i in range(interval, len(lst)):
        key = lst[i]            
        j = i - interval          
        while j >= 0 and key < lst[j]:
            lst[j + interval] = lst[j]
            j = j - interval    
        lst[j + interval] = key

def shell_sort(n):
    # write your code here
    base_interval = n // 2
    while base_interval > 0:
        insertion_sort(lst, base_interval)
        base_interval //= 2



## This input required for testing
# If you want to test you code you can enter data in the following format:
# 1 2 3 4 5
lst = list(map(int, input().split()))
size = len(lst)

# function call
shell_sort(size)
print(lst)