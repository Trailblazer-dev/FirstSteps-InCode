'''Here is a project for a car game'''
print("_____welcome to xcar game____")
while True:
    user = str(input(":..."))
    if user == 'help':
        content = {
            "start": "- to start the car",
            "stop": "-to stop the car",
            "quit": "-to exit"
        }
        for r in content:
            print(r)
        while True:
            input2 = str(input("any of the 3 term from above\n"))
            if input2.lower() == 'start':
                print("The car started ..... ready to go")
                break
            elif input2.lower() == 'stop':
                print("car stopped")
                break
            elif input2.lower() == 'quit':
                print("Process finished with exit code 0")
                break
            else:
                print("try again")
        break
    else:
        print("I don't understand that")        