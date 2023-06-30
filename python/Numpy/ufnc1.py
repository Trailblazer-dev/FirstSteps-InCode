'''All of the discussed arithmetic functions take a where parameter in which we can specify that condition
'''
import  numpy as np
#Addition
a = np.array([3,4,21,8])
b = np.array([12,9,2,9])
sum = np.add(a,b)
print(">>sum is: ", sum)
#Subtraction
sub = np.subtract(a,b)
print(">> substraction is : ", sub)
#Multiplication
mult = np.multiply(a,b)
print(">>> multiplication: ", mult)
# division
div = np.divide(a,b)
print(">> division is: ",div)
#Power
'''power() function rises the values from the 1st array to the power of the values of the 2nd arary '''
p = np.power(a,b)
print(">> power is: ",p)
#Remainder
'''Both the mod() and the remainder() functions return the remainder '''
rem = np.mod(a,b)
print(">>remainder is :", rem)
#Quotient and mod
'''divmod() returns both the quotient and the mod'''
di = np.divmod(a,b)
print("...Lemme see..",di)#the first array contains quotient and second is mod
#Absolute values
'''Both absolute() and the abs() funtion do the same but we should use absolute() to avoid confusion with python inbuilt math.abs()'''
arr = np.array([-1,-2,1,3,-2])
av = np.absolute(arr)
print("<?>",av)