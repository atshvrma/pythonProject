def print_first_item(my_complex_tuple):
    print(my_complex_tuple[0])


def concat_my_tuple(my_basic_tuple, my_complex_tuple):
    new_tuple = my_basic_tuple + my_complex_tuple

    print(new_tuple)

    for item in new_tuple:
        print(item, end=" ")


def get_first_item(my_complex_tuple):
    var = my_complex_tuple[3:]

    print(var)


def reverse_my_tuple(my_complex_tuple):
    var = my_complex_tuple[::-1]
    print(var)


def get_ranged_items(my_complex_tuple, start, end):
    var = my_complex_tuple[start:end]
    print(var)

if __name__ == '__main__':
    my_basic_tuple = (2,4)

    my_complex_tuple = (2, "Geeks", 3.14, "this", "is", "tuple", True)


    # print_first_item(my_complex_tuple)
    #
    # concat_my_tuple(my_basic_tuple, my_complex_tuple)
    #
    # get_first_item(my_complex_tuple)

    reverse_my_tuple(my_complex_tuple)

    get_ranged_items(my_complex_tuple, 2, 5)


    # ✅ 2. Access Last 3 Elements
    t = ('a', 'b', 'c', 'd', 'e')
    print(t[-3:])  # Output: ('c', 'd', 'e')
