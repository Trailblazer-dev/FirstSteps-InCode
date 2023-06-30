'''Normal distribution is continueus whereas poisson is discrete But we cans see that similar to binomial for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean'''
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50, scale=7, size=1000),hist=False,label='normal')
sns.distplot(random.poisson(lam= 50, size=1000),hist=False,label='poisson')
plt.legend()
plt.show()