d = open("word.txt", "w")
print(d.write("Today something unexpected happenend! my ex just calls me and she stills love me \
    To my surprise the feeling which I was try to erase from excistence have just merged from \
        no where .Am totally confused"))
print(d)
d.close()
#to open and read the file we use "r" mode and read()
f = open("word.txt", "rb")
print(f.read())
