#Here we will deal with matrix
matric = [
    [1, 2, 3],
    [3, 4, 7],
    [2, 9, 4]
]#matric in python are listed using list
print(matric[0][1])# the first index present the first nested list ,the second index specifies the value inside the nested list
for row in matric:
    for i in row:
        print(i)#This is how we loop a matrix