#there is a program which helps someone choose his dress code for the day determined by temperature
temperature = float(input("Enter the current temperature\n"))
if temperature > 30:
    print("should probably drink alot of water and wear light clothes which are confortable")
elif temperature < 10:
    print("should probably drink something hot to give u warm and wear heavy clothes to keep you warm")
else:
    print("should probably keep yourself dehdrated and don't wear heavy clothes or very light ones")
print("Have a nice day ")