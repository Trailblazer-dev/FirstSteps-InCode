import numpy as np
'''stacking is same as concatenation the only difference is that stacking is done along a new axis'''
first = np.array([2,3,5])
second = np.array([3,9,3])
con = np.stack([first,second], axis=1)# if the x is not explicitly passed it is taken as 0 which the result is putting them one over the other
print(con)
print(">> stacking along Rows")
conR = np.hstack([first, second])
print(conR)
print(">> Stacking along Columns")
conC = np.vstack([first, second])
print(conC)
print(">> stacking along Height(depth)")
conH = np.dstack([first, second])
print(conH)