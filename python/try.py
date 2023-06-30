try:
    print(c)
except:
    print("An exception occured")
o = 0    
try:
    print(o)
except NameError:
    print("Variable is not defined")
else: # if the exception does not capture the nameError the else will the printed
    print("Something else went wrong")
finally:
    print("check your code")
#finally block will be execute regardless if it will raise an error or not
    