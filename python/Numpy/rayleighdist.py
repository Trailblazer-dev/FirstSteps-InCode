'''Rayleigh distribution is used in signal processing; it has two parameters: scale,size'''
from numpy import random 
w = random.rayleigh(scale=2, size=(2,4))
print(w)
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.rayleigh(scale=2, size=1000), hist=False)
plt.show()
#NOTE the similarity between Rayleigh and Chi Square distribution at stddev and 2 degree of freedom rayleigh and chi sqaure represent the same distributions
