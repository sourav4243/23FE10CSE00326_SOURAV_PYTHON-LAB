# 1. Write a python program to triple all numbers in a list using python map

l = [1,2,3,4,5,6]
def triple(x):
  return x*3

print(list(map(triple,l)))