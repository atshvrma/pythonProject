
# def addNumber(val1, val2):
#     print(int(val1)+int(val2))

# Extraction :  Read the file from S3 file is in csv

# Transform : convert the csv format to my database table

# Load : Save it database/ nosql/ datalake

def print_my_name(my_name):
    print("Hello, " + my_name)


def print_my_bank_balance(bank_balance):
    print("your bank balance is :" + bank_balance)


def is_user_interested(are_you_interested):
    print("Your response is " + are_you_interested)


def add_my_numbers(num1, num2):
    result = num1 + num2
    return result


def suubtract_my_numbers(param, param1):
    return param - param1


if __name__ == '__main__':
    entered_value = input("Enter your name :")
    print( "Hello, "+ entered_value)
    # #
    # bank_balance = input("Enter your bank balance : ")
    # bank_balance = float(bank_balance)
    # # # print(float(bank_balance))
    # # # print(type(bank_balance))
    # #
    # # if bank_balance == '20.50' and entered_value == "Atish":
    # #     print("User is our bank customer")
    #
    # if bank_balance < 200 :
    #     print("Your balance is less than 200")
    # elif bank_balance > 200:
    #     print("Your balance is greater than 200")
    # else:
    #     print("Your balance is 200")
    #
    # x = -10
    # if x > 0:
    #     print("Positive")
    # elif x == 0:
    #     print("Zero")
    # else:
    #     print("Negative")


    # # for loop
    # for i in range(5, 20):
    #     if i == 15 :
    #         break
    #     elif i == 10:
    #         continue
    #     print(i, end=", ")
    #
    #
    #
    # # count = 0
    # # while count < 5:
    # #     print(count)
    # #     count += 1
    #
    # #
    # # value = 2
    # # value *= 2
    # # print(value)
    #
    # # are_you_interested = input("Are you interested ? ")
    # # is_user_interested(are_you_interested)
    # #
    # # print(type(are_you_interested))
    # #
    # # another_var = bool(are_you_interested)
    # #
    # # print(type(another_var))
    #
    # # print(add_my_numbers(2,5))
    #
    # # print(suubtract_my_numbers(3,4))
    #
    #
    #
