'''Poisson distribution is a Discrete distribution.It estimates how many times an event can happen in specified time e.g if someone eats twice a day wht is the probability he will eat thrice?
It has two parameters: lam(rate or known number of occurences ),size(the shape of the returned array)'''
from numpy import random
x = random.poisson(lam=2,size=10)
print(x)