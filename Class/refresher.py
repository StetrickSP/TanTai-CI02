#list_4 = [23,4567,84,56,543,4,567]
#list_4.sort(reverse=True)
#print(list_4)

#set_5 = set("abcdef")

#set_5.add("MindX")
#print(set_5)

# import numpy as np
# #x = int(input("Enter number of the starting point of the range you want for the first list: (from) "))
# #y = int(input("Enter number of the ending point of the range you want for the first list: (to) "))
# #n = int(input("Enter number of numbers you want for the first list: "))
# #a = int(input("Enter number of the starting point of the range you want for the second list: (from) "))
# #b = int(input("Enter number of the ending point of the range you want for the second list: (to) "))
# #m = int(input("Enter number of numbers you want for the second list: "))
# #arr1 = np.random.randint(x,y,n).tolist()
# #arr2 = np.random.randint(a,b,m).tolist()
# #for i in arr2:
#   #  arr1.append(i)
# #arr1.sort(reverse=True)
# #print(arr1)
# x = int(input("Day se la mot list number random, xin hay nhap so phan tu cua list: "))
# list1 = np.random.randint(0,1000,x).tolist()
# print(max(list1))
# print(min(list1))
# print(sum(list1) / len(list1))

import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 5  # Amplitude in cm
T = 2  # Period in seconds
omega = 2 * np.pi / T  # Angular frequency

# Time array
t = np.linspace(0, 4, 500)  # Time from 0 to 4 seconds
x = A * np.sin(omega * t)  # Displacement function

# Plot
plt.figure(figsize=(8, 4))
plt.plot(t, x, label=r'$x(t) = 5 \sin(\pi t)$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8)
plt.title("Simple Harmonic Motion: Displacement vs. Time", fontsize=14)
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Displacement (cm)", fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.4)
plt.show()
