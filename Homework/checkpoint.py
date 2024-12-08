import time

# Hàm nhập dữ liệu
def input_data():
    n = int(input("Nhập số lượng chuỗi (1 ≤ n ≤ 50): "))
    if not (1 <= n <= 50):
        raise ValueError("Số lượng chuỗi phải nằm trong khoảng 1 ≤ n ≤ 50.")
    print(f"Nhập {n} chuỗi:")
    data = [input(f"Chuỗi {i + 1}: ")[:20] for i in range(n)]
    return data

# Thuật toán Selection Sort
def selection_sort(arr):
    comparisons = 0
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    execution_time = time.time() - start_time
    return arr, comparisons, execution_time

# Thuật toán Insertion Sort
def insertion_sort(arr):
    comparisons = 0
    start_time = time.time()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    execution_time = time.time() - start_time
    return arr, comparisons, execution_time

# Thuật toán Bubble Sort
def bubble_sort(arr):
    comparisons = 0
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    execution_time = time.time() - start_time
    return arr, comparisons, execution_time

# Chương trình chính
def main():
    data = input_data()
    print("\nDữ liệu ban đầu:", data)

    # Thực thi Selection Sort
    selection_sorted, selection_comparisons, selection_time = selection_sort(data[:])
    print("\nSelection Sort:")
    print("Kết quả sắp xếp:", selection_sorted)
    print(f"Số lần so sánh: {selection_comparisons}, Thời gian thực thi: {selection_time:.6f} giây")

    # Thực thi Insertion Sort
    insertion_sorted, insertion_comparisons, insertion_time = insertion_sort(data[:])
    print("\nInsertion Sort:")
    print("Kết quả sắp xếp:", insertion_sorted)
    print(f"Số lần so sánh: {insertion_comparisons}, Thời gian thực thi: {insertion_time:.6f} giây")

    # Thực thi Bubble Sort
    bubble_sorted, bubble_comparisons, bubble_time = bubble_sort(data[:])
    print("\nBubble Sort:")
    print("Kết quả sắp xếp:", bubble_sorted)
    print(f"Số lần so sánh: {bubble_comparisons}, Thời gian thực thi: {bubble_time:.6f} giây")

    # So sánh hiệu suất
    print("\nSo sánh hiệu suất:")
    print(f"Selection Sort: {selection_comparisons} comparisons, {selection_time:.6f} seconds")
    print(f"Insertion Sort: {insertion_comparisons} comparisons, {insertion_time:.6f} seconds")
    print(f"Bubble Sort: {bubble_comparisons} comparisons, {bubble_time:.6f} seconds")

    # Nhận xét
    print("\nNhận xét:")
    if min(selection_time, insertion_time, bubble_time) == selection_time:
        print("Selection Sort hiệu quả nhất về thời gian.")
    elif min(selection_time, insertion_time, bubble_time) == insertion_time:
        print("Insertion Sort hiệu quả nhất về thời gian.")
    else:
        print("Bubble Sort hiệu quả nhất về thời gian.")

# Chạy chương trình
if __name__ == "__main__":
    main()
