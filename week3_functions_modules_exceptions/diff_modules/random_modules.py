import random


num = random.randint(1, 10)
print("Random number:", num)

#
fruits = ["apple", "banana", "mango", "grape"]
print(fruits)
choice = random.choice(fruits)
print("Random fruit:", choice)
#
#
names = ["Alice", "Bob", "Charlie", "Diana"]
print(names)
random.shuffle(names)
print("Shuffled names:", names)
#
#
f = random.random()
print(type(f))
print("Random float:", f)
#
# # create a game for lucky draw
#
