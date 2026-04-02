Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> arr = np.array([1, 2, 3, 4, 5, 6])
>>> print("original array:")
original array:
>>> print(arr)
[1 2 3 4 5 6]
>>> reshaped_arr = arr.reshape(2,3)
>>> print("\nReshaped Array (2x3):")

Reshaped Array (2x3):
>>> print(reshaped_arr)
[[1 2 3]
 [4 5 6]]
>>> print("\nFirst Row:", reshaped_arr[0])

First Row: [1 2 3]
>>> print("\n elements at index [1][2]:", reshaped_arr[1][2])

 elements at index [1][2]: 6
>>> total_sum = np.sum(arr)
>>> print("\nSum of all elements:", total_sum)

Sum of all elements: 21
