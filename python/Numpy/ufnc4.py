#This program will deal with how to get lcm and gcd using numpy
import numpy as np
no1 = 4
n02 = 8
print("Here is the lcm for 4 and 8 :",np.lcm(no1,n02))
print("Here is the gcd for 4 and 8 :", np.gcd(no1, n02))
d = np.array([2,4,6])#in order to get lcm of an array we add reduce to lcm
print("Here is the lcm for an array",np.lcm.reduce(d))
print("Here is the gcd for an array", np.gcd.reduce(d))