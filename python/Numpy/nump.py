#Numpy is a python library  which is used for working with arrays .Numpy is a shor for Numerical python
import numpy as np
#numpy is usually imported under the np alias "alias are an alternate name for referring to the same thing"
'''The array object in Numpy is called "ndarray" .we can create a numpy ndarray object using the array()'''
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
for r in arr:
    print(r)
'''Why use Numpy ? PYTHON we have list that serve the purpose of arrays but they are slow to process so the NUMPY  aims to providr an array object that us up to 50* faster than the traditional python list
arrays are very frequently used in data science where speed and resource are very important'''
#a dimension in arrays in one level of array depth 
# 0-d ARRAYS each value in an array is a 0-D array as shown below
print("below is the single 0-D array")
arr0 = np.array(33)
print(arr0)
# A 1-D arrays are like the first example above which is the most common and basic arrays.
# A 2-D arrays are used often to represent matrix or 2nd order tensors
print("below is the 2-D array")
arr2 = np.array([[1,2,3], [3,4,6]])
for d in arr2:
    print(d)
#3-D arrays often represent a 3rd order tensor
print("Below is a 3-D arrays that is used often to represent a 3rd order tensor")
arr3 = np.array([[[4,6,7],[1,5,0]],[[5,8,9],[3,2,5]],[[6,3,8],[4,7,3]]])
for d in arr3:
    print(d)
#numpy arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have
print("let see how many dimensions does arr3 have ",arr3.ndim)
# IT appears someone can specify the number of dimension by using ndmin when declaring array
arr4 = np.array([[[2,3],[3,3]],[[4,3],[3,5]],[[3,6],[6,4]],[[4,5],[3,4]]], ndmin=3)
print(arr4.ndim)
'''I get it now the ndmin argument is used to specific the minimum number of dimension tha an array should have'''
    