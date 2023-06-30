#example without using ufunc .we used a python built-in zip() method
w = [1,2,3,4]
o = [3,5,9,8]
p = []
for i, j in zip(w,o):
    p.append(i+j)
print(p)

#with ufunc ,we can use the add() function
import  numpy as np
z = np.add(w,o)
print(">>", z)

'''To create your own ufunc , you have to define a funtion like b4 then you add it to your numpy ufunc library with ther frompyfunc() method
# frompyfunc() takes the following arguments(functio:the name of the function,input:number of input arguments,ouputs:number of output arrays)'''
def root(o,p):
    return o+p
root = np.frompyfunc(root, 2,1)
print(root([3,4,9],[0,2,4]))
#To check the type of a function to check if it is a ufunc or not.A ufunc should return<class'numpy.ufunc'>
print("><",type(np.add))#IT seems the add is a ufunc
'''To test if the funtion is a ufunc in an if statement use numpy.ufunc or np.ufunc'''
if type(np.add) == np.ufunc:
    print("add is an ufunc")
else:
    print("add is not an ufunc")