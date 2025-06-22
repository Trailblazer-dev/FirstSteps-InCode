from car import ElectricCar

my_leaf = ElectricCar("bmw",'nfs',2008)
print(my_leaf.get_descriptive_name())

my_leaf.battery.get_range()