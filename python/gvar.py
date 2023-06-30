'''you can specific the title of the graph by using the "titl()" function # someone can use xlabel to specific x axis in plot and ylabel for y axis
You can also set  font properties for Title and labesl as show below and even choose position of Title by using loc parameter in title()function'''
import matplotlib.pyplot as plt
import numpy as np
points = np.array([11,21,40,8,0])
scores = np.array([100,78,40,20,55])
font1 = {'family':'serif', 'color':'blue','size':20}
font2 = {'family':'serif', 'color':'darkred','size': 15}
plt.title("Students data", loc= 'center')
plt.xlabel("points",fontdict= font1)
plt.ylabel("scores", fontdict= font2)
plt.plot(points,scores, '*:b')
plt.show()
'''Someone also can add grid lines using the grid() function. You can use the axis parameter in grid funtion to specify which grid line to display i.e grid(axis = 'x'),'y' or 'both' by default is grid dispalys both
Also someone can setline properties for the grid(color='color', linestyle='linestyle',linewidth= number).'''
btc = np.array([0,1000,1500,800,1200])
binance = np.array([0,1100,1700,1000, 1500])
plt.title("Digital currency", loc="center")
plt.xlabel("bitcoin")
plt.ylabel("binance coin")
plt.grid(axis="both",color='red',linestyle='-',linewidth= 1.5)
plt.plot(btc,binance)
plt.show()