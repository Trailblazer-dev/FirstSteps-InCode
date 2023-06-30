'''Chi Square distribution is used as a basis to verify the hypothesis. It has two parameters:
df(degree of freedom),size(shape of the returned array)'''
from numpy import random
x = random.chisquare(df=2, size=(2,3))
print(x)
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()