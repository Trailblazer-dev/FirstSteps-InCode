from numpy import random
'''Normal distribution is one of the most important distributions .It fits the probability distribution of many events
it has 3 parameters: i.e loc :>>(mean, where the peak of the bell exists), scale(standard Deviation, how the flat graph distribution should be),
size(The shape of the returned array)'''
s = random.normal(loc=1,scale=2,size=(2,3))
print(s)
