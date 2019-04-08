print("Learning about lists in python")
mylist = [1, 2, "abc", [30, "Chandan"], 30.50]

print(mylist[2:4])
print(mylist[3])
print(mylist[3][1])


print("Operations on list")

# append
fruits = ["apple", "banana", "guava"]
fruits.append("grapes")
fruits.append(40.50)
print(fruits)

# extend
cars = ["maruti", "tesla", "toyota"]
cars.extend("honda")
print(cars)

# insert
animals = ["lion", "goat", "camel"]
animals.insert(1, "rat")
print(animals)

