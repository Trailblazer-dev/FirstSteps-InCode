'''Draw a line in a diagram from position (1,3) to (2,8) then to (6,1) and finally to position (8,10)'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,6,8])
y = np.array([3,8,1,10])
plt.plot(x, y, 'o:r') # the first specifies the marker the colon specifies the line should be dotted the last is color
plt.show()
#You can use the keyword argument "marker" to emphasize each point with a specified marker
buttons = np.array([0,4,8,15])
holes = np.array([1,2, 6,12])
plt.plot(buttons, holes, marker = 'o', ms = 30,mec = 'y', mfc ='g' )#it is also possible to specify the marker size, mec ser edge color,
plt.show()
# you can choose various ways which to mark the point of ur graph i.e 'x','+','s'...
''' you can also choose if the line should be continuoes or dotted solid line "_" dotted line ":" dashed line "__"'''
