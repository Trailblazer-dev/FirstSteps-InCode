#NOTE last we are dealing with sets
import numpy as np
arr = np.array([1,1,1,2,3,4,4,9])
x = np.unique(arr)
print(x)
#To find the unique values of two arrays, use the union1d() method.
arr1 = np.array([3,3,4,5,6,6,9])
y = np.union1d(arr, arr1)
print(">", y)
#To find only the values that are present in both arrays, use the intersect1d() method
z = np.intersect1d(arr,arr1, assume_unique=True)# Note: the intersect1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.
print(">>",z)
#To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
s =np.setxor1d(arr, arr1)
print(">>>", s)