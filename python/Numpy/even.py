'''This is a program that will only return even number from original array'''
import numpy as np
month = np.array([30,28,31,30,31,30,31,31,30,31,30,31])
filt = []
for loop in month:
    if loop % 2 == 0:
        filt.append(True)
    else:
        filt.append(False)
new = month[filt]
print(">>output:", new)
print(">>filt:", filt)