# is a program that get user weight in kg or pounds and output it
weight = float(input("Weight:\n"))
for r in range(6):
    unit = str(input("(K)for kg, (L)for pounds"))
    if unit.upper() == 'K':
        print("You weight :", weight *0.45 , "Pounds")
        break
    elif unit.upper() == 'L':# when u use upper() make sure the char in the equation is capital 
            print("Your weight : ", weight /0.45, "kilograms")
            break
    else:
        print("try again")
