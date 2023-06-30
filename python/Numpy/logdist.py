'''Logistic Distribution is used to describe growth. It is used extensively in machine learning in logistic regression, neural networks etc
loc-(mean,where the peak is . Default 0),scale-(standard deviation, the flatness of distribution. Default 1),size-(The shape of the returned array)'''
from numpy import random
x = random.logistic(loc=1, scale= 2, size=(2,3))
print(x)