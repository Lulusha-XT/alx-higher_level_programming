#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = int(input("Enter an index: "))
new_element = int(input("Enter a value: "))
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
