'''These python script will hold a program to determine if someone is qualified for a passport i.e if he has no criminal record and his/her citizenship
'''
r = 0
while r < 40:
    print("___")
    r +=1
print("WELCOME TO OUR OFFICE")
for e in range(40):
    print("____")
print("please processed to the machines on the walls to input ur details")
for w in range(30):
    print("____")
full_name = str(input("Enter your fullname\n"))
citizen = bool(input("Are a citizen (type True if ur or False if not)"))
# I have no knowledge how to hide this part from the citizen so that the machine can cross check if he/she has a criminal record in goverment database 
for s in range(2):
    admin = str(input("senior staff please enter the keyword\n"))
    if admin == '   ':
        criminal_record = bool(input("Enter bool expression\n"))
        if criminal_record == True and citizen == False:
            print("Please sir/madam ur not qualified please move back ")
        else:
            print("well you have qualified please procced with your document to second floor")
        break
    else:
        print("please try again or follow the protocol")
print( "if you need any other service feel free to ask")
