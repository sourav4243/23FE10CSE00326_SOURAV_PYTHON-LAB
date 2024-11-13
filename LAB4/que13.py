# 13. Write a program to display the following pattern:
# A
# B B
# C C C
# D D D D
# E E E E E

n = int(input("Enter num of rows: "))
for i in range(1,n+1):
  for j in range(1,i+1):
      print(chr(i+64),end=' ')
  print()