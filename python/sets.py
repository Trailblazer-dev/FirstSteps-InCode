'''set is very different from other built in data type since it is unordered
meaning is not indexed ,does not accept duplicate and is unchangeable but 
you can remove Items and add new'''
members = {"David", "John", "Joseph", "Soul"}
print(members)
for e in members:
    print(e)
    #when I say unordered this is what I Mean
members.add("Solomon")
members.update("Daniel")
print(members)
# In set you can't specific the item you want to remove it will remove random item