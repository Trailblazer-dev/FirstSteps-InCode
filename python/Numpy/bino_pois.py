'''Binomial distribution only has two possible outcomes whereas poisson distribution can have unlimited possible outcomes'''
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=1000, p=0.01, size=1000),hist=False,kde_kws={'label':'binomial'})
sns.distplot(random.poisson(lam=10, size=1000), hist=False, kde_kws= {'label':'poisson'})
plt.legend()
plt.show()