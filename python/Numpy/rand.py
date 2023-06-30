from numpy import random
c = random.randint(8)
print(c)#This with generate a random number starting from 0 to 5
d = random.randint(10000)
print(d)
print("Let check float")
z = random.rand()#rand() return a random float btwn 0 and 1
print(z)
'''These is how we generate a 1D array'''
arr = random.randint(30, size=(8))
print(arr)
#to create a 3D or 2D we specific in size the number of rows and columns
a = random.randint(50, size=(2,4))
print(a)
space = []
for z in space:
    print(">>>>")
f = random.rand(2,5)
print(f)
'''choice() method allows someone to generate a random value based on an array of values'''
real = random.choice([6207,4126,0000,3196])
print(">>>",real)
# when you add size parameter to choice you create an array with the given values
g = random.choice([3,8,7,4], size=(2,3))
print("<<<", g)