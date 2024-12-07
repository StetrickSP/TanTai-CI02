#list_4 = [23,4567,84,56,543,4,567]
#list_4.sort(reverse=True)
#print(list_4)

#set_5 = set("abcdef")

#set_5.add("MindX")
#print(set_5)

import numpy as np
#x = int(input("Enter number of the starting point of the range you want for the first list: (from) "))
#y = int(input("Enter number of the ending point of the range you want for the first list: (to) "))
#n = int(input("Enter number of numbers you want for the first list: "))
#a = int(input("Enter number of the starting point of the range you want for the second list: (from) "))
#b = int(input("Enter number of the ending point of the range you want for the second list: (to) "))
#m = int(input("Enter number of numbers you want for the second list: "))
#arr1 = np.random.randint(x,y,n).tolist()
#arr2 = np.random.randint(a,b,m).tolist()
#for i in arr2:
  #  arr1.append(i)
#arr1.sort(reverse=True)
#print(arr1)
x = int(input("Day se la mot list number random, xin hay nhap so phan tu cua list: "))
list1 = np.random.randint(0,1000,x).tolist()
print(max(list1))
print(min(list1))
print(sum(list1) / len(list1))