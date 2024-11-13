# 4. write a python program to create a list containing the power of said number in bases raised to the index using map
base = int(input("Enter the base number: "))
length = int(input("Enter the length of the required list: "))

print(list(map(lambda x: base ** x, range(length))))