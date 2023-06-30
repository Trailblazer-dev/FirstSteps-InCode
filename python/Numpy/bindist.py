'''Binomial distribution is a Discrete distribution it describes the outcome of binary scenarios.It has three parameters
n(number of trials),p(probability of occurence of each trial), size(shape pf the returned array)'''
from numpy import random
x = random.binomial(n=10, p=0.5, size=10)
print(x)