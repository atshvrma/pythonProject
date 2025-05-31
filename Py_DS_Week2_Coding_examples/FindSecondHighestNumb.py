def second_highest(numbers):
    # Remove duplicates
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return "No second highest number"

    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

def get_highest_number(numbers):
    # Remove duplicates
    unique_num = list(set(numbers))
    unique_num.sort(reverse=True)
    return unique_num[0]

if __name__ == '__main__':
    # Example usage
    nums = [5, 3, 9, 1, 9, 7, 7]
    print(len(nums))



    # strVal = "abcd"
    # print(len(strVal))
    #
    # fruits = ["Apple", "Banana"]
    # print(len(fruits))
    print("Second highest:", second_highest(nums))
    print(get_highest_number(nums))