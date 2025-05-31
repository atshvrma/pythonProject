def print_my_list(fruits):
    for item in fruits:
        print(item, end=" ")

    # print(fruits.index("Apple"))
    # print(fruits.count("Apple"))

    # if "engine" not in fruits:
    #     print("\ndoes not exists")




def sort_my_list_with_new_var(fruits):
    sortedList = sorted(fruits)

    for item in fruits:
        print(item, end=" ")

    print()

    for item in sortedList:
        print(item, end=" ")


def add_fruits(fruits, new_fruit):
    # this will add fruit in fruit list
    fruits.insert(new_fruit)

    for item in fruits:
        print(item, end=" ")


def remove_fruit_by_index(fruits, idx):
    fruits.pop(idx)
    for item in fruits:
        print(item, end=" ")


def remove_fruit_by_value(fruits, param):
    fruits.remove(param)
    for item in fruits:
        print(item, end=" ")


def clear_my_fruit_basket(fruits):
    fruits.clear()

    for item in fruits:
        print(item, end=" ")


def sort_my_list(fruits):
   fruits.sort()
   for item in fruits:
       print(item, end=" ")


if __name__ == '__main__':
    fruits = [ "Mango", "Orange", "Pineapple", "Grapes", "Strawberry",
               "Banana", "Watermelon", "Papaya", "Kiwi", "Apple"]

    print_my_list(fruits)

    # sort_my_list(fruits)

    sort_my_list_with_new_var(fruits)

    # add_fruits(fruits, "Guava")

    # remove_fruit_by_index(fruits, 0)

    # remove_fruit_by_value(fruits, "Apple")

    # clear_my_fruit_basket(fruits)



