arr = [5, 2, 9, 1, 5, 6]
print(arr)
def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"Меняем {arr[j]} с {arr[j + 1]}\n")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
                print(f"Проходка {count}-ая: {arr}\n")
    return f"\nFinal result:\n{arr}"

print(bubble_sort(arr))
