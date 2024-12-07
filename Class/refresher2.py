def input_array():
  arr = []
  n = int(input("Nhap so phan tu cua mang: "))
  for i in range(n):
    value = int(input(f"Phan tu thu {i+1}: "))
    arr.append(value)
  return arr

def binary_search(arr: list[int], num: int):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left <= right: 
        mid = (left + right) // 2 
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            left = mid + 1
        elif arr[mid] < num:
            right = mid - 1
    return False

a = int(input("Enter target: "))
l = input_array()

print(binary_search(l,a))