''' Tuple are quite unique once they have been created they are unchangeable meaning if you want to 
add or remove item in tuple you have to convert the tuple to list then list to tuple back
'''
specs = ("Hp", "CORE i7", "4GB and more", "64 bits ", "500 gb to 1 tb capacity", 840)
print(specs[3])
# tuple are ordered as u can see they are indexed
print(specs[3:])
list = list(specs)
print(type(list))
print(list)
list.append("light")
print(list)
specs = tuple(list)
print(specs)# That is how it is done
