import matplotlib.pyplot as plt
import numpy as np
d =np.array(["Monday","Tuesday","Wenesday","Thursday","Friday"])
h = np.array([1.3,2.0,1.5,2.5,0.5])
font = {'family':'eufm10','color':'orange','size': 12}
font1 = {'family':'eufm10','color':'red','size':15}
plt.bar(d,h, color="purple")# to display horizontal bars just use barh in place of plt.bar
plt.xlabel("coding days",fontdict=font)
plt.ylabel("coding hours", fontdict=font1)
plt.title("time spent well")
plt.show()