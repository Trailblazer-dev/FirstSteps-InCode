'''Price of a house is 1M .If the buyer has good credit, they need to put down 10%
otherwise they need to put down 20 % .print the down payment'''
print("The house cost is :$1000000M")
for clariy in range(3):
    seller = str(input("Enter the code to proof ur the seller please\n"))
    if seller == '2020/2019': 
        good_credit = str(input("Does the buyer have good or bad credit? hint<good,bad> on input accepted!!!\n"))
        if good_credit == 'good':
            down_pay = 0.1 * 10e6
        else :
            down_pay = 0.2 * 10e6
        break
    else:
        print("sorry you have 2 attempt remaining !!!take caution seller ")
print ("your down payment will be : ", down_pay)
# extra mile is never that crowded
