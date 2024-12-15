def input_array():
    yourArr = []
    print("Please enter your array.")
    a = int(input("Enter the number of numbers in your array: "))
    for i in range(a):
        c = int(input(f'Enter the number {i+1} of your arr:'))
        yourArr.append(c)
    return yourArr

def input_target():
    yourTarget = int(input("Enter your target: "))
    return yourTarget

def linear_search(arr:list[int], target:int):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1

# print(linear_search(yourArr,point))

######################## Bai 2: Kiem so lann xuat hien

def count_appearances(arr:list):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

# myList = input_array()
# print(count_appearances(myList))

######################## Bai 3: Viết hàm tìm tất cả các vị trí của một phần tử trong danh sách

def count_target(arr:list,target):
    appearances = []
    for i in range(len(arr)):
        if arr[i] == target:
            appearances.append(i)
    return appearances

myList = input_array()
point = input_target()
print(count_target(myList,point))

