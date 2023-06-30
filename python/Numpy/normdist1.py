from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=3,scale=1,size=(2,3)),hist=False)
plt.show()