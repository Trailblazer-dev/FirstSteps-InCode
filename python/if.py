score = int (input ("Enter your score\n"))
em_oji = {
     ":)": "😄",
     ":|": "😞",
     "%": "💯"
}
if score < 50:
	print ("You have no been able to reach pass mark ",em_oji[":|"])
else:
	print ("You have passed the pass mark", em_oji[":)"], "well done", em_oji["%"])

no1 = int(input("Enter an integer/n"))
no_2 = int(input("Enter second integer/n"))
no_3 = int(input("Enter third integer/n"))
if no1 >= no_2 and no1 >= no_3:
     larger = no1
elif no_2 >= no1 and no_2 >= no_3:
     larger = no_2
else:
     larger = no_3
print("The largerst number is :", larger)
     

