import matplotlib.pyplot as plt
import numpy as np
tea = np.random.normal(10,50,100)
plt.hist(tea,color='green')
plt.show()
circle = np.array([5,2,9])
label = ["man united","arsenal", "man city"]
favour = ["black","red","grey"]#To se color we use color parameter
plt.pie(circle, labels=label, colors=favour,shadow=True)#To add a shadow to the pie chart use set shadow parameter to True
plt.legend()#It is used to display a key
plt.show()

films = np.array([2.0,6.5,1.4])
title = ['movies','series','animation']
my = [0.1,0.2,0.1]
plt.pie(films, labels=title, startangle=90,explode=my)
plt.show()
'''Maybe you want one of the wedges to stand out you can use "explode" parameter whcih specifies how far from the center each wedge is displayed'''
