'''The main difference is that normal distribution is continuos whereas binomial is discrete'''
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50, scale=5, size=1000),hist=False, label='normal')
sns.distplot(random.binomial(n=100, p= 0.5, size=1000),hist=False,label= 'binomial')
plt.legend()
plt.show()