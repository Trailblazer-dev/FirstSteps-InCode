list = ["house", "apartment", "skyscrappers", "hospitals", 023.31, 111]
car = ["Toyota", "Tesla", "BMW", "audi", 1992, 3312 , True]
print(list[3:])
list[3] = "schools"  #if you want to change a specific value in a list u use index of that item in the list
print(list[3])
list.insert(6, "cinema")
#to insert a new item without replacing any we use insert() keyword
print(list)
car.append("Ferari")
# you can also use append() keyword in place of insert()
print(car)
list.extend(car)
#extend() appends two list if necessary even tuples
print(list)
#there are various way to remove items in a  list like remove(),clear(),pop(),
car.remove(1992)# here we insert the items/object name as in the list
print(car)
car.pop(5)
print(car)#here we use indexing to specificy want we want to remove in list like here we remove True
'''list.clear()# empties the list  but the list remains but has nothing
#Just like delete which deletes list completely
print(list)'''
'''for r in list:
    print(r)'''
e = 0
while e < len(car):
    print(car)
    e += 1
#Note update() keyword is not a built in method thus cannot be used in list
    