'''Multinormial distribution is a generalization of binomial distribution.
It describes outcomes of multi-nomial scenarios like for Blood type of a population, dice roll outcome:It has three parameters:n(number of possible outcomes),pvals(list of probabilities of outcomes),size(The shape of the returned array)'''
#Below is an example of a dice
from numpy import random
c = random.multinomial(n=6, pvals=(1/6,1/6,1/6,1/6,1/6,1/6))
print(c)
#NOTE multinomial samples will NOT produce a single value They will produce one value for each pval
