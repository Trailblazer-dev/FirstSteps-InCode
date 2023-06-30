name = input("Enter your first name and last  name")
print("Hello ", name.upper())
print(len(name))
print(name[:4].lower())
#The keyword upper() and lower() change the strings to upper case and lower case respectively
k = "meat is ready mr"
print(k.replace("a", "e"))
#The keyword replace() replaces all string with the same character in the text hence making it ineffective
text = "I am confused I don't know if I should become a  developer or sth else like{}"
print(text.format("hacker"))
#Here I have used the keyword format() which works with {} to