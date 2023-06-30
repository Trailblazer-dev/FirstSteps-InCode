#Here is program which prompt the user to enter his name which should not be less than 3 character and more than 50 characters
while True:
    name = str(input("Enter your name\n"))
    if len(name) >= 3 and len(name) <= 50:# use of combination of conditional statement like math makes the code  inaccurate
        print("name look's good")
        break
    else:
        print("The name must atleast have 3 character and 50 less character")
