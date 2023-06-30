'''zipf distribution are used  to sample data based on zipf's law. It has two parameters a(distribution parameter),size(shape of the returned array)'''
#zipf's law In a collection , the nth common term is 1/n times of the most common term
from numpy import random
x = random.zipf(a=2, size=(2,3))
print(x) 
import matplotlib.pyplot as plt
import seaborn as sns
l = random.zipf(a=2,size=1000)
sns.distplot(l[l<10],kde=False)
plt.show()