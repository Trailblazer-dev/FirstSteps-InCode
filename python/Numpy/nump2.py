import numpy as np
pen = np.array([2,4,6,2,4])
print(pen.dtype)
flash = np.array(["tv","woofer", "router","remote"])
print(flash.dtype)
# The array()function can take various argument like below also someone can specif the size
defeat = np.array([2,4,5,6,7,8], dtype='i4')
print(defeat)
'''The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.'''
dec = np.array([2.43,2.112,5.32,94.3,32.5])
full = dec.astype('i')
print(">>",full)
ful = dec.astype(bool)
print(">", ful)
print(ful.dtype)
foll = ful.astype(float)
#When you convert boolean to float all that were true become 1 and false becone 0
print(">>",foll)
'''The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.'''
may = np.array([3,3,5,6,4,9,0])
dub = may.copy()
rip = may.view()
may[2] = 2
print(may)
print(">>copy", dub)# the copy is not affected by the change of original data
print(">>view", rip) # so it true view is afted by change of original array
rip[0] = 199
print(">>learn",rip)
print("<<", may)# so change in view affects the change the original array
print("<>",dub.base)# base is used to if the array owns the data . As from above comment we have written that copy owns the data thus it will return NONE
print("<>v",rip.base)
socks = np.array([[2,2,4],[9,3,2]])
print(socks.shape)# so shape indicate the number of row and column
wifi = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("let display the shape >",wifi.shape)
pasw = wifi.reshape(4,3)
print(">>reshape :", pasw)
for d in pasw:
    for s in d:
        print(">>:",s)
# There is an altenative when it comes to numpy
for q in np.nditer(wifi):
    print(wifi)
