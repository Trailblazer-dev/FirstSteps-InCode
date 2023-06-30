'''Ther are primarily five ways of rounding off decimals in Numpy
tuncation,fix,rounding, floor, ceil'''
import numpy as np
#Truncation
fn = np.trunc([-2.2302,3.8023])
#Trunc() or fix() remove the decimals and return the float number closest to zero
print(fn)
#Rounding 
'''around() function increments preceding digit or decimal by 1 if >= 5 else do nothing'''
no = np.around([0.53023,3.9033,3.49032,-2.4343])
print(">> round",no)
#Floor
'''floor() function rounds off decimal to nearest lower integer'''
low = np.floor([-3.6003,2.903,1.2039,-84.303])
print(">>floor, does not roundoff",low)
#ceil
'''ceil() function rounds off decimal to neares upper integer e.g 2.0233 is 3'''
upp = np.ceil([-2.8493,4.02032,8.9237,-3.73])
print(">>pop out",upp)