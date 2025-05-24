import scope_example_1

print(scope_example_1.var_1)

print(scope_example_1.x)

scope_example_1.my_function()

#
#
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1