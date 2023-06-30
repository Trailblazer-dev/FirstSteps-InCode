import matplotlib.pyplot as plt
import numpy as np
items = np.array([3,5,2])
tools = np.array([1,6,0])
plt.subplot(3,2,1)
plt.plot(items, tools)
plt.xlabel("items")
plt.ylabel("tools")
plt.title("Equipment")


items = np.array([2,4,7])
tools = np.array([4,6,7])
plt.subplot(3,2,2)
plt.plot(items,tools)
plt.xlabel("items")
plt.ylabel("tools")
plt.title("Equibment 2")


items = np.array([2,3,9])
tools = np.array([1,3,13])
plt.subplot(3,2,3)
plt.plot(items,tools)
plt.xlabel("items")
plt.ylabel("tools")
plt.title("Equipment 3")


items = np.array([7,11,14])
tools = np.array([8,12,16])
plt.subplot(3,2,4)
plt.plot(items, tools)
plt.xlabel("items")
plt.ylabel("tools")
plt.title("Equipment 4")
# this one is for scattered points also someone can increase a color map 

items = np.array([2,4,5])
tools = np.array([7,8,9])
color = np.array([1,5,10])
plt.subplot(3,2,5)
plt.scatter(items, tools, c=color, cmap='viridis')
plt.colorbar()
 
items = np.array([3,4,5])
tools = np.array([4,5,6])
plt.subplot(3,2,6)
plt.plot(items, tools)


plt.tight_layout()
plt.show()