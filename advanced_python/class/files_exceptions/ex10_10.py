
a = input("Enter a number: ")
b = input("Enter another number: ")

try:
    result = int(a) + int(b)
except ValueError:
    print("Please enter valid integers.")
else:
    print(f"The sum of {a} and {b} is {result}.")
    