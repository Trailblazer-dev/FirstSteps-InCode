'''Used to describe probability where every event has equal chances of occuring.It has three parameters:a(lower bound-0.0),b(uppper bound-default 1.0),size(The shape of the returned array)'''
from numpy import random
x = random.uniform(size=(2,3))
print(x)