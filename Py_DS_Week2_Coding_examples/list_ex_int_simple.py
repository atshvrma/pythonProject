

myList = [4, 5, 1, 7, -1, -25, 1, 1]
        # 0, 1, 2, 3,  4,  5,   6
        # -7, -6,  -5,-4, -3,-2,-1
print(myList.count(1))

print(myList)

for item in myList:
    print(item, end=" ,")

print()
print(myList.index(5))

print(myList[-1])

print(myList[2:5])

# myList.sort()
# for item in myList:
#     print(item, end=",")

# newList = sorted(myList, reverse=True)
myList.insert(2, 200)

for item in myList:
    print(item, end =", ")
