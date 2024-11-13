# 8. wap to convert a given list of integers and a tuple of integers in a list of strings

integer_list = [1, 2, 3, 4, 5]
integer_tuple = (6, 7, 8, 9, 10)

list_of_strings_of_List = list(map(str,integer_list))
list_of_strings_of_Tuple = list(map(str,integer_tuple))

print(f"List of strings from the list: {list_of_strings_of_List}")
print(f"List of strings from the tuple: {list_of_strings_of_Tuple}")