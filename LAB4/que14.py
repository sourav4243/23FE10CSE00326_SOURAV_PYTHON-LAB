# 14. Write a program to display the following pattern:
# *****
# ****
# ***
# **
# *
n = int(input("Enter num of rows: "))
for i in range(n + 1, 0,  -1):
  for j in range(i + 1, 2, -1):
      print("*", end=" ")
  print()