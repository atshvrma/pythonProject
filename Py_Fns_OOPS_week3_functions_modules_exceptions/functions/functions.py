import string_utils

greet_message = "Hello World !!"

def call_print_my_word(param):
    print(param)


def add_numbers(a, b):
    # print(a)
    # print(b)
    # do more stuff
    result = a + b
    return result

def subtract_numbers(a, b=5):
    print("print a val: "+str(a))
    return a - b

if __name__ == '__main__':
    call_print_my_word("Hello Worlds")

    print(
       subtract_numbers(25, 15)
    )
    #
    # print(string_utils.is_palindrome("Racecar"))


    print(add_numbers(18, 24))
    #
    print(add_numbers(32, 8))
    #
    print(add_numbers("Hello", "rahul"))
    #
    print(add_numbers(3.14, 2.6))