#The area of a triangle is 1/2 *l*w
l = int(input("Enter the lenth of triangle\n"))
w = int(input("Enter the w of triangle\n"))
area = 1/2*l*w
print("The area of a triangle with measurement of {} and {} is ".format\
    (l,w), area)
#There is alternative way of getting the area of triangle which is s=a+b+c = sqrt{(s-a)*(s-b)*(s-c)}
a = int(input("Enter the length of a side of the triangle\n"))
b = int(input("Enter the length of b side of the triangle\n"))
c = int(input("Enter the length of c side of the triangle\n"))
import math
s = a+b+c
area2 = math.sqrt((s-a)*(s-b)*(s-c))#**0.5 will still give the same number
print("The area of the triangle is ",area2)