import functions
import function_1
import string_utils

if __name__ == '__main__':
    # functions.call_print_my_word("Hello class")
    # function_1.greet()
    #
    # print(functions.subtract_numbers(50, 10))

    # print(string_utils.is_palindrome("Racecar"))
    # #
    # print(string_utils.is_palindrome("Rahul"))
    #
    # print(string_utils.count_vowels("atish"))

    list_vals = ["Atish", "Susus", "Laxmi"]

    for item in list_vals:
        print(string_utils.is_palindrome(item))
