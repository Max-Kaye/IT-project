the_list_of_fruits = ["apple", "banana", "cherry"]

for fruit in the_list_of_fruits:
    print(fruit)

print("-----------------------------")

print ("removing it")
print(the_list_of_fruits.pop(0))  # calling "pop" removes the zeroth element and returns it
print ("after removing it:")
print(the_list_of_fruits)  # the list is now shorter!
