# 7. write a python program to add 2 given lists and find differences between them using map
list1 = list(map(int, input("Enter list1 elements: ").split()))
list2 = list(map(int, input("Enter list2 elements: ").split()))
def add(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))
def difference(list1, list2):
    return list(map(lambda x, y: abs(x - y), list1, list2))

if len(list1) != len(list2):
  print("Lists must be of same length.")
else:
  addedList = add(list1, list2)
  print("Added List:", addedList)
  diffList = difference(list1, list2)
  print("Difference List:", diffList)