from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=10000),hist=False)
plt.show()