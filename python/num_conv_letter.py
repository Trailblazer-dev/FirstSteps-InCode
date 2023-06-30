#This is called mapping
code = (input("Enter your code"))
words = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six"
}
output = ""
for r in code:
    output +=   words.get(r, "!") + " "
print(output)