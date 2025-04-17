# Replace ___ with your code

def count_occurrences(lst, n):
    return sum(1 for elem in lst if elem == n)

    # count = 0
    # for elem in lst:
    #     if elem == n:
    #         count += 1
    # return count

lst = [3, 3, 4, 5, 6, 6, 6, 2]

# take integer input
n = int(input())

# call count_occurrences() to
# count the number of occurrences of n
count = count_occurrences(lst, n)

print(count)