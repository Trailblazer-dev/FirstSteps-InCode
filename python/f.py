def gender():
    g = input("Enter your gender please\t")
    if g.lower() == 'male':
        print("Hello mr {}", input().format())
    elif g.lower() == 'female':
        print("Hello mrs {}", input().format())
    else:
        print("nice meeting your sir/madam {}", input().format())
gender()
course = input("Enter the course your are doing \n")
print("Hello ")
