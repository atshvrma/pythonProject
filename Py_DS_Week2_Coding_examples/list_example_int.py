



def sort_my_list_but_dont_change_orig(myList):
    sortedList = sorted(myList)

    for item in myList:
        print(item, end=" ")

    print()

    for item in sortedList:
        print(item, end=" ")










def print_my_list(myList1):
    # for item in myList1:
    #     print(item, end=" ")
    print(myList1.count(1))

def print_zeroth_item(myList):
    print(myList[3])

def print_last_item(myList):
    print(myList[-3])

def print_part_of_list(myList, initial_position, last_position):
    print(
        myList[initial_position : last_position]
    )


def sort_my_list(myList):
   myList.sort()
   for item in myList:
       print(item, end=" ")


if __name__ == '__main__':
    myList = [4, 5, 1, 7, -1, -25, 1]
    print(type(myList))
    print(myList.count())


    #indexes# 0, 1, 2, 3, 4, 5
            # 0, 1, 2, 3, -3, -2, -1
    # print_my_list(myList)

    # print_zeroth_item(myList)
    #
    # print_last_item(myList)
    # #
    # print_part_of_list(myList, 2, 6)
    #
    # sort_my_list(myList)

    sort_my_list_but_dont_change_orig(myList)



