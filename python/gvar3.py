import matplotlib.pyplot as plt
import numpy as np
'''With the subplot() funtion you can draw multiple plots in one figure'''
x = np.array([1,2,4,6])
y = np.array([2,4,6,7])
plt.subplot(1, 2,1)#subplot()function takes 3 arguments i.e has 1 row,2 columns and this is the first plot
plt.plot(x,y)
plt.title("random data")
#plot 2:
x1 = np.array([0,2,3,4])
y1 = np.array([10,13,16,20])
plt.subplot(1,2,2)# 1 row, 2 column, 2 plot
'''You can draw as  many plots you like on one figure  just describe the number of rows,column and the index of the plot'''
plt.plot(x1,y1)
plt.title("random statistics")
plt.suptitle('DATA')
plt.show()