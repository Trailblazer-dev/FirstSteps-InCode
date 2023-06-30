'''Filtering is getting some elements out of an existing and creating a new array out of them '''
import numpy as np
janet = np.array([32,84,34,21])
daisy = [True,False,True,False]# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is exclude from the filtered array
r = janet[daisy]
print(r)
'''Above was just an example the filter array id used based on conditions'''
count = np.array([2022,2021,2023,2010,2013])
filter_arr = []
for number in count:
    if number <2020:
        filter_arr.append(True)
        print("last decade")
    else:
        print("current decade")
        filter_arr.append(False)
new = count[filter_arr]
print(">>", new)
print(filter_arr)
'''Check out a file on this directory which goes by the name even.py'''
#These is alternative way of writing even.py is simple way
check = np.array([42,33,98,4893,202,382,3275])
filt = check % 2 == 0
ne = check[filt]
print(">>:output", ne)