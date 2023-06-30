'''Probability is set by number between 0 and 1, where 0 mean the value will never occur and 1 mean the value will occur many times'''
from numpy import random
cat = random.choice([4,5,1,0,7], p=[0.3,0.2,0.1,0.0,0.4], size=(2,3))# NOTE the some of the probability should be 1
print(cat)
length = len(cat)
print("length:",length)
'''Permutation refer to an arrangement of elements e.g[3,2,1] is a permutation of [1,2,3]
numpy has two module for this : shuffle() and permutation() '''
import numpy as np
arr = np.array([2,4,6,9,10])
random.shuffle(arr)
print(arr)# NOTE shuffle() method makes changes to the original array
print(">>",random.permutation(arr))# NOTE permutation() methos returns a re-arranged array and leaves the original array un-changed
