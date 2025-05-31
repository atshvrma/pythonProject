def get_dict_item(d1, key):
    print(d1[key])


def add_dict_item(dict_orig, key, value):
    dict_orig[key] = value
    print(dict_orig)


def delete_dict_item(d1, key):
    # d1.pop(key)
    # print(d1)

    # remove last_item
    # key, val = d1.popitem()
    d1.pop(key)
    key, val = d1.popitem()
    # print(key)
    # print(val)
    #
    # Iterate over values
    for value in d1.keys():
        print(value)

    # Nested Dict
    d = {1: 'Geeks', 2: 'For',
         3:
             {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}
         }

    print(d)
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    car.update({"color": "White"})
    print(car)


def print_dict_items(d1):
    for k in d1.keys():
        print("keys :" + str(k))
        # print("value :" + str(v))


if __name__ == '__main__':
    d1 = {1: 'Four', 2: 'Achievers', 3: 'Noida'}
    # print(d1)
    d1[4] = 'Dehradun'

    d2 = dict(a="apple", b="banana", c="coconut")
    # print(d2)

    d3 = {'a1': "Akanksha", 'a2': "Atwo"}

    # print_dict_items(d3)
    # print(d2['a'])

    # d1[1] = "Dehradun"

    # d1.pop(2)
    key, val = d1.popitem()
    print(key)
    print(val)
    # get_dict_item(d1, 1)
    #
    # get_dict_item(d2, "a")
    #
    # add_dict_item(d1, 4 ,"Dehradun")
    #
    # add_dict_item(d2, "d","date")
    #
    # delete_dict_item(d1, 1)
    #
    # delete_dict_item(d2, 'b')

    d = {1: 'Geeks', 2: 'For',
         3:
             {'A': 'Welcome', 'B': 'To', 'C':
                 {'a' : 'apple', 'b': 'banana'}
              }
         }

    print(d)
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    car2 = {
        "brand": "Maruti",
        "model": "Baleno",
        "year": 2015
    }


    print(car2["brand"])

    # car.update({"color": "White"})
    # print(car)
    #
    # dict1 = {'name': 'a1', 'name': 'a2'}
    # print(dict1)
    #
