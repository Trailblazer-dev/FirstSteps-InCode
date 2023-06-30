'''Numpy provide functions to perfom log at the base 1,e and 10'''
#Log at Base 2
import numpy as np
h = np.arange(1,10)
print(np.log2(h))
# log at base 10
l = np.arange(1,10)
print(">>",np.log10(l))
#Natural log or log at base e
print(">>>",np.log(l))
#NOTE
'''Numpy does not provide any function to take log at any base , so we can use the frompyfunc() function along with inbuilt function math.log() '''
from math import log
npl = np.frompyfunc(log,2,1)
print(">>>>",npl(100,16))