'''splitting is reverse operation of Joining'''
import numpy as np
no = np.array([2,3,4,5,67,9,8])
s = np.array_split(no,4)# if the array jas less elements than required it will adjust from the end accordingly
print(s)
'''NOTE we also have method split() available but it will not adjust the elements when elements are less in source array fro  splitting like  array_split()'''
# when you split array your can access the arrays using their index like below
print(s[2])
'''You can search for a certain value and return the indexes that get a match'''
r = np.where(no == 8)
print(r)# it will output the index where the data is found
'''There is a method called searchsorted() which performs a binary search in the array and returns the index where the specified value would be inserted to maintain the search order'''
x = np.searchsorted(no, 9)
print(x)
'''Sorting means putting elements in an ordered sequence'''
aplha = np.array(['A','C','D','B'])
print(np.sort(aplha))