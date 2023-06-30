T =True
print("Be real  to yourself", T)
def Kali():
    d=int(input("Enter your age "))
    if d>18 :
        print("Your of age to make your own decision")
        return True 
    else:
        print("Your are underage your parent or guardian will make decision for you")
        return False
is_of_age = Kali()
drink={
        "non alcoholic":{"sprite", "coca cola", "stone", "krest"},
        "alcoholic":{"Jack dan  iel", "smarnoff", "Tuskies", "walker"},
        "energy drinks":{"novida","black energy", "monster"}
    }
if is_of_age:
    print("Drinks available are \n",drink.keys())
else:
    print("drinks available are \n", drink["non alcoholic"])
print("\nafter deciding the kind of drink you wish to take head to our website and order in your phone")
