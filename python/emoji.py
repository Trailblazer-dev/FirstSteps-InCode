message = input(">")
words = message.split(' ')
emojis ={
    ":)": "😃",
    ":(": "😞",
}
n = " "
for e in words:
    n +=emojis.get(e, e)+ " "
print(n)