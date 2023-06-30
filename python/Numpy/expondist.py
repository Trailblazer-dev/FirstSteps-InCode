'''Exponential ditribution is used for describing time till next event e.d failure/succes etc;
It has two parameters: scale(inverse of rate,defaults to 1.0),size(shape of returned array)'''
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()
#NOTE THE RELATION BETWEEN POISSON AND EXPONENTIAL DISTRIBUTION is that poisson distribution deals with number of occurences of an event in a time period  whereas exponential distribution deals with the time between these events
