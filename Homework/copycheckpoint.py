import time

myArr = [12,34,5,678,90,9,876,543]

def selection_sort(arr):
    comparisons = 0
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    execution_time = (time.time() - start_time) * 1e9
    return arr, comparisons, execution_time

print(selection_sort(myArr))
            

