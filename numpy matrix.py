Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import numpy as np
>>> a = np.array([[1,2],
...               [3,4]])
>>> b = np.array([[5,6],
...               [7,8]])
>>> print("Matrix A:")
Matrix A:
>>> print(a)
[[1 2]
 [3 4]]
>>> print("\nMatrix B:")

Matrix B:
>>> print(B)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(B)
NameError: name 'B' is not defined. Did you mean: 'b'?
>>> print(b)
[[5 6]
 [7 8]]
>>> addition = a+b
>>> print("\naddition (a + b):")

addition (a + b):
>>> print(addition)
[[ 6  8]
 [10 12]]
>>> multiplication = np.dot(a, b)
>>> print("\n Matrix Multiplicaton (a x b):")

 Matrix Multiplicaton (a x b):
>>> print(multiplication)
[[19 22]
 [43 50]]
>>> transpose_A = np.transpose(A)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    transpose_A = np.transpose(A)
NameError: name 'A' is not defined. Did you mean: 'a'?
>>> transpose_a = np.transpose(a)
>>> print("\ntranspose of matrix a:")

transpose of matrix a:
>>> print(transpose_a)
[[1 3]
 [2 4]]
