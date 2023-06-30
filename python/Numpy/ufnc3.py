'''There is difference between addition and summation. Summation is the overall addition'''
import numpy as np
a = np.array([2,4,6])
b = np.array([8,7,2])
c = np.sum([a,b])
print(">>>",c)# There it will output a number not an array
d = np.sum([a,b], axis=1)
print(">>",d)#when you specify axis it will find the summation of each arrays
i = np.array([8,4,2,2])#This is a cummulative summation which start from left to right
j = np.cumsum([i])
print(j)
'''Let check about product'''
pro = np.prod([a,b])
print(">", pro) #It act as summation but it is like product summation
pro1 = np.prod([a,b], axis=1)
print(">", pro1)
#cumprod it like cumsum the only difference is the multiplication
print(np.cumprod([a,b]))
#Let check to the opposite of summation which is discrete difference
print(np.diff([a])) # i.e (4-2,6-4)
