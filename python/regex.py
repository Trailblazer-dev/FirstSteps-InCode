import re
ai = "With the rapid upcoming technology a lot of things will be changing very soon,\
    let hope for the best while we expect the worst"
print(re.search("^rapid", ai))
#^ research if the string starts with rapid and return none 
print(re.search("up.*ing", ai))
# .* research for the word that start with up and ends with ing and it founds a mathch and output rest of string
print(re.search("ho.+e", ai))
print(re.split("\s", ai))
# re.split splits the string after every whitspace character
print(re.findall("the", ai))