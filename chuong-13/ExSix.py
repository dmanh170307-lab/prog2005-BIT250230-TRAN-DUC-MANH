def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
mang = [29, 10, 14, 37, 13]
print(f"Mảng sau khi sắp xếp: {selection_sort(mang)}")