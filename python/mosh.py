message = "where are you {}?"
print(message.format("rich"))
# below is a formatted string
first_gf = "Janet"
second_gf = "Joan"
names = f"{first_gf} this was his first girlfriend , then followed by {second_gf}.not bad at all"
print(names)
print(names.find("n"))
# find displays the find place which it encounters the character and displays it index
# If you want to change a certain word u can use replace keyword
print(names.replace("girlfriend", "love"))#what happens here is that it replaces girlfriend and insert love in the place for gf
# so replace takes two arguments
'''The in operator is like a boolean operator'''
print("then" in names)