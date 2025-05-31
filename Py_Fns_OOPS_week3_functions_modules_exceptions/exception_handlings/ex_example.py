# def basic_exception():
#     try:
#         x = int(input("Enter a number: "))
#         print("You entered:", x)
#     except ValueError:
#         print("Invalid input! Please enter a valid number.")
#
#
# basic_exception()


# def multiple():
#     try:
#         a = int(input("Enter a number: "))
#         b = int(input("Enter another number: "))
#         result = a / b
#         print("Result:", result)
#     except ValueError:
#         print("Please enter only numbers.")
#     except ZeroDivisionError:
#         print("Cannot divide by zero!")
#
# multiple()
#
# try:
#     num = int(input("Enter a number: "))
#     print("you entered ", num )
# except ValueError:
#     print("That's not a number.")
# else:
#     print("Thanks for entering:", num)



# write a program for file not found
list_vals = [1,2,3]



try:
    f = open("sample.py", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found.")
else:
    print("tried reading a py file")
finally:
    print("Finished trying to read the file.")


