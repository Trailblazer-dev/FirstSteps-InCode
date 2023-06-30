import numpy as np
D3 = np.array([[[2,3,5],[3,8,9]],[[3,4,5],[1,4,8]]])
for c in np.nditer(D3):
    print(c,">>next")
'''We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating
Numpy does not change the data type of the elements in-place(where the elements is in array ) so it needs some other space to perform this action,that extra space is called buffer, and in order to enable it in nditer() we pass flags =['buffered']
l'''
details = np.array([[[902,20,22],[300, 321, 292]],[[23, 32, 92],[31,39,121]]])
for n in np.nditer(details, flags=['buffered'], op_dtypes=['S']):
    print(n)
'''Enumeration means mentioning sequence number of somethings one by one
Sometimes we require corresponding index of the elements while iterating the ndenumerate() method can be used for those usecases'''
print("Enumeration")
arr = np.array([2,4,7])
for no, c in np.ndenumerate(arr):
    print(no,c)
'''In SQL we join tables based on a key , whereas in Numpy we join arrays by axes. We pass a sequence of arrays that we want join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0'''
print("Join")
com = np.concatenate([D3, details], axis=1)# in concatenate the arrays must have the same number of dimension
print(com)