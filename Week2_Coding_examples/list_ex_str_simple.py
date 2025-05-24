fruits = [ "Mango", "Orange", "Pineapple", "Grapes", "Strawberry",
               "Banana", "Watermelon", "Papaya", "Kiwi", "Apple"]

for item in fruits:
    print(item, end=", ")


print()

# fruits.sort()
# for item in fruits:
#     print(item, end=", ")

fruits.append("DragonFruit")
# for item in fruits:
#     print(item, end=", ")


fruits.insert(1, "Cherries")
for item in fruits:
    print(item, end=", ")


print()
fruits.pop(0)# index
fruits.remove("Apple") # value

fruits.clear()

for item in fruits:
    print(item, end=", ")