#Difference between logisticc and normal distribution
'''Both distribution are near identical, but logistic distribution has more area under the tails,meaning it represents more possibility of occurence of an event further away from the mean
For higher value of scale the normal and logistic distribution are near identical apart from the peak'''
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(scale=2, size=1000), hist=False, kde_kws={'label':'normal'})
sns.distplot(random.logistic(size=1000),hist=False,kde_kws={'label':'logistic'})
plt.legend()
plt.show()