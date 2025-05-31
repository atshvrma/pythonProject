
def diff_between_two_sets():
    set1 = set()
    set2 = set()

    for i in range(5):
        set1.add(i)

    for j in range(3, 9):
        set2.add(j)

    # Difference of two sets
    set3 = set1 - set2

    print(" Difference of two sets using difference() function")
    print(set3)


def diff_between_two_set():


    # Sets for attendees
    day1_attendees = {"Alice", "Bob", "Charlie", "David"}
    day2_attendees = {"Charlie", "David", "Eve", "Frank"}

    # Find who attended both days
    both_days = day1_attendees.union(day2_attendees)

    print("Attended both days:", both_days)

if __name__ == '__main__':
    # diff_between_two_set()

    # set1 = {"a", "b", "c", "a", "b", "c", "a", "d"}
    # print(type(set1))
    # #
    # print(set1)
    # for item in set1:
    #     print(item, end=", ")
    # #
    # #
    # print()
    # s = set(["a", "b", "c", "a"])
    # print(type(s))
    # # #
    # # # Adding element to the set
    # s.add("e")
    # print(s)


    # Python program to
    # demonstrate difference
    # of two sets

    # set1 = set()
    # set2 = set()
    #
    # for i in range(5):
    #     set1.add(i)
    #
    # for i in range(3, 9):
    #     set2.add(i)
    #
    # print(set1)
    # print(set2)
    #
    # # Difference of two sets
    # set3 = set1.difference(set2)
    #
    # print(" Difference of two sets using difference() function")
    # print(set3)
    #
    # # Difference of two sets
    # # using '-' operator
    # set3 = set1 - set2
    #
    # print("\nDifference of two sets using '-' operator")
    # print(set3)
    #
    #
    # #intersection
    #
    # Sets for attendees
    day1_attendees = {"Alice", "Bob", "Charlie", "David"}
    day2_attendees = {"Charlie", "David", "Eve", "Frank"}

    # Find who attended both days
    both_days = day1_attendees.intersection(day2_attendees)

    print("Attended both days:", both_days)
    #


    # set1={90}
    # set2={10}
    # print(type(set1))
    # for i in range(6):
    #     set1.add(i)
    #
    # for i in range(2,9):
    #     # print(set2)
    #     set2.add(i)
    #
    # set3=set1.difference(set2)
    # print(set3)

